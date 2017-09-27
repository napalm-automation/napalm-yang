import ast
import copy

from napalm_yang import helpers


def _flatten_dictionary(obj, path, key_name):
    """
    This method tries to use the path `?my_field` to convert:

    a:
        aa: 1
        ab: 2
    b:
        ba: 3
        ba: 4

    into:

    - my_field: a
      aa: 1
      ab: 2
    - my_field: b
      ba: 3
      ba: 4
    """
    result = []
    if ">" in key_name:
        key_name, group_key = key_name.split(">")
    else:
        group_key = None

    for k, v in obj.items():
        if path:
            if k == path[0]:
                path.pop(0)
        if k.startswith("#"):
            continue
        r = _resolve_path(v, list(path))

        if isinstance(r, dict):
            # You can either have a dict here, which means your path is like ?a.b
            # or a list, which means you have a path like ?a.?b
            r = [r]

        for e in r:
            if group_key:
                e[group_key] = {kk: vv for kk, vv in v.items() if kk not in path}
            e[key_name] = k
            result.append(e)
    return result


def _flatten_list(obj, path, key_name):
    new_key, key = key_name.split(":")
    result = []

    for o in obj:
        r = _resolve_path(o, list(path))

        if isinstance(r, dict):
            # XML gets confused when there is a list with only one element
            # and is treated as a dict when converting to a dict
            r = [r]
        old_value = o.pop(key)
        for e in r:
            e[new_key] = old_value
            merged_dict = dict({kk: vv for kk, vv in o.items() if kk not in path})
            merged_dict.update(e)
            result.append(merged_dict)

    return result


def _resolve_path(obj, path):
    if not path:
        return obj
    current = path.pop(0)
    if current[0] != "?":
        if isinstance(obj, dict):
            obj = obj[current]
        elif isinstance(obj, list):
            obj = obj[int(current)]
        return _resolve_path(obj, path)
    else:
        if isinstance(obj, dict) and ":" in current:
            # We assume that this is supposed to be a list but xmldict
            # turned a one element list into a dict
            obj = [obj]

        if isinstance(obj, dict):
            return _flatten_dictionary(obj, path, current[1:])
        elif isinstance(obj, list):
            return _flatten_list(obj, path, current[1:])


class BaseParser(object):

    def __init__(self, keys, extra_vars):
        self.keys = keys
        self.extra_vars = extra_vars

    def resolve_path(self, obj, path, default=None, check_presence=False):
        if path == "":
            return obj
        path = path.split(".")
        try:
            r = _resolve_path(obj, path)
        except (KeyError, IndexError):
            return default

        if check_presence:
            return not bool(path)
        return r

    def init_native(self, native):
        return native

    def parse_list(self, attribute, mapping, bookmarks):
        mapping = copy.deepcopy(mapping)
        mapping = helpers.resolve_rule(mapping, attribute, self.keys, self.extra_vars,
                                       None, process_all=False)
        for m in mapping:
            pdb = m.get("pdb", {})
            if pdb:
                import pdb
                pdb.set_trace()
                continue
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
            pdb = m.get("pdb", {})
            if pdb:
                import pdb
                pdb.set_trace()
                continue
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
            pdb = m.get("pdb", {})
            if pdb:
                import pdb
                pdb.set_trace()
                continue
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
