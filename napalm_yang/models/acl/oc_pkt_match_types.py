"""
This module defines common types for use in models requiring
data definitions related to packet matches.
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports
from napalm_yang import oc_ext
from napalm_yang import inet

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()
openconfig_extensions.openconfig_version = "0.2.0"


__namespace__ = "http://openconfig.net/yang/packet-match-types"
__yang_version__ = "1"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-04-27": {
        "revision": "2016-04-27"
    }, 
    "2016-08-08": {
        "revision": "2016-08-08"
    }
}



# typedef

class PortNumRange(yang_base.BaseBinding):
    """
    Port numbers may be represented as a single value,
    an inclusive range as <lower>..<higher>, or as ANY to
    indicate a wildcard.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.port_num_range = yang.Union(type="defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'inet:port-number': defaultdict(<function _nested_default_dict at 0x1081b1578>, {}), u'string': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'pattern': u'^(6[0-5][0-5][0-3][0-5]|[0-5]?[0-9]?[0-9]?[0-9]?[0-9]?)\\.\\.(6[0-5][0-5][0-3][0-5]|[0-5]?[0-9]?[0-9]?[0-9]?[0-9]?)$'}), u'enumeration': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'enum': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'ANY': defaultdict(<function _nested_default_dict at 0x1081b1578>, {'info': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'description': u'Indicates any valid port number (e.g., wildcard)'})})})})})", )


class EthertypeType(yang_base.BaseBinding):
    """
    The Ethertype value may be expressed as a 16-bit number in
    hexadecimal notation, or using a type defined by the
    ETHERTYPE identity
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ethertype_type = yang.Union(type="defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'identityref': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'base': u'ETHERTYPE'}), u'uint16': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'range': u'1..65535'})})", )


class IpProtocolType(yang_base.BaseBinding):
    """
    The IP protocol number may be expressed as a valid protocol
    number (integer) or using a protocol type defined by the
    IP_PROTOCOL identity
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ip_protocol_type = yang.Union(type="defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'identityref': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'base': u'IP_PROTOCOL'}), u'uint8': defaultdict(<function _nested_default_dict at 0x1081b1578>, {u'range': u'0..254'})})", )



# Identities
Tcp_Ack = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_ACK",
    description="""TCP ACK flag"""
    )

Ip_Protocol = yang.Identity(
    base="None",
    value="IP_PROTOCOL",
    description="""Base identity for commonly used IP protocols used in
packet header matches"""
    )

Ip_Udp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_UDP",
    description="""User Datagram Protocol (17)"""
    )

Ethertype_Arp = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_ARP",
    description="""Address resolution protocol (0x0806)"""
    )

Tcp_Syn = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_SYN",
    description="""TCP SYN flag"""
    )

Ethertype_Vlan = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_VLAN",
    description="""VLAN-tagged frame (as defined by IEEE 802.1q) (0x8100). Note
that this value is also used to represent Shortest Path
Bridging (IEEE 801.1aq) frames."""
    )

Ip_Pim = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_PIM",
    description="""Protocol Independent Multicast (103)"""
    )

Ip_Icmp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_ICMP",
    description="""Internet Control Message Protocol (1)"""
    )

Tcp_Fin = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_FIN",
    description="""TCP FIN flag"""
    )

Ethertype_Roce = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_ROCE",
    description="""RDMA over Converged Ethernet (0x8915)"""
    )

Tcp_Ece = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_ECE",
    description="""TCP ECN-Echo flag.  If the SYN flag is set, indicates that
the TCP peer is ECN-capable, otherwise indicates that a
packet with Congestion Experienced flag in the IP header
is set"""
    )

Tcp_Flags = yang.Identity(
    base="None",
    value="TCP_FLAGS",
    description="""Common TCP flags used in packet header matches"""
    )

Tcp_Rst = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_RST",
    description="""TCP RST flag"""
    )

Ethertype = yang.Identity(
    base="None",
    value="ETHERTYPE",
    description="""Base identity for commonly used Ethertype values used
in packet header matches on Ethernet frames.  The Ethertype
indicates which protocol is encapsulated in the Ethernet
payload."""
    )

Ethertype_Ipv4 = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_IPV4",
    description="""IPv4 protocol (0x0800)"""
    )

Ip_Tcp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_TCP",
    description="""Transmission Control Protocol (6)"""
    )

Ethertype_Ipv6 = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_IPV6",
    description="""IPv6 protocol (0x86DD)"""
    )

Tcp_Urg = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_URG",
    description="""TCP urgent flag"""
    )

Ip_Igmp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_IGMP",
    description="""Internet Group Membership Protocol (2)"""
    )

Ethertype_Mpls = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_MPLS",
    description="""MPLS unicast (0x8847)"""
    )

Tcp_Psh = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_PSH",
    description="""TCP push flag"""
    )

Ip_Auth = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_AUTH",
    description="""Authentication header, e.g., for IPSEC (51)"""
    )

Ip_Gre = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_GRE",
    description="""Generic Routing Encapsulation (47)"""
    )

Ip_Rsvp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_RSVP",
    description="""Resource Reservation Protocol (46)"""
    )

Ethertype_Lldp = yang.Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_LLDP",
    description="""Link Layer Discovery Protocol (0x88CC)"""
    )

Tcp_Cwr = yang.Identity(
    base="TCP_FLAGS",
    value="TCP_CWR",
    description="""TCP Congestion Window Reduced flag"""
    )

Ip_L2Tp = yang.Identity(
    base="IP_PROTOCOL",
    value="IP_L2TP",
    description="""Layer Two Tunneling Protocol v.3 (115)"""
    )


# Classes to support containers and lists


# Top-uses
# Top-containers{}