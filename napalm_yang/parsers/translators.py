import napalm_yang
from napalm_yang import text_helpers

from lxml import etree


class BaseTranslator(object):

    @classmethod
    def init_element(cls, attribute, model, mapping, translation):
        print(mapping)
        method_name = "_init_element_{}".format(mapping["mode"])
        return getattr(cls, method_name)(attribute, model, mapping, translation)

    @classmethod
    def parse_leaf(cls, attribute, model, mapping, translation):
        method_name = "_parse_leaf_{}".format(mapping["mode"])
        return getattr(cls, method_name)(attribute, model, mapping, translation)

    @classmethod
    def parse_container(cls, attribute, model, mapping, translation):
        method_name = "_parse_container_{}".format(mapping["mode"])
        return getattr(cls, method_name)(attribute, model, mapping, translation)

    @classmethod
    def _parse_leaf_skip(cls, attribute, model, mapping, translation):
        return translation
    _init_element_skip = _parse_leaf_skip
    _parse_container_skip = _parse_leaf_skip


class XMLTranslator(BaseTranslator):

    @classmethod
    def post_processing(cls, translator):
        return etree.tounicode(translator.translation, pretty_print=True)

    @classmethod
    def init_translation(cls, metadata, translation):
        if "xml_root" in metadata.keys():
            return etree.Element(metadata["xml_root"])
        else:
            return translation

    @classmethod
    def _init_element_container(cls, attribute, model, mapping, translation):
        t = translation

        condition = mapping.get("when", None)
        if condition:
            value = model

            for attr in condition.split("."):
                value = getattr(value, attr)

            if not value:
                return t

        for element in mapping["container"].split("."):
            t = etree.SubElement(t, element)

        key_element = mapping.get("key_element", None)
        if key_element:
            attr = model

            for e in mapping["key_value"].split("."):
                attr = getattr(attr, e)

            key = etree.SubElement(t, key_element)
            key.text = "{}".format(attr.value)

        replace = mapping.get("replace", None)
        if replace:
            t.set("replace", "replace")

        return t

    _parse_container_container = _init_element_container

    @classmethod
    def _parse_leaf_element(cls, attribute, model, mapping, translation):
        if not model.value:
            return

        value = mapping.get("format_value", model.value)

        e = etree.SubElement(translation, mapping["element"])
        e.text = "{}".format(value)

    @classmethod
    def _parse_leaf_if_false(cls, attribute, model, mapping, translation):
        if not model.value:
            return cls._init_element_container(attribute, model, mapping, translation)

    @classmethod
    def _parse_leaf_if_true(cls, attribute, model, mapping, translation):
        if model.value:
            return cls._init_element_container(attribute, model, mapping, translation)


class TextTranslator:

    def translate(self, obj, translation_map, previous=None):
        return self._translate_yang_model(obj, translation_map, previous, None, None)

    def _translate_yang_model(self, obj, translation_map, previous, key, parent_key):
        translation = ""
        for k, v in obj.items():
            previous_v = getattr(previous, k) if previous is not None else None
            if issubclass(v.__class__, napalm_yang.List):
                translation += self._yang_translate_list(v, translation_map[k], previous_v, key)
            else:
                if issubclass(v.__class__, napalm_yang.BaseBinding):
                    if not v._meta["config"]:
                        continue
                    translation += self._translate_yang_model(getattr(obj, k), translation_map[k],
                                                              previous_v, key, parent_key)

                value = getattr(obj, k)
                p_value = getattr(previous, k) if previous else None
                if previous and value == p_value:
                    # If we have a previous element and their values are equal
                    # let's skip this as we are merging
                    continue

                if not value:
                    string = translation_map[k].get("_remove", "")
                else:
                    string = translation_map[k].get("_string", "")

                translation += self._yang_translate_string(string,
                                                           value=getattr(obj, k), key=key,
                                                           parent_key=parent_key)
                translation += self._yang_translate_map(translation_map[k].get("_map", {}),
                                                        value=getattr(obj, k), key=key,
                                                        parent_key=parent_key)

        return translation

    def _yang_translate_list(self, l, translation_map, previous, parent_key):
        translation = ""

        if previous is not None:
            for k in previous.keys():
                if k not in l.keys():
                    translation += text_helpers.translate_string(translation_map.get("_remove", ""),
                                                                 key=k)

        for element_key, element_data in l.items():
            previous_element = previous.get(element_key, None) if previous is not None else None

            translation += self._yang_translate_string(translation_map.get("_string", ""),
                                                       key=element_key, parent_key=parent_key)
            translation += self._translate_yang_model(element_data, translation_map,
                                                      previous_element, element_key, parent_key)

        return translation

    def _yang_translate_map(self, m, value, **kwargs):
        if m:
            return self._yang_translate_string(m[str(value)]["_string"], value=value, **kwargs)
        else:
            return ""

    def _yang_translate_string(self, string, **kwargs):
        if string:
            return string.format(**kwargs)
        else:
            return ""
