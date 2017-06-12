import netaddr


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
        "cidr_to_netmask": cidr_to_netmask,
        "normalize_prefix": normalize_prefix,
        "normalize_address": normalize_address,
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


def normalize_prefix(value):
    """
    Converts an IPv4 or IPv6 prefix writen in various formats to its CIDR representation.

    This filter works only on prefixes. Use normalize_address if you wish to normalize an address
    without a network mask.

    Examples:
        >>> "{{ '192.168.0.0 255.255.255.0'|normalize_prefix }}" -> "192.168.0.0/24"
        >>> "{{ '192.168/255.255.255.0'|normalize_prefix }}" -> "192.168.0.0/24"
        >>> "{{ '2001:DB8:0:0:1:0:0:1/64'|normalize_prefix }}" -> "2001:db8::1:0:0:1/64"
    """
    value = value.replace(' ', '/')
    return str(netaddr.IPNetwork(value))


def normalize_address(value):
    """
    Converts an IPv4 or IPv6 address writen in various formats to a standard textual representation.

    This filter works only on addresses without network mask. Use normalize_prefix to normalize
    networks.

    Examples:
        >>> "{{ '192.168.0.1'|normalize_address }}" -> "192.168.0.1"
        >>> "{{ '192.168.1'|normalize_address }}" -> "192.168.0.1"
        >>> "{{ '2001:DB8:0:0:1:0:0:1'|normalize_address }}" -> "2001:db8::1:0:0:1"

    """
    return str(netaddr.IPAddress(value))
