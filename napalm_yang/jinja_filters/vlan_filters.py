from napalm_yang.jinja_filters.helpers import check_empty


def filters():
    return {
        "vlan_range_to_oc": vlan_range_to_oc,
        "oc_to_vlan_range": oc_to_vlan_range,
        "expand_range": expand_range,
    }


@check_empty(default=None)
def vlan_range_to_oc(value):
    """
    Converts an industry standard vlan range into a list that can be
    interpreted by openconfig. For example:

    "1, 2, 3-10" -> ["1", "2", "3..10"]
    """
    return [s.replace("-", "..") for s in value.split(",")]


@check_empty()
def oc_to_vlan_range(value):
    """
    Converts an industry standard vlan range into a list that can be
    interpreted by openconfig. For example:

    ["1", "2", "3..10"] -> "1, 2, 3-10"
    """
    return ",".join(["{}".format(s).replace("..", "-") for s in value])


@check_empty()
def expand_range(value):
    """
    Expands a range:

    "1, 2, 4-10" -> [1, 2, 4, 5, 6, 7, 8, 9, 10]
    """
    r = []
    for v in value.split(","):
        if "-" in v:
            s = v.split("-")
            r.extend(range(int(s[0]), int(s[1]) + 1))
        else:
            r.append(int(v))
    return r
