from lxml import etree

import itertools

import re

from napalm_yang.parsers.base import BaseParser


class XMLParser(BaseParser):

    @classmethod
    def init_native(cls, native):
        r = []
        for n in native:
            if hasattr(n, "xpath"):
                r.append(n)
            else:
                r.append(etree.fromstring(n))
        return r

    @classmethod
    def _parse_list_default(cls, mapping, data):
        post_process_filter = mapping.pop("post_process_filter", None)

        for element in data.xpath(mapping["xpath"]):
            key = element.xpath(mapping["key"])[0].text.strip()
            if post_process_filter:
                key = cls._parse_post_process_filter(post_process_filter, key)
            yield key, element, {}

    @classmethod
    def _parse_list_nested(cls, mapping, data):
        path = mapping["xpath"].split("/")
        iterators = []
        list_vars = []
        cls._parse_list_nested_recursive(data, path, iterators, list_vars)
        return cls._parse_list_container_helper(mapping, iterators, data, list_vars)

    @classmethod
    def _parse_list_nested_recursive(cls, data, path, iterators, list_vars, cur_vars=None):
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
            for _ in data:
                list_vars.append(cur_vars)
            iterators.append(data)
            return data

        if p.startswith("?"):
            for x in data:
                key, var_path = p.split(".")
                cur_vars.update({key.lstrip("?"): x.xpath(var_path)[0].text})
                cls._parse_list_nested_recursive(x, path, iterators, list_vars, cur_vars)
        else:
            x = data.xpath(p)
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
                post_process_filter = mapping.pop("post_process_filter", None)

                if composite_key:
                    key = " ".join([extra_vars[k] for k in composite_key])
                elif forced_key:
                    key = forced_key
                elif key_attribute:
                    key = element.xpath(key_attribute)[0].text.strip()
                else:
                    key = element.tag

                if post_process_filter:
                    key = cls._parse_post_process_filter(post_process_filter, key, extra_vars)

                yield key, element, extra_vars

    @classmethod
    def _parse_list_container(cls, mapping, data):
        data = data.xpath(mapping["xpath"])

        nested = mapping.get("nested", False)
        root = data[0] if nested and len(data) else data

        return cls._parse_list_container_helper(mapping, [root], root)

    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
        element = data.xpath(mapping["xpath"])

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
    def _parse_leaf_map(cls, mapping, data):
        value = cls._parse_leaf_default(mapping, data)

        if "regex" in mapping.keys():
            value = re.search(mapping["regexp"], value).group("value")

        return mapping["map"][value] if value else None

    @classmethod
    def _parse_leaf_is_present(cls, mapping, data):
        return cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, data):
        return not cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)
