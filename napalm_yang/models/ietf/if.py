"""
This module contains a collection of YANG definitions for
managing network interfaces.
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http://trustee.ietf.org/license-info).
This version of this YANG module is part of RFC 7223; see
the RFC itself for full legal notices.
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports
from napalm_yang import yang

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()


__namespace__ = "urn:ietf:params:xml:ns:yang:ietf-interfaces"
__contact__ = "WG Web:   <http://tools.ietf.org/wg/netmod/>\nWG List:  <mailto:netmod@ietf.org>\nWG Chair: Thomas Nadeau\n          <mailto:tnadeau@lucidvision.com>\nWG Chair: Juergen Schoenwaelder\n          <mailto:j.schoenwaelder@jacobs-university.de>\nEditor:   Martin Bjorklund\n          <mailto:mbj@tail-f.com>"
__organization__ = "IETF NETMOD (NETCONF Data Modeling Language) Working Group"
__revision__ = {
    "2014-05-08": {
        "revision": "2014-05-08"
    }
}



# typedef

class InterfaceRef(yang_base.BaseBinding):
    """
    This type is used by data models that need to reference
    configured interfaces.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.interface_ref = yang.Leafref(path="/if:interfaces/if:interface/if:name", )


class InterfaceStateRef(yang_base.BaseBinding):
    """
    This type is used by data models that need to reference
    the operationally present interfaces.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.interface_state_ref = yang.Leafref(path="/if:interfaces-state/if:interface/if:name", )



# Identities
InterfaceType = yang.Identity(
    base="None",
    value="interface-type",
    description="""Base identity from which specific interface types are
derived."""
    )


# Classes to support containers and lists



class Interfaces_Interface_92(yang.List, yang_base.BaseBinding):
    """
    The list of configured interfaces on the device.
    The operational state of an interface is available in the
    /interfaces-state/interface list.  If the configuration of a
    system-controlled interface cannot be used by the system
    (e.g., the interface hardware present does not match the
    interface type), then the configuration is not applied to
    the system-controlled interface shown in the
    /interfaces-state/interface list.  If the configuration
    of a user-controlled interface cannot be used by the system,
    the configured interface is not instantiated in the
    /interfaces-state/interface list.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.type = Identityref(_meta={"mandatory": True}, base="interface-type")
        self.link_up_down_trap_enable = Enumeration(_meta={"mandatory": False}, enum={
            "disabled": {
                "value": "2"
            }, 
            "enabled": {
                "value": "1"
            }
        })
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class IetfInterfaces_Interfaces_89(yang_base.BaseBinding):
    """
    Interface configuration parameters.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        self.interface = Interfaces_Interface_92()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Interface_Statistics_392(yang_base.BaseBinding):
    """
    A collection of interface-related statistics objects.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.out_octets = yang.Counter64(_meta={"mandatory": False}, )
        self.in_errors = yang.Counter32(_meta={"mandatory": False}, )
        self.discontinuity_time = yang.DateAndTime(_meta={"mandatory": True}, )
        self.in_discards = yang.Counter32(_meta={"mandatory": False}, )
        self.out_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_errors = yang.Counter32(_meta={"mandatory": False}, )
        self.out_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_discards = yang.Counter32(_meta={"mandatory": False}, )
        self.in_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_unknown_protos = yang.Counter32(_meta={"mandatory": False}, )
        self.in_octets = yang.Counter64(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfacesState_Interface_226(yang.List, yang_base.BaseBinding):
    """
    The list of interfaces on the device.
    System-controlled interfaces created by the system are
    always present in this list, whether they are configured or
    not.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.statistics = Interface_Statistics_392()
        # list
        # leaf
        self.name = String(_meta={"mandatory": False}, )
        self.speed = yang.Gauge64(_meta={"mandatory": False}, )
        self.phys_address = yang.PhysAddress(_meta={"mandatory": False}, )
        self.admin_status = Enumeration(_meta={"mandatory": True}, enum={
            "down": {
                "info": {
                    "description": "Not ready to pass packets and not in some test mode."
                }, 
                "value": "2"
            }, 
            "testing": {
                "info": {
                    "description": "In some test mode."
                }, 
                "value": "3"
            }, 
            "up": {
                "info": {
                    "description": "Ready to pass packets."
                }, 
                "value": "1"
            }
        })
        self.type = Identityref(_meta={"mandatory": True}, base="interface-type")
        self.last_change = yang.DateAndTime(_meta={"mandatory": False}, )
        self.oper_status = Enumeration(_meta={"mandatory": True}, enum={
            "dormant": {
                "info": {
                    "description": "Waiting for some external event."
                }, 
                "value": "5"
            }, 
            "down": {
                "info": {
                    "description": "The interface does not pass any packets."
                }, 
                "value": "2"
            }, 
            "lower-layer-down": {
                "info": {
                    "description": "Down due to state of lower-layer interface(s)."
                }, 
                "value": "7"
            }, 
            "not-present": {
                "info": {
                    "description": "Some component (typically hardware) is missing."
                }, 
                "value": "6"
            }, 
            "testing": {
                "info": {
                    "description": "In some test mode.  No operational packets can\nbe passed."
                }, 
                "value": "3"
            }, 
            "unknown": {
                "info": {
                    "description": "Status cannot be determined for some reason."
                }, 
                "value": "4"
            }, 
            "up": {
                "info": {
                    "description": "Ready to pass packets."
                }, 
                "value": "1"
            }
        })
        self.if_index = Int32(_meta={"mandatory": True}, range="1..2147483647")
        # leaflist
        self.lower_layer_if = yang.LeafList(InterfaceStateRef(_meta={"mandatory": False}, ))
        self.higher_layer_if = yang.LeafList(InterfaceStateRef(_meta={"mandatory": False}, ))
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class IetfInterfaces_InterfacesState_222(yang_base.BaseBinding):
    """
    Data nodes for the operational state of interfaces.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        self.interface = InterfacesState_Interface_226()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        



# Top-uses
# Top-containers
class C(O):
    pass
{
    "feature": {
        "arbitrary-names": {
            "info": {
                "description": "This feature indicates that the device allows user-controlled\ninterfaces to be named arbitrarily."
            }
        }, 
        "if-mib": {
            "info": {
                "description": "This feature indicates that the device implements\nthe IF-MIB."
            }
        }, 
        "pre-provisioning": {
            "info": {
                "description": "This feature indicates that the device supports\npre-provisioning of interface configuration, i.e., it is\npossible to configure an interface whose physical interface\nhardware is not present on the device."
            }
        }
    }
}