class BaseTranslator(object):

    def __init__(self, merge, replace):
        self.merge = merge
        self.replace = replace

    def init_element(self, attribute, model, other, mapping, translation):
        method_name = "_init_element_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def default_element(self, mapping, translation, replacing=False):
        method_name = "_default_element_{}".format(mapping["mode"])
        return getattr(self, method_name)(mapping, translation, replacing)

    def parse_leaf(self, attribute, model, other, mapping, translation):
        method_name = "_parse_leaf_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def parse_container(self, attribute, model, other, mapping, translation):
        method_name = "_parse_container_{}".format(mapping["mode"])
        return getattr(self, method_name)(attribute, model, other, mapping, translation)

    def _parse_leaf_skip(self, attribute, model, other, mapping, translation):
        return translation
    _init_element_skip = _parse_leaf_skip
    _parse_container_skip = _parse_leaf_skip

    def _default_element_skip(self, mapping, translation, replacing):
        return
