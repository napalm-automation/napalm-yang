import napalm_yang

from napalm_yang.parsers.extractors import TextExtractor, XMLExtractor
from napalm_yang.parsers.translators import TextTranslator, XMLTranslator

import yaml

import logging
import os
import sys


logger = logging.getLogger("napalm-yang")


def get_parsers(type_):
    parsers = {
        "TextExtractor": TextExtractor,
        "XMLExtractor": XMLExtractor,
        "TextTranslator": TextTranslator,
        "XMLTranslator": XMLTranslator,
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
    module_dir = os.path.dirname(__file__)
    full_path = os.path.join(module_dir, 'mappings', device.profile, path, filename)

    if os.path.exists(full_path):
        return full_path
    else:
        msg = "Couldn't find parsing file: {}".format(full_path)
        logger.error(msg)
        raise IOError(msg)


def read_yang_map(prefix, attribute, device, parser_path):
    filename = os.path.join(prefix, "{}.yaml".format(attribute))

    try:
        filepath = find_yang_file(device, filename, parser_path)
    except IOError:
        return

    with open(filepath, "r") as f:
        return yaml.load(f.read())


class Translator(object):

    def __init__(self, device=None, attribute=None, model=None, translation=None,
                 bookmarks=None, keys=None):
        self.device = device
        self.attribute = attribute
        self.model = model

        self.translation = translation

        if model:
            self.prefix = model.prefix

        # Placeholder for storing keys
        self.keys = keys or {"parent_key": None}
        self.bookmarks = bookmarks or {"parent": None}

    def parse(self):

        self.parser_map = read_yang_map(self.model.prefix, self.attribute, self.device,
                                        "translators")
        if not self.parser_map:
            return

        metadata = self.parser_map["metadata"]
        self.translator = get_parsers(metadata["parser"])()

        self.translation = self.translator.init_translation(metadata, self.translation)

        # Let's parse the root element
        self._parse_element(self.attribute, self.model, self.parser_map[self.attribute],
                            self.translation)

        return self.translator.post_processing(self)

    def _parse_element(self, attribute, model, mapping, translation):
        if issubclass(model.__class__, napalm_yang.List):
            self._parse_list(attribute, model, mapping, translation)
        elif issubclass(model.__class__, napalm_yang.BaseBinding):
            self.bookmarks[attribute] = translation
            self.bookmarks["parent"] = translation
            translation = self._parse_container(attribute, model, mapping, translation)
            self._parse(mapping, model, translation)
        else:
            self._parse_leaf(attribute, model, mapping, translation)

        return translation

    def _parse(self, parser_map, obj, translation):
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
                    Translator(self.device, attribute, model, translation,
                               self.bookmarks, self.keys).parse()
                    continue
            self._parse_element(attribute, model, mapping, translation)

    def _parse_list(self, attribute, model, mapping, translation):
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]

        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.bookmarks[attribute] = {}

        for key, element in model.items():
            logger.debug("Translating {} {}".format(attribute, key))

            et = self.translator.init_element(attribute, element, mapping, translation,
                                              self.bookmarks, self.keys)

            if et is None:
                # if we got None this means we didn't implement this
                break

            key_name = "{}_key".format(attribute)
            self.keys[key_name] = key
            self.bookmarks[attribute][key] = et
            self.keys["parent_key"] = key
            self.bookmarks["parent"] = et

            self._parse(mapping, element, et)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark

    def _parse_leaf(self, attribute, model, mapping, translation):
        action = mapping["_translation"]
        if isinstance(action, list):
            for a in action:
                self.translator.parse_leaf(attribute, model, a, translation,
                                           self.bookmarks, self.keys)
        else:
            self.translator.parse_leaf(attribute, model, action, translation,
                                       self.bookmarks, self.keys)

    def _parse_container(self, attribute, model, mapping, translation):
        return self.translator.parse_container(attribute, model, mapping, translation,
                                               self.bookmarks, self.keys)


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

    def _execute_method(self, device, methods):
        result = []
        for m in methods:
            attr = device
            for p in m["method"].split("."):
                attr = getattr(attr, p)

            result.append(attr(**m["args"]))

        return result

    def parse(self):
        self.parser_map = read_yang_map(self.model.prefix, self.attribute, self.device,
                                        "extractors")
        if not self.parser_map:
            return

        metadata = self.parser_map["metadata"]
        self.parser = get_parsers(metadata["parser"])
        self.prefix = metadata["prefix"]

        self.texts[self.attribute] = self._execute_method(self.device,
                                                          metadata["execute"]["config"])

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
