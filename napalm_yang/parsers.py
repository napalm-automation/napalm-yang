import napalm_yang
from napalm_yang import text_helpers

import yaml

import logging
import os
import re
import sys


logger = logging.getLogger("napalm-yang")
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


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


def parse(device, attribute, model):
    filename = os.path.join(model.prefix, "{}.yaml".format(attribute))

    try:
        filepath = find_yang_file(device, filename, "parsers")
    except IOError:
        return

    with open(filepath, "r") as f:
        parser_map = yaml.load(f.read())

    metadata = parser_map["metadata"]
    parser = get_parsers(metadata["parser"])

    if "cli" in metadata["execute"]["config"].keys():
        config = "\n".join(device.cli(metadata["execute"]["config"]["cli"]).values())

    parser(prefix=metadata["prefix"],
           device=device).populate(model, config, parser_map[attribute])


class TextExtractor:

    def __init__(self, prefix, device):
        self.prefix = prefix
        self.device = device
        self.key = None

    def populate(self, model, config, mappings):
        self.parse(model, config, config, mappings)

    def parse(self, model, config, partial_config, mappings):
        for k, v in model.items():
            if not v._meta["config"] and issubclass(v.__class__, napalm_yang.BaseBinding):
                continue

            try:
                mapping_element = mappings[k]
            except KeyError:
                if v.prefix == self.prefix:
                    raise KeyError("Couldn't find parser for field '{}'".format(k))
                else:
                    parse(self.device, k, v)
                    continue
            if issubclass(v.__class__, napalm_yang.List):
                self.parse_text_to_list(v, config, partial_config, mapping_element)
            elif issubclass(v.__class__, napalm_yang.BaseBinding):
                self.parse(v, config, partial_config, mapping_element)
            else:
                self.parse_text_to_attr(v, partial_config, mapping_element)

    def parse_text_to_list(self, model, config, partial_config, mappings):
        if "_block_capture" in mappings.keys():
            regexp = text_helpers.translate_string(mappings["_block_capture"], parent_key=self.key)
            block_matches = re.finditer(regexp, config, re.MULTILINE)
        elif "_subblock_capture" in mappings.keys():
            regexp = text_helpers.translate_string(mappings["_subblock_capture"],
                                                   parent_key=self.key)
            block_matches = re.finditer(regexp, partial_config, re.MULTILINE)

        for match in block_matches:
            name = match.group("key")
            self.key = name
            block_config = match.group("block")

            obj = model.get_element(name)

            self.parse(obj, config, block_config, mappings)

    def parse_text_to_attr(self, attr, config, mappings):
        if mappings["_type"] == "boolean":
            if "_absent" in mappings.keys():
                regexp = text_helpers.translate_string(mappings["_absent"], parent_key=self.key)
                match = re.search(regexp, config, re.MULTILINE)
                attr(match is None)
            elif "_present" in mappings.keys():
                regexp = text_helpers.translate_string(mappings["_present"], parent_key=self.key)
                match = re.search(regexp, config, re.MULTILINE)
                attr(match is not None)

            return
        else:
            regexp = text_helpers.translate_string(mappings["_search"], parent_key=self.key)
            match = re.search(regexp, config, re.MULTILINE)

        if match:
            if mappings["_type"] == "mapping":
                value = mappings["_map"][match.group("value")]
            else:
                value = match.group("value")
        else:
            value = mappings["_default"]

        try:
            attr(value)
        except ValueError:
            attr(eval(value))
