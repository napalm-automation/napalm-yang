"""
This module contains general data definitions for use in BGP
policy. It can be imported by modules that make use of BGP
attributes
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_bgp_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import inet
from napalm_yang import oc_types
# Imcludes

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.1.1")



__namespace__ = "http://openconfig.net/yang/bgp-types"
__yang_version__ = "1"
__prefix__ = "oc-bgp-types"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-06-21": {
        "revision": "2016-06-21"
    }
}



# extensions

# features


# typedef

class BgpSessionDirection(Enumeration):
    """
    Type to describe the direction of NLRI transmission
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "INBOUND": {
        "info": {
            "description": "Refers to all NLRI received from the BGP peer"
        }
    }, 
    "OUTBOUND": {
        "info": {
            "description": "Refers to all NLRI advertised to the BGP peer"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class BgpWellKnownCommunityType(Identityref):
    """
    Type definition for well-known IETF community attribute
    values
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, base = "BGP_WELL_KNOWN_STD_COMMUNITY", ):

        super().__init__(_meta=_meta, base = base, )

class BgpStdCommunityType(Union):
    """
    Type definition for standard commmunity attributes
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "string": {
        "pattern": "([0-9]+:[0-9]+)"
    }, 
    "uint32": {
        "range": "65536..4294901759"
    }
}, ):

        self.types = []
        self.types.append(String({
    "pattern": "([0-9]+:[0-9]+)"
}))
        self.types.append(Uint32({
    "range": "65536..4294901759"
}))
        

        super().__init__(_meta=_meta, type_ = type_, )

class BgpExtCommunityType(Union):
    """
    Type definition for extended community attributes
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "string": {
        "pattern": "(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])"
    }
}, ):

        self.types = []
        self.types.append(String({
    "pattern": "(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])"
}))
        

        super().__init__(_meta=_meta, type_ = type_, )

class BgpCommunityRegexpType(oc_types.StdRegexp):
    """
    Type definition for communities specified as regular
    expression patterns
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, ):

        super().__init__(_meta=_meta, )

