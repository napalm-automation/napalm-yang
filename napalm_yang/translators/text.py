from builtins import super

from napalm_yang.translators.xml import XMLTranslator

from lxml import etree

import napalm_yang


class TextTranslator(XMLTranslator):

    def init_translation(self, metadata, translation):
        if metadata.get("root", False):
            return etree.Element("configuration")
        return translation

    def post_processing(self, translator):
        return self._xml_to_text(translator.translation)

    def _translate_leaf_default(self, attribute, model, other, mapping, translation):
        force = False

        if model == other and not self.replace:
            return

        if not model._changed() and other is not None and not self.replace:
            force = True
            mapping["value"] = mapping["negate"]
        if not model._changed() and other is not None and self.replace:
            return

        mapping["element"] = "command"
        super()._translate_leaf_default(attribute, model, other, mapping, translation, force)

    def _init_element_default(self, attribute, model, other, mapping, translation):
        extra_vars = {}
        if other is not None:
            if not napalm_yang.utils.diff(model, other) and not self.replace:
                # If objects are equal we return None as that aborts translating
                # the rest of the object
                return False, {}

        if not model._changed() and other is not None and not self.replace:
            mapping["key_value"] = mapping["negate"]
        if not model._changed() and other is not None and self.replace:
            return translation, {}

        mapping["key_element"] = "command"
        mapping["container"] = model._yang_name

        for i in ('prefix', 'negate_prefix'):
            if i in mapping:
                extra_vars[i] = mapping.get(i)

        t = super()._init_element_default(attribute, model, other, mapping, translation)

        end = mapping.get("end", "")
        if end and t is not None:
            e = etree.SubElement(translation, "command")
            e.text = end

        return t, extra_vars

    def _default_element_default(self, mapping, translation, replacing):
        extra_vars = {}

        if (replacing or self.replace) and not mapping.get("replace", True):
            return None, {}

        if not self.merge and not self.replace:
            return None, {}

        if self.merge and replacing:
            return None, {}

        e = etree.SubElement(translation, "command")
        e.text = mapping["negate"]

        for i in ('prefix', 'negate_prefix'):
            if i in mapping:
                extra_vars[i] = mapping.get(i)

        return None, extra_vars

    def _xml_to_text(self, xml, text=""):
        for element in xml:
            if element.tag == "command" and element.text is not None:
                text += element.text
            text += self._xml_to_text(element)
        return text
