import ast

from napalm_yang.translators.xml import XMLTranslator

from lxml import etree


class JunosTranslator(XMLTranslator):

    def openconfig_vlan_vlan_members(
        self, attribute, model, other, mapping, translation, bookmarks
    ):
        vlans = ast.literal_eval(str(model))
        vlan_xml = translation.find("vlan") or etree.SubElement(translation, "vlan")
        for v in vlans:
            t = etree.SubElement(vlan_xml, "members")
            v = str(v)
            if v == "1..4094":
                v = "all"
            t.text = str(v)
