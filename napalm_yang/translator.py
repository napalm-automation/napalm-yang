from napalm_yang import helpers


import logging
logger = logging.getLogger("napalm-yang")


class Translator(object):

    def __init__(self, model, profile,
                 translation=None, keys=None, bookmarks=None,
                 merge=None, replace=None, other=None):
        self.model = model
        self.profile = profile
        self._defining_module = model._defining_module
        self._yang_name = model._yang_name

        self.translation = translation
        self.keys = keys or {"parent_key": None}
        self.bookmarks = bookmarks or {self._yang_name: translation, "parent": translation}

        self.merge = merge
        self.replace = replace
        self.other = other or merge or replace

        self.mapping = helpers.read_yang_map(model._defining_module, model._yang_name,
                                             self.profile, "translators")

        if self.mapping:
            translator = helpers.get_parser(self.mapping["metadata"]["processor"])
            self.translator = translator(merge=bool(merge), replace=bool(replace))

            if translation is None:
                self.translation = self.translator.init_translation(self.mapping["metadata"],
                                                                    self.translation)

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

    def _translate_container(self, attribute, model, mapping, translation, other):
        if model._yang_type:
            self.bookmarks["parent"] = translation

            rule = helpers.resolve_rule(mapping["_process"], attribute, self.keys,
                                        None, model, self.bookmarks)

            et = self.translator.translate_container(attribute, model, other, rule,
                                                     translation, self.bookmarks)

            if et is None:
                return

            self.bookmarks[attribute] = et
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
                translator = Translator(v, self.profile, et, self.keys,
                                        self.bookmarks, self.merge, self.replace, other_attr)
                translator.translate()
            else:
                self._translate(v._yang_name, v, mapping[v._yang_name], et, other_attr)

    def _translate_list(self, attribute, model, mapping, translation, other):
        # Saving state to restore them later
        old_parent_key = self.keys["parent_key"]
        old_parent_bookmark = self.bookmarks["parent"]

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

            translation_rule = helpers.resolve_rule(mapping["_process"], attribute,
                                                    self.keys, None, element, self.bookmarks)

            self.translator.default_element(translation_rule, translation, self.bookmarks,
                                            replacing=True)
            et = self.translator.init_element(attribute, element, other_element, translation_rule,
                                              translation, self.bookmarks)

            if et is None:
                logger.info("Skipping {} as not implemented or objects are equal".format(attribute))
                continue

            self.bookmarks[attribute][key] = et
            self.bookmarks["parent"] = et

            self._translate(attribute, element, mapping, et, other_element)

        # Restore state
        self.keys["parent_key"] = old_parent_key
        self.bookmarks["parent"] = old_parent_bookmark

        if other:
            # Let's default elements not present in the model
            for key in other:
                element = other[key]
                if key not in model.keys():
                    key_name = "{}_key".format(attribute)
                    self.keys[key_name] = key
                    self.keys["parent_key"] = key

                    translation_rule = helpers.resolve_rule(mapping["_process"], attribute,
                                                            self.keys, None, element,
                                                            self.bookmarks)

                    self.translator.default_element(translation_rule, translation, self.bookmarks)

    def _translate_leaf(self, attribute, model, mapping, translation, other):
        rule = helpers.resolve_rule(mapping["_process"], attribute, self.keys, None, model,
                                    self.bookmarks)
        self.translator.translate_leaf(attribute, model, other, rule, translation, self.bookmarks)
