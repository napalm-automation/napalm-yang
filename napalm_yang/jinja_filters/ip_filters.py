import netaddr


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
    }


def netmask_to_cidr(value):
    """ Converts a network mask to it's CIDR value. """
    return netaddr.IPAddress(value).netmask_bits()
