from napalm_yang.parsers.base import BaseParser

import re


class TextParser(BaseParser):

    @classmethod
    def _parse_list_block(cls, mapping):
        block_matches = re.finditer(mapping["regexp"], mapping["from"], re.MULTILINE + re.I)

        for match in block_matches:
            extra_vars = match.groupdict()
            key = extra_vars.pop("key")
            block = extra_vars.pop("block")
            yield key, block, extra_vars

    @classmethod
    def _parse_leaf_search(cls, mapping, check_default=True):
        match = re.search(mapping["regexp"], mapping["from"], re.MULTILINE + re.I)

        if match:
            return match.group("value")
        elif check_default:
            return mapping.get("default", None)
        else:
            return None

    @classmethod
    def _parse_leaf_is_present(cls, mapping):
        value = cls._parse_leaf_search(mapping, check_default=False)
        return bool(value)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping):
        value = cls._parse_leaf_search(mapping, check_default=False)
        return not bool(value)

    @classmethod
    def _parse_leaf_map(cls, mapping):
        value = cls._parse_leaf_search(mapping)
        return mapping["map"][value]
