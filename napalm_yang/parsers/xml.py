from lxml import etree
import re

from napalm_yang.parsers.base import BaseParser


class XMLParser(BaseParser):

    @classmethod
    def _parse_list_xpath(cls, mapping):
        xml = etree.fromstring(mapping["from"])

        for element in xml.xpath(mapping["xpath"]):
            key = element.xpath("name")[0].text
            yield key, etree.tostring(element), {}

    @classmethod
    def _parse_leaf_xpath(cls, mapping, check_default=True, check_presence=False):
        xml = etree.fromstring(mapping["from"])
        element = xml.xpath(mapping["xpath"])

        if element and not check_presence:
            regexp = mapping.get("regexp", None)
            if regexp:
                return re.search(mapping["regexp"], element[0].text).group("value")
            else:
                return element[0].text
        elif element and check_presence:
            return True
        elif check_default:
            return mapping.get("default", None)
        else:
            return None

    @classmethod
    def _parse_leaf_map(cls, mapping):
        value = cls._parse_leaf_xpath(mapping)
        value = re.search(mapping["regexp"], value).group("value")

        return mapping["map"][value]

    @classmethod
    def _parse_leaf_is_present(cls, mapping):
        return cls._parse_leaf_xpath(mapping, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping):
        return not cls._parse_leaf_xpath(mapping, check_default=False, check_presence=True)
