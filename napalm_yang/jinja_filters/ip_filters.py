import netaddr


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
        "cidr_to_netmask": cidr_to_netmask,
    }


def netmask_to_cidr(value):
    """
    Converts a network mask to it's CIDR value.

    Examples:
        >>> "{{ '255.255.255.0'|netmask_to_cidr }}" -> "24"
    """
    return netaddr.IPAddress(value).netmask_bits()


def cidr_to_netmask(value):
    """
    Converts a CIDR prefix-length to a network mask.

    Examples:
        >>> "{{ '24'|cidr_to_netmask }}" -> "255.255.255.0"
    """
    return netaddr.IPNetwork("1.1.1.1/{}".format(value)).netmask