class BgpOriginAttrType(Enumeration):
    """
    Type definition for standard BGP origin attribute
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "EGP": {
        "info": {
            "description": "Origin of the NLRI is EGP"
        }
    }, 
    "IGP": {
        "info": {
            "description": "Origin of the NLRI is internal"
        }
    }, 
    "INCOMPLETE": {
        "info": {
            "description": "Origin of the NLRI is neither IGP or EGP"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class PeerType(Enumeration):
    """
    labels a peer or peer group as explicitly internal or
    external
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "EXTERNAL": {
        "info": {
            "description": "external (eBGP) peer"
        }
    }, 
    "INTERNAL": {
        "info": {
            "description": "internal (iBGP) peer"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class RemovePrivateAsOption(Identityref):
    """
    set of options for configuring how private AS path numbers
    are removed from advertisements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, base = "REMOVE_PRIVATE_AS_OPTION", ):

        super().__init__(_meta=_meta, base = base, )

class Percentage(Uint8):
    """
    Integer indicating a percentage value
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, range_ = "0..100", ):

        super().__init__(_meta=_meta, range_ = range_, )

class RrClusterIdType(Union):
    """
    union type for route reflector cluster ids:
    option 1: 4-byte number
    option 2: IP address
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "inet:ipv4-address": {}, 
    "uint32": {}
}, ):

        self.types = []
        self.types.append(inet.Ipv4Address({}))
        self.types.append(Uint32({}))
        

        super().__init__(_meta=_meta, type_ = type_, )

class CommunityType(Enumeration):
    """
    type describing variations of community attributes:
    STANDARD: standard BGP community [rfc1997]
    EXTENDED: extended BGP community [rfc4360]
    BOTH: both standard and extended community
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "BOTH": {
        "info": {
            "description": "send both standard and extended communities"
        }
    }, 
    "EXTENDED": {
        "info": {
            "description": "send only extended communities"
        }
    }, 
    "NONE": {
        "info": {
            "description": "do not send any community attribute"
        }
    }, 
    "STANDARD": {
        "info": {
            "description": "send only standard communities"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )


# Identities
Bgp_Capability = Identity(
    base=None,
    value="BGP_CAPABILITY",
    description="""Base identity for a BGP capability"""
    )

Mpbgp = Identity(
    base=Bgp_Capability,
    value="MPBGP",
    description="""Multi-protocol extensions to BGP"""
    )

Route_Refresh = Identity(
    base=Bgp_Capability,
    value="ROUTE_REFRESH",
    description="""The BGP route-refresh functionality"""
    )

Asn32 = Identity(
    base=Bgp_Capability,
    value="ASN32",
    description="""4-byte (32-bit) AS number functionality"""
    )

Graceful_Restart = Identity(
    base=Bgp_Capability,
    value="GRACEFUL_RESTART",
    description="""Graceful restart functionality"""
    )

Add_Paths = Identity(
    base=Bgp_Capability,
    value="ADD_PATHS",
    description="""BGP add-paths"""
    )

Afi_Safi_Type = Identity(
    base=None,
    value="AFI_SAFI_TYPE",
    description="""Base identity type for AFI,SAFI tuples for BGP-4"""
    )

Ipv4_Unicast = Identity(
    base=Afi_Safi_Type,
    value="IPV4_UNICAST",
    description="""IPv4 unicast (AFI,SAFI = 1,1)"""
    )

Ipv6_Unicast = Identity(
    base=Afi_Safi_Type,
    value="IPV6_UNICAST",
    description="""IPv6 unicast (AFI,SAFI = 2,1)"""
    )

Ipv4_Labeled_Unicast = Identity(
    base=Afi_Safi_Type,
    value="IPV4_LABELED_UNICAST",
    description="""Labeled IPv4 unicast (AFI,SAFI = 1,4)"""
    )

Ipv6_Labeled_Unicast = Identity(
    base=Afi_Safi_Type,
    value="IPV6_LABELED_UNICAST",
    description="""Labeled IPv6 unicast (AFI,SAFI = 2,4)"""
    )

L3Vpn_Ipv4_Unicast = Identity(
    base=Afi_Safi_Type,
    value="L3VPN_IPV4_UNICAST",
    description="""Unicast IPv4 MPLS L3VPN (AFI,SAFI = 1,128)"""
    )

L3Vpn_Ipv6_Unicast = Identity(
    base=Afi_Safi_Type,
    value="L3VPN_IPV6_UNICAST",
    description="""Unicast IPv6 MPLS L3VPN (AFI,SAFI = 2,128)"""
    )

L3Vpn_Ipv4_Multicast = Identity(
    base=Afi_Safi_Type,
    value="L3VPN_IPV4_MULTICAST",
    description="""Multicast IPv4 MPLS L3VPN (AFI,SAFI = 1,129)"""
    )

L3Vpn_Ipv6_Multicast = Identity(
    base=Afi_Safi_Type,
    value="L3VPN_IPV6_MULTICAST",
    description="""Multicast IPv6 MPLS L3VPN (AFI,SAFI = 2,129)"""
    )

L2Vpn_Vpls = Identity(
    base=Afi_Safi_Type,
    value="L2VPN_VPLS",
    description="""BGP-signalled VPLS (AFI,SAFI = 25,65)"""
    )

L2Vpn_Evpn = Identity(
    base=Afi_Safi_Type,
    value="L2VPN_EVPN",
    description="""BGP MPLS Based Ethernet VPN (AFI,SAFI = 25,70)"""
    )

Bgp_Well_Known_Std_Community = Identity(
    base=None,
    value="BGP_WELL_KNOWN_STD_COMMUNITY",
    description="""Reserved communities within the standard community space
defined by RFC1997. These communities must fall within the
range 0x00000000 to 0xFFFFFFFF"""
    )

No_Export = Identity(
    base=Bgp_Well_Known_Std_Community,
    value="NO_EXPORT",
    description="""Do not export NLRI received carrying this community outside
the bounds of this autonomous system, or this confederation if
the local autonomous system is a confederation member AS. This
community has a value of 0xFFFFFF01."""
    )

No_Advertise = Identity(
    base=Bgp_Well_Known_Std_Community,
    value="NO_ADVERTISE",
    description="""All NLRI received carrying this community must not be
advertised to other BGP peers. This community has a value of
0xFFFFFF02."""
    )

No_Export_Subconfed = Identity(
    base=Bgp_Well_Known_Std_Community,
    value="NO_EXPORT_SUBCONFED",
    description="""All NLRI received carrying this community must not be
advertised to external BGP peers - including over confederation
sub-AS boundaries. This community has a value of 0xFFFFFF03."""
    )

Nopeer = Identity(
    base=Bgp_Well_Known_Std_Community,
    value="NOPEER",
    description="""An autonomous system receiving NLRI tagged with this community
is advised not to readvertise the NLRI to external bi-lateral
peer autonomous systems. An AS may also filter received NLRI
from bilateral peer sessions when they are tagged with this
community value"""
    )

Remove_Private_As_Option = Identity(
    base=None,
    value="REMOVE_PRIVATE_AS_OPTION",
    description="""Base identity for options for removing private autonomous
system numbers from the AS_PATH attribute"""
    )

Private_As_Remove_All = Identity(
    base=Remove_Private_As_Option,
    value="PRIVATE_AS_REMOVE_ALL",
    description="""Strip all private autonmous system numbers from the AS_PATH.
This action is performed regardless of the other content of the
AS_PATH attribute, and for all instances of private AS numbers
within that attribute."""
    )

Private_As_Replace_All = Identity(
    base=Remove_Private_As_Option,
    value="PRIVATE_AS_REPLACE_ALL",
    description="""Replace all instances of private autonomous system numbers in
the AS_PATH with the local BGP speaker's autonomous system
number. This action is performed regardless of the other
content of the AS_PATH attribute, and for all instances of
private AS number within that attribute."""
    )


# Classes to support containers and lists


# Top-uses

# Top-containers


# augments