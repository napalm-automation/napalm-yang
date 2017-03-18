"""
This sub-module contains groupings that are related to support
for multiple protocols in BGP. The groupings are common across
multiple contexts.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_bgp = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import oc_types
from napalm_yang import oc_bgp_types
from napalm_yang import oc_rpol
# Imcludes
from openconfig_bgp_common import *


# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.1.1")



__prefix__ = "oc-bgp"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-06-21": {
        "revision": "2016-06-21"
    }
}



class BgpCommonMpAllAfiSafiCommon(BaseBinding):
    """
    Grouping for configuration common to all AFI,SAFI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.prefix_limit = BgpCommonMpAllAfiSafiCommon_PrefixLimit_300()
        self.prefix_limit._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        


class BgpCommonMpL3VpnIpv4Ipv6UnicastCommon(BgpCommonMpAllAfiSafiCommon):
    """
    Common configuration applied across L3VPN for IPv4
    and IPv6
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv4Ipv6MulticastCommon(BgpCommonMpAllAfiSafiCommon):
    """
    Common configuration applied across L3VPN for IPv4
    and IPv6
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL2VpnCommon(BgpCommonMpAllAfiSafiCommon):
    """
    Common configuration applied across L2VPN address
    families
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        





class BgpCommonMpIpv4UnicastGroup(BaseBinding):
    """
    Group for IPv4 Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ipv4_unicast = BgpCommonMpIpv4UnicastGroup_Ipv4Unicast_94()
        self.ipv4_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4LabeledUnicastGroup(BaseBinding):
    """
    Group for IPv4 Labeled Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ipv4_labeled_unicast = BgpCommonMpIpv4LabeledUnicastGroup_Ipv4LabeledUnicast_135()
        self.ipv4_labeled_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        

class BgpCommonMpIpv6UnicastGroup(BaseBinding):
    """
    Group for IPv6 Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ipv6_unicast = BgpCommonMpIpv6UnicastGroup_Ipv6Unicast_114()
        self.ipv6_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True


class BgpCommonMpIpv4LabeledUnicastGroup(BaseBinding):
    """
    Group for IPv4 Labeled Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ipv4_labeled_unicast = BgpCommonMpIpv4LabeledUnicastGroup_Ipv4LabeledUnicast_135()
        self.ipv4_labeled_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True


class BgpCommonMpIpv6LabeledUnicastGroup(BaseBinding):
    """
    Group for IPv6 Labeled Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ipv6_labeled_unicast = BgpCommonMpIpv6LabeledUnicastGroup_Ipv6LabeledUnicast_155()
        self.ipv6_labeled_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv4UnicastGroup(BaseBinding):
    """
    Group for IPv4 Unicast L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l3vpn_ipv4_unicast = BgpCommonMpL3VpnIpv4UnicastGroup_L3VpnIpv4Unicast_175()
        self.l3vpn_ipv4_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        


class BgpCommonMpL3VpnIpv6UnicastGroup(BaseBinding):
    """
    Group for IPv6 Unicast L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l3vpn_ipv6_unicast = BgpCommonMpL3VpnIpv6UnicastGroup_L3VpnIpv6Unicast_195()
        self.l3vpn_ipv6_unicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        


class BgpCommonMpIpv4Ipv6UnicastCommon(BgpCommonMpAllAfiSafiCommon):
    """
    Common configuration that is applicable for IPv4 and IPv6
    unicast
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpCommonMpIpv4Ipv6UnicastCommon_Config_331()
        self.config._parent = weakref.ref(self)
        self.state = BgpCommonMpIpv4Ipv6UnicastCommon_State_337()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv6MulticastGroup(BaseBinding):
    """
    Group for IPv6 L3VPN multicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l3vpn_ipv6_multicast = BgpCommonMpL3VpnIpv6MulticastGroup_L3VpnIpv6Multicast_237()
        self.l3vpn_ipv6_multicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True

class BgpCommonMpL2VpnVplsGroup(BaseBinding):
    """
    Group for BGP-signalled VPLS configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l2vpn_vpls = BgpCommonMpL2VpnVplsGroup_L2VpnVpls_258()
        self.l2vpn_vpls._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        

class BgpCommonMpL3VpnIpv4MulticastGroup(BaseBinding):
    """
    Group for IPv4 L3VPN multicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l3vpn_ipv4_multicast = BgpCommonMpL3VpnIpv4MulticastGroup_L3VpnIpv4Multicast_216()
        self.l3vpn_ipv4_multicast._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        

class BgpCommonMpL2VpnEvpnGroup(BaseBinding):
    """
    Group for BGP EVPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.l2vpn_evpn = BgpCommonMpL2VpnEvpnGroup_L2VpnEvpn_279()
        self.l2vpn_evpn._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        

class BgpCommonMpAllAfiSafiCommonPrefixLimitConfig(BaseBinding):
    """
    Configuration parameters relating to prefix-limits for an
    AFI-SAFI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.shutdown_threshold_pct = oc_types.Percentage(_meta={"mandatory": False},
        )
        self.shutdown_threshold_pct._parent = weakref.ref(self)
        self.restart_timer = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.restart_timer._parent = weakref.ref(self)
        self.max_prefixes = Uint32(_meta={"mandatory": False},
        )
        self.max_prefixes._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4Ipv6UnicastCommonConfig(BaseBinding):
    """
    Common configuration parameters for IPv4 and IPv6 Unicast
    address families
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.send_default_route = Boolean(_meta={"mandatory": False},
        )
        self.send_default_route._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        






class PrefixLimit_Config_305(BgpCommonMpAllAfiSafiCommonPrefixLimitConfig):
    """
    Configuration parameters relating to the prefix
    limit for the AFI-SAFI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        


# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class BgpCommonMpAfiSafiGracefulRestartConfig(BaseBinding):
    """
    BGP graceful restart parameters that apply on a per-AFI-SAFI
    basis
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpAfiSafiConfig(BaseBinding):
    """
    Configuration parameters used for all BGP AFI-SAFIs
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        self.afi_safi_name = Identityref(_meta={"mandatory": False},
            base=oc_bgp_types.Afi_Safi_Type,
        )
        self.afi_safi_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpAllAfiSafiListContents(BgpCommonMpL2VpnEvpnGroup, BgpCommonMpL2VpnVplsGroup, BgpCommonMpL3VpnIpv6MulticastGroup, BgpCommonMpL3VpnIpv4MulticastGroup, BgpCommonMpL3VpnIpv6UnicastGroup, BgpCommonMpL3VpnIpv4UnicastGroup, BgpCommonMpIpv6LabeledUnicastGroup, BgpCommonMpIpv4LabeledUnicastGroup, BgpCommonMpIpv6UnicastGroup, BgpCommonMpIpv4UnicastGroup, oc_rpol.ApplyPolicyGroup):
    """
    A common grouping used for contents of the list that is used
    for AFI-SAFI entries
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4UnicastGroup_Ipv4Unicast_94(BgpCommonMpIpv4Ipv6UnicastCommon):
    """
    IPv4 unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:IPV4_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        





class BgpCommonMpIpv6UnicastGroup_Ipv6Unicast_114(BgpCommonMpIpv4Ipv6UnicastCommon):
    """
    IPv6 unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:IPV6_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4LabeledUnicastGroup_Ipv4LabeledUnicast_135(BgpCommonMpAllAfiSafiCommon):
    """
    IPv4 Labeled Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:IPV4_LABELED_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv6LabeledUnicastGroup_Ipv6LabeledUnicast_155(BgpCommonMpAllAfiSafiCommon):
    """
    IPv6 Labeled Unicast configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:IPV6_LABELED_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv4UnicastGroup_L3VpnIpv4Unicast_175(BgpCommonMpL3VpnIpv4Ipv6UnicastCommon):
    """
    Unicast IPv4 L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L3VPN_IPV4_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        


class BgpCommonMpL3VpnIpv6UnicastGroup_L3VpnIpv6Unicast_195(BgpCommonMpL3VpnIpv4Ipv6UnicastCommon):
    """
    Unicast IPv6 L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L3VPN_IPV6_UNICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv4MulticastGroup_L3VpnIpv4Multicast_216(BgpCommonMpL3VpnIpv4Ipv6MulticastCommon):
    """
    Multicast IPv4 L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L3VPN_IPV4_MULTICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpL3VpnIpv6MulticastGroup_L3VpnIpv6Multicast_237(BgpCommonMpL3VpnIpv4Ipv6MulticastCommon):
    """
    Multicast IPv6 L3VPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L3VPN_IPV6_MULTICAST'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        





class BgpCommonMpL2VpnVplsGroup_L2VpnVpls_258(BgpCommonMpL2VpnCommon):
    """
    BGP-signalled VPLS configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L2VPN_VPLS'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



class BgpCommonMpL2VpnEvpnGroup_L2VpnEvpn_279(BgpCommonMpL2VpnCommon):
    """
    BGP EVPN configuration options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../afi-safi-name = 'oc-bgp-types:L2VPN_EVPN'"
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixLimit_Config_305(BgpCommonMpAllAfiSafiCommonPrefixLimitConfig):
    """
    Configuration parameters relating to the prefix
    limit for the AFI-SAFI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixLimit_State_312(BgpCommonMpAllAfiSafiCommonPrefixLimitConfig):
    """
    State information relating to the prefix-limit for the
    AFI-SAFI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class BgpCommonMpAllAfiSafiCommon_PrefixLimit_300(BaseBinding):
    """
    Configure the maximum number of prefixes that will be
    accepted from a peer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = PrefixLimit_Config_305()
        self.config._parent = weakref.ref(self)
        self.state = PrefixLimit_State_312()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4Ipv6UnicastCommon_Config_331(BgpCommonMpIpv4Ipv6UnicastCommonConfig):
    """
    Configuration parameters for common IPv4 and IPv6 unicast
    AFI-SAFI options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonMpIpv4Ipv6UnicastCommon_State_337(BgpCommonMpIpv4Ipv6UnicastCommonConfig):
    """
    State information for common IPv4 and IPv6 unicast
    parameters
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        





# Top-uses

# Top-containers


# augments
