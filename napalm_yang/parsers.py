import napalm_yang
from napalm_yang import text_helpers

import yaml

import logging
import os
import re
import sys


logger = logging.getLogger("napalm-yang")


def get_parsers(type_):
    parsers = {
        "text": TextExtractor,
        "xml": XMLExtractor,
    }
    return parsers[type_]


def find_yang_file(device, filename, path):
    """
    Find the necessary file for the given test case.

    Args:
        device(napalm device connection): for which device
        filename(str): file to find
        path(str): where to find it relative to where the module is installed
    """
    # Find base_dir of submodule
    module_dir = os.path.dirname(sys.modules[device.__module__].__file__)
    full_path = os.path.join(module_dir, 'yang_mappings', path, filename)

    if os.path.exists(full_path):
        return full_path
    else:
        msg = "Couldn't find parsing file: {}".format(full_path)
        logger.error(msg)
        raise IOError(msg)


class Parser(object):

    def __init__(self, device, attribute, model, texts=None, keys=None, extra_vars=None):
        self.device = device
        self.attribute = attribute
        self.model = model

        # Dictionary used to store blocks of text
        self.texts = texts or {"parent": None}
        # Placeholder for storing keys
        self.keys = keys or {"parent_key": None}
        self.extra_vars = extra_vars or {"parent": None}

    def _read_yang_map(self):
        filename = os.path.join(self.model.prefix, "{}.yaml".format(self.attribute))

        try:
            filepath = find_yang_file(self.device, filename, "parsers")
        except IOError:
            return

        with open(filepath, "r") as f:
            return yaml.load(f.read())

    def _execute_raw(self, device, raw):
        result = []
        for element in raw:
            attr = device
            for p in element["path"].split("."):
                attr = getattr(attr, p)

            result.append(attr(**element["args"]))

        return result

    def parse(self):
        self.parser_map = self._read_yang_map()
        if not self.parser_map:
            return

        metadata = self.parser_map["metadata"]
        self.parser = get_parsers(metadata["parser"])
        self.prefix = metadata["prefix"]

        if "cli" in metadata["execute"]["config"].keys():
            # TODO make this a list
            self.texts[self.attribute] = "\n".join(self.device.cli(
                metadata["execute"]["config"]["cli"]).values()
            )
        elif "raw" in metadata["execute"]["config"].keys():
            self.texts[self.attribute] = self._execute_raw(self.device,
                                                           metadata["execute"]["config"]["raw"])

        self._parse(self.parser_map[self.attribute], self.model)

    def _parse(self, parser_map, obj):
        for attribute, model in obj.items():
            logger.debug("Processing '{}'".format(attribute))
            if not model._meta["config"] and issubclass(model.__class__, napalm_yang.BaseBinding):
                continue

            try:
                mapping = parser_map[attribute]
            except KeyError:
                if model.prefix == self.prefix:
                    raise KeyError("Couldn't find parser for field '{}'".format(attribute))
                else:
                    Parser(self.device, attribute, model,
                           self.texts, self.keys, self.extra_vars).parse()
                    continue

            if issubclass(model.__class__, napalm_yang.List):
                self._parse_list(attribute, model, mapping)
            elif issubclass(model.__class__, napalm_yang.BaseBinding):
                self._parse(mapping, model)
            else:
                self._parse_leaf(model, mapping)

    def _parse_list(self, attribute, model, mapping):
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_text = self.texts["parent"]
        old_parent_extra_vars = self.extra_vars["parent"]

        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.texts[attribute] = {}

        for key, block, extra_vars in self.parser.parse_list(mapping, self.texts, self.keys,
                                                             self.extra_vars):
            obj = model.get_element(key)

            key_name = "{}_key".format(attribute)
            self.keys[key_name] = key
            self.texts[attribute][key] = block
            self.extra_vars[attribute] = extra_vars

            # These two are necessary in cases where an element may be present in subtrees. For
            # example, ipv4.config.enabled is present in both interfaces and subinterfaces
            self.keys["parent_key"] = key
            self.texts["parent"] = block
            self.extra_vars["parent"] = extra_vars

            self._parse(mapping, obj)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.texts["parent"] = old_parent_text
        self.extra_vars["parent"] = old_parent_extra_vars

    def _parse_leaf(self, attr, mapping):
        value = self.parser.parse_leaf(mapping, self.texts, self.keys, self.extra_vars)

        if value is None:
            return

        try:
            attr(value)
        except ValueError as e:
            try:
                attr(eval(value))
            except Exception:
                logger.error(e)
                logger.error("Problem parsing attr '{}' with value '{}' ({}).\n{}".format(
                    attr.__class__.__name__, value, value.__class__, attr.__dict__))
                raise


