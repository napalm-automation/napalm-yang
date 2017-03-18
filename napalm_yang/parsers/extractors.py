from napalm_yang import text_helpers

from lxml import etree


import logging
import re


logger = logging.getLogger("napalm-yang")


class BaseExtractor(object):

    @classmethod
    def init_config(cls, config):
        return config

    @classmethod
    def _get_text(cls, texts, path, keys, extra_vars):
        vars = dict(keys)
        vars.update(extra_vars)

        path = [text_helpers.translate_string(p, **vars) for p in path.split(".")]

        for p in path:
            if isinstance(texts, str):
                return texts
            try:
                texts = texts[p]
            except TypeError:
                texts = texts[int(p)]
        return texts

    @classmethod
    def parse_list(cls, mapping, texts, keys, extra_vars):
        method_name = "_parse_list_{}".format(mapping["_list_extraction"]["mode"])
        for key, block, extra_vars in getattr(cls, method_name)(mapping, texts, keys, extra_vars):
            yield key, block, extra_vars

    @classmethod
    def parse_leaf(cls, mapping, texts, keys, extra_vars):
        method_name = "_parse_leaf_{}".format(mapping["_leaf_extraction"]["mode"])
        return getattr(cls, method_name)(mapping, texts, keys, extra_vars)

    @classmethod
    def _parse_leaf_key(cls, mapping, texts, keys, extra_vars):
        leaf_extraction = mapping["_leaf_extraction"]
        value = keys[leaf_extraction["value"]]

        if "regexp" in leaf_extraction.keys():
            value = re.search(mapping["_leaf_extraction"]["regexp"], value).group("value")
        return value

    @classmethod
    def _parse_list_not_implemented(cls, mapping, texts, keys, extra_vars):
        return {}

    @classmethod
    def _parse_leaf_not_implemented(cls, mapping, texts, keys, extra_vars):
        return


class XMLExtractor(BaseExtractor):

    @classmethod
    def init_config(cls, config):
        if isinstance(config, str):
            return etree.fromstring(config)
        else:
            return config

    @classmethod
    def _parse_list_xpath(cls, mapping, texts, keys, extra_vars):
        list_extraction = mapping["_list_extraction"]
        texts = cls._get_text(texts, list_extraction["from"], keys, extra_vars)

        for element in texts.xpath(list_extraction["xpath"]):
            key = element.xpath("name")[0].text
            yield key, element, {}

    @classmethod
    def _parse_leaf_xpath(cls, mapping, texts, keys, extra_vars,
                          check_default=True, check_presence=False):
        leaf_extraction = mapping["_leaf_extraction"]
        texts = cls._get_text(texts, leaf_extraction["from"], keys, extra_vars)

        element = texts.xpath(leaf_extraction["xpath"])

        if element and not check_presence:
            return element[0].text
        elif element and check_presence:
            return True
        elif check_default:
            return leaf_extraction["default"]
        else:
            return None

    @classmethod
    def _parse_leaf_map(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_xpath(mapping, texts, keys, extra_vars)
        value = re.search(mapping["_leaf_extraction"]["regexp"], value).group("value")

        return mapping["_leaf_extraction"]["map"][value]

    @classmethod
    def _parse_leaf_is_present(cls, mapping, texts, keys, extra_vars):
        return cls._parse_leaf_xpath(mapping, texts, keys, extra_vars,
                                     check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, texts, keys, extra_vars):
        return not cls._parse_leaf_xpath(mapping, texts, keys, extra_vars,
                                         check_default=False, check_presence=True)


class TextExtractor(BaseExtractor):

    @classmethod
    def _parse_list_block(cls, mapping, texts, keys, extra_vars):
        list_extraction = mapping["_list_extraction"]
        texts = cls._get_text(texts, list_extraction["from"], keys, extra_vars)
        block_regexp = list_extraction["regexp"]

        regexp = text_helpers.translate_string(block_regexp, **keys)
        block_matches = re.finditer(regexp, texts, re.MULTILINE)

        for match in block_matches:
            extra_vars = match.groupdict()
            key = extra_vars.pop("key")
            block = extra_vars.pop("block")
            yield key, block, extra_vars

    @classmethod
    def _parse_leaf_search(cls, mapping, texts, keys, extra_vars, check_default=True):
        leaf_extraction = mapping["_leaf_extraction"]
        texts = cls._get_text(texts, leaf_extraction["from"], keys, extra_vars)
        regexp = text_helpers.translate_string(leaf_extraction["regexp"], **keys)

        match = re.search(regexp, texts, re.MULTILINE)

        if match:
            return match.group("value")
        elif check_default:
            return mapping["_leaf_extraction"]["default"]
        else:
            return None

    @classmethod
    def _parse_leaf_is_present(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars, check_default=False)
        return bool(value)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars, check_default=False)
        return not bool(value)

    @classmethod
    def _parse_leaf_map(cls, mapping, texts, keys, extra_vars):
        value = cls._parse_leaf_search(mapping, texts, keys, extra_vars)
        return mapping["_leaf_extraction"]["map"][value]

    @classmethod
    def _parse_leaf_extra_vars(cls, mapping, texts, keys, extra_vars):
        leaf_extraction = mapping["_leaf_extraction"]
        return cls._get_text(extra_vars, leaf_extraction["var"], keys, extra_vars)
