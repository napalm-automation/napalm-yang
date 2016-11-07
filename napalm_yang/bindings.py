"""Code to attach bindings."""
import yang_types


def attach_childs(cls, ns):
    for k, v in cls.container.items():
        setattr(cls, k, ns[v]())

    for k, v in cls.leaf.items():
        # cls_name is of type 'yang:counter64'
        cls_name = v['type']['value'].split(':')[1]
        yang_type = getattr(yang_types, cls_name)
        options = v['type']['options']
        setattr(cls, k.replace('-', '_'), yang_type(options))
