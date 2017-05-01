class BaseTranslator(object):

    def __init__(self, merge, replace):
        self.merge = merge
        self.replace = replace

    def init_element(self, attribute, model, other, mapping, translation):
        for m in mapping:
            method_name = "_init_element_{}".format(m["mode"])
            t = getattr(self, method_name)(attribute, model, other, m, translation)
            if t is False:
                # if it's False we want to return None to signal we want to abort
                return None
            elif t is not None:
                return t

    def default_element(self, mapping, translation, replacing=False):
        for m in mapping:
            method_name = "_default_element_{}".format(m["mode"])
            getattr(self, method_name)(m, translation, replacing)

    def translate_leaf(self, attribute, model, other, mapping, translation):
        for m in mapping:
            method_name = "_translate_leaf_{}".format(m["mode"])
            getattr(self, method_name)(attribute, model, other, m, translation)

    def translate_container(self, attribute, model, other, mapping, translation):
        for m in mapping:
            method_name = "_translate_container_{}".format(m["mode"])
            t = getattr(self, method_name)(attribute, model, other, m, translation)
            if t is False:
                # if it's False we want to return None to signal we want to abort
                return None
            elif t is not None:
                return t

    def _translate_leaf_skip(self, attribute, model, other, mapping, translation):
        return translation

    _init_element_skip = _translate_leaf_skip
    _translate_leaf_gate = _translate_leaf_skip

    def _translate_container_gate(self, attribute, model, other, mapping, translation):
        return None

    _translate_container_skip = _translate_leaf_skip

    def _default_element_skip(self, mapping, translation, replacing):
        return None
