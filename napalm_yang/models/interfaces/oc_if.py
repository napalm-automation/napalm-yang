"""
Model for managing network interfaces and subinterfaces.  This
module also defines convenience types / groupings for other
models to create references to interfaces:

 base-interface-ref (type) -  reference to a base interface
 interface-ref (grouping) -  container for reference to a
   interface + subinterface
 interface-ref-state (grouping) - container for read-only
   (opstate) reference to interface + subinterface

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7223 with an alternate structure
(particularly for operational state data) and and with
additional configuration items.
"""
from builtins import super

from napalm_yang import *



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import ietf_if

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()
openconfig_extensions.openconfig_version = "1.1.0"

__namespace__ = "http://openconfig.net/yang/interfaces"
__yang_version__ = "1"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-12-22": {
        "revision": "2016-12-22"
    }
}



# features


# typedef

class InterfaceId(BaseTypeDef):
    """
    User-defined identifier for an interface, generally used to
    name a interface reference.  The id can be arbitrary but a
    useful convention is to use a combination of base interface
    name and subinterface index.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.interface_id = String()


class BaseInterfaceRef(BaseTypeDef):
    """
    Reusable type for by-name reference to a base interface.
    This type may be used in cases where ability to reference
    a subinterface is not required.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.base_interface_ref = Leafref(path="/oc-if:interfaces/oc-if:interface/oc-if:name", )



# Identities

# Classes to support containers and lists



