from napalm_yang.jinja_filters.helpers import check_empty
import netaddr


def filters():
    return {
        "dotted_mac_to_colon": dotted_mac_to_colon,
        "colon_mac_to_dotted": colon_mac_to_dotted,
    }


@check_empty()
def dotted_mac_to_colon(value):
    mac = netaddr.EUI(value)
    mac.dialect = netaddr.mac_unix_expanded
    return str(mac)


@check_empty()
def colon_mac_to_dotted(value):
    mac = netaddr.EUI(value)
    mac.dialect = netaddr.mac_cisco
    return str(mac)
