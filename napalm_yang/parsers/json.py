from __future__ import absolute_import
from builtins import super

import re
import json

from napalm_yang.parsers.base import BaseParser


class JSONParser(BaseParser):

    @classmethod
    def init_native(cls, native):
        resp = []
        for k in native:
            if isinstance(k, str):
                resp.append(json.loads(k))
            else:
                resp.append(k)

        return super().init_native(resp)

    @classmethod
    def _parse_list_dict(cls, mapping, key=None):
        d = json.loads(mapping['from'])
        if isinstance(d, dict):
            for k, v in d.items():
                yield k, v, {}

    @classmethod
    def _parse_leaf_dict(cls, mapping, check_default=True, check_presence=False):
        d = mapping['from']
        if d and not check_presence:
            regexp = mapping.get('regexp', None)
            if regexp:
                match = re.search(mapping['regexp'], d)
                if match:
                    return match.group('value')
            else:
                return d
        else:
            if d and check_presence:
                return True
            if check_default:
                return mapping.get('default', None)
            return
        return

    @classmethod
    def _parse_leaf_map(cls, mapping):
        value = cls._parse_leaf_path(mapping)
        if value:
            return mapping['map'][value]
        else:
            return None

    @classmethod
    def _parse_leaf_is_present(cls, mapping):
        return cls._parse_leaf_path(mapping, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping):
        return not cls._parse_leaf_path(mapping, check_default=False, check_presence=True)
