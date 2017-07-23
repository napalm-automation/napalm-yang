from __future__ import absolute_import

import copy
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
        def _iterator(d, key_element):
            # key_element is necessary when we have lists of dicts
            if key_element and d:
                if key_element in d:
                    # xmltodict returns a dict when there is only one element
                    d = [d]

                for v in d:
                    k = get_element_with_cdata(v, key_element)
                    yield k, v
            elif d:
                for k, v in d.items():
                    yield k, v

        def _process_key_value(key, value, regexp, mapping):
            key_value = mapping.get('key_value')
            composite_key = mapping.get('composite_key')
            if key_value:
                key = key_value
            elif regexp:
                match = regexp.match(key)
                if match:
                    key = match.group('value')
                else:
                    return

            if composite_key:
                key = " ".join([key for _ in range(0, composite_key)])
            return key

        d = cls.resolve_path(data, mapping["path"], mapping.get("default"))

        regexp = mapping.get('regexp')
        if regexp:
            regexp = re.compile(regexp)

        for k, v in _iterator(d, mapping.get("key")):
            expand_list = mapping.get("expand_list")
            if expand_list:
                dd = cls.resolve_path(v, expand_list)
                copied_data = copy.deepcopy(v)
                copied_data.pop(expand_list)
                for kk, vv in _iterator(dd, mapping.get("expanded_key")):
                    vv = {expand_list: vv}
                    vv.update(copied_data)
                    key = _process_key_value(kk, vv, regexp, mapping)
                    if key:
                        yield key, vv, {}
            else:
                key = _process_key_value(k, v, regexp, mapping)
                if key:
                    yield key, v, {}


    @classmethod
    def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
        if "value" in mapping:
            d = mapping["value"]
        elif "path" in mapping:
            d = cls.resolve_path(data, mapping["path"], mapping.get("default"), check_presence)
        else:
            d = None

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
        return cls._parse_leaf_default(mapping, data,
                                       check_default=False, check_presence=True) is True

    @classmethod
    def _parse_leaf_is_absent(cls, mapping, data):
        return not cls._parse_leaf_default(mapping, data, check_default=False, check_presence=True)
        return not cls._parse_leaf_is_present(mapping, data)
