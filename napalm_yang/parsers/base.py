import ast
import copy

from napalm_yang import helpers


class BaseParser(object):

    def __init__(self, keys, extra_vars):
        self.keys = keys
        self.extra_vars = extra_vars

    def resolve_path(self, my_dict, path, default=None, check_presence=False):
        if path is None:
            return

        b = my_dict
        path_split = path.split(".") if len(path) else []
        result = None

        while True:
            if not path_split:
                break
            p = path_split.pop(0)
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
                    if not isinstance(v, dict):
                        result.append((k, v))
                        continue
                    r = self.resolve_path(v, ".".join(path_split), default, check_presence)
                    if not r:
                        break
                    if isinstance(r, list):
                        for rr in r:
                            rr[p[1:]] = k
                            if isinstance(v, dict):
                                for kk, vv in v.items():
                                    if kk != path_split[0] and path_split[0][0] != "?":
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
        if check_presence:
            return not path_split

        if not result:
            result = b

        return result

    def init_native(self, native):
        return native

    def parse_list(self, attribute, mapping, bookmarks):
        mapping = copy.deepcopy(mapping)
        mapping = helpers.resolve_rule(mapping, attribute, self.keys, self.extra_vars,
                                       None, process_all=False)
        for m in mapping:
            # parent will change as the tree is processed so we save it
            # so we can restore it
            parent = bookmarks["parent"]

            data = self.resolve_path(bookmarks, m.get("from", "parent"))

            for key, block, extra_vars in self._parse_list_default(attribute, m, data):
                yield key, block, extra_vars

            # we restore the parent
            bookmarks["parent"] = parent

    def parse_leaf(self, attribute, mapping, bookmarks):
        mapping = helpers.resolve_rule(mapping, attribute, self.keys,
                                       self.extra_vars, None, process_all=False)
        for m in mapping:
            data = self.resolve_path(bookmarks, m.get("from", "parent"))
            result = self._parse_leaf_default(attribute, m, data)

            if result is not None:
                try:
                    result = ast.literal_eval(result)
                except (ValueError, SyntaxError):
                    pass
                return result

    def parse_container(self, attribute, mapping, bookmarks):
        mapping = helpers.resolve_rule(mapping, attribute, self.keys, self.extra_vars, None,
                                       process_all=False)
        for m in mapping:
            # parent will change as the tree is processed so we save it
            # so we can restore it
            parent = bookmarks["parent"]
            data = self.resolve_path(bookmarks, m.get("from", "parent"))
            result, extra_vars = self._parse_container_default(attribute, m, data)
            if result or extra_vars:
                break

            # we restore the parent
            bookmarks["parent"] = parent
        return result, extra_vars

    def _parse_post_process_filter(self, post_process_filter, **kwargs):
        kwargs.update(self.keys)
        return helpers.template(post_process_filter, extra_vars=self.extra_vars, **kwargs)
