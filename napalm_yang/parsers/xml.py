from builtins import super

from napalm_yang.parsers.jsonp import JSONParser

import xmltodict


class XMLParser(JSONParser):

    @classmethod
    def init_native(cls, native):
        resp = []
        for n in native:
            if isinstance(n, dict):
                resp.append(n)
            else:
                resp.append(xmltodict.parse(n, force_cdata=True))

        return resp

    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
        attribute = mapping.get("attribute", None)
        if attribute:
            attribute = "@{}".format(attribute)
            mapping["path"] = "{}.{}".format(mapping["path"], attribute)
        elif not check_presence:
            mapping["path"] = "{}.{}".format(mapping["path"], "#text")
        return super()._parse_leaf_default(mapping, data, check_default, check_presence)
