"""Code to attach bindings."""
import yang_types


def _resolve_path(path):
    if ":" in path:
        path = path.split(":")[-1]
    return path


def attach_childs(cls, ns):
    def _attach_childs(cls, containers, leafs, lists, ns):
        for k, v in containers.items():
            setattr(cls, k, ns[v]())

        for k, v in leafs.items():
            # cls_name is of type 'yang:counter64'
            cls_name = v['type']['value'].replace('Yang:', '')
            yang_type = getattr(yang_types, cls_name)
            options = v['type']['options']
            setattr(cls, k, yang_type(options))

        for k, v in lists.items():
            cls_name = v
            yang_type = ns[cls_name]
            setattr(cls, k, yang_types.Yang_list(yang_type))

    _attach_childs(cls, cls.container, cls.leaf, cls.list, ns)

    grouping = ns['groupings']
    for u in cls.uses:
        u = _resolve_path(u)
        _attach_childs(cls, grouping[u]['container'], grouping[u]['leaf'], grouping[u]['list'], ns)
