"""
This sub-module contains groupings that are specific to the
global context of the OpenConfig BGP module
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
from napalm_yang import yang
from napalm_yang import oc_ext
# Imcludes
from openconfig_bgp_common_multiprotocol import *

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



# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class BgpGlobalConfig(BaseBinding):
    """
    Global configuration options for the BGP router.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.as_ = inet.AsNumber(_meta={"mandatory": True},
        )
        self.as_._parent = weakref.ref(self)
        self.router_id = yang.DottedQuad(_meta={"mandatory": False},
        )
        self.router_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpGlobalState(BgpCommonState):
    """
    Operational state parameters for the BGP neighbor
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
        




class BgpGlobalDefaultRouteDistanceConfig(BaseBinding):
    """
    Configuration options relating to the administrative distance
    (or preference) assigned to routes received from different
    sources (external, internal, and local).
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.external_route_distance = Uint8(_meta={"mandatory": False},
            range_="1..255",
        )
        self.external_route_distance._parent = weakref.ref(self)
        self.internal_route_distance = Uint8(_meta={"mandatory": False},
            range_="1..255",
        )
        self.internal_route_distance._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpGlobalConfederationConfig(BaseBinding):
    """
    Configuration options specifying parameters when the local
    router is within an autonomous system which is part of a BGP
    confederation.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.identifier = inet.AsNumber(_meta={"mandatory": False},
        )
        self.identifier._parent = weakref.ref(self)
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        # leaflist
        self.member_as = LeafList(inet.AsNumber(_meta={"mandatory": False}, ))
        self.member_as._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class AfiSafi_Config_136(BgpCommonMpAfiSafiConfig):
    """
    Configuration parameters for the AFI-SAFI
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
        




class AfiSafi_State_141(BgpCommonState, BgpCommonMpAfiSafiConfig):
    """
    State information relating to the AFI-SAFI
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
        




class GracefulRestart_Config_152(BgpCommonMpAfiSafiGracefulRestartConfig):
    """
    Configuration options for BGP graceful-restart
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
        




class GracefulRestart_State_157(BgpCommonMpAfiSafiGracefulRestartConfig):
    """
    State information for BGP graceful-restart
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
        




class AfiSafi_GracefulRestart_149(BaseBinding):
    """
    Parameters relating to BGP graceful-restart
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_152()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_157()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpGlobalAfiSafiList_AfiSafi_120(List, BgpCommonMpAllAfiSafiListContents, BgpCommonGlobalGroupUseMultiplePaths, BgpCommonRouteSelectionOptions):
    """
    AFI,SAFI configuration available for the
    neighbour or group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = AfiSafi_Config_136()
        self.config._parent = weakref.ref(self)
        self.state = AfiSafi_State_141()
        self.state._parent = weakref.ref(self)
        self.graceful_restart = AfiSafi_GracefulRestart_149()
        self.graceful_restart._parent = weakref.ref(self)
        # list
        # leaf
        self.afi_safi_name = Leafref(_meta={"mandatory": False},
            path="../config/afi-safi-name",
        )
        self.afi_safi_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "afi_safi_name"





class BgpGlobalAfiSafiList(BaseBinding):
    """
    List of address-families associated with the BGP instance
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.afi_safi = BgpGlobalAfiSafiList_AfiSafi_120()
        self.afi_safi._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpGlobalBase_Config_176(BgpGlobalConfig):
    """
    Configuration parameters relating to the global BGP router
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
        




class BgpGlobalBase_State_181(BgpGlobalState, BgpGlobalConfig):
    """
    State information relating to the global BGP router
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
        




class DefaultRouteDistance_Config_195(BgpGlobalDefaultRouteDistanceConfig):
    """
    Configuration parameters relating to the default route
    distance
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
        




class DefaultRouteDistance_State_201(BgpGlobalDefaultRouteDistanceConfig):
    """
    State information relating to the default route distance
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
        




class BgpGlobalBase_DefaultRouteDistance_189(BaseBinding):
    """
    Administrative distance (or preference) assigned to
    routes received from different sources
    (external, internal, and local).
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = DefaultRouteDistance_Config_195()
        self.config._parent = weakref.ref(self)
        self.state = DefaultRouteDistance_State_201()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Confederation_Config_214(BgpGlobalConfederationConfig):
    """
    Configuration parameters relating to BGP confederations
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
        




class Confederation_State_219(BgpGlobalConfederationConfig):
    """
    State information relating to the BGP confederations
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
        




class BgpGlobalBase_Confederation_209(BaseBinding):
    """
    Parameters indicating whether the local system acts as part
    of a BGP confederation
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Confederation_Config_214()
        self.config._parent = weakref.ref(self)
        self.state = Confederation_State_219()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GracefulRestart_Config_230(BgpCommonGracefulRestartConfig):
    """
    Configuration parameters relating to graceful-restart
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
        




class GracefulRestart_State_235(BgpCommonGracefulRestartConfig):
    """
    State information associated with graceful-restart
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
        




class BgpGlobalBase_GracefulRestart_227(BaseBinding):
    """
    Parameters relating the graceful restart mechanism for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_230()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_235()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpGlobalBase_AfiSafis_246(BgpGlobalAfiSafiList):
    """
    Address family specific configuration
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
        




class BgpGlobalBase(BgpCommonRouteSelectionOptions, BgpCommonGlobalGroupUseMultiplePaths):
    """
    Global configuration parameters for the BGP router
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpGlobalBase_Config_176()
        self.config._parent = weakref.ref(self)
        self.state = BgpGlobalBase_State_181()
        self.state._parent = weakref.ref(self)
        self.default_route_distance = BgpGlobalBase_DefaultRouteDistance_189()
        self.default_route_distance._parent = weakref.ref(self)
        self.confederation = BgpGlobalBase_Confederation_209()
        self.confederation._parent = weakref.ref(self)
        self.graceful_restart = BgpGlobalBase_GracefulRestart_227()
        self.graceful_restart._parent = weakref.ref(self)
        self.afi_safis = BgpGlobalBase_AfiSafis_246()
        self.afi_safis._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments