"""
This sub-module contains common groupings that are common across
multiple contexts within the BGP module. That is to say that they
may be application to a subset of global, peer-group or neighbor
contexts.
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
from napalm_yang import inet
from napalm_yang import oc_ext
from napalm_yang import oc_bgp_types
from napalm_yang import oc_rpol
# Imcludes

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



# extensions

# features


# typedef


# Identities

#
class BgpCommonUseMultiplePathsEbgpConfig(BaseBinding):
    """
    Configuration parameters relating to multipath for eBGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.allow_multiple_as = Boolean(_meta={"mandatory": False},
        )
        self.allow_multiple_as._parent = weakref.ref(self)
        self.maximum_paths = Uint32(_meta={"mandatory": False},
        )
        self.maximum_paths._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonUseMultiplePathsIbgpConfig(BaseBinding):
    """
    Configuration parmaeters relating to multipath for iBGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.maximum_paths = Uint32(_meta={"mandatory": False},
        )
        self.maximum_paths._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonRouteSelectionOptionsConfig(BaseBinding):
    """
    Set of configuration options that govern best
    path selection.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enable_aigp = Boolean(_meta={"mandatory": False},
        )
        self.enable_aigp._parent = weakref.ref(self)
        self.ignore_as_path_length = Boolean(_meta={"mandatory": False},
        )
        self.ignore_as_path_length._parent = weakref.ref(self)
        self.advertise_inactive_routes = Boolean(_meta={"mandatory": False},
        )
        self.advertise_inactive_routes._parent = weakref.ref(self)
        self.ignore_next_hop_igp_metric = Boolean(_meta={"mandatory": False},
        )
        self.ignore_next_hop_igp_metric._parent = weakref.ref(self)
        self.always_compare_med = Boolean(_meta={"mandatory": False},
        )
        self.always_compare_med._parent = weakref.ref(self)
        self.external_compare_router_id = Boolean(_meta={"mandatory": False},
        )
        self.external_compare_router_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        

 # Classes to support containers and lists



class BgpCommonNeighborGroupTimersConfig(BaseBinding):
    """
    Config parameters related to timers associated with the BGP
    peer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.connect_retry = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.connect_retry._parent = weakref.ref(self)
        self.keepalive_interval = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.keepalive_interval._parent = weakref.ref(self)
        self.minimum_advertisement_interval = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.minimum_advertisement_interval._parent = weakref.ref(self)
        self.hold_time = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.hold_time._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupConfig(BaseBinding):
    """
    Neighbor level configuration items.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.send_community = oc_bgp_types.CommunityType(_meta={"mandatory": False},
        )
        self.send_community._parent = weakref.ref(self)
        self.local_as = inet.AsNumber(_meta={"mandatory": False},
        )
        self.local_as._parent = weakref.ref(self)
        self.description = String(_meta={"mandatory": False},
        )
        self.description._parent = weakref.ref(self)
        self.route_flap_damping = Boolean(_meta={"mandatory": False},
        )
        self.route_flap_damping._parent = weakref.ref(self)
        self.peer_as = inet.AsNumber(_meta={"mandatory": False},
        )
        self.peer_as._parent = weakref.ref(self)
        self.remove_private_as = oc_bgp_types.RemovePrivateAsOption(_meta={"mandatory": False},
        )
        self.remove_private_as._parent = weakref.ref(self)
        self.auth_password = String(_meta={"mandatory": False},
        )
        self.auth_password._parent = weakref.ref(self)
        self.peer_type = oc_bgp_types.PeerType(_meta={"mandatory": False},
        )
        self.peer_type._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupTransportConfig(BaseBinding):
    """
    Configuration parameters relating to the transport protocol
    used by the BGP session to the peer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.tcp_mss = Uint16(_meta={"mandatory": False},
        )
        self.tcp_mss._parent = weakref.ref(self)
        self.local_address = Union(_meta={"mandatory": False},
            type_={
            "inet:ip-address": {}, 
            "string": {}
        },
        )
        self.local_address._parent = weakref.ref(self)
        self.mtu_discovery = Boolean(_meta={"mandatory": False},
        )
        self.mtu_discovery._parent = weakref.ref(self)
        self.passive_mode = Boolean(_meta={"mandatory": False},
        )
        self.passive_mode._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupErrorHandlingConfig(BaseBinding):
    """
    Configuration parameters relating to enhanced error handling
    behaviours for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.treat_as_withdraw = Boolean(_meta={"mandatory": False},
        )
        self.treat_as_withdraw._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupLoggingOptionsConfig(BaseBinding):
    """
    Configuration parameters specifying the logging behaviour for
    BGP sessions to the peer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.log_neighbor_state_changes = Boolean(_meta={"mandatory": False},
        )
        self.log_neighbor_state_changes._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupMultihopConfig(BaseBinding):
    """
    Configuration parameters specifying the multihop behaviour for
    BGP sessions to the peer
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
        self.multihop_ttl = Uint8(_meta={"mandatory": False},
        )
        self.multihop_ttl._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupRouteReflectorConfig(BaseBinding):
    """
    Configuration parameters determining whether the behaviour of
    the local system when acting as a route-reflector
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.route_reflector_client = Boolean(_meta={"mandatory": False},
        )
        self.route_reflector_client._parent = weakref.ref(self)
        self.route_reflector_cluster_id = oc_bgp_types.RrClusterIdType(_meta={"mandatory": False},
        )
        self.route_reflector_cluster_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupAsPathOptionsConfig(BaseBinding):
    """
    Configuration parameters allowing manipulation of the AS_PATH
    attribute
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.replace_peer_as = Boolean(_meta={"mandatory": False},
        )
        self.replace_peer_as._parent = weakref.ref(self)
        self.allow_own_as = Uint8(_meta={"mandatory": False},
        )
        self.allow_own_as._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonNeighborGroupAddPathsConfig(BaseBinding):
    """
    Configuration parameters specfying whether the local system
    will send or receive multiple paths using ADD_PATHS
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.receive = Boolean(_meta={"mandatory": False},
        )
        self.receive._parent = weakref.ref(self)
        self.eligible_prefix_policy = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:policy-definitions/oc-rpol:policy-definition/oc-rpol:name",
        )
        self.eligible_prefix_policy._parent = weakref.ref(self)
        self.send_max = Uint8(_meta={"mandatory": False},
        )
        self.send_max._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonGracefulRestartConfig(BaseBinding):
    """
    Configuration parameters relating to BGP graceful restart.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.helper_only = Boolean(_meta={"mandatory": False},
        )
        self.helper_only._parent = weakref.ref(self)
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        self.stale_routes_time = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.stale_routes_time._parent = weakref.ref(self)
        self.restart_time = Uint16(_meta={"mandatory": False},
            range_="0..4096",
        )
        self.restart_time._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonUseMultiplePathsConfig(BaseBinding):
    """
    Generic configuration options relating to use of multiple
    paths for a referenced AFI-SAFI, group or neighbor
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
        




class BgpCommonUseMultiplePathsEbgpAsOptionsConfig(BaseBinding):
    """
    Configuration parameters specific to eBGP multipath applicable
    to all contexts
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.allow_multiple_as = Boolean(_meta={"mandatory": False},
        )
        self.allow_multiple_as._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class UseMultiplePaths_Config_416(BgpCommonUseMultiplePathsConfig):
    """
    Configuration parameters relating to multipath
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
        




class UseMultiplePaths_State_421(BgpCommonUseMultiplePathsConfig):
    """
    State parameters relating to multipath
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
        




