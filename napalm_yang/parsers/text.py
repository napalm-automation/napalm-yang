from napalm_yang.parsers.base import BaseParser

import itertools

import re


class TextParser(BaseParser):

    @classmethod
    def _parse_list_default(cls, mapping, data):
        block_matches = re.finditer(mapping["regexp"], data, re.MULTILINE + re.I)

        mandatory_elements = mapping.pop("mandatory", [])

        for match in itertools.chain(block_matches, mandatory_elements):
            if isinstance(match, dict):
                yield match["key"], match["block"] or "Aasd123asv", match["extra_vars"]
            else:
                composite_key = mapping.get("composite_key", None)
                forced_key = mapping.get("key", None)
                post_process_filter = mapping.get("post_process_filter", None)

                extra_vars = match.groupdict()
                block = extra_vars.pop("block")

                if composite_key:
                    key = " ".join([match.group(k) for k in composite_key])
                elif forced_key:
                    key = forced_key
                else:
                    key = extra_vars.pop("key")

                if post_process_filter:
                    key = cls._parse_post_process_filter(post_process_filter, key, extra_vars)

                extra_vars["_get_duplicates"] = mapping.get("flat", False)

                yield key, block, extra_vars

    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True):
        match = re.search(mapping["regexp"], data, re.MULTILINE + re.I)

        if match:
            return match.group("value")
        elif check_default:
            return mapping.get("default", None)
        else:
            return None

    @classmethod
    def _parse_leaf_is_present(cls, mapping, data):
        value = cls._parse_leaf_default(mapping, data, check_default=False)
        return bool(value)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, data):
        value = cls._parse_leaf_default(mapping, data, check_default=False)
        return not bool(value)

    @classmethod
    def _parse_leaf_map(cls, mapping, data):
        value = cls._parse_leaf_default(mapping, data)
        return mapping["map"][value]
