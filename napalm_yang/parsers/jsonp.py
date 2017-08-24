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

    def _parse_list_default(self, attribute, mapping, data, key=None):
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

        if any([x in mapping for x in ["skip", "gate"]]):
            return

        d = self.resolve_path(data, mapping.get("path", ""), mapping.get("default"))

        regexp = mapping.get('regexp')
        if regexp:
            regexp = re.compile(regexp)

        for k, v in _iterator(d, mapping.get("key")):
            if k.startswith("#"):
                continue
            key, extra_vars = _process_key_value(k, v, regexp, mapping)
            if key:
                extra_vars.update(mapping.get("extra_vars", {}))
                yield key, v, extra_vars

    def _parse_leaf_default(self, attribute, mapping, data):
        if any([x in mapping for x in ["skip", "gate"]]):
            return

        present = mapping.get("present", None)
        check_presence = present is not None

        if "path" in mapping:
            d = self.resolve_path(data, mapping["path"], mapping.get("default"), check_presence)
        else:
            d = None

        if "value" in mapping:
            d = self._parse_post_process_filter(mapping["value"], value=d)

        if d:
            regexp = mapping.get('regexp', None)
            if regexp:
                match = re.search(mapping['regexp'], d)
                d = match.group('value') if match else None

        if d and "map" in mapping:
            d = mapping['map'][d.lower()]

        if check_presence:
            d = bool(d and present or not d and not present)

        d = mapping.get('default', None) if d is None else d
        return d

    def _parse_container_default(self, attribute, mapping, data):
        if "skip" in mapping:
            return "", {}
        elif "gate" in mapping:
            return None, {}

        d = self.resolve_path(data, mapping["path"], mapping.get("default"))
        return d, {}
