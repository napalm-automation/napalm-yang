"""
Model for managing IP interfaces.

This model reuses most of the IETF YANG model for IP management
described by RFC 7277.  The primary differences are in the
structure of configuration and state data.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_ip = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import oc_if
from napalm_yang import inet
from napalm_yang import oc_vlan

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.1.0")



__namespace__ = "http://openconfig.net/yang/interfaces/ip"
__yang_version__ = "1"
__prefix__ = "oc-ip"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-12-22": {
        "revision": "2016-12-22"
    }
}



# extensions

# features


# typedef

class IpAddressOrigin(Enumeration):
    """
    The origin of an address.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "DHCP": {
        "info": {
            "description": "Indicates an address that has been assigned to this\nsystem by a DHCP server."
        }
    }, 
    "LINK_LAYER": {
        "info": {
            "description": "Indicates an address created by IPv6 stateless\nautoconfiguration that embeds a link-layer address in its\ninterface identifier."
        }
    }, 
    "OTHER": {
        "info": {
            "description": "None of the following."
        }
    }, 
    "RANDOM": {
        "info": {
            "description": "[adapted from RFC 7277]\n\nIndicates an address chosen by the system at\nrandom, e.g., an IPv4 address within 169.254/16, an\nRFC 4941 temporary address, or an RFC 7217 semantically\nopaque address."
        }
    }, 
    "STATIC": {
        "info": {
            "description": "Indicates that the address has been statically\nconfigured - for example, using NETCONF or a Command Line\nInterface."
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class NeighborOrigin(Enumeration):
    """
    The origin of a neighbor entry.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "DYNAMIC": {
        "info": {
            "description": "[adapted from RFC 7277]\n\nIndicates that the mapping has been dynamically resolved\nusing, e.g., IPv4 ARP or the IPv6 Neighbor Discovery\nprotocol."
        }
    }, 
    "OTHER": {
        "info": {
            "description": "None of the following."
        }
    }, 
    "STATIC": {
        "info": {
            "description": "Indicates that the mapping has been statically\nconfigured - for example, using NETCONF or a Command Line\nInterface."
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )


# Identities

# Classes to support containers and lists



class Ipv4GlobalConfig(BaseBinding):
    """
    Configuration data for IPv4 interfaces across
    all addresses assigned to the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        self.mtu = Uint16(_meta={"mandatory": False},
            range_="68..max",
        )
        self.mtu._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4AddressConfig(BaseBinding):
    """
    Per IPv4 adresss configuration data for the
    interface.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ip = inet.Ipv4AddressNoZone(_meta={"mandatory": False},
        )
        self.ip._parent = weakref.ref(self)
        self.prefix_length = Uint8(_meta={"mandatory": False},
            range_="0..32",
        )
        self.prefix_length._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4NeighborConfig(BaseBinding):
    """
    [adapted from IETF IP model RFC 7277]

    Per IPv4 neighbor configuration data. Neighbor
    entries are analagous to static ARP entries, i.e., they
    create a correspondence between IP and link-layer addresses
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ip = inet.Ipv4AddressNoZone(_meta={"mandatory": False},
        )
        self.ip._parent = weakref.ref(self)
        self.link_layer_address = yang.PhysAddress(_meta={"mandatory": True},
        )
        self.link_layer_address._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4AddressState(BaseBinding):
    """
    State variables for IPv4 addresses on the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.origin = IpAddressOrigin(_meta={"mandatory": False},
        )
        self.origin._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4NeighborState(BaseBinding):
    """
    State variables for IPv4 neighbor entries on the interface.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.origin = NeighborOrigin(_meta={"mandatory": False},
        )
        self.origin._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6GlobalConfig(BaseBinding):
    """
    Configuration data at the global level for each
    IPv6 interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        self.dup_addr_detect_transmits = Uint32(_meta={"mandatory": False},
        )
        self.dup_addr_detect_transmits._parent = weakref.ref(self)
        self.mtu = Uint32(_meta={"mandatory": False},
            range_="1280..max",
        )
        self.mtu._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6AddressConfig(BaseBinding):
    """
    Per-address configuration data for IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ip = inet.Ipv6AddressNoZone(_meta={"mandatory": False},
        )
        self.ip._parent = weakref.ref(self)
        self.prefix_length = Uint8(_meta={"mandatory": True},
            range_="0..128",
        )
        self.prefix_length._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6AddressState(BaseBinding):
    """
    Per-address operational state data for IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.status = Enumeration(_meta={"mandatory": False},
            enum={
            "DEPRECATED": {
                "info": {
                    "description": "This is a valid but deprecated address that should\nno longer be used as a source address in new\ncommunications, but packets addressed to such an\naddress are processed as expected."
                }
            }, 
            "DUPLICATE": {
                "info": {
                    "description": "The address has been determined to be non-unique on\nthe link and so must not be used."
                }
            }, 
            "INACCESSIBLE": {
                "info": {
                    "description": "The address is not accessible because the interface\nto which this address is assigned is not\noperational."
                }
            }, 
            "INVALID": {
                "info": {
                    "description": "This isn't a valid address, and it shouldn't appear\nas the destination or source address of a packet."
                }
            }, 
            "OPTIMISTIC": {
                "info": {
                    "description": "The address is available for use, subject to\nrestrictions, while its uniqueness on a link is\nbeing verified."
                }
            }, 
            "PREFERRED": {
                "info": {
                    "description": "This is a valid address that can appear as the\ndestination or source address of a packet."
                }
            }, 
            "TENTATIVE": {
                "info": {
                    "description": "The uniqueness of the address on the link is being\nverified.  Addresses in this state should not be\nused for general communication and should only be\nused to determine the uniqueness of the address."
                }
            }, 
            "UNKNOWN": {
                "info": {
                    "description": "The status cannot be determined for some reason."
                }
            }
        },
        )
        self.status._parent = weakref.ref(self)
        self.origin = IpAddressOrigin(_meta={"mandatory": False},
        )
        self.origin._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6NeighborConfig(BaseBinding):
    """
    Per-neighbor configuration data for IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ip = inet.Ipv6AddressNoZone(_meta={"mandatory": False},
        )
        self.ip._parent = weakref.ref(self)
        self.link_layer_address = yang.PhysAddress(_meta={"mandatory": True},
        )
        self.link_layer_address._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6NeighborState(BaseBinding):
    """
    Per-neighbor state variables for IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.origin = NeighborOrigin(_meta={"mandatory": False},
        )
        self.origin._parent = weakref.ref(self)
        self.neighbor_state = Enumeration(_meta={"mandatory": False},
            enum={
            "DELAY": {
                "info": {
                    "description": "The neighbor is no longer known to be reachable, and\n     traffic has recently been sent to the neighbor.\n     Rather than probe the neighbor immediately, however,\n     delay sending probes for a short while in order to\n     give upper-layer protocols a chance to provide\n     reachability confirmation."
                }
            }, 
            "INCOMPLETE": {
                "info": {
                    "description": "Address resolution is in progress, and the link-layer\n     address of the neighbor has not yet been\n     determined."
                }
            }, 
            "PROBE": {
                "info": {
                    "description": "The neighbor is no longer known to be reachable, and\n     unicast Neighbor Solicitation probes are being sent\n     to verify reachability."
                }
            }, 
            "REACHABLE": {
                "info": {
                    "description": "Roughly speaking, the neighbor is known to have been\n     reachable recently (within tens of seconds ago)."
                }
            }, 
            "STALE": {
                "info": {
                    "description": "The neighbor is no longer known to be reachable, but\n     until traffic is sent to the neighbor no attempt\n     should be made to verify its reachability."
                }
            }
        },
        )
        self.neighbor_state._parent = weakref.ref(self)
        self.is_router = Empty(_meta={"mandatory": False},
        )
        self.is_router._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpIpv6Config(BaseBinding):
    """
    IPv6-specific configuration data for VRRP on IPv6
    interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.virtual_link_local = inet.IpAddress(_meta={"mandatory": False},
        )
        self.virtual_link_local._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpIpv6State(IpVrrpIpv6Config):
    """
    IPv6-specific operational state for VRRP on IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpTrackingConfig(BaseBinding):
    """
    Configuration data for tracking interfaces
    in a VRRP group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.track_interface = Leafref(_meta={"mandatory": False},
            path="/oc-if:interfaces/oc-if:interface/oc-if:name",
        )
        self.track_interface._parent = weakref.ref(self)
        self.priority_decrement = Uint8(_meta={"mandatory": False},
            range_="0..254",
        )
        self.priority_decrement._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpTrackingState(BaseBinding):
    """
    Operational state data for tracking interfaces in a VRRP
    group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceTracking_Config_515(IpVrrpTrackingConfig):
    """
    Configuration data for VRRP interface tracking
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceTracking_State_522(IpVrrpTrackingState, IpVrrpTrackingConfig):
    """
    Operational state data for VRRP interface tracking
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class IpVrrpTrackingTop_InterfaceTracking_511(BaseBinding):
    """
    Top-level container for VRRP interface tracking
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = InterfaceTracking_Config_515()
        self.config._parent = weakref.ref(self)
        self.state = InterfaceTracking_State_522()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpTrackingTop(BaseBinding):
    """
    Top-level grouping for VRRP interface tracking
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.interface_tracking = IpVrrpTrackingTop_InterfaceTracking_511()
        self.interface_tracking._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpConfig(BaseBinding):
    """
    Configuration data for VRRP on IP interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.advertisement_interval = Uint16(_meta={"mandatory": False},
            range_="1..4095",
        )
        self.advertisement_interval._parent = weakref.ref(self)
        self.accept_mode = Boolean(_meta={"mandatory": False},
        )
        self.accept_mode._parent = weakref.ref(self)
        self.virtual_router_id = Uint8(_meta={"mandatory": False},
            range_="1..255",
        )
        self.virtual_router_id._parent = weakref.ref(self)
        self.preempt_delay = Uint16(_meta={"mandatory": False},
            range_="0..3600",
        )
        self.preempt_delay._parent = weakref.ref(self)
        self.priority = Uint8(_meta={"mandatory": False},
            range_="1..254",
        )
        self.priority._parent = weakref.ref(self)
        self.preempt = Boolean(_meta={"mandatory": False},
        )
        self.preempt._parent = weakref.ref(self)
        # leaflist
        self.virtual_address = LeafList(inet.IpAddress(_meta={"mandatory": False}, ))
        self.virtual_address._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class IpVrrpState(BaseBinding):
    """
    Operational state data for VRRP on IP interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.current_priority = Uint8(_meta={"mandatory": False},
        )
        self.current_priority._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VrrpGroup_Config_644(IpVrrpConfig):
    """
    Configuration data for the VRRP group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VrrpGroup_State_651(IpVrrpState, IpVrrpConfig):
    """
    Operational state data for the VRRP group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Vrrp_VrrpGroup_630(List, IpVrrpTrackingTop):
    """
    List of VRRP groups, keyed by virtual router id
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = VrrpGroup_Config_644()
        self.config._parent = weakref.ref(self)
        self.state = VrrpGroup_State_651()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.virtual_router_id = Leafref(_meta={"mandatory": False},
            path="../config/virtual-router-id",
        )
        self.virtual_router_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "virtual_router_id"





class IpVrrpTop_Vrrp_622(BaseBinding):
    """
    Enclosing container for VRRP groups handled by this
    IP interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.vrrp_group = Vrrp_VrrpGroup_630()
        self.vrrp_group._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpVrrpTop(BaseBinding):
    """
    Top-level grouping for Virtual Router Redundancy Protocol
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.vrrp = IpVrrpTop_Vrrp_622()
        self.vrrp._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Address_Config_691(Ipv4AddressConfig):
    """
    Configuration data for each configured IPv4
    address on the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Address_State_699(Ipv4AddressState, Ipv4AddressConfig):
    """
    Operational state data for each IPv4 address
    configured on the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Addresses_Address_679(List, BaseBinding):
    """
    The list of configured IPv4 addresses on the interface.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Address_Config_691()
        self.config._parent = weakref.ref(self)
        self.state = Address_State_699()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.ip = Leafref(_meta={"mandatory": False},
            path="../oc-ip:config/oc-ip:ip",
        )
        self.ip._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ip"





class Ipv4_Addresses_675(BaseBinding):
    """
    Enclosing container for address list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.address = Addresses_Address_679()
        self.address._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Neighbor_Config_734(Ipv4NeighborConfig):
    """
    Configuration data for each configured IPv4
    address on the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Neighbor_State_742(Ipv4NeighborState, Ipv4NeighborConfig):
    """
    Operational state data for each IPv4 address
    configured on the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Neighbors_Neighbor_716(List, BaseBinding):
    """
    A list of mappings from IPv4 addresses to
    link-layer addresses.

    Entries in this list are used as static entries in the
    ARP Cache.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Neighbor_Config_734()
        self.config._parent = weakref.ref(self)
        self.state = Neighbor_State_742()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.ip = Leafref(_meta={"mandatory": False},
            path="../oc-ip:config/oc-ip:ip",
        )
        self.ip._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ip"





class Ipv4_Neighbors_712(BaseBinding):
    """
    Enclosing container for neighbor list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.neighbor = Neighbors_Neighbor_716()
        self.neighbor._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4_Config_756(Ipv4GlobalConfig):
    """
    Top-level IPv4 configuration data for the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4_State_763(Ipv4GlobalConfig):
    """
    Top level IPv4 operational state data
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Ipv4Top_Ipv4_671(oc_if.SubUnnumberedTop):
    """
    Parameters for the IPv4 address family.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.addresses = Ipv4_Addresses_675()
        self.addresses._parent = weakref.ref(self)
        self.neighbors = Ipv4_Neighbors_712()
        self.neighbors._parent = weakref.ref(self)
        self.config = Ipv4_Config_756()
        self.config._parent = weakref.ref(self)
        self.state = Ipv4_State_763()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv4Top(BaseBinding):
    """
    Top-level configuration and state for IPv4
    interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.ipv4 = Ipv4Top_Ipv4_671()
        self.ipv4._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Address_Config_798(Ipv6AddressConfig):
    """
    Configuration data for each IPv6 address on
    the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Address_State_807(Ipv6AddressState, Ipv6AddressConfig):
    """
    State data for each IPv6 address on the
    interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Addresses_Address_786(List, BaseBinding):
    """
    The list of configured IPv6 addresses on the interface.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Address_Config_798()
        self.config._parent = weakref.ref(self)
        self.state = Address_State_807()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.ip = Leafref(_meta={"mandatory": False},
            path="../oc-ip:config/oc-ip:ip",
        )
        self.ip._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ip"





class Ipv6_Addresses_782(BaseBinding):
    """
    Enclosing container for address list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.address = Addresses_Address_786()
        self.address._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Neighbor_Config_837(Ipv6NeighborConfig):
    """
    Configuration data for each IPv6 address on
    the interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Neighbor_State_845(Ipv6NeighborState, Ipv6NeighborConfig):
    """
    State data for each IPv6 address on the
    interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Neighbors_Neighbor_824(List, BaseBinding):
    """
    List of IPv6 neighbors
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Neighbor_Config_837()
        self.config._parent = weakref.ref(self)
        self.state = Neighbor_State_845()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.ip = Leafref(_meta={"mandatory": False},
            path="../oc-ip:config/oc-ip:ip",
        )
        self.ip._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ip"





class Ipv6_Neighbors_820(BaseBinding):
    """
    Enclosing container for list of IPv6 neighbors
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.neighbor = Neighbors_Neighbor_824()
        self.neighbor._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6_Config_858(Ipv6GlobalConfig):
    """
    Top-level config data for the IPv6 interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6_State_864(Ipv6GlobalConfig):
    """
    Top-level operational state data for the IPv6 interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Ipv6Top_Ipv6_778(oc_if.SubUnnumberedTop):
    """
    Parameters for the IPv6 address family.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.addresses = Ipv6_Addresses_782()
        self.addresses._parent = weakref.ref(self)
        self.neighbors = Ipv6_Neighbors_820()
        self.neighbors._parent = weakref.ref(self)
        self.config = Ipv6_Config_858()
        self.config._parent = weakref.ref(self)
        self.state = Ipv6_State_864()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6Top(BaseBinding):
    """
    Top-level configuration and state for IPv6 interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.ipv6 = Ipv6Top_Ipv6_778()
        self.ipv6._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment, Ipv6Top, Ipv4Top):
    """IPv4 addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        Ipv6Top.__init__(self)
        
        Ipv4Top.__init__(self)
        



# Load the augmentation
Augment_0()()

class Augment_1(BaseAugment, IpVrrpTop):
    """Additional IP addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpTop.__init__(self)
        



# Load the augmentation
Augment_1()()

class Augment_2(BaseAugment, IpVrrpTop):
    """Additional IP addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan', u'oc-ip:ipv4', u'oc-ip:addresses', u'oc-ip:address']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpTop.__init__(self)
        



# Load the augmentation
Augment_2()()

class Augment_3(BaseAugment, IpVrrpIpv6Config):
    """Additional VRRP data for IPv6 interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address', u'vrrp', u'vrrp-group', u'config']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpIpv6Config.__init__(self)
        



# Load the augmentation
Augment_3()()

class Augment_4(BaseAugment, Ipv6Top, Ipv4Top):
    """IPv4 addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        Ipv6Top.__init__(self)
        
        Ipv4Top.__init__(self)
        



# Load the augmentation
Augment_4()()

class Augment_5(BaseAugment, IpVrrpTop):
    """Additional IP addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpTop.__init__(self)
        



# Load the augmentation
Augment_5()()

class Augment_6(BaseAugment, IpVrrpIpv6Config):
    """Additional VRRP data for IPv6 interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address', u'vrrp', u'vrrp-group', u'config']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpIpv6Config.__init__(self)
        



# Load the augmentation
Augment_6()()

class Augment_7(BaseAugment, IpVrrpTop):
    """Additional IP addr family configuration for
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv4', u'oc-ip:addresses', u'oc-ip:address']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpTop.__init__(self)
        



# Load the augmentation
Augment_7()()

class Augment_8(BaseAugment, IpVrrpIpv6State):
    """Additional VRRP data for IPv6 interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address', u'vrrp', u'vrrp-group', u'state']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpIpv6State.__init__(self)
        



# Load the augmentation
Augment_8()()

class Augment_9(BaseAugment, IpVrrpIpv6State):
    """Additional VRRP data for IPv6 interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv6', u'oc-ip:addresses', u'oc-ip:address', u'vrrp', u'vrrp-group', u'state']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        IpVrrpIpv6State.__init__(self)
        



# Load the augmentation
Augment_9()()
