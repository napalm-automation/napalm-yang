from napalm_yang.translator.xml import XMLTranslator

from lxml import etree


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
