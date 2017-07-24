from napalm_yang.jinja_filters.helpers import check_empty


def filters():
    return {
        "vlan_range_to_oc": vlan_range_to_oc,
    }


@check_empty
def vlan_range_to_oc(value):
    """
    Converts an industry standard vlan range into a list that can be
    interpreted by openconfig. For example:

    "1, 2, 3-10" -> ["1", "2", "3..10"]
    """
    return [s.replace("-", "..") for s in value.split(",")]
