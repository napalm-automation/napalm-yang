import netaddr


def filters():
    return {
        "netmask_to_cidr": netmask_to_cidr,
        "cidr_to_netmask": cidr_to_netmask,
    }


def netmask_to_cidr(value):
    """ Converts a network mask to it's CIDR value. """
    return netaddr.IPAddress(value).netmask_bits()


def cidr_to_netmask(value):
    """ Converts a CIDR prefix-length to a network mask. """
    return netaddr.IPNetwork("1.1.1.1/{}".format(value)).netmask
