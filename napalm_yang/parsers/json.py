from __future__ import absolute_import

import re
import json

from napalm_yang.parsers.base import BaseParser


class JSONParser(BaseParser):

    @classmethod
    def init_native(cls, native):
        resp = []
        for k in native:
            if isinstance(k, dict):
                resp.append(k)
            else:
                resp.append(json.loads(k))

        return resp

    @classmethod
    def _parse_list_default(cls, mapping, data, key=None):
        d = cls.resolve_path(data, mapping["path"], mapping.get("default"))

        regexp = mapping.get('regexp', None)
        if regexp:
            regexp = re.compile(regexp)
        if isinstance(d, dict):
            for k, v in d.items():
                if regexp:
                    match = regexp.match(k)
                    if match:
                        k = match.group('value')
                    else:
                        continue
                yield k, v, {}

    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
        d = cls.resolve_path(data, mapping["path"], mapping.get("default"))
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
    def _parse_container_default(cls, mapping, data):
        d = cls.resolve_path(data, mapping["path"], mapping.get("default"))
        return d, {}

    @classmethod
    def _parse_leaf_map(cls, mapping, data):
        v = cls._parse_leaf_default(mapping, data)
        return mapping['map'][v.lower()]

    @classmethod
    def _parse_leaf_is_present(cls, mapping, data):
        return cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, data):
        return not cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)
