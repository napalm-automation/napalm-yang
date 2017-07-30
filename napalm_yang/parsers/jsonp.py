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

    def init_native(self, native):
        resp = []
        for k in native:
            if isinstance(k, dict):
                resp.append(k)
            else:
                resp.append(json.loads(k))

        return resp

    def _parse_list_default(self, mapping, data, key=None):
        def _eval_key(key_mapping, **kwargs):
            if "{{" in key_mapping:
                try:
                    return self._parse_post_process_filter(key_mapping, **kwargs)
                except Exception as e:
                    return "{}".format(e)
            else:
                return get_element_with_cdata(kwargs, key_mapping)

        def _iterator(d, key_mapping):
            if key_mapping and d:
                if isinstance(d, dict):
                    # xmltodict returns a dict when there is only one element
                    d = [d]
                for v in d:
                    if not isinstance(v, dict):
                        # Nothing to resolve
                        k = _eval_key(key_mapping)
                    else:
                        k = _eval_key(key_mapping, **v)
                    yield k, v
            elif d:
                # If there is no key_mapping we can only assume it's a dict
                # so the key is implicit
                for k, v in d.items():
                    yield k, v

        def _process_key_value(key, value, regexp, mapping):
            extra_vars = {}
            if regexp:
                match = regexp.match(key)
                if match:
                    key = match.group('value')
                    extra_vars = match.groupdict()
                else:
                    return None, {}
            return key, extra_vars

        d = self.resolve_path(data, mapping["path"], mapping.get("default"))

        regexp = mapping.get('regexp')
        if regexp:
            regexp = re.compile(regexp)

        for k, v in _iterator(d, mapping.get("key")):
            if k.startswith("#"):
                continue
            key, extra_vars = _process_key_value(k, v, regexp, mapping)
            if key:
                yield key, v, extra_vars

    def _parse_leaf_default(self, mapping, data, check_default=True, check_presence=False):
        if "path" in mapping:
            d = self.resolve_path(data, mapping["path"], mapping.get("default"), check_presence)
        else:
            d = None

        if "value" in mapping:
            d = self._parse_post_process_filter(mapping["value"], value=d)

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

    def _parse_container_default(self, mapping, data):
        d = self.resolve_path(data, mapping["path"], mapping.get("default"))
        return d, {}

    def _parse_leaf_map(self, mapping, data):
        v = self._parse_leaf_default(mapping, data)
        if v:
            return mapping['map'][v.lower()]
        else:
            return

    def _parse_leaf_is_present(self, mapping, data):
        return self._parse_leaf_default(mapping, data,
                                        check_default=False, check_presence=True) is True

    def _parse_leaf_is_absent(self, mapping, data):
        return not self._parse_leaf_is_present(mapping, data)
