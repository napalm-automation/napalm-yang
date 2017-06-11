from napalm_yang.helpers import template


class BaseParser(object):

    @classmethod
    def init_native(cls, native):
        return native

    @classmethod
    def parse_list(cls, mapping):
        for m in mapping:
            method_name = "_parse_list_{}".format(m["mode"])
            for key, block, extra_vars in getattr(cls, method_name)(m):
                yield key, block, extra_vars

    @classmethod
    def parse_leaf(cls, mapping):
        for m in mapping:
            method_name = "_parse_leaf_{}".format(m["mode"])
            result = getattr(cls, method_name)(m)
            if result is not None:
                return result

    @classmethod
    def parse_container(cls, mapping):
        for m in mapping:
            method_name = "_parse_container_{}".format(m["mode"])
            result, extra_vars = getattr(cls, method_name)(m)
            if result or extra_vars:
                break
        return result, extra_vars

    @classmethod
    def _parse_leaf_skip(cls, mapping):
        return

    _parse_leaf_gate = _parse_leaf_skip

    @classmethod
    def _parse_container_skip(cls, mapping):
        return "", {}

    @classmethod
    def _parse_list_skip(cls, mapping):
        return {}

    _parse_list_gate = _parse_list_skip

    @classmethod
    def _parse_leaf_value(cls, mapping):
        return mapping["value"]

    @classmethod
    def _parse_container_gate(cls, mapping):
        """This basically stops parsing the tree by returning None"""
        return None, {}

    @classmethod
    def _parse_post_process_filter(cls, post_process_filter, key, extra_vars={}):
        kwargs = dict()
        kwargs['key'] = key
        kwargs["extra_vars"] = extra_vars
        key = template(post_process_filter, **kwargs)
        return key

    """
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
    """
