from lxml import etree

import itertools

import re

from napalm_yang.parsers.base import BaseParser


class XMLParser(BaseParser):

    @classmethod
    def _parse_list_xpath(cls, mapping):
        xml = etree.fromstring(mapping["from"])

        mandatory_elements = mapping.pop("mandatory", [])

        for element in itertools.chain(xml.xpath(mapping["xpath"]), mandatory_elements):
            if isinstance(element, dict):
                yield element["key"], element["block"], element["extra_vars"]
            else:
                key = element.xpath(mapping["key"])[0].text.strip()
                yield key, etree.tostring(element), {}

    @classmethod
    def _parse_list_nested(cls, mapping):
        xml = etree.fromstring(mapping["from"])
        path = mapping["xpath"].split("/")
        iterators = []
        list_vars = []
        cls._parse_list_nested_recursive(xml, path, iterators, list_vars)
        return cls._parse_list_container_helper(mapping, iterators, xml, list_vars)

    @classmethod
    def _parse_list_nested_recursive(cls, xml, path, iterators, list_vars, cur_vars=None):
        """
        This helps parsing shit like:

            <protocols>
                <bgp>
                    <group>
                        <name>my_peers</name>
                        <neighbor>
                            <name>192.168.100.2</name>
                            <description>adsasd</description>
                            <peer-as>65100</peer-as>
                        </neighbor>
                        <neighbor>
                            <name>192.168.100.3</name>
                            <peer-as>65100</peer-as>
                        </neighbor>
                    </group>
                    <group>
                        <name>my_other_peers</name>
                        <neighbor>
                            <name>172.20.0.1</name>
                            <peer-as>65200</peer-as>
                        </neighbor>
                    </group>
                </bgp>
            </protocols>

        """
        cur_vars = dict(cur_vars) if cur_vars else {}
        if path:
            p = path[0]
            path = path[1:]
        else:
            for _ in xml:
                list_vars.append(cur_vars)
            iterators.append(xml)
            return xml

        if p.startswith("?"):
            for x in xml:
                key, var_path = p.split(".")
                cur_vars.update({key.lstrip("?"): x.xpath(var_path)[0].text})
                cls._parse_list_nested_recursive(x, path, iterators, list_vars, cur_vars)
        else:
            x = xml.xpath(p)
            cls._parse_list_nested_recursive(x, path, iterators, list_vars, cur_vars)

    @classmethod
    def _parse_list_container_helper(cls, mapping, iterators, root, list_vars=None):
        mandatory_elements = mapping.pop("mandatory", [])

        iterators = itertools.chain.from_iterable(iterators)

        for element in itertools.chain(iterators, mandatory_elements):
            if isinstance(element, dict):
                yield element["key"], element["block"], element["extra_vars"]
            else:
                key_name = "{}_name".format(root.tag if mapping.get("nested", False)
                                            else root[0].tag)
                extra_vars = {
                    key_name: element.tag
                }

                if list_vars:
                    extra_vars.update(list_vars.pop(0))

                composite_key = mapping.get("composite_key", None)
                forced_key = mapping.get("key", None)
                key_attribute = mapping.get("key_attribute", None)

                if composite_key:
                    key = " ".join([extra_vars[k] for k in composite_key])
                elif forced_key:
                    key = forced_key
                elif key_attribute:
                    key = element.xpath(key_attribute)[0].text.strip()
                else:
                    key = element.tag

                yield key, etree.tostring(element), extra_vars

    @classmethod
    def _parse_list_container(cls, mapping):
        xml = etree.fromstring(mapping["from"])
        xml = xml.xpath(mapping["xpath"])

        nested = mapping.get("nested", False)
        root = xml[0] if nested and len(xml) else xml

        return cls._parse_list_container_helper(mapping, [root], root)

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
