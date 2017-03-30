from lxml import etree
import re

from napalm_yang.parsers.base import BaseParser


class XMLParser(BaseParser):

    @classmethod
    def _parse_list_xpath(cls, mapping):
        xml = etree.fromstring(mapping["from"])

        for element in xml.xpath(mapping["xpath"]):
            key = element.xpath("name")[0].text.strip()
            yield key, etree.tostring(element), {}

    @classmethod
    def _parse_leaf_xpath(cls, mapping, check_default=True, check_presence=False):
        xml = etree.fromstring(mapping["from"])
        element = xml.xpath(mapping["xpath"])

        if element and not check_presence:
            if "attribute" in mapping.keys():
                element = element[0].get(mapping["attribute"])
            else:
                element = element[0].text.strip()

            regexp = mapping.get("regexp", None)
            if regexp:
                match = re.search(mapping["regexp"], element)
                if match:
                    return match.group("value")
            else:
                return element
        elif element and check_presence:
            return True
        elif check_default:
            return mapping.get("default", None)
        else:
            return None

    @classmethod
    def _parse_leaf_map(cls, mapping):
        value = cls._parse_leaf_xpath(mapping)

        if "regex" in mapping.keys():
            value = re.search(mapping["regexp"], value).group("value")

        return mapping["map"][value] if value else None

    @classmethod
    def _parse_leaf_is_present(cls, mapping):
        return cls._parse_leaf_xpath(mapping, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping):
        return not cls._parse_leaf_xpath(mapping, check_default=False, check_presence=True)
