import os
import copy

import yaml

from napalm_yang.parsers.text import TextExtractor
from napalm_yang.parsers.xml import XMLExtractor

from napalm_yang import text_helpers


import logging
logger = logging.getLogger("napalm-yang")


def get_parser(parser):
    parsers = {
        "TextExtractor": TextExtractor,
        "XMLExtractor": XMLExtractor,
        #  "TextTranslator": TextTranslator,
        #  "XMLTranslator": XMLTranslator,
    }
    return parsers[parser]


def find_yang_file(profile, filename, path):
    """
    Find the necessary file for the given test case.

    Args:
        device(napalm device connection): for which device
        filename(str): file to find
        path(str): where to find it relative to where the module is installed
    """
    # Find base_dir of submodule
    module_dir = os.path.dirname(__file__)
    full_path = os.path.join(module_dir, 'mappings', profile, path, filename)

    if os.path.exists(full_path):
        return full_path
    else:
        msg = "Couldn't find parsing file: {}".format(full_path)
        logger.error(msg)
        raise IOError(msg)


def read_yang_map(yang_prefix, attribute, profile, parser_path):
    logger.info("Finding parser for {}:{}".format(yang_prefix, attribute))
    filename = os.path.join(yang_prefix, "{}.yaml".format(attribute))

    try:
        filepath = find_yang_file(profile, filename, parser_path)
    except IOError:
        return

    with open(filepath, "r") as f:
        return yaml.load(f.read())


def _resolve_rule(rule, attribute, keys, extra_vars=None, translation_model=None,
                  parse_bookmarks=None):
    if isinstance(rule, list):
        raise Exception("Wrong rule for attr: {}. List can be used only on leafs".format(attribute))
    elif isinstance(rule, str):
        if rule in ["unnecessary", "not_implemented"]:
            return {"mode": "skip", "reason": rule}
        else:
            raise Exception("Not sure what to do with rule {} on attribute {}".format(rule,
                                                                                      attribute))
    kwargs = dict(keys)
    rule = dict(rule)
    kwargs["translation_model"] = translation_model
    kwargs["parse_bookmarks"] = parse_bookmarks
    kwargs["attribute"] = attribute
    kwargs["extra_vars"] = extra_vars

    for k, v in rule.items():
        if isinstance(v, dict):
            _resolve_rule(v, attribute, keys, extra_vars, translation_model, parse_bookmarks)
        elif isinstance(v, list):
            for e in k:
                _resolve_rule(e, attribute, keys, extra_vars, translation_model, parse_bookmarks)
        elif isinstance(v, str):
            rule[k] = text_helpers.template(v, **kwargs)

    if "when" in rule.keys():
        w = rule["when"]
        try:
            import ast
            w = ast.literal_eval(w)
        except Exception:
            w = True if w in ["true", "True"] else False
        if not w:
            return {"mode": "skip", "reason": "criteria failed"}
        rule["when"] = bool(w)

    return rule


class Parser(object):

    def __init__(self, model, profile, is_config,
                 config=None, keys=None, bookmarks=None, extra_vars=None):
        self.model = model
        self.profile = profile
        self.is_config = is_config
        self._defining_module = model._defining_module
        self._yang_name = model._yang_name

        parser_path = os.path.join("parsers", "config" if is_config else "state")
        self.mapping = read_yang_map(model._defining_module, model._yang_name,
                                     self.profile, parser_path)

        self.keys = keys or {"parent_key": None}
        self.extra_vars = extra_vars or {}

        if config:
            self.bookmarks = {self._yang_name: config, "parent": config}
            self.config = config
        else:
            # TODO
            pass

        self.bookmarks = bookmarks or self.bookmarks

        if self.mapping:
            self.parser = get_parser(self.mapping["metadata"]["parser"])

    def parse(self):
        if not self.mapping:
            return
        self._parse(self._yang_name, self.model, self.mapping[self._yang_name])

    def _parse(self, attribute, model, mapping):
        logger.debug("Parsing attribute: {}".format(model._yang_path()))

        if model._is_container in ("container", ):
            self._parse_container(attribute, model, mapping)
        elif model._yang_type in ("list", ):
            self._parse_list(attribute, model, mapping)
        else:
            self._parse_leaf(attribute, model, mapping)

    def _parse_container(self, attribute, model, mapping):
        mapping["_parse"] = _resolve_rule(mapping["_parse"], attribute, self.keys, self.extra_vars,
                                          None, self.bookmarks)
        for k, v in model:
            logger.debug("Parsing attribute: {}".format(v._yang_path()))
            if self.is_config and (not v._is_config or k == "state"):
                continue
            elif not self.is_config and (v._is_config or k == "config"):
                continue

            if v._defining_module != self._defining_module and v._defining_module is not None:
                logger.debug("Skipping attribute: {}:{}".format(v._defining_module, attribute))
                parser = Parser(v, self.profile, self.is_config, self.config,
                                self.keys, self.bookmarks, self.extra_vars)
                parser.parse()
            else:
                self._parse(k, v, mapping[k])

    def _parse_list(self, attribute, model, mapping):
        mapping_copy = copy.deepcopy(mapping)
        mapping_copy["_parse"] = _resolve_rule(mapping_copy["_parse"], attribute, self.keys,
                                               self.extra_vars, None, self.bookmarks)
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]
        old_parent_extra_vars = self.extra_vars

        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.bookmarks[attribute] = {}

        for key, block, extra_vars in self.parser.parse_list(mapping_copy["_parse"]):
            logger.debug("Parsing element {}[{}]".format(attribute, key))
            obj = model.add(key)

            key_name = "{}_key".format(attribute)
            self.keys[key_name] = key
            self.bookmarks[attribute][key] = block
            self.extra_vars[attribute] = extra_vars

            # These two are necessary in cases where an element may be present in subtrees. For
            # example, ipv4.config.enabled is present in both interfaces and subinterfaces
            self.keys["parent_key"] = key
            self.bookmarks["parent"] = block
            self.extra_vars = extra_vars

            element_mapping = copy.deepcopy(mapping)
            self._parse(key, obj, element_mapping)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark
        self.extra_vars = old_parent_extra_vars

    def _parse_leaf(self, attribute, model, mapping):
        mapping["_parse"] = _resolve_rule(mapping["_parse"], attribute, self.keys,
                                          self.extra_vars, None, self.bookmarks)

        # We can't set attributes that are keys
        if model._is_keyval:
            return

        value = self.parser.parse_leaf(mapping["_parse"])

        if value is None:
            setattr(model._parent, attribute, getattr(model, "default")())
        else:
            setattr(model._parent, attribute, value)
