from napalm_yang import base


def model_to_dict(model):
    def get_key(key, model, parent_defining_module):
        key = "{} {}".format(key, "[rw]" if model._is_config else "[ro]")

        if parent_defining_module != model._defining_module:
            key = "{}:{}".format(model._defining_module, key)
        return key

    if model._yang_type in ("container", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model}
    elif model._yang_type in ("list", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model._contained_class()}
    else:
        return model._yang_type


def _diff_root(f, s):
    result = {}
    for k in f.elements():
        v = getattr(f, k)
        w = getattr(s, k)

        r = diff(v, w)
        if r:
            result[k] = diff(v, w)

    return result


def _diff_list(f, s):
    result = {}

    first_keys = set(f.keys())
    second_keys = set(s.keys())

    both = first_keys & second_keys
    first_only = first_keys - second_keys
    second_only = second_keys - first_keys

    both_dict = {}
    for k in both:
        r = diff(f[k], s[k])
        if r:
            both_dict[k] = r

    if both_dict:
        result["both"] = both_dict

    if first_only or second_only:
        result["first_only"] = list(first_only)
        result["second_only"] = list(second_only)

    return result


def diff(f, s):
    if isinstance(f, base.Root) or f._yang_type in ("container", None):
        result = _diff_root(f, s)
    elif f._yang_type in ("list", ):
        result = _diff_list(f, s)
    else:
        result = {}
        first = "{}".format(f)
        second = "{}".format(s)
        if first != second:
            result = {
                "first": first,
                "second": second,
            }

    return result
