"""Code to attach bindings."""
import yang_types


# TODO This is actually duplicated, figure out how to best do this
def safe_class_name(value):
    """Return a safe class name. For example, from interface-state to InterfaceState"""
    return ''.join([t.title() for t in value.split('-')])


# TODO This is actually duplicated, figure out how to best do this
def safe_attr_name(value):
    """Return a safe attr name. For example, from in-octets to in_octets"""
    reserved_keywords = []
    if value in reserved_keywords:
        value = "{}_".format(value)
    return '_'.join([t for t in value.split('-')])


def attach_childs(cls, ns):
    def _attach_childs(cls, containers, leafs, lists, ns):
        for k, v in containers.items():
            setattr(cls, k, ns[v]())

        for k, v in leafs.items():
            # cls_name is of type 'yang:counter64'
            cls_name = v['type']['value'].split(':')[1]
            yang_type = getattr(yang_types, cls_name)
            options = v['type']['options']
            setattr(cls, safe_attr_name(k), yang_type(options))

        for k, v in lists.items():
            cls_name = safe_class_name(v)
            yang_type = ns[cls_name]
            setattr(cls, safe_attr_name(k), yang_types.yang_list(yang_type))

    _attach_childs(cls, cls.container, cls.leaf, cls.list, ns)

    grouping = ns['groupings']
    for u in cls.uses:
        _attach_childs(cls, grouping[u]['container'], grouping[u]['leaf'], grouping[u]['list'], ns)
