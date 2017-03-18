"""
This sub-module contains groupings that are specific to the
neighbor context of the OpenConfig BGP module.
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
from napalm_yang import oc_bgp_types
from napalm_yang import inet
from napalm_yang import oc_types
from napalm_yang import oc_rpol
from napalm_yang import oc_ext
from napalm_yang import yang
# Imcludes
from openconfig_bgp_common_structure import *

from openconfig_bgp_peer_group import *

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


class BgpNeighborCountersMessageTypesState(BaseBinding):
    """
    Grouping of BGP message types, included for re-use
    across counters
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.NOTIFICATION = Uint64(_meta={"mandatory": False},
        )
        self.NOTIFICATION._parent = weakref.ref(self)
        self.UPDATE = Uint64(_meta={"mandatory": False},
        )
        self.UPDATE._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborQueueCountersState(BaseBinding):
    """
    Counters relating to the message queues associated with the
    BGP peer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.output = Uint32(_meta={"mandatory": False},
        )
        self.output._parent = weakref.ref(self)
        self.input = Uint32(_meta={"mandatory": False},
        )
        self.input._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborTransportState(BaseBinding):
    """
    Operational state parameters relating to the transport session
    used for the BGP session
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.remote_address = inet.IpAddress(_meta={"mandatory": False},
        )
        self.remote_address._parent = weakref.ref(self)
        self.remote_port = inet.PortNumber(_meta={"mandatory": False},
        )
        self.remote_port._parent = weakref.ref(self)
        self.local_port = inet.PortNumber(_meta={"mandatory": False},
        )
        self.local_port._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborErrorHandlingState(BaseBinding):
    """
    Operational state parameters relating to enhanced error
    error handling for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.erroneous_update_messages = Uint32(_meta={"mandatory": False},
        )
        self.erroneous_update_messages._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborTimersState(BaseBinding):
    """
    Operational state parameters relating to BGP timers associated
    with the BGP session
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.negotiated_hold_time = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.negotiated_hold_time._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiGracefulRestartState(BaseBinding):
    """
    Operational state variables relating to the graceful-restart
    mechanism on a per-AFI-SAFI basis
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.received = Boolean(_meta={"mandatory": False},
        )
        self.received._parent = weakref.ref(self)
        self.advertised = Boolean(_meta={"mandatory": False},
        )
        self.advertised._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborGracefulRestartState(BaseBinding):
    """
    Operational state information relevant to graceful restart
    for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.local_restarting = Boolean(_meta={"mandatory": False},
        )
        self.local_restarting._parent = weakref.ref(self)
        self.peer_restart_time = Uint16(_meta={"mandatory": False},
            range_="0..4096",
        )
        self.peer_restart_time._parent = weakref.ref(self)
        self.mode = Enumeration(_meta={"mandatory": False},
            enum={
            "BILATERAL": {
                "info": {
                    "description": "The local router is operating in both helper mode, and\nhence retains forwarding state during a remote restart,\nand also maintains forwarding state during local session\nrestart"
                }
            }, 
            "HELPER_ONLY": {
                "info": {
                    "description": "The local router is operating in helper-only mode, and\nhence will not retain forwarding state during a local\nsession restart, but will do so during a restart of the\nremote peer"
                }
            }, 
            "REMOTE_HELPER": {
                "info": {
                    "description": "The local system is able to retain routes during restart\nbut the remote system is only able to act as a helper"
                }
            }
        },
        )
        self.mode._parent = weakref.ref(self)
        self.peer_restarting = Boolean(_meta={"mandatory": False},
        )
        self.peer_restarting._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiState_Prefixes_403(BaseBinding):
    """
    Prefix counters for the BGP session
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.received = Uint32(_meta={"mandatory": False},
        )
        self.received._parent = weakref.ref(self)
        self.sent = Uint32(_meta={"mandatory": False},
        )
        self.sent._parent = weakref.ref(self)
        self.installed = Uint32(_meta={"mandatory": False},
        )
        self.installed._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiState(BaseBinding):
    """
    Operational state parameters relating to an individual AFI,
    SAFI for a neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.prefixes = BgpNeighborAfiSafiState_Prefixes_403()
        self.prefixes._parent = weakref.ref(self)
        # list
        # leaf
        self.active = Boolean(_meta={"mandatory": False},
        )
        self.active._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        


# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class BgpNeighborConfig(BaseBinding):
    """
    Configuration parameters relating to a base BGP neighbor that
    are not also applicable to any other context
    (e.g., peer group)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.neighbor_address = inet.IpAddress(_meta={"mandatory": False},
        )
        self.neighbor_address._parent = weakref.ref(self)
        self.peer_group = Leafref(_meta={"mandatory": False},
            path="../../../../peer-groups/peer-group/peer-group-name",
        )
        self.peer_group._parent = weakref.ref(self)
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class UseMultiplePaths_Config_84(BgpCommonUseMultiplePathsConfig):
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
        




class UseMultiplePaths_State_89(BgpCommonUseMultiplePathsConfig):
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
        




class Ebgp_Config_99(BgpCommonUseMultiplePathsEbgpAsOptionsConfig):
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
        




class Ebgp_State_104(BgpCommonUseMultiplePathsEbgpAsOptionsConfig):
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
        




class UseMultiplePaths_Ebgp_96(BaseBinding):
    """
    Multipath configuration for eBGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Ebgp_Config_99()
        self.config._parent = weakref.ref(self)
        self.state = Ebgp_State_104()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborUseMultiplePaths_UseMultiplePaths_79(BaseBinding):
    """
    Parameters related to the use of multiple-paths for the same
    NLRI when they are received only from this neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = UseMultiplePaths_Config_84()
        self.config._parent = weakref.ref(self)
        self.state = UseMultiplePaths_State_89()
        self.state._parent = weakref.ref(self)
        self.ebgp = UseMultiplePaths_Ebgp_96()
        self.ebgp._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborUseMultiplePaths(BaseBinding):
    """
    Multipath configuration and state applicable to a BGP
    neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.use_multiple_paths = BgpNeighborUseMultiplePaths_UseMultiplePaths_79()
        self.use_multiple_paths._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Messages_Sent_193(BgpNeighborCountersMessageTypesState):
    """
    Counters relating to BGP messages sent to the neighbor
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
        




class Messages_Received_199(BgpNeighborCountersMessageTypesState):
    """
    Counters for BGP messages received from the neighbor
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
        




class BgpNeighborState_Messages_189(BaseBinding):
    """
    Counters for BGP messages sent and received from the
    neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.sent = Messages_Sent_193()
        self.sent._parent = weakref.ref(self)
        self.received = Messages_Received_199()
        self.received._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborState_Queues_206(BgpNeighborQueueCountersState):
    """
    Counters related to queued messages associated with the
    BGP neighbor
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
        




class BgpNeighborState(BaseBinding):
    """
    Operational state parameters relating only to a BGP neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.messages = BgpNeighborState_Messages_189()
        self.messages._parent = weakref.ref(self)
        self.queues = BgpNeighborState_Queues_206()
        self.queues._parent = weakref.ref(self)
        # list
        # leaf
        self.session_state = Enumeration(_meta={"mandatory": False},
            enum={
            "ACTIVE": {
                "info": {
                    "description": "neighbor is down, and the local system is awaiting\na conncetion from the remote peer"
                }
            }, 
            "CONNECT": {
                "info": {
                    "description": "neighbor is down, and the session is waiting for\nthe underlying transport session to be established"
                }
            }, 
            "ESTABLISHED": {
                "info": {
                    "description": "neighbor is up - the BGP session with the peer is\nestablished"
                }
            }, 
            "IDLE": {
                "info": {
                    "description": "neighbor is down, and in the Idle state of the\nFSM"
                }
            }, 
            "OPENCONFIRM": {
                "info": {
                    "description": "neighbor is in the process of being established.\nThe local system is awaiting a NOTIFICATION or\nKEEPALIVE message"
                }
            }, 
            "OPENSENT": {
                "info": {
                    "description": "neighbor is in the process of being established.\nThe local system has sent an OPEN message"
                }
            }
        },
        )
        self.session_state._parent = weakref.ref(self)
        self.established_transitions = yang.Counter64(_meta={"mandatory": False},
        )
        self.established_transitions._parent = weakref.ref(self)
        self.last_established = oc_types.Timeticks64(_meta={"mandatory": False},
        )
        self.last_established._parent = weakref.ref(self)
        # leaflist
        self.supported_capabilities = LeafList(Identityref(_meta={"mandatory": False}, base="oc-bgp-types:BGP_CAPABILITY"))
        self.supported_capabilities._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiState_Prefixes_403(BaseBinding):
    """
    Prefix counters for the BGP session
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.received = Uint32(_meta={"mandatory": False},
        )
        self.received._parent = weakref.ref(self)
        self.sent = Uint32(_meta={"mandatory": False},
        )
        self.sent._parent = weakref.ref(self)
        self.installed = Uint32(_meta={"mandatory": False},
        )
        self.installed._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiState(BaseBinding):
    """
    Operational state parameters relating to an individual AFI,
    SAFI for a neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.prefixes = BgpNeighborAfiSafiState_Prefixes_403()
        self.prefixes._parent = weakref.ref(self)
        # list
        # leaf
        self.active = Boolean(_meta={"mandatory": False},
        )
        self.active._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AfiSafi_Config_447(BgpCommonMpAfiSafiConfig):
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
        




class AfiSafi_State_452(BgpNeighborAfiSafiState, BgpCommonMpAfiSafiConfig):
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
        




class GracefulRestart_Config_464(BgpCommonMpAfiSafiGracefulRestartConfig):
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
        




class GracefulRestart_State_469(BgpNeighborAfiSafiGracefulRestartState, BgpCommonMpAfiSafiGracefulRestartConfig):
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
        




class AfiSafi_GracefulRestart_461(BaseBinding):
    """
    Parameters relating to BGP graceful-restart
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_464()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_469()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborAfiSafiList_AfiSafi_430(List, BgpNeighborUseMultiplePaths, BgpCommonMpAllAfiSafiListContents):
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
        self.config = AfiSafi_Config_447()
        self.config._parent = weakref.ref(self)
        self.state = AfiSafi_State_452()
        self.state._parent = weakref.ref(self)
        self.graceful_restart = AfiSafi_GracefulRestart_461()
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





