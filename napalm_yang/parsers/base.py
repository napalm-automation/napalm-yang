from napalm_yang.helpers import template


class BaseParser(object):

    @staticmethod
    def resolve_bookmark(bookmarks, path):
        if path is None:
            return
        b = bookmarks
        for p in path.split("."):
            try:
                b = b[p]
            except TypeError:
                b = b[int(p)]
            bookmark = b
        return bookmark

    @classmethod
    def init_native(cls, native):
        return native

    @classmethod
    def parse_list(cls, mapping, bookmarks):
        for m in mapping:
            # parent will change as the tree is processed so we save it
            # so we can restore it
            parent = bookmarks["parent"]

            mandatory_elements = m.get("mandatory", [])
            for me in mandatory_elements:
                me["block"] = cls.resolve_bookmark(bookmarks, me["block"])

            data = cls.resolve_bookmark(bookmarks, m.get("from", "parent"))
            method_name = "_parse_list_{}".format(m.get("mode", "default"))
            for key, block, extra_vars in getattr(cls, method_name)(m, data):
                yield key, block, extra_vars

            # we restore the parent
            bookmarks["parent"] = parent

    @classmethod
    def parse_leaf(cls, mapping, bookmarks):
        for m in mapping:
            data = cls.resolve_bookmark(bookmarks, m.get("from", "parent"))
            method_name = "_parse_leaf_{}".format(m.get("mode", "default"))
            result = getattr(cls, method_name)(m, data)
            if result is not None:
                return result

    @classmethod
    def parse_container(cls, mapping, bookmarks):
        for m in mapping:
            # parent will change as the tree is processed so we save it
            # so we can restore it
            parent = bookmarks["parent"]
            data = cls.resolve_bookmark(bookmarks, m.get("from", "parent"))
            method_name = "_parse_container_{}".format(m.get("mode", "default"))
            result, extra_vars = getattr(cls, method_name)(m, data)
            if result or extra_vars:
                break

            # we restore the parent
            bookmarks["parent"] = parent
        return result, extra_vars

    @classmethod
    def _parse_leaf_skip(cls, mapping, bookmarks):
        return

    _parse_leaf_gate = _parse_leaf_skip

    @classmethod
    def _parse_container_skip(cls, mapping, bookmarks):
        return "", {}

    @classmethod
    def _parse_list_skip(cls, mapping, bookmarks):
        return {}

    _parse_list_gate = _parse_list_skip

    @classmethod
    def _parse_leaf_value(cls, mapping, bookmarks):
        return mapping["value"]

    @classmethod
    def _parse_container_gate(cls, mapping, bookmarks):
        """This basically stops parsing the tree by returning None"""
        return None, {}

    @classmethod
    def _parse_post_process_filter(cls, post_process_filter, key, extra_vars={}):
        kwargs = dict()
        kwargs['key'] = key
        kwargs["extra_vars"] = extra_vars
        key = template(post_process_filter, **kwargs)
        return key
