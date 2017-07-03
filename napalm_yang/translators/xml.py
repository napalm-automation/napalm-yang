from napalm_yang.translators.base import BaseTranslator

from lxml import etree


class XMLTranslator(BaseTranslator):

    def post_processing(self, translator):
        return etree.tounicode(translator.translation, pretty_print=True)

    def init_translation(self, metadata, translation):
        if "xml_root" in metadata.keys():
            return etree.Element(metadata["xml_root"])
        else:
            return translation

    def _init_element_default(self, attribute, model, other, mapping, translation):
        t = translation

        for element in mapping["container"].split("/"):
            try:
                if mapping.get("reuse", False):
                    t = t.xpath(element)[0]
                else:
                    t = etree.SubElement(t, element)
            except IndexError:
                t = etree.SubElement(t, element)

        key_element = mapping.get("key_element", None)
        if key_element:
            key = etree.SubElement(t, key_element)

            value = mapping.get("key_value", None)
            if value:
                key.text = value

        replace = mapping.get("replace", None)
        if replace and self.replace:
            t.set("replace", "replace")

        return t

    _translate_container_default = _init_element_default

    def _default_element_default(self, mapping, translation, replacing):
        if not self.merge:
            return None, {}

        if self.merge and replacing:
            return None, {}

        t = translation

        for element in mapping["container"].split("."):
            t = etree.SubElement(t, element)

        key_element = mapping.get("key_element", None)
        if key_element:
            key = etree.SubElement(t, key_element)
            key.text = "{}".format(mapping["key_value"])

        if mapping.get("delete_on_merge", True):
            t.set("delete", "delete")

        return t, {}

    def _translate_leaf_default(self, attribute, model, other, mapping, translation, force=False):
        delete = False
        if not model._changed() and other and self.merge:
            delete = True
        elif not model._changed() and not force:
            return

        try:
            # We want to make sure we capture None
            value = mapping["value"]
        except Exception:
            value = None if not model._changed() else model

        e = translation
        for element in mapping["element"].split("/"):
            e = etree.SubElement(e, element)

        if delete:
            e.set("delete", "delete")

        if value is not None:
            e.text = "{}".format(value)

    def _translate_leaf_map(self, attribute, model, other, mapping, translation):
        mapping["value"] = mapping["map"][model]
        self._translate_leaf_default(attribute, model, other, mapping, translation)
