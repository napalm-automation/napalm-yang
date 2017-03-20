

class BaseParser(object):

    @classmethod
    def init_config(cls, config):
        return config

    @classmethod
    def parse_list(cls, mapping):
        method_name = "_parse_list_{}".format(mapping["mode"])
        for key, block, extra_vars in getattr(cls, method_name)(mapping):
            yield key, block, extra_vars

    @classmethod
    def parse_leaf(cls, mapping):
        method_name = "_parse_leaf_{}".format(mapping["mode"])
        return getattr(cls, method_name)(mapping)

    @classmethod
    def _parse_leaf_skip(cls, mapping):
        return

    @classmethod
    def _parse_list_skip(cls, mapping):
        return {}

    @classmethod
    def _parse_leaf_value(cls, mapping):
        return mapping["value"]

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
