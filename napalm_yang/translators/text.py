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

    def _parse_leaf_element(self, attribute, model, other, mapping, translation):
        force = False

        if model == other and not self.replace:
            return

        if not model._changed() and other is not None and not self.replace:
            force = True
            mapping["value"] = mapping["negate"]
        if not model._changed() and other is not None and self.replace:
            return

        mapping["element"] = "command"
        super()._parse_leaf_element(attribute, model, other, mapping, translation, force)

    def _init_element_container(self, attribute, model, other, mapping, translation):
        if other is not None:
            if not napalm_yang.utils.diff(model, other) and not self.replace:
                # If objects are equal we return None as that aborts translating
                # the rest of the object
                return

        if not model._changed() and other is not None and not self.replace:
            print(attribute, model, other)
            mapping["key_value"] = mapping["negate"]
        if not model._changed() and other is not None and self.replace:
            return translation

        mapping["key_element"] = "command"
        mapping["container"] = model._yang_name
        return super()._init_element_container(attribute, model, other, mapping, translation)

    #  def _parse_container_container(self, attribute, model, other, mapping, translation):
    #      mapping["key_element"] = "container"
    #      mapping["container"] = model._yang_name
    #      return super()._init_element_container(attribute, model, other, mapping, translation)

    def _default_element_container(self, mapping, translation, replacing):
        if (replacing or self.replace) and not mapping.get("replace", True):
            return

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
