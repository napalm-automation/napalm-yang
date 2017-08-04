from napalm_yang import helpers
from napalm_yang.parsers import get_parser

import copy

import logging
logger = logging.getLogger("napalm-yang")


class Translator(object):

    def __init__(self, model, profile,
                 translation=None, keys=None, bookmarks=None,
                 merge=None, replace=None, other=None, extra_vars=None):
        self.model = model
        self.profile = profile
        self._defining_module = model._defining_module
        self._yang_name = model._yang_name

        self.translation = translation
        self.keys = keys or {"parent_key": None}
        self.extra_vars = extra_vars or {}

        self.merge = merge
        self.replace = replace
        self.other = other or merge or replace

        self.mapping = helpers.read_yang_map(model._defining_module, model._yang_name,
                                             self.profile, "translators")

        if self.mapping:
            translator = get_parser(self.mapping["metadata"]["processor"])
            self.translator = translator(merge=bool(merge), replace=bool(replace))

            if translation is None:
                self.translation = self.translator.init_translation(self.mapping["metadata"],
                                                                    self.translation)

        self.bookmarks = bookmarks or {"root_{}".format(self._yang_name): translation,
                                       "parent": translation}

    def translate(self):
        if not self.mapping:
            return ""
        self._translate(self._yang_name, self.model, self.mapping[self._yang_name],
                        self.translation, self.other)
        return self.translator.post_processing(self)

    def _translate(self, attribute, model, mapping, translation, other):
        logger.debug("Translating attribute: {}".format(model._yang_path()))

        if model._is_container in ("container", ):
            self._translate_container(attribute, model, mapping, translation, other)
        elif model._yang_type in ("list", ):
            self._translate_list(attribute, model, mapping, translation, other)
        else:
            self._translate_leaf(attribute, model, mapping, translation, other)

    def _translate_leaf(self, attribute, model, mapping, translation, other):
        rule = helpers.resolve_rule(mapping["_process"], attribute, self.keys, self.extra_vars,
                                    model, self.bookmarks, bool(self.replace), bool(self.merge))
        self.translator.translate_leaf(attribute, model, other, rule, translation, self.bookmarks)

    def _translate_container(self, attribute, model, mapping, translation, other):
        if model._yang_type:
            self.bookmarks["parent"] = translation

            rule = helpers.resolve_rule(mapping["_process"], attribute, self.keys, self.extra_vars,
                                        model, self.bookmarks, bool(self.replace), bool(self.merge))

            et, extra_vars = self.translator.translate_container(attribute, model, other, rule,
                                                                 translation, self.bookmarks)

            if et is None:
                return

            self.bookmarks[attribute] = et
            self.extra_vars.update(extra_vars)
        else:
            et = translation

        for k, v in model:
            logger.debug("Parsing attribute: {}".format(v._yang_path()))
            other_attr = getattr(other, k, None)
            if not v._is_config or k == "state":
                logger.debug("Skipping attribute: {}:{}".format(v._defining_module, attribute))
                continue

            if v._defining_module != self._defining_module and v._defining_module is not None:
                logger.debug("Skipping attribute: {}:{}".format(v._defining_module, attribute))
                translator = Translator(v, self.profile, et, self.keys, self.bookmarks, self.merge,
                                        self.replace, other_attr, self.extra_vars)
                translator.translate()
            else:
                self._translate(k, v, mapping[v._yang_name], et, other_attr)

    def _translate_list(self, attribute, model, mapping, translation, other):
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]
        old_extra_vars = copy.deepcopy(self.extra_vars)

        # We will use this to store blocks of configuration
        # for each individual element of the list
        self.bookmarks[attribute] = {}

        for key in model:
            element = model[key]
            logger.debug("Translating {} {}".format(attribute, key))

            try:
                other_element = other[key]
            except Exception:
                other_element = None

            key_name = "{}_key".format(attribute)
            self.keys[key_name] = key
            self.keys["parent_key"] = key

            translation_rule_negate = helpers.resolve_rule(mapping["_process"], attribute,
                                                           self.keys, self.extra_vars, element,
                                                           self.bookmarks, bool(self.replace),
                                                           bool(self.merge), True)
            translation_rule = helpers.resolve_rule(mapping["_process"], attribute,
                                                    self.keys, self.extra_vars, element,
                                                    self.bookmarks, bool(self.replace),
                                                    bool(self.merge), False)

            self.translator.default_element(translation_rule_negate, translation, self.bookmarks,
                                            replacing=True)
            et, extra_vars = self.translator.init_element(attribute, element, other_element,
                                                          translation_rule, translation,
                                                          self.bookmarks)

            if et is None:
                logger.info("Skipping {} as not implemented or objects are equal".format(attribute))
                continue

            self.bookmarks[attribute][key] = et
            self.bookmarks["parent"] = et
            self.extra_vars.update(extra_vars)

            self._translate(attribute, element, mapping, et, other_element)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark
        self.extra_vars = old_extra_vars

        if other:
            # Let's default elements not present in the model
            self._default_element_list(attribute, other, mapping, translation, model)

    def _default_element_list(self, attribute, running, mapping, translation, candidate):
        # we'll restore old values when we leave this branch
        old_extra_vars = copy.deepcopy(self.extra_vars)
        for key in running:
            logger.info("Defaulting {}: {}".format(attribute, key))
            element = running[key]

            candidate = candidate or {}

            if key not in candidate.keys():
                key_name = "{}_key".format(attribute)
                self.keys[key_name] = key
                self.keys["parent_key"] = key

                translation_rule = helpers.resolve_rule(mapping["_process"], attribute,
                                                        self.keys, self.extra_vars, element,
                                                        self.bookmarks, bool(self.replace),
                                                        bool(self.merge), True)

                extra_vars = self.translator.default_element(translation_rule, translation,
                                                             self.bookmarks)
                self.extra_vars.update(extra_vars)

                if any([t.get("continue_negating", False) for t in translation_rule]):
                    self._default_child(attribute, element, mapping, translation)

        # Restore state
        self.extra_vars = old_extra_vars

    def _default_child(self, attribute, running, mapping, translation):
        logger.debug("Defaulting child attribute: {}".format(running._yang_path()))

        if running._is_container in ("container", ):
            for k, v in running:
                if not v._is_config or k == "state":
                    continue
                elif v._defining_module != self._defining_module and v._defining_module is not None:
                    continue
                else:
                    self._default_child(k, v, mapping[v._yang_name], translation)
        elif running._yang_type in ("list", ):
            self._default_element_list(attribute, running, mapping, translation, None)
