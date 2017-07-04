from __future__ import absolute_import

import re
import json

from collections import OrderedDict

from napalm_yang.parsers.base import BaseParser


def get_element_with_cdata(dictionary, element):
    e = dictionary[element]
    if isinstance(e, OrderedDict):
        # this is for xmltodict
        return e["#text"]
    else:
        return e


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
        def _iterator(d, mapping):
            # key_element is necessary when we have lists of dicts
            key_element = mapping.get("key")

            if key_element and d:
                if key_element in d:
                    # xmltodict returns a dict when there is only one element
                    d = [d]

                key_element = mapping["key"]
                for v in d:
                    k = get_element_with_cdata(v, key_element)
                    yield k, v
            elif d:
                for k, v in d.items():
                    yield k, v

        d = cls.resolve_path(data, mapping["path"], mapping.get("default"))

        regexp = mapping.get('regexp', None)
        if regexp:
            regexp = re.compile(regexp)

        for k, v in _iterator(d, mapping):
            if regexp:
                match = regexp.match(k)
                if match:
                    k = match.group('value')
                else:
                    continue
            yield k, v, {}

    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
        d = cls.resolve_path(data, mapping["path"], mapping.get("default"), check_presence)
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
        if v:
            return mapping['map'][v.lower()]
        else:
            return

    @classmethod
    def _parse_leaf_is_present(cls, mapping, data):
        return cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, data):
        return not cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)
