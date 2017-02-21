"""
This module defines configuration and operational state
data for network access control lists (i.e., filters, rules,
etc.).  ACLs are organized into ACL sets, with each set
containing one or more ACL entries.  ACL sets are identified
by a unique name, while each entry within a set is assigned
a sequence-id that determines the order in which the ACL
rules are applied to a packet.

The model allows individual ACL rules to combine match criteria
from various fields in the packet, along with an action that
defines how matching packets should be handled.  Note that some
device implementations may require separate entries for match
criteria that cross protocol layers, e.g., MAC layer and IP
layer matches.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_acl = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import oc_if
from napalm_yang import oc_match

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.2.0")



__namespace__ = "http://openconfig.net/yang/acl"
__yang_version__ = "1"
__prefix__ = "oc-acl"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-01-22": {
        "revision": "2016-01-22"
    }, 
    "2016-08-08": {
        "revision": "2016-08-08"
    }
}



# extensions

# features


# typedef


# Identities
Forwarding_Action = Identity(
    base=None,
    value="FORWARDING_ACTION",
    description="""Base identity for actions in the forwarding category"""
    )

Accept = Identity(
    base=Forwarding_Action,
    value="ACCEPT",
    description="""Accept the packet"""
    )

Drop = Identity(
    base=Forwarding_Action,
    value="DROP",
    description="""Drop packet without sending any ICMP error message"""
    )

Reject = Identity(
    base=Forwarding_Action,
    value="REJECT",
    description="""Drop the packet and send an ICMP error message to the source"""
    )

Log_Action = Identity(
    base=None,
    value="LOG_ACTION",
    description="""Base identity for defining the destination for logging
actions"""
    )

Log_Syslog = Identity(
    base=Log_Action,
    value="LOG_SYSLOG",
    description="""Log the packet in Syslog"""
    )

Log_None = Identity(
    base=Log_Action,
    value="LOG_NONE",
    description="""No logging"""
    )

Acl_Counter_Capability = Identity(
    base=None,
    value="ACL_COUNTER_CAPABILITY",
    description="""Base identity for system to indicate how it is able to report
counters"""
    )

Interface_Only = Identity(
    base=Acl_Counter_Capability,
    value="INTERFACE_ONLY",
    description="""ACL counters are available and reported only per interface"""
    )

Aggregate_Only = Identity(
    base=Acl_Counter_Capability,
    value="AGGREGATE_ONLY",
    description="""ACL counters are aggregated over all interfaces, and reported
only per ACL entry"""
    )

Interface_Aggregate = Identity(
    base=Acl_Counter_Capability,
    value="INTERFACE_AGGREGATE",
    description="""ACL counters are reported per interface, and also aggregated
and reported per ACL entry."""
    )


# Classes to support containers and lists



class InputInterfaceConfig(BaseBinding):
    """
    Config of interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InputInterfaceState(BaseBinding):
    """
    State information of interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InputInterface_Config_144(InputInterfaceConfig):
    """
    Config data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InputInterface_State_150(InputInterfaceState, InputInterfaceConfig):
    """
    State information
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class InputInterfaceTop_InputInterface_140(oc_if.InterfaceRef):
    """
    Input interface container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = InputInterface_Config_144()
        self.state = InputInterface_State_150()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InputInterfaceTop(BaseBinding):
    """
    Input interface top level container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.input_interface = InputInterfaceTop_InputInterface_140()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ActionConfig(BaseBinding):
    """
    Config of action type
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.forwarding_action = Identityref(_meta={"mandatory": True},
            base=Forwarding_Action,
        )
        self.log_action = Identityref(_meta={"mandatory": False},
            base=Log_Action,
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ActionState(BaseBinding):
    """
    State information of action type
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Actions_Config_208(ActionConfig):
    """
    Config data for ACL actions
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Actions_State_214(ActionState, ActionConfig):
    """
    State information for ACL actions
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class ActionTop_Actions_203(BaseBinding):
    """
    Enclosing container for list of ACL actions associated
    with an entry
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Actions_Config_208()
        self.state = Actions_State_214()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ActionTop(BaseBinding):
    """
    ACL action type top level container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.actions = ActionTop_Actions_203()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclCountersState(BaseBinding):
    """
    Common grouping for ACL counters
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.matched_octets = yang.Counter64(_meta={"mandatory": False},
        )
        self.matched_packets = yang.Counter64(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AccessListEntriesConfig(BaseBinding):
    """
    Access List Entries (ACE) config.
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.sequence_id = Uint32(_meta={"mandatory": False},
        )
        self.description = String(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AccessListEntriesState(AclCountersState):
    """
    Access List Entries state.
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclEntry_Config_321(AccessListEntriesConfig):
    """
    Access list entries config
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclEntry_State_327(AccessListEntriesState, AccessListEntriesConfig):
    """
    State information for ACL entries
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class AclEntries_AclEntry_308(List, ActionTop, InputInterfaceTop, oc_match.TransportFieldsTop, oc_match.IpProtocolFieldsTop, oc_match.EthernetHeaderTop):
    """
    List of ACL entries comprising an ACL set
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = AclEntry_Config_321()
        self.state = AclEntry_State_327()
        # list
        # leaf
        self.sequence_id = Leafref(_meta={"mandatory": False},
            path="../config/sequence-id",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "sequence_id"





class AccessListEntriesTop_AclEntries_304(BaseBinding):
    """
    Access list entries container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.acl_entry = AclEntries_AclEntry_308()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AccessListEntriesTop(BaseBinding):
    """
    Access list entries to level container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.acl_entries = AccessListEntriesTop_AclEntries_304()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclSetConfig(BaseBinding):
    """
    Access Control List config
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.description = String(_meta={"mandatory": False},
        )
        self.name = String(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclSetState(BaseBinding):
    """
    Access Control List state
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclSet_Config_390(AclSetConfig):
    """
    Access list config
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclSet_State_396(AclSetState, AclSetConfig):
    """
    Access list state information
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class AclSets_AclSet_376(List, AccessListEntriesTop):
    """
    List of ACL sets, each comprising of a list of ACL
    entries
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = AclSet_Config_390()
        self.state = AclSet_State_396()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class AclSetTop_AclSets_372(BaseBinding):
    """
    Access list entries variables enclosing container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.acl_set = AclSets_AclSet_376()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclSetTop(BaseBinding):
    """
    Access list entries variables top level container
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.acl_sets = AclSetTop_AclSets_372()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceAclEntriesConfig(BaseBinding):
    """
    Configuration data for per-interface ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceAclEntriesState(AclCountersState):
    """
    Operational state data for per-interface ACL entries
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.sequence_id = Leafref(_meta={"mandatory": False},
            path="/acl/acl-sets/acl-set[name=current()/../../../../set-name]/acl-entries/acl-entry/sequence-id",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclEntry_State_458(InterfaceAclEntriesState, InterfaceAclEntriesConfig):
    """
    Operational state data for per-interface ACL entries
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class AclEntries_AclEntry_442(List, BaseBinding):
    """
    List of ACL entries assigned to an interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.state = AclEntry_State_458()
        # list
        # leaf
        self.sequence_id = Leafref(_meta={"mandatory": False},
            path="../state/sequence-id",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "sequence_id"





class InterfaceAclEntriesTop_AclEntries_437(BaseBinding):
    """
    Enclosing container for list of references to ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.acl_entry = AclEntries_AclEntry_442()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class InterfaceAclEntriesTop(BaseBinding):
    """
    Top-level grouping for per-interface ACL entries
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.acl_entries = InterfaceAclEntriesTop_AclEntries_437()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceIngressAclConfig(BaseBinding):
    """
    Configuration data for per-interface ingress ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False},
            path="/acl/acl-sets/acl-set/config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceIngressAclState(BaseBinding):
    """
    Operational state data for the per-interface ingress ACL
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IngressAclSet_Config_512(InterfaceIngressAclConfig):
    """
    Configuration data 
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IngressAclSet_State_519(InterfaceIngressAclState, InterfaceIngressAclConfig):
    """
    Operational state data for interface ingress ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class IngressAclSets_IngressAclSet_499(List, InterfaceAclEntriesTop):
    """
    List of ingress ACLs on the interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = IngressAclSet_Config_512()
        self.state = IngressAclSet_State_519()
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False},
            path="../config/set-name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "set_name"





class InterfaceIngressAclTop_IngressAclSets_494(BaseBinding):
    """
    Enclosing container the list of ingress ACLs on the
    interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.ingress_acl_set = IngressAclSets_IngressAclSet_499()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceIngressAclTop(BaseBinding):
    """
    Top-level grouping for per-interface ingress ACL data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.ingress_acl_sets = InterfaceIngressAclTop_IngressAclSets_494()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceEgressAclConfig(BaseBinding):
    """
    Configuration data for per-interface egress ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False},
            path="/acl/acl-sets/acl-set/config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceEgressAclState(BaseBinding):
    """
    Operational state data for the per-interface egress ACL
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EgressAclSet_Config_575(InterfaceEgressAclConfig):
    """
    Configuration data 
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EgressAclSet_State_582(InterfaceEgressAclState, InterfaceEgressAclConfig):
    """
    Operational state data for interface egress ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class EgressAclSets_EgressAclSet_562(List, InterfaceAclEntriesTop):
    """
    List of egress ACLs on the interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = EgressAclSet_Config_575()
        self.state = EgressAclSet_State_582()
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False},
            path="../config/set-name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "set_name"





class InterfaceEgressAclTop_EgressAclSets_557(BaseBinding):
    """
    Enclosing container the list of egress ACLs on the
    interface
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.egress_acl_set = EgressAclSets_EgressAclSet_562()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class InterfaceEgressAclTop(BaseBinding):
    """
    Top-level grouping for per-interface egress ACL data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.egress_acl_sets = InterfaceEgressAclTop_EgressAclSets_557()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclInterfacesConfig(BaseBinding):
    """
    Configuration data for interface references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.id = oc_if.InterfaceId(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclInterfacesState(BaseBinding):
    """
    Operational state data for interface references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Interface_Config_637(AclInterfacesConfig):
    """
    Configuration for ACL per-interface data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Interface_State_644(AclInterfacesState, AclInterfacesConfig):
    """
    Operational state for ACL per-interface data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class Interfaces_Interface_624(List, InterfaceEgressAclTop, InterfaceIngressAclTop, oc_if.InterfaceRef):
    """
    List of interfaces on which ACLs are set
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Interface_Config_637()
        self.state = Interface_State_644()
        # list
        # leaf
        self.id = Leafref(_meta={"mandatory": False},
            path="../config/id",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "id"





class AclInterfacesTop_Interfaces_619(BaseBinding):
    """
    Enclosing container for the list of interfaces on which
    ACLs are set
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.interface = Interfaces_Interface_624()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclInterfacesTop(BaseBinding):
    """
    Top-level grouping for interface-specific ACL data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.interfaces = AclInterfacesTop_Interfaces_619()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclConfig(BaseBinding):
    """
    Global configuration data for ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclState(BaseBinding):
    """
    Global operational state data for ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.counter_capability = Identityref(_meta={"mandatory": False},
            base=Acl_Counter_Capability,
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Acl_Config_689(AclConfig):
    """
    Global config data for ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Acl_State_696(AclState, AclConfig):
    """
    Global operational state data for ACLs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class AclTop_Acl_684(AclInterfacesTop, AclSetTop):
    """
    Top level enclosing container for ACL model config
    and operational state data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Acl_Config_689()
        self.state = Acl_State_696()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AclTop(BaseBinding):
    """
    Top level grouping for ACL data and structure
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.acl = AclTop_Acl_684()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
acl = AclTop()


# Top-containers


# augments