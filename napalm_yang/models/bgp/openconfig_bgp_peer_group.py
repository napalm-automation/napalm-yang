"""
This sub-module contains groupings that are specific to the
peer-group context of the OpenConfig BGP module.
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
from napalm_yang import oc_rpol
# Imcludes
from openconfig_bgp_common_structure import *

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



class BgpPeerGroupConfig(BaseBinding):
    """
    Configuration parameters relating to a base BGP peer group that
    are not also applicable to any other context (e.g., neighbor)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.peer_group_name = String(_meta={"mandatory": False},
        )
        self.peer_group_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AfiSafi_Config_68(BgpCommonMpAfiSafiConfig):
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
        




class AfiSafi_State_73(BgpCommonMpAfiSafiConfig):
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
        




class GracefulRestart_Config_83(BgpCommonMpAfiSafiGracefulRestartConfig):
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
        




class GracefulRestart_State_88(BgpCommonMpAfiSafiGracefulRestartConfig):
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
        




class AfiSafi_GracefulRestart_80(BaseBinding):
    """
    Parameters relating to BGP graceful-restart
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_83()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_88()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpPeerGroupAfiSafiList_AfiSafi_52(List, BgpCommonMpAllAfiSafiListContents, BgpCommonGlobalGroupUseMultiplePaths, BgpCommonRouteSelectionOptions):
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
        self.config = AfiSafi_Config_68()
        self.config._parent = weakref.ref(self)
        self.state = AfiSafi_State_73()
        self.state._parent = weakref.ref(self)
        self.graceful_restart = AfiSafi_GracefulRestart_80()
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





class BgpPeerGroupAfiSafiList(BaseBinding):
    """
    List of address-families associated with the BGP peer-group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.afi_safi = BgpPeerGroupAfiSafiList_AfiSafi_52()
        self.afi_safi._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpPeerGroupBase_Config_106(BgpCommonNeighborGroupConfig, BgpPeerGroupConfig):
    """
    Configuration parameters relating to the BGP neighbor or
    group
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
        




class BgpPeerGroupBase_State_113(BgpCommonState, BgpCommonNeighborGroupConfig, BgpPeerGroupConfig):
    """
    State information relating to the BGP peer-group
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
        




class Timers_Config_126(BgpCommonNeighborGroupTimersConfig):
    """
    Configuration parameters relating to timers used for the
    BGP neighbor or peer group
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
        




class Timers_State_132(BgpCommonNeighborGroupTimersConfig):
    """
    State information relating to the timers used for the BGP
    group
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
        




class BgpPeerGroupBase_Timers_122(BaseBinding):
    """
    Timers related to a BGP peer-group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Timers_Config_126()
        self.config._parent = weakref.ref(self)
        self.state = Timers_State_132()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Transport_Config_145(BgpCommonNeighborGroupTransportConfig):
    """
    Configuration parameters relating to the transport
    session(s) used for the BGP neighbor or group
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
        




class Transport_State_151(BgpCommonNeighborGroupTransportConfig):
    """
    State information relating to the transport session(s)
    used for the BGP neighbor or group
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
        




class BgpPeerGroupBase_Transport_141(BaseBinding):
    """
    Transport session parameters for the BGP peer-group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Transport_Config_145()
        self.config._parent = weakref.ref(self)
        self.state = Transport_State_151()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ErrorHandling_Config_164(BgpCommonNeighborGroupErrorHandlingConfig):
    """
    Configuration parameters enabling or modifying the
    behavior or enhanced error handling mechanisms for the BGP
    group
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
        




class ErrorHandling_State_171(BgpCommonNeighborGroupErrorHandlingConfig):
    """
    State information relating to enhanced error handling
    mechanisms for the BGP group
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
        




class BgpPeerGroupBase_ErrorHandling_160(BaseBinding):
    """
    Error handling parameters used for the BGP peer-group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = ErrorHandling_Config_164()
        self.config._parent = weakref.ref(self)
        self.state = ErrorHandling_State_171()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GracefulRestart_Config_183(BgpCommonGracefulRestartConfig):
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
        




class GracefulRestart_State_188(BgpCommonGracefulRestartConfig):
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
        




class BgpPeerGroupBase_GracefulRestart_180(BaseBinding):
    """
    Parameters relating the graceful restart mechanism for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_183()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_188()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpPeerGroupBase_AfiSafis_204(BgpPeerGroupAfiSafiList):
    """
    Per-address-family configuration parameters associated with
    thegroup
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
        




class BgpPeerGroupBase(oc_rpol.ApplyPolicyGroup, BgpCommonGlobalGroupUseMultiplePaths, BgpCommonStructureNeighborGroupAddPaths, BgpCommonStructureNeighborGroupAsPathOptions, BgpCommonStructureNeighborGroupRouteReflector, BgpCommonStructureNeighborGroupEbgpMultihop, BgpCommonStructureNeighborGroupLoggingOptions):
    """
    Parameters related to a BGP group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpPeerGroupBase_Config_106()
        self.config._parent = weakref.ref(self)
        self.state = BgpPeerGroupBase_State_113()
        self.state._parent = weakref.ref(self)
        self.timers = BgpPeerGroupBase_Timers_122()
        self.timers._parent = weakref.ref(self)
        self.transport = BgpPeerGroupBase_Transport_141()
        self.transport._parent = weakref.ref(self)
        self.error_handling = BgpPeerGroupBase_ErrorHandling_160()
        self.error_handling._parent = weakref.ref(self)
        self.graceful_restart = BgpPeerGroupBase_GracefulRestart_180()
        self.graceful_restart._parent = weakref.ref(self)
        self.afi_safis = BgpPeerGroupBase_AfiSafis_204()
        self.afi_safis._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpPeerGroupList_PeerGroup_216(List, BgpPeerGroupBase):
    """
    List of BGP peer-groups configured on the local system -
    uniquely identified by peer-group name
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.peer_group_name = Leafref(_meta={"mandatory": False},
            path="../config/peer-group-name",
        )
        self.peer_group_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "peer_group_name"





class BgpPeerGroupList(BaseBinding):
    """
    The list of BGP peer groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.peer_group = BgpPeerGroupList_PeerGroup_216()
        self.peer_group._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments