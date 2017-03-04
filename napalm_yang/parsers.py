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

    def __init__(self, device, attribute, model, texts=None, keys=None):
        self.device = device
        self.attribute = attribute
        self.model = model

        # Dictionary used to store blocks of text
        self.texts = texts or {}
        # Placeholder for storing keys
        self.keys = keys or {}

    def _read_yang_map(self):
        filename = os.path.join(self.model.prefix, "{}.yaml".format(self.attribute))

        try:
            filepath = find_yang_file(self.device, filename, "parsers")
        except IOError:
            return

        with open(filepath, "r") as f:
            return yaml.load(f.read())

    def parse(self):
        self.parser_map = self._read_yang_map()
        if not self.parser_map:
            return

        metadata = self.parser_map["metadata"]
        self.parser = get_parsers(metadata["parser"])
        self.prefix = metadata["prefix"]

        if "cli" in metadata["execute"]["config"].keys():
            self.texts[self.attribute] = "\n".join(self.device.cli(
                metadata["execute"]["config"]["cli"]).values()
            )

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
                    #  parse(self.device, k, v, config, partial_config)
                    continue

            if issubclass(model.__class__, napalm_yang.List):
                self._parse_list(attribute, model, mapping)
            elif issubclass(model.__class__, napalm_yang.BaseBinding):
                self._parse(mapping, model)
            else:
                self._parse_leaf(model, mapping)

    def _parse_list(self, attribute, model, mapping):
        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.texts[attribute] = {}

        for key, block in self.parser.parse_list(mapping, self.texts, self.keys):
            obj = model.get_element(key)
            self.keys["{}_key".format(attribute)] = key
            self.texts[attribute][key] = block
            self._parse(mapping, obj)

    def _parse_leaf(self, attr, mapping):
        value = self.parser.parse_leaf(mapping, self.texts, self.keys)

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


class TextExtractor:

    @classmethod
    def _get_text(cls, texts, path, keys):
        path = [text_helpers.translate_string(p, **keys) for p in path.split(".")]
        for p in path:
            texts = texts[p]
        return texts

    @classmethod
    def parse_list(cls, mapping, texts, keys):
        method_name = "_parse_list_{}".format(mapping["_list_extraction"]["mode"])
        for key, block in getattr(cls, method_name)(mapping, texts, keys):
            yield key, block

    @classmethod
    def _parse_list_block(cls, mapping, texts, keys):
        list_extraction = mapping["_list_extraction"]
        texts = texts[list_extraction["from"]]
        block_regexp = list_extraction["regexp"]

        regexp = text_helpers.translate_string(block_regexp, **keys)
        block_matches = re.finditer(regexp, texts, re.MULTILINE)

        for match in block_matches:
            key = match.group("key")
            block = match.group("block")
            yield key, block

    @classmethod
    def _parse_list_not_implemented(cls, mapping, texts, keys):
        return {}

    @classmethod
    def parse_leaf(cls, mapping, texts, keys):
        method_name = "_parse_leaf_{}".format(mapping["_leaf_extraction"]["mode"])
        return getattr(cls, method_name)(mapping, texts, keys)

    @classmethod
    def _parse_leaf_search(cls, mapping, texts, keys):
        leaf_extraction = mapping["_leaf_extraction"]
        texts = cls._get_text(texts, leaf_extraction["from"], keys)
        regexp = text_helpers.translate_string(leaf_extraction["regexp"], **keys)

        match = re.search(regexp, texts, re.MULTILINE)
        if match:
            return match.group("value")
        else:
            return mapping["_leaf_extraction"]["default"]

    @classmethod
    def _parse_leaf_is_present(cls, mapping, texts, keys):
        value = cls._parse_leaf_search(mapping, texts, keys)
        return bool(value)

    @classmethod
    def _parse_leaf_map(cls, mapping, texts, keys):
        value = cls._parse_leaf_search(mapping, texts, keys)
        return mapping["_leaf_extraction"]["map"][value]

    @classmethod
    def _parse_leaf_key(cls, mapping, texts, keys):
        return keys[mapping["_leaf_extraction"]["value"]]

    @classmethod
    def _parse_leaf_not_implemented(cls, mapping, texts, keys):
        pass