class BaseExtractor(object):

    @classmethod
    def _get_text(cls, texts, path, keys, extra_vars):
        vars = dict(keys)
        vars.update(extra_vars)

        path = [text_helpers.translate_string(p, **vars) for p in path.split(".")]
        for p in path:
            try:
                texts = texts[p]
            except TypeError:
                texts = texts[int(p)]
        return texts

    @classmethod
    def parse_list(cls, mapping, texts, keys, extra_vars):
        method_name = "_parse_list_{}".format(mapping["_list_extraction"]["mode"])
        for key, block, extra_vars in getattr(cls, method_name)(mapping, texts, keys, extra_vars):
            yield key, block, extra_vars

    @classmethod
    def parse_leaf(cls, mapping, texts, keys, extra_vars):
        method_name = "_parse_leaf_{}".format(mapping["_leaf_extraction"]["mode"])
        return getattr(cls, method_name)(mapping, texts, keys, extra_vars)

    @classmethod
    def _parse_leaf_key(cls, mapping, texts, keys, extra_vars):
        leaf_extraction = mapping["_leaf_extraction"]
        value = keys[leaf_extraction["value"]]

        if "regexp" in leaf_extraction.keys():
            value = re.search(mapping["_leaf_extraction"]["regexp"], value).group("value")
        return value

    @classmethod
    def _parse_list_not_implemented(cls, mapping, texts, keys, extra_vars):
        return {}

    @classmethod
    def _parse_leaf_not_implemented(cls, mapping, texts, keys, extra_vars):
        return


class XMLExtractor(BaseExtractor):

    @classmethod
    def _parse_list_xpath(cls, mapping, texts, keys, extra_vars):
        list_extraction = mapping["_list_extraction"]
        texts = cls._get_text(texts, list_extraction["from"], keys, extra_vars)

        for element in texts.xpath(list_extraction["xpath"]):
            key = element.xpath("name")[0].text
            yield key, element, {}

    @classmethod
    def _parse_leaf_xpath(cls, mapping, texts, keys, extra_vars,
                          check_default=True, check_presence=False):
        leaf_extraction = mapping["_leaf_extraction"]
        texts = cls._get_text(texts, leaf_extraction["from"], keys, extra_vars)

        element = texts.xpath(leaf_extraction["xpath"])

        if element and not check_presence:
            return element[0].text
        elif element and check_presence:
            return True
        elif check_default:
            return leaf_extraction["default"]
        else:
            return None

    @classmethod
    def _parse_leaf_map(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_xpath(mapping, texts, keys, extra_vars)
        value = re.search(mapping["_leaf_extraction"]["regexp"], value).group("value")

        return mapping["_leaf_extraction"]["map"][value]

    @classmethod
    def _parse_leaf_is_present(cls, mapping, texts, keys, extra_vars):
        return cls._parse_leaf_xpath(mapping, texts, keys, extra_vars,
                                     check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, texts, keys, extra_vars):
        return not cls._parse_leaf_xpath(mapping, texts, keys, extra_vars,
                                         check_default=False, check_presence=True)


class TextExtractor(BaseExtractor):

    @classmethod
    def _parse_list_block(cls, mapping, texts, keys, extra_vars):
        list_extraction = mapping["_list_extraction"]
        texts = texts[list_extraction["from"]]
        block_regexp = list_extraction["regexp"]

        regexp = text_helpers.translate_string(block_regexp, **keys)
        block_matches = re.finditer(regexp, texts, re.MULTILINE)

        for match in block_matches:
            extra_vars = match.groupdict()
            key = extra_vars.pop("key")
            block = extra_vars.pop("block")
            yield key, block, extra_vars

    @classmethod
    def _parse_leaf_search(cls, mapping, texts, keys, extra_vars, check_default=True):
        leaf_extraction = mapping["_leaf_extraction"]
        texts = cls._get_text(texts, leaf_extraction["from"], keys, extra_vars)
        regexp = text_helpers.translate_string(leaf_extraction["regexp"], **keys)

        match = re.search(regexp, texts, re.MULTILINE)

        if match:
            return match.group("value")
        elif check_default:
            return mapping["_leaf_extraction"]["default"]
        else:
            return None

    @classmethod
    def _parse_leaf_is_present(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars, check_default=False)
        return bool(value)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars, check_default=False)
        return not bool(value)

    @classmethod
    def _parse_leaf_map(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars)
        return mapping["_leaf_extraction"]["map"][value]

    @classmethod
    def _parse_leaf_extra_vars(cls, mapping, texts, keys, extra_vars):
        leaf_extraction = mapping["_leaf_extraction"]
        return cls._get_text(extra_vars, leaf_extraction["var"], keys, extra_vars)
