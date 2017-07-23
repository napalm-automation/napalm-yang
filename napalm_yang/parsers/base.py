from napalm_yang.helpers import template


class BaseParser(object):

    @classmethod
    def resolve_path(cls, my_dict, path, default=None, check_presence=False):
        if path is None:
            return

        b = my_dict
        path_split = path.split(".") if len(path) else []
        result = None

        for i, p in enumerate(path_split):
            if p[0] == "?":
                result = [] if result is None else result

                if isinstance(b, dict) and ":" not in p:
                    iterator = b.items()
                else:
                    if isinstance(b, dict):
                        b = [b]
                    p, var_name = p.split(":")
                    try:
                        iterator = {e[var_name]: e for e in b}.items()
                    except Exception:
                        iterator = {e[var_name]["#text"]: e for e in b}.items()

                for k, v in iterator:
                    if k.startswith("#"):
                        continue
                    r = cls.resolve_path(v, ".".join(path_split[i+1:]), default, check_presence)
                    if isinstance(r, list):
                        for rr in r:
                            rr[p[1:]] = k
                            for kk, vv in v.items():
                                if kk != path_split[i+1]:
                                    rr[kk] = vv
                            result.append(rr)
                    else:
                        r[p[1:]] = k
                        result.append(r)
                break
            try:
                if isinstance(b, dict):
                    b = b[p]
                elif isinstance(b, list):
                    b = b[int(p)]
                elif p == "#text":
                    continue
                else:
                    raise Exception(b)
            except (KeyError, TypeError, IndexError, ValueError):
                return default
        else:
            if check_presence:
                return i == len(path_split) - 1

        if not result:
            result = b

        return result

    @classmethod
    def init_native(cls, native):
        return native

    @classmethod
    def parse_list(cls, mapping, bookmarks):
        for m in mapping:
            # parent will change as the tree is processed so we save it
            # so we can restore it
            parent = bookmarks["parent"]

            data = cls.resolve_path(bookmarks, m.get("from", "parent"))
            method_name = "_parse_list_{}".format(m.get("mode", "default"))

            if method_name == "_parse_list_manual":
                m["block"] = cls.resolve_path(bookmarks, m["block"],
                                              default=m["block"])

            for key, block, extra_vars in getattr(cls, method_name)(m, data):
                yield key, block, extra_vars

            # we restore the parent
            bookmarks["parent"] = parent

    @classmethod
    def _parse_list_manual(cls, mapping, data):
        yield mapping["key"], mapping["block"], mapping["extra_vars"]

    @classmethod
    def parse_leaf(cls, mapping, bookmarks):
        for m in mapping:
            data = cls.resolve_path(bookmarks, m.get("from", "parent"))
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
            data = cls.resolve_path(bookmarks, m.get("from", "parent"))
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