class BgpNeighborAfiSafiList(BaseBinding):
    """
    List of address-families associated with the BGP neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.afi_safi = BgpNeighborAfiSafiList_AfiSafi_430()
        self.afi_safi._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborBase_Config_487(BgpCommonNeighborGroupConfig, BgpNeighborConfig):
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
        




class BgpNeighborBase_State_494(BgpNeighborState, BgpCommonNeighborGroupConfig, BgpNeighborConfig):
    """
    State information relating to the BGP neighbor
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
        




class Timers_Config_506(BgpCommonNeighborGroupTimersConfig):
    """
    Configuration parameters relating to timers used for the
    BGP neighbor
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
        




class Timers_State_512(BgpNeighborTimersState, BgpCommonNeighborGroupTimersConfig):
    """
    State information relating to the timers used for the BGP
    neighbor
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
        




class BgpNeighborBase_Timers_503(BaseBinding):
    """
    Timers related to a BGP neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Timers_Config_506()
        self.config._parent = weakref.ref(self)
        self.state = Timers_State_512()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Transport_Config_525(BgpCommonNeighborGroupTransportConfig):
    """
    Configuration parameters relating to the transport
    session(s) used for the BGP neighbor
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
        




class Transport_State_531(BgpNeighborTransportState, BgpCommonNeighborGroupTransportConfig):
    """
    State information relating to the transport session(s)
    used for the BGP neighbor
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
        




class BgpNeighborBase_Transport_522(BaseBinding):
    """
    Transport session parameters for the BGP neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Transport_Config_525()
        self.config._parent = weakref.ref(self)
        self.state = Transport_State_531()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ErrorHandling_Config_545(BgpCommonNeighborGroupErrorHandlingConfig):
    """
    Configuration parameters enabling or modifying the
    behavior or enhanced error handling mechanisms for the BGP
    neighbor
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
        




class ErrorHandling_State_552(BgpNeighborErrorHandlingState, BgpCommonNeighborGroupErrorHandlingConfig):
    """
    State information relating to enhanced error handling
    mechanisms for the BGP neighbor
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
        




class BgpNeighborBase_ErrorHandling_541(BaseBinding):
    """
    Error handling parameters used for the BGP neighbor or
    group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = ErrorHandling_Config_545()
        self.config._parent = weakref.ref(self)
        self.state = ErrorHandling_State_552()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GracefulRestart_Config_565(BgpCommonGracefulRestartConfig):
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
        




class GracefulRestart_State_570(BgpNeighborGracefulRestartState, BgpCommonGracefulRestartConfig):
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
        




class BgpNeighborBase_GracefulRestart_562(BaseBinding):
    """
    Parameters relating the graceful restart mechanism for BGP
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = GracefulRestart_Config_565()
        self.config._parent = weakref.ref(self)
        self.state = GracefulRestart_State_570()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborBase_AfiSafis_587(BgpNeighborAfiSafiList):
    """
    Per-address-family configuration parameters associated with
    the neighbor
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
        




class BgpNeighborBase(oc_rpol.ApplyPolicyGroup, BgpNeighborUseMultiplePaths, BgpCommonStructureNeighborGroupAddPaths, BgpCommonStructureNeighborGroupAsPathOptions, BgpCommonStructureNeighborGroupRouteReflector, BgpCommonStructureNeighborGroupEbgpMultihop, BgpCommonStructureNeighborGroupLoggingOptions):
    """
    Parameters related to a BGP neighbor
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpNeighborBase_Config_487()
        self.config._parent = weakref.ref(self)
        self.state = BgpNeighborBase_State_494()
        self.state._parent = weakref.ref(self)
        self.timers = BgpNeighborBase_Timers_503()
        self.timers._parent = weakref.ref(self)
        self.transport = BgpNeighborBase_Transport_522()
        self.transport._parent = weakref.ref(self)
        self.error_handling = BgpNeighborBase_ErrorHandling_541()
        self.error_handling._parent = weakref.ref(self)
        self.graceful_restart = BgpNeighborBase_GracefulRestart_562()
        self.graceful_restart._parent = weakref.ref(self)
        self.afi_safis = BgpNeighborBase_AfiSafis_587()
        self.afi_safis._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpNeighborList_Neighbor_599(List, BgpNeighborBase):
    """
    List of BGP neighbors configured on the local system,
    uniquely identified by peer IPv[46] address
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.neighbor_address = Leafref(_meta={"mandatory": False},
            path="../config/neighbor-address",
        )
        self.neighbor_address._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "neighbor_address"





class BgpNeighborList(BaseBinding):
    """
    The list of BGP neighbors
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.neighbor = BgpNeighborList_Neighbor_599()
        self.neighbor._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
