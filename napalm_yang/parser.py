import os

import copy

from napalm_yang import helpers
from napalm_yang.parsers import get_parser

import logging
logger = logging.getLogger("napalm-yang")


class Parser(object):

    def __init__(self, model, device=None, profile=None, is_config=None,
                 native=None, keys=None, bookmarks=None, extra_vars=None):
        self.model = model
        self.device = device
        self.profile = profile or device.profile
        self.is_config = is_config
        self._defining_module = model._defining_module
        self._yang_name = model._yang_name

        parser_path = os.path.join("parsers", "config" if is_config else "state")
        self.mapping = helpers.read_yang_map(model._defining_module, model._yang_name,
                                             self.profile, parser_path)

        self.keys = keys or {"parent_key": None}
        self.extra_vars = extra_vars or {}

        if self.mapping and device:
            device_output = self._execute_methods(device,
                                                  self.mapping["metadata"].get("execute", []))

        else:
            device_output = []

        native = native or []

        self.native = []

        for n in native + device_output:
            if isinstance(n, basestring):
                self.native.append(n.replace("\r", ""))  # Parsing will be easier
            else:
                self.native.append(n)

        if not self.native:
            raise Exception("I don't have any data to operate with")

        if self.mapping:
            self.parser = get_parser(self.mapping["metadata"]["processor"])(self.keys,
                                                                            self.extra_vars)

        self.bookmarks = bookmarks or {}

    def _execute_methods(self, device, methods):
        result = []
        for m in methods:
            attr = device
            for p in m["method"].split("."):
                attr = getattr(attr, p)
            args = m.get("args", [])
            if not isinstance(args, list):
                raise TypeError("args must be type list, not type {}".format(type(args)))
            kwargs = m.get("kwargs", {})
            if not isinstance(kwargs, dict):
                raise TypeError("kwargs must be type dict, not type {}".format(type(kwargs)))
            r = attr(*args, **kwargs)

            if isinstance(r, dict) and all([isinstance(x, (str, unicode)) for x in r.values()]):
                # Some vendors like junos return commands enclosed by a key
                r = "\n".join(r.values())

            result.append(r)

        return result

    def parse(self):
        if not self.mapping:
            return
        self.native = self.parser.init_native(self.native)
        self.bookmarks["root_{}".format(self._yang_name)] = self.native
        if "parent" not in self.bookmarks:
            self.bookmarks["parent".format(self._yang_name)] = self.native
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
        mapping["_process"] = helpers.resolve_rule(mapping["_process"], attribute, self.keys,
                                                   self.extra_vars, None, self.bookmarks,
                                                   process_all=False)

        # Saving state
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]
        old_parent_extra_vars = self.extra_vars

        if model._yang_type is not None:
            # None means it's an element of a list
            block, extra_vars = self.parser.parse_container(mapping["_process"], self.bookmarks)

            if block is None:
                return
            elif block != "" or extra_vars:
                self.bookmarks["parent"] = block
                self.bookmarks[attribute] = block
                self.extra_vars[attribute] = extra_vars

        for k, v in model:
            logger.debug("Parsing attribute: {}".format(v._yang_path()))
            if self.is_config and (not v._is_config or k == "state"):
                continue
            elif not self.is_config and (v._is_config or k == "config") \
                    and v._yang_type not in ("container", "list"):
                continue

            if v._defining_module != self._defining_module and v._defining_module is not None:
                logger.debug("Skipping attribute: {}:{}".format(v._defining_module, attribute))
                parser = Parser(v, self.device, self.profile, self.is_config, self.native,
                                self.keys, self.bookmarks, self.extra_vars)
                parser.parse()
            else:
                self._parse(k, v, mapping[v._yang_name])

        # Restoring state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark
        self.extra_vars = old_parent_extra_vars

    def _parse_list(self, attribute, model, mapping):
        mapping_copy = copy.deepcopy(mapping)
        mapping_copy["_process"] = helpers.resolve_rule(mapping_copy["_process"], attribute,
                                                        self.keys, self.extra_vars, None,
                                                        self.bookmarks, process_all=False)
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]
        old_parent_extra_vars = self.extra_vars

        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.bookmarks[attribute] = {}

        for key, block, extra_vars in self.parser.parse_list(mapping_copy["_process"],
                                                             self.bookmarks):
            logger.debug("Parsing element {}[{}]".format(attribute, key))

            try:
                obj = model.add(key)
            except KeyError as e:
                if "is already defined as a list entry" in e.message and \
                   extra_vars.get("_get_duplicates"):
                    obj = model[key]
                else:
                    raise

            key_name = "{}_key".format(attribute)
            self.keys[key_name] = key
            self.bookmarks[attribute][key] = block
            self.extra_vars[attribute] = extra_vars

            # These two are necessary in cases where an element may be present in subtrees. For
            # example, ipv4.config.enabled is present in both interfaces and subinterfaces
            self.keys["parent_key"] = key
            self.bookmarks["parent"] = block
            self.extra_vars["parent"] = extra_vars

            element_mapping = copy.deepcopy(mapping)
            self._parse(key, obj, element_mapping)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark
        self.extra_vars = old_parent_extra_vars

    def _parse_leaf(self, attribute, model, mapping):
        mapping["_process"] = helpers.resolve_rule(mapping["_process"], attribute, self.keys,
                                                   self.extra_vars, None, self.bookmarks,
                                                   process_all=False)

        # We can't set attributes that are keys
        if model._is_keyval:
            return

        value = self.parser.parse_leaf(mapping["_process"], self.bookmarks)

        if value is not None:
            setter = getattr(model._parent, "_set_{}".format(attribute))
            try:
                setter(value)
            except ValueError:
                logger.error("Wrong value for {}: {}".format(attribute, value))
                raise

            # parent.model is now a new class
            model = getattr(model._parent, attribute)
            model._mchanged = True
