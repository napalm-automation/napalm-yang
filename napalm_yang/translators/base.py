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
        et = translation
        extra_vars = {}
        for m in mapping:
            mode = m.get("mode", "default")
            if mode == "skip":
                continue
            elif mode == "gate":
                return None, {}

            t = _find_translation_point(m, bookmarks, et)
            method_name = "_init_element_{}".format(mode)
            et = getattr(self, method_name)(attribute, model, other, m, t)
            if isinstance(et, tuple):
                extra_vars = et[1]
                et = et[0]
            if et is False:
                # if it's False we want to return None to signal we want to abort
                return None, {}
        return et, extra_vars

    def default_element(self, mapping, translation, bookmarks, replacing=False):
        t = translation
        extra_vars = {}
        for m in mapping:
            mode = m.get("mode", "default")
            if mode == "skip":
                continue
            elif mode == "gate":
                return {}

            t = _find_translation_point(m, bookmarks, t)
            method_name = "_default_element_{}".format(mode)
            t, ev = getattr(self, method_name)(m, t, replacing)
            extra_vars.update(ev)
        return extra_vars

    def translate_leaf(self, attribute, model, other, mapping, translation, bookmarks):
        for m in mapping:
            mode = m.get("mode", "default")
            if mode == "skip":
                continue
            elif mode == "gate":
                return

            t = _find_translation_point(m, bookmarks, translation)
            method_name = "_translate_leaf_{}".format(mode)
            getattr(self, method_name)(attribute, model, other, m, t)

    def translate_container(self, attribute, model, other, mapping, translation, bookmarks):
        et = translation
        extra_vars = {}
        for m in mapping:
            mode = m.get("mode", "default")
            if mode == "skip":
                continue
            elif mode == "gate":
                return None, {}

            t = _find_translation_point(m, bookmarks, et)
            method_name = "_translate_container_{}".format(mode)
            et = getattr(self, method_name)(attribute, model, other, m, t)
            if isinstance(et, tuple):
                extra_vars = et[1]
                et = et[0]
            if et is False:
                # if it's False we want to return None to signal we want to abort
                return None, {}
        return et, extra_vars