class Ebgp_Config_431(BgpCommonUseMultiplePathsEbgpConfig):
    """
    Configuration parameters relating to eBGP multipath
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
        




class Ebgp_State_436(BgpCommonUseMultiplePathsEbgpConfig):
    """
    State information relating to eBGP multipath
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
        




class UseMultiplePaths_Ebgp_428(BaseBinding):
    """
    Multipath parameters for eBGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Ebgp_Config_431()
        self.config._parent = weakref.ref(self)
        self.state = Ebgp_State_436()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ibgp_Config_447(BgpCommonUseMultiplePathsIbgpConfig):
    """
    Configuration parameters relating to iBGP multipath
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
        




class Ibgp_State_452(BgpCommonUseMultiplePathsIbgpConfig):
    """
    State information relating to iBGP multipath
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
        




class UseMultiplePaths_Ibgp_444(BaseBinding):
    """
    Multipath parameters for iBGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Ibgp_Config_447()
        self.config._parent = weakref.ref(self)
        self.state = Ibgp_State_452()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonGlobalGroupUseMultiplePaths_UseMultiplePaths_411(BaseBinding):
    """
    Parameters related to the use of multiple paths for the
    same NLRI
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = UseMultiplePaths_Config_416()
        self.config._parent = weakref.ref(self)
        self.state = UseMultiplePaths_State_421()
        self.state._parent = weakref.ref(self)
        self.ebgp = UseMultiplePaths_Ebgp_428()
        self.ebgp._parent = weakref.ref(self)
        self.ibgp = UseMultiplePaths_Ibgp_444()
        self.ibgp._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonGlobalGroupUseMultiplePaths(BaseBinding):
    """
    Common grouping used for both global and groups which provides
    configuration and state parameters relating to use of multiple
    paths
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.use_multiple_paths = BgpCommonGlobalGroupUseMultiplePaths_UseMultiplePaths_411()
        self.use_multiple_paths._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



class RouteSelectionOptions_Config_563(BgpCommonRouteSelectionOptionsConfig):
    """
    Configuration parameters relating to route selection
    options
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
        




class RouteSelectionOptions_State_569(BgpCommonRouteSelectionOptionsConfig):
    """
    State information for the route selection options
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
        




class BgpCommonRouteSelectionOptions_RouteSelectionOptions_560(BaseBinding):
    """
    Parameters relating to options for route selection
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = RouteSelectionOptions_Config_563()
        self.config._parent = weakref.ref(self)
        self.state = RouteSelectionOptions_State_569()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonRouteSelectionOptions(BaseBinding):
    """
    Configuration and state relating to route selection options
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.route_selection_options = BgpCommonRouteSelectionOptions_RouteSelectionOptions_560()
        self.route_selection_options._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonState(BaseBinding):
    """
    Grouping containing common counters relating to prefixes and
    paths
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.total_prefixes = Uint32(_meta={"mandatory": False},
        )
        self.total_prefixes._parent = weakref.ref(self)
        self.total_paths = Uint32(_meta={"mandatory": False},
        )
        self.total_paths._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