class InterfaceRefCommon(BaseBinding):
    """
    Reference leafrefs to interface / subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.interface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface/oc-if:name")
        self.subinterface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index")
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRefStateContainer_State_103(InterfaceRefCommon):
    """
    Operational state for interface-ref
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class InterfaceRefStateContainer(BaseBinding):
    """
    Reusable opstate w/container for a reference to an
    interface or subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.state = InterfaceRefStateContainer_State_103()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRef_Config_121(InterfaceRefCommon):
    """
    Configured reference to interface / subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRef_InterfaceRef_117(InterfaceRefStateContainer):
    """
    Reference to an interface or subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = InterfaceRef_Config_121()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRef(BaseBinding):
    """
    Reusable definition for a reference to an interface or
    subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.interface_ref = InterfaceRef_InterfaceRef_117()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRefState_InterfaceRef_137(InterfaceRefStateContainer):
    """
    Reference to an interface or subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRefState(BaseBinding):
    """
    Reusable opstate w/container for a reference to an
    interface or subinterface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.interface_ref = InterfaceRefState_InterfaceRef_137()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCommonConfig(BaseBinding):
    """
    Configuration data data nodes common to physical interfaces
    and subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysConfig(InterfaceCommonConfig):
    """
    Configuration data for physical interfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.type = Identityref(_meta={"mandatory": True}, base="ietf-if:interface-type")
        self.mtu = Uint16(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysHoldtimeConfig(BaseBinding):
    """
    Configuration data for interface hold-time settings --
    applies to physical interfaces.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.down = Uint32(_meta={"mandatory": False}, )
        self.up = Uint32(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysHoldtimeState(BaseBinding):
    """
    Operational state data for interface hold-time.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class HoldTime_Config_332(InterfacePhysHoldtimeConfig):
    """
    Configuration data for interface hold-time settings.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class HoldTime_State_339(InterfacePhysHoldtimeState, InterfacePhysHoldtimeConfig):
    """
    Operational state data for interface hold-time.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class InterfacePhysHoldtimeTop_HoldTime_327(BaseBinding):
    """
    Top-level container for hold-time settings to enable
    dampening advertisements of interface transitions.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = HoldTime_Config_332()
        self.state = HoldTime_State_339()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysHoldtimeTop(BaseBinding):
    """
    Top-level grouping for setting link transition
    dampening on physical and other types of interfaces.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.hold_time = InterfacePhysHoldtimeTop_HoldTime_327()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCommonState(BaseBinding):
    """
    Operational state data (in addition to intended configuration)
    at the global level for this interface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.ifindex = Uint32(_meta={"mandatory": False}, )
        self.admin_status = Enumeration(_meta={"mandatory": True}, enum={
            "DOWN": {
                "info": {
                    "description": "Not ready to pass packets and not in some test mode."
                }
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode."
                }
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }
            }
        })
        self.last_change = yang.Timeticks(_meta={"mandatory": False}, )
        self.oper_status = Enumeration(_meta={"mandatory": True}, enum={
            "DORMANT": {
                "info": {
                    "description": "Waiting for some external event."
                }, 
                "value": "5"
            }, 
            "DOWN": {
                "info": {
                    "description": "The interface does not pass any packets."
                }, 
                "value": "2"
            }, 
            "LOWER_LAYER_DOWN": {
                "info": {
                    "description": "Down due to state of lower-layer interface(s)."
                }, 
                "value": "7"
            }, 
            "NOT_PRESENT": {
                "info": {
                    "description": "Some component (typically hardware) is missing."
                }, 
                "value": "6"
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode.  No operational packets can\nbe passed."
                }, 
                "value": "3"
            }, 
            "UNKNOWN": {
                "info": {
                    "description": "Status cannot be determined for some reason."
                }, 
                "value": "4"
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }, 
                "value": "1"
            }
        })
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCountersState_Counters_475(BaseBinding):
    """
    A collection of interface-related statistics objects.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.out_octets = yang.Counter64(_meta={"mandatory": False}, )
        self.in_errors = yang.Counter64(_meta={"mandatory": False}, )
        self.in_discards = yang.Counter64(_meta={"mandatory": False}, )
        self.out_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_errors = yang.Counter64(_meta={"mandatory": False}, )
        self.out_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.last_clear = yang.DateAndTime(_meta={"mandatory": False}, )
        self.in_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_discards = yang.Counter64(_meta={"mandatory": False}, )
        self.in_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_unknown_protos = yang.Counter32(_meta={"mandatory": False}, )
        self.in_octets = yang.Counter64(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCountersState(BaseBinding):
    """
    Operational state representing interface counters
    and statistics.  Some of these are adapted from RFC 7223
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.counters = InterfaceCountersState_Counters_475()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedConfig(BaseBinding):
    """
    Configuration data for unnumbered subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedState(BaseBinding):
    """
    Operational state data unnumbered subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Unnumbered_Config_779(SubUnnumberedConfig):
    """
    Configuration data for unnumbered interface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Unnumbered_State_786(SubUnnumberedState, SubUnnumberedConfig):
    """
    Operational state data for unnumbered interfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class SubUnnumberedTop_Unnumbered_773(InterfaceRef):
    """
    Top-level container for setting unnumbered interfaces.
    Includes reference the interface that provides the
    address information
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = Unnumbered_Config_779()
        self.state = Unnumbered_State_786()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedTop(BaseBinding):
    """
    Top-level grouping unnumbered subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.unnumbered = SubUnnumberedTop_Unnumbered_773()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesConfig(InterfaceCommonConfig):
    """
    Configuration data for subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.index = Uint32(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesState(InterfaceCountersState, InterfaceCommonState):
    """
    Operational state data for subinterfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Subinterface_Config_853(SubinterfacesConfig):
    """
    Configurable items at the subinterface level
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Subinterface_State_860(SubinterfacesState, SubinterfacesConfig):
    """
    Operational state data for logical interfaces
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Subinterfaces_Subinterface_837(List, BaseBinding):
    """
    The list of subinterfaces (logical interfaces) associated
    with a physical interface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = Subinterface_Config_853()
        self.state = Subinterface_State_860()
        # list
        # leaf
        self.index = Leafref(_meta={"mandatory": False}, path="../config/index")
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "index"





class SubinterfacesTop_Subinterfaces_832(BaseBinding):
    """
    Enclosing container for the list of subinterfaces associated
    with a physical interface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        self.subinterface = Subinterfaces_Subinterface_837()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesTop(BaseBinding):
    """
    Subinterface data for logical interfaces associated with a
    given interface
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.subinterfaces = SubinterfacesTop_Subinterfaces_832()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Interface_Config_905(InterfacePhysConfig):
    """
    Configurable items at the global, physical interface
    level
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Interface_State_913(InterfaceCountersState, InterfaceCommonState, InterfacePhysConfig):
    """
    Operational state data at the global interface level
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Interfaces_Interface_884(List, SubinterfacesTop, InterfacePhysHoldtimeTop):
    """
    The list of named interfaces on the device.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = Interface_Config_905()
        self.state = Interface_State_913()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False}, path="../config/name")
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class InterfacesTop_Interfaces_878(BaseBinding):
    """
    Top level container for interfaces, including configuration
    and state data.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        self.interface = Interfaces_Interface_884()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacesTop(BaseBinding):
    """
    Top-level grouping for interface configuration and
    operational state data
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.interfaces = InterfacesTop_Interfaces_878()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
class Interfaces(InterfacesTop):
    pass


# Top-containers{}
