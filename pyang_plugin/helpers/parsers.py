"""Some helpers functions to help rearranging YANG for easier templating."""
from utils import text_helpers


class FilterModule(object):
    """Useful jinja2 filters"""

    def filters(self):
        """Return jinja2 filters that this module provide."""
        return {
            'augment2class': augment2class,
            'yang2class': yang2class,
        }


def augment2class(augs):
    result = []
    i = 0
    for class_name, data in augs.items():
        name = "Augment_{}".format(i)
        i += 1

        s = class_name.split("/")
        s.pop(0)  # first element is empty
        extra_attrs = {
            'path': s,
        }

        result.append(yang2class(name, data, 'BaseAugment', extra_attrs))

    return result


def _parse_attrs(attrs):
    result = {}
    for a, d in attrs.items():
        for t, v in d["type"].items():
            arguments = []
            for argument_name, argument_value in v.items():
                arguments.append("{} = \"{}\"".format(argument_name, argument_value))

            arguments = ", ".join(arguments)
            attribute = "{}({})".format(text_helpers.safe_class_name(t), arguments)
        result[text_helpers.safe_attr_name(a)] = attribute
    return result


def _parse_container_attrs(attrs):
    return {text_helpers.safe_attr_name(a[0]): text_helpers.safe_class_name(a[1])
            for a in attrs.get("container", [])}


def yang2class(class_name, data, parent, extra_attrs):
    uses = [text_helpers.safe_class_name(x) for x in data.pop("uses", [])]
    uses.insert(0, parent)

    info = data.pop("info")

    result = {
        "name": text_helpers.safe_class_name(class_name),
        "docstring": info.pop("description", ""),
        "parent": ", ".join(uses),
        "super": uses,
        "attrs": {"{}".format(text_helpers.safe_attr_name(k)): v
                  for k, v in extra_attrs.items()},
        "container": _parse_container_attrs(data.pop("container", {})),
        "_meta": {}
    }

    result["_meta"]["when"] = data.pop("when", None)

    result["attrs"].update(_parse_attrs(data.pop("leaf", {})))
    result["attrs"].update(_parse_attrs(data.pop("leaf-list", {})))
    result["attrs"].update(_parse_attrs(data.pop("leaf-list", {})))

    if data or info:
        for k, v in data.items():
            for kk, vv in v.items():
                pass
                #  print(k, kk, vv)
        raise Exception("We forgot to parse something:\ndata: {}\ninfo:{}".format(data, info))

    return result
