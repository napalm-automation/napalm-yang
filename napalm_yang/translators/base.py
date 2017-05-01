def _find_translation_point(rule, bookmarks, translation):
    if "in" in rule.keys():
        t = bookmarks
        for p in rule["in"].split("."):
            try:
                t = t[p]
            except TypeError:
                t = t[int(p)]
            translation = t
    return translation


class BaseTranslator(object):

    def __init__(self, merge, replace):
        self.merge = merge
        self.replace = replace

    def init_element(self, attribute, model, other, mapping, translation, bookmarks):
        for m in mapping:
            t = _find_translation_point(m, bookmarks, translation)
            method_name = "_init_element_{}".format(m["mode"])
            et = getattr(self, method_name)(attribute, model, other, m, t)
            if et is False:
                # if it's False we want to return None to signal we want to abort
                return None
            elif et is not None:
                return et

    def default_element(self, mapping, translation, bookmarks, replacing=False):
        for m in mapping:
            t = _find_translation_point(m, bookmarks, translation)
            method_name = "_default_element_{}".format(m["mode"])
            getattr(self, method_name)(m, t, replacing)

    def translate_leaf(self, attribute, model, other, mapping, translation, bookmarks):
        for m in mapping:
            t = _find_translation_point(m, bookmarks, translation)
            method_name = "_translate_leaf_{}".format(m["mode"])
            getattr(self, method_name)(attribute, model, other, m, t)

    def translate_container(self, attribute, model, other, mapping, translation, bookmarks):
        for m in mapping:
            t = _find_translation_point(m, bookmarks, translation)
            method_name = "_translate_container_{}".format(m["mode"])
            et = getattr(self, method_name)(attribute, model, other, m, t)
            if et is False:
                # if it's False we want to return None to signal we want to abort
                return None
            elif et is not None:
                return et

    def _translate_leaf_skip(self, attribute, model, other, mapping, translation):
        return translation

    _init_element_skip = _translate_leaf_skip
    _translate_leaf_gate = _translate_leaf_skip

    def _translate_container_gate(self, attribute, model, other, mapping, translation):
        return None

    _translate_container_skip = _translate_leaf_skip

    def _default_element_skip(self, mapping, translation, replacing):
        return None
