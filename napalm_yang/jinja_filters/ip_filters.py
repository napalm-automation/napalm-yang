import netaddr

from napalm_yang.jinja_filters.helpers import check_empty


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
        "cidr_to_netmask": cidr_to_netmask,
        "normalize_prefix": normalize_prefix,
        "normalize_address": normalize_address,
        "prefix_to_addrmask": prefix_to_addrmask,
    }


@check_empty
def netmask_to_cidr(value):
    """
    Converts a network mask to it's CIDR value.

    Examples:
        >>> "{{ '255.255.255.0'|netmask_to_cidr }}" -> "24"
    """
    return netaddr.IPAddress(value).netmask_bits()


@check_empty
def cidr_to_netmask(value):
    """
    Converts a CIDR prefix-length to a network mask.

    Examples:
        >>> "{{ '24'|cidr_to_netmask }}" -> "255.255.255.0"
    """
    return str(netaddr.IPNetwork("1.1.1.1/{}".format(value)).netmask)


@check_empty
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


@check_empty
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


@check_empty
def prefix_to_addrmask(value, sep=' '):
    """
    Converts a CIDR formatted prefix into an address netmask representation.
    Argument sep specifies the separator between the address and netmask parts.
    By default it's a single space.

    Examples:
        >>> "{{ '192.168.0.1/24|prefix_to_addrmask }}" -> "192.168.0.1 255.255.255.0"
        >>> "{{ '192.168.0.1/24|prefix_to_addrmask('/') }}" -> "192.168.0.1/255.255.255.0"
    """
    prefix = netaddr.IPNetwork(value)
    return '{}{}{}'.format(prefix.ip, sep, prefix.netmask)
