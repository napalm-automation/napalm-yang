from builtins import super

import napalm_yang
from napalm_yang import text_helpers

from lxml import etree


class BaseTranslator(object):

    def __init__(self, merge, replace):
        self.merge = merge
        self.replace = replace

    def init_element(self, attribute, model, other, mapping, translation):
        method_name = "_init_element_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def default_element(self, mapping, translation, replacing=False):
        method_name = "_default_element_{}".format(mapping["mode"])
        return getattr(self, method_name)(mapping, translation, replacing)

    def parse_leaf(self, attribute, model, other, mapping, translation):
        method_name = "_parse_leaf_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def parse_container(self, attribute, model, other, mapping, translation):
        method_name = "_parse_container_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def _parse_leaf_skip(self, attribute, model, other, mapping, translation):
        return translation
    _init_element_skip = _parse_leaf_skip
    _parse_container_skip = _parse_leaf_skip

    def _default_element_skip(self, mapping, translation, replacing):
        return


class XMLTranslator(BaseTranslator):

    def post_processing(self, translator):
        return etree.tounicode(translator.translation, pretty_print=True)

    def init_translation(self, metadata, translation):
        if "xml_root" in metadata.keys():
            return etree.Element(metadata["xml_root"])
        else:
            return translation

    def _init_element_container(self, attribute, model, other, mapping, translation):
        t = translation

        for element in mapping["container"].split("."):
            t = etree.SubElement(t, element)

        key_element = mapping.get("key_element", None)
        if key_element:
            key = etree.SubElement(t, key_element)
            key.text = "{}".format(mapping["key_value"])

        #  replace = mapping.get("replace", None)
        #  if replace:
            #  t.set("replace", "replace")

        return t

    _parse_container_container = _init_element_container

    def _default_element_container(self, mapping, translation, replacing):
        pass

    def _parse_leaf_element(self, attribute, model, other, mapping, translation, force=False):
        if model.value is None and not force:
            return

        try:
            # We want to make sure we capture None
            value = mapping["value"]
        except Exception:
            value = model.value

        e = etree.SubElement(translation, mapping["element"])

        if value is not None:
            e.text = "{}".format(value)


class TextTranslator(XMLTranslator):

    def init_translation(self, metadata, translation):
        if metadata.get("root", False):
            return etree.Element("configuration")
        return translation

    def post_processing(self, translator):
        return self._xml_to_text(translator.translation)

    def _parse_leaf_element(self, attribute, model, other, mapping, translation):
        force = False
        if self.merge and other:
            if model.value == other.value:
                return
            elif model.value is None:
                force = True
                mapping["value"] = mapping["negate"]

        mapping["element"] = "command"
        super()._parse_leaf_element(attribute, model, other, mapping, translation, force)

    def _init_element_container(self, attribute, model, other, mapping, translation):
        mapping["key_element"] = "command"
        return super()._init_element_container(attribute, model, other, mapping, translation)

    def _default_element_container(self, mapping, translation, replacing):
        if not self.merge and not self.replace:
            return

        if self.merge and replacing:
            return

        e = etree.SubElement(translation, "command")
        e.text = mapping["negate"]

    def _xml_to_text(self, xml, text=""):
        for element in xml:
            if element.tag == "command":
                text += element.text
            text += self._xml_to_text(element)
        return text


class TextTranslator2:

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
