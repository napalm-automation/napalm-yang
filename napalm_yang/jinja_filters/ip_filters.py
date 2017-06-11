import netaddr


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
        "cidr_to_netmask": cidr_to_netmask,
        "addrmask_to_cidr": addrmask_to_cidr,
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


def addrmask_to_cidr(value):
    """
    Converts an address and network mask to it's CIDR representation.

    Examples:
        >>> "{{ '192.168.0.0 255.255.255.0'|addrmask_to_cidr }}" -> "192.168.0.0/24"
    """
    value = value.replace(' ', '/')
    return str(netaddr.IPNetwork(value))

