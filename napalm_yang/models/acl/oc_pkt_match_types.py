"""
This module defines common types for use in models requiring
data definitions related to packet matches.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_pkt_match_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import inet

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.2.0")



__namespace__ = "http://openconfig.net/yang/packet-match-types"
__yang_version__ = "1"
__prefix__ = "oc-pkt-match-types"
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



# extensions

# features


# typedef

class PortNumRange(Union):
    """
    Port numbers may be represented as a single value,
    an inclusive range as <lower>..<higher>, or as ANY to
    indicate a wildcard.
    """
    def __init__(self, _meta=None, type_ = {
    "enumeration": {
        "enum": {
            "ANY": {
                "info": {
                    "description": "Indicates any valid port number (e.g., wildcard)"
                }
            }
        }
    }, 
    "inet:port-number": {}, 
    "string": {
        "pattern": "^(6[0-5][0-5][0-3][0-5]|[0-5]?[0-9]?[0-9]?[0-9]?[0-9]?)\\.\\.(6[0-5][0-5][0-3][0-5]|[0-5]?[0-9]?[0-9]?[0-9]?[0-9]?)$"
    }
}, ):
        super().__init__(_meta=_meta, type_ = type_, )

class IpProtocolType(Union):
    """
    The IP protocol number may be expressed as a valid protocol
    number (integer) or using a protocol type defined by the
    IP_PROTOCOL identity
    """
    def __init__(self, _meta=None, type_ = {
    "identityref": {
        "base": "IP_PROTOCOL"
    }, 
    "uint8": {
        "range": "0..254"
    }
}, ):
        super().__init__(_meta=_meta, type_ = type_, )

class EthertypeType(Union):
    """
    The Ethertype value may be expressed as a 16-bit number in
    hexadecimal notation, or using a type defined by the
    ETHERTYPE identity
    """
    def __init__(self, _meta=None, type_ = {
    "identityref": {
        "base": "ETHERTYPE"
    }, 
    "uint16": {
        "range": "1..65535"
    }
}, ):
        super().__init__(_meta=_meta, type_ = type_, )


# Identities
Tcp_Ack = Identity(
    base="TCP_FLAGS",
    value="TCP_ACK",
    description="""TCP ACK flag"""
    )

Ip_Protocol = Identity(
    base="None",
    value="IP_PROTOCOL",
    description="""Base identity for commonly used IP protocols used in
packet header matches"""
    )

Ip_Udp = Identity(
    base="IP_PROTOCOL",
    value="IP_UDP",
    description="""User Datagram Protocol (17)"""
    )

Ethertype_Arp = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_ARP",
    description="""Address resolution protocol (0x0806)"""
    )

Tcp_Syn = Identity(
    base="TCP_FLAGS",
    value="TCP_SYN",
    description="""TCP SYN flag"""
    )

Ethertype_Vlan = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_VLAN",
    description="""VLAN-tagged frame (as defined by IEEE 802.1q) (0x8100). Note
that this value is also used to represent Shortest Path
Bridging (IEEE 801.1aq) frames."""
    )

Ip_Pim = Identity(
    base="IP_PROTOCOL",
    value="IP_PIM",
    description="""Protocol Independent Multicast (103)"""
    )

Ip_Icmp = Identity(
    base="IP_PROTOCOL",
    value="IP_ICMP",
    description="""Internet Control Message Protocol (1)"""
    )

Tcp_Fin = Identity(
    base="TCP_FLAGS",
    value="TCP_FIN",
    description="""TCP FIN flag"""
    )

Ethertype_Roce = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_ROCE",
    description="""RDMA over Converged Ethernet (0x8915)"""
    )

Tcp_Ece = Identity(
    base="TCP_FLAGS",
    value="TCP_ECE",
    description="""TCP ECN-Echo flag.  If the SYN flag is set, indicates that
the TCP peer is ECN-capable, otherwise indicates that a
packet with Congestion Experienced flag in the IP header
is set"""
    )

Tcp_Flags = Identity(
    base="None",
    value="TCP_FLAGS",
    description="""Common TCP flags used in packet header matches"""
    )

Tcp_Rst = Identity(
    base="TCP_FLAGS",
    value="TCP_RST",
    description="""TCP RST flag"""
    )

Ethertype = Identity(
    base="None",
    value="ETHERTYPE",
    description="""Base identity for commonly used Ethertype values used
in packet header matches on Ethernet frames.  The Ethertype
indicates which protocol is encapsulated in the Ethernet
payload."""
    )

Ethertype_Ipv4 = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_IPV4",
    description="""IPv4 protocol (0x0800)"""
    )

Ip_Tcp = Identity(
    base="IP_PROTOCOL",
    value="IP_TCP",
    description="""Transmission Control Protocol (6)"""
    )

Ethertype_Ipv6 = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_IPV6",
    description="""IPv6 protocol (0x86DD)"""
    )

Tcp_Urg = Identity(
    base="TCP_FLAGS",
    value="TCP_URG",
    description="""TCP urgent flag"""
    )

Ip_Igmp = Identity(
    base="IP_PROTOCOL",
    value="IP_IGMP",
    description="""Internet Group Membership Protocol (2)"""
    )

Ethertype_Mpls = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_MPLS",
    description="""MPLS unicast (0x8847)"""
    )

Tcp_Psh = Identity(
    base="TCP_FLAGS",
    value="TCP_PSH",
    description="""TCP push flag"""
    )

Ip_Auth = Identity(
    base="IP_PROTOCOL",
    value="IP_AUTH",
    description="""Authentication header, e.g., for IPSEC (51)"""
    )

Ip_Gre = Identity(
    base="IP_PROTOCOL",
    value="IP_GRE",
    description="""Generic Routing Encapsulation (47)"""
    )

Ip_Rsvp = Identity(
    base="IP_PROTOCOL",
    value="IP_RSVP",
    description="""Resource Reservation Protocol (46)"""
    )

Ethertype_Lldp = Identity(
    base="ETHERTYPE",
    value="ETHERTYPE_LLDP",
    description="""Link Layer Discovery Protocol (0x88CC)"""
    )

Tcp_Cwr = Identity(
    base="TCP_FLAGS",
    value="TCP_CWR",
    description="""TCP Congestion Window Reduced flag"""
    )

Ip_L2Tp = Identity(
    base="IP_PROTOCOL",
    value="IP_L2TP",
    description="""Layer Two Tunneling Protocol v.3 (115)"""
    )


# Classes to support containers and lists


# Top-uses

# Top-containers