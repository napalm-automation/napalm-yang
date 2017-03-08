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
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_if = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import ietf_if

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.1.0")



__namespace__ = "http://openconfig.net/yang/interfaces"
__yang_version__ = "1"
__prefix__ = "oc-if"
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

class BaseInterfaceRef(Leafref):
    """
    Reusable type for by-name reference to a base interface.
    This type may be used in cases where ability to reference
    a subinterface is not required.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, path = "/oc-if:interfaces/oc-if:interface/oc-if:name", ):

        super().__init__(_meta=_meta, path = path, )

class InterfaceId(String):
    """
    User-defined identifier for an interface, generally used to
    name a interface reference.  The id can be arbitrary but a
    useful convention is to use a combination of base interface
    name and subinterface index.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, ):

        super().__init__(_meta=_meta, )


# Identities

# Classes to support containers and lists



class InterfaceRefCommon(BaseBinding):
    """
    Reference leafrefs to interface / subinterface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.interface = Leafref(_meta={"mandatory": False},
            path="/oc-if:interfaces/oc-if:interface/oc-if:name",
        )
        self.interface._parent = weakref.ref(self)
        self.subinterface = Leafref(_meta={"mandatory": False},
            path="/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index",
        )
        self.subinterface._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRefStateContainer_State_103(InterfaceRefCommon):
    """
    Operational state for interface-ref
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
        




class InterfaceRefStateContainer(BaseBinding):
    """
    Reusable opstate w/container for a reference to an
    interface or subinterface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.state = InterfaceRefStateContainer_State_103()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRef_Config_121(InterfaceRefCommon):
    """
    Configured reference to interface / subinterface
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
        




class InterfaceRef_InterfaceRef_117(InterfaceRefStateContainer):
    """
    Reference to an interface or subinterface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = InterfaceRef_Config_121()
        self.config._parent = weakref.ref(self)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.interface_ref = InterfaceRef_InterfaceRef_117()
        self.interface_ref._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceRefState_InterfaceRef_137(InterfaceRefStateContainer):
    """
    Reference to an interface or subinterface
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
        




class InterfaceRefState(BaseBinding):
    """
    Reusable opstate w/container for a reference to an
    interface or subinterface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.interface_ref = InterfaceRefState_InterfaceRef_137()
        self.interface_ref._parent = weakref.ref(self)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.enabled._parent = weakref.ref(self)
        self.description = String(_meta={"mandatory": False},
        )
        self.description._parent = weakref.ref(self)
        self.name = String(_meta={"mandatory": False},
        )
        self.name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysConfig(InterfaceCommonConfig):
    """
    Configuration data for physical interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.type_ = Identityref(_meta={"mandatory": True},
            base=ietf_if.InterfaceType,
        )
        self.type_._parent = weakref.ref(self)
        self.mtu = Uint16(_meta={"mandatory": False},
        )
        self.mtu._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysHoldtimeConfig(BaseBinding):
    """
    Configuration data for interface hold-time settings --
    applies to physical interfaces.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.down = Uint32(_meta={"mandatory": False},
        )
        self.down._parent = weakref.ref(self)
        self.up = Uint32(_meta={"mandatory": False},
        )
        self.up._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacePhysHoldtimeState(BaseBinding):
    """
    Operational state data for interface hold-time.
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
        




class HoldTime_Config_332(InterfacePhysHoldtimeConfig):
    """
    Configuration data for interface hold-time settings.
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
        




class HoldTime_State_339(InterfacePhysHoldtimeState, InterfacePhysHoldtimeConfig):
    """
    Operational state data for interface hold-time.
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
        




class InterfacePhysHoldtimeTop_HoldTime_327(BaseBinding):
    """
    Top-level container for hold-time settings to enable
    dampening advertisements of interface transitions.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = HoldTime_Config_332()
        self.config._parent = weakref.ref(self)
        self.state = HoldTime_State_339()
        self.state._parent = weakref.ref(self)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.hold_time = InterfacePhysHoldtimeTop_HoldTime_327()
        self.hold_time._parent = weakref.ref(self)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ifindex = Uint32(_meta={"mandatory": False},
        )
        self.ifindex._parent = weakref.ref(self)
        self.admin_status = Enumeration(_meta={"mandatory": True},
            enum={
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
        },
        )
        self.admin_status._parent = weakref.ref(self)
        self.last_change = yang.Timeticks(_meta={"mandatory": False},
        )
        self.last_change._parent = weakref.ref(self)
        self.oper_status = Enumeration(_meta={"mandatory": True},
            enum={
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
        },
        )
        self.oper_status._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCountersState_Counters_475(BaseBinding):
    """
    A collection of interface-related statistics objects.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.out_octets = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_octets._parent = weakref.ref(self)
        self.in_errors = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_errors._parent = weakref.ref(self)
        self.in_discards = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_discards._parent = weakref.ref(self)
        self.out_unicast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_unicast_pkts._parent = weakref.ref(self)
        self.out_errors = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_errors._parent = weakref.ref(self)
        self.out_multicast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_multicast_pkts._parent = weakref.ref(self)
        self.in_multicast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_multicast_pkts._parent = weakref.ref(self)
        self.last_clear = yang.DateAndTime(_meta={"mandatory": False},
        )
        self.last_clear._parent = weakref.ref(self)
        self.in_unicast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_unicast_pkts._parent = weakref.ref(self)
        self.out_broadcast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_broadcast_pkts._parent = weakref.ref(self)
        self.out_discards = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_discards._parent = weakref.ref(self)
        self.in_broadcast_pkts = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_broadcast_pkts._parent = weakref.ref(self)
        self.in_unknown_protos = yang.Counter32(_meta={"mandatory": False},
        )
        self.in_unknown_protos._parent = weakref.ref(self)
        self.in_octets = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_octets._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceCountersState(BaseBinding):
    """
    Operational state representing interface counters
    and statistics.  Some of these are adapted from RFC 7223
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.counters = InterfaceCountersState_Counters_475()
        self.counters._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedConfig(BaseBinding):
    """
    Configuration data for unnumbered subinterfaces
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
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedState(BaseBinding):
    """
    Operational state data unnumbered subinterfaces
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
        




class Unnumbered_Config_779(SubUnnumberedConfig):
    """
    Configuration data for unnumbered interface
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
        




class Unnumbered_State_786(SubUnnumberedState, SubUnnumberedConfig):
    """
    Operational state data for unnumbered interfaces
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
        




class SubUnnumberedTop_Unnumbered_773(oc_if.InterfaceRef):
    """
    Top-level container for setting unnumbered interfaces.
    Includes reference the interface that provides the
    address information
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Unnumbered_Config_779()
        self.config._parent = weakref.ref(self)
        self.state = Unnumbered_State_786()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubUnnumberedTop(BaseBinding):
    """
    Top-level grouping unnumbered subinterfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.unnumbered = SubUnnumberedTop_Unnumbered_773()
        self.unnumbered._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesConfig(InterfaceCommonConfig):
    """
    Configuration data for subinterfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.index = Uint32(_meta={"mandatory": False},
        )
        self.index._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesState(InterfaceCountersState, InterfaceCommonState):
    """
    Operational state data for subinterfaces
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
        




class Subinterface_Config_853(SubinterfacesConfig):
    """
    Configurable items at the subinterface level
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
        




class Subinterface_State_860(SubinterfacesState, SubinterfacesConfig):
    """
    Operational state data for logical interfaces
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
        




class Subinterfaces_Subinterface_837(List, BaseBinding):
    """
    The list of subinterfaces (logical interfaces) associated
    with a physical interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Subinterface_Config_853()
        self.config._parent = weakref.ref(self)
        self.state = Subinterface_State_860()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.index = Leafref(_meta={"mandatory": False},
            path="../config/index",
        )
        self.index._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "index"





class SubinterfacesTop_Subinterfaces_832(BaseBinding):
    """
    Enclosing container for the list of subinterfaces associated
    with a physical interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.subinterface = Subinterfaces_Subinterface_837()
        self.subinterface._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SubinterfacesTop(BaseBinding):
    """
    Subinterface data for logical interfaces associated with a
    given interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.subinterfaces = SubinterfacesTop_Subinterfaces_832()
        self.subinterfaces._parent = weakref.ref(self)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
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
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Interface_Config_905()
        self.config._parent = weakref.ref(self)
        self.state = Interface_State_913()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../config/name",
        )
        self.name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class InterfacesTop_Interfaces_878(BaseBinding):
    """
    Top level container for interfaces, including configuration
    and state data.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.interface = Interfaces_Interface_884()
        self.interface._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacesTop(BaseBinding):
    """
    Top-level grouping for interface configuration and
    operational state data
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.interfaces = InterfacesTop_Interfaces_878()
        self.interfaces._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
interfaces = model_factory(InterfacesTop)


# Top-containers


# augments