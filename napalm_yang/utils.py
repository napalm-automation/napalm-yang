from napalm_yang import base


def model_to_dict(model, mode=""):
    """
    Given a model, return a representation of the model in a dict.

    This is mostly useful to have a quick visual represenation of the model.

    Args:

        model (PybindBase): Model to transform.
        mode (string): Whether to print config, state or all elements ("" for all)

    Returns:

        dict: A dictionary representing the model.

    Examples:


        >>> config = napalm_yang.base.Root()
        >>>
        >>> # Adding models to the object
        >>> config.add_model(napalm_yang.models.openconfig_interfaces())
        >>> config.add_model(napalm_yang.models.openconfig_vlan())
        >>> # Printing the model in a human readable format
        >>> pretty_print(napalm_yang.utils.model_to_dict(config))
        >>> {
        >>>     "openconfig-interfaces:interfaces [rw]": {
        >>>         "interface [rw]": {
        >>>             "config [rw]": {
        >>>                 "description [rw]": "string",
        >>>                 "enabled [rw]": "boolean",
        >>>                 "mtu [rw]": "uint16",
        >>>                 "name [rw]": "string",
        >>>                 "type [rw]": "identityref"
        >>>             },
        >>>             "hold_time [rw]": {
        >>>                 "config [rw]": {
        >>>                     "down [rw]": "uint32",
        >>>                     "up [rw]": "uint32"
            (trimmed for clarity)
    """
    def is_mode(obj, mode):
        if mode == "":
            return True
        elif mode == "config":
            return obj._yang_name == "config" or obj._is_config
        elif mode == "state":
            return obj._yang_name == "state" or not obj._is_config
        else:
            raise ValueError("mode can only be config, state or ''. Passed: {}".format(mode))

    def get_key(key, model, parent_defining_module):
        key = "{} {}".format(key, "[rw]" if model._is_config else "[ro]")

        if parent_defining_module != model._defining_module:
            key = "{}:{}".format(model._defining_module, key)
        return key

    if model._yang_type in ("container", "list", ):
        cls = model if model._yang_type in ("container", ) else model._contained_class()
        result = {}
        for k, v in cls:
            r = model_to_dict(v, mode)
            if r:
                result[get_key(k, v, model._defining_module)] = r
        return result
    else:
        return model._yang_type if is_mode(model, mode) else None


def _diff_root(f, s):
    result = {}
    for k in f.elements():
        v = getattr(f, k)
        w = getattr(s, k)

        r = diff(v, w)
        if r:
            result[k] = r

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
    """
    Given two models, return the difference between them.

    Args:

        f (Pybindbase): First element.
        s (Pybindbase): Second element.

    Returns:

        dict: A dictionary highlighting the differences.

    Examples:

        >>> diff = napalm_yang.utils.diff(candidate, running)
        >>> pretty_print(diff)
        >>> {
        >>>     "interfaces": {
        >>>         "interface": {
        >>>             "both": {
        >>>                 "Port-Channel1": {
        >>>                     "config": {
        >>>                         "mtu": {
        >>>                             "first": "0",
        >>>                             "second": "9000"
        >>>                         }
        >>>                     }
        >>>                 }
        >>>             },
        >>>             "first_only": [
        >>>                 "Loopback0"
        >>>             ],
        >>>             "second_only": [
        >>>                 "Loopback1"
        >>>             ]
        >>>         }
        >>>     }
        >>> }
    """
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
