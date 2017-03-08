"""
This module defines configuration and state variables for VLANs,
in addition to VLAN parameters associated with interfaces
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_vlan = LocalNamespace()



# Imports
from napalm_yang import oc_if
from napalm_yang import oc_lag
from napalm_yang import ift
from napalm_yang import oc_ext
from napalm_yang import oc_vlan_types
from napalm_yang import oc_eth

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.0.2")



__namespace__ = "http://openconfig.net/yang/vlan"
__yang_version__ = "1"
__prefix__ = "oc-vlan"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-05-26": {
        "revision": "2016-05-26"
    }
}



# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class VlanConfig(BaseBinding):
    """
    VLAN configuration container.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.status = Enumeration(_meta={"mandatory": False},
            enum={
            "ACTIVE": {
                "info": {
                    "description": "VLAN is active"
                }
            }, 
            "SUSPENDED": {
                "info": {
                    "description": "VLAN is inactive / suspended"
                }
            }
        },
        )
        self.status._parent = weakref.ref(self)
        self.vlan_id = oc_vlan_types.VlanId(_meta={"mandatory": False},
        )
        self.vlan_id._parent = weakref.ref(self)
        self.name = String(_meta={"mandatory": False},
        )
        self.name._parent = weakref.ref(self)
        self.tpid = Identityref(_meta={"mandatory": False},
            base=oc_vlan_types.Tpid_Types,
        )
        self.tpid._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanState(BaseBinding):
    """
    State variables for VLANs
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
        




class Members_Member_92(List, oc_if.InterfaceRefState):
    """
    List of references to interfaces / subinterfaces
    associated with the VLAN.
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
        self._meta["key"] = ""





class VlanMembersState_Members_88(BaseBinding):
    """
    Enclosing container for list of member interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.member = Members_Member_92()
        self.member._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanMembersState(BaseBinding):
    """
    List of interfaces / subinterfaces belonging to the VLAN.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.members = VlanMembersState_Members_88()
        self.members._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanEthernetConfig(BaseBinding):
    """
    VLAN related configuration that is part of the physical
    Ethernet interface.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.interface_mode = oc_vlan_types.VlanModeType(_meta={"mandatory": False},
        )
        self.interface_mode._parent = weakref.ref(self)
        self.native_vlan = Union(_meta={"mandatory": False},
            type_={
            "oc-vlan-types:qinq-id": {}, 
            "oc-vlan-types:vlan-id": {}
        },
        )
        self.native_vlan._parent = weakref.ref(self)
        self.access_vlan = Union(_meta={"mandatory": False},
            type_={
            "oc-vlan-types:qinq-id": {}, 
            "oc-vlan-types:vlan-id": {}
        },
        )
        self.access_vlan._parent = weakref.ref(self)
        # leaflist
        self.trunk_vlans = LeafList(Union(_meta={"mandatory": False}, type_={
            "oc-vlan-types:qinq-id": {}, 
            "oc-vlan-types:qinq-id-range": {}, 
            "oc-vlan-types:vlan-id": {}, 
            "oc-vlan-types:vlan-range": {}
        }))
        self.trunk_vlans._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class VlanEthernetState(BaseBinding):
    """
    VLAN related operational state that is part of Ethernet
    interface state data
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
        




class SwitchedVlan_Config_184(VlanEthernetConfig):
    """
    Configuration parameters for VLANs
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
        




class SwitchedVlan_State_190(VlanEthernetState, VlanEthernetConfig):
    """
    State variables for VLANs
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
        




class VlanEthernetTop_SwitchedVlan_178(BaseBinding):
    """
    Enclosing container for VLAN interface-specific
    data on Ethernet interfaces.  These are for standard
    L2, switched-style VLANs.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = SwitchedVlan_Config_184()
        self.config._parent = weakref.ref(self)
        self.state = SwitchedVlan_State_190()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanEthernetTop(BaseBinding):
    """
    Top-level grouping for VLAN data associated with an
    Ethernet interface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.switched_vlan = VlanEthernetTop_SwitchedVlan_178()
        self.switched_vlan._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanLogicalConfig(BaseBinding):
    """
    VLAN related configuration that is part of subinterface
    (logical interface) configuration.  These are generally
    L3 VLANs with an id that is local.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.vlan_id = Union(_meta={"mandatory": False},
            type_={
            "oc-vlan-types:qinq-id": {}, 
            "oc-vlan-types:vlan-id": {}
        },
        )
        self.vlan_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanLogicalState(BaseBinding):
    """
    VLAN related operational state that is part of logical
    interface state data
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
        




class Vlan_Config_249(VlanConfig):
    """
    Configuration parameters for VLANs
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
        




class Vlan_State_255(VlanState, VlanConfig):
    """
    State variables for VLANs
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
        




class Vlans_Vlan_237(List, VlanMembersState):
    """
    Configured VLANs keyed by id
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Vlan_Config_249()
        self.config._parent = weakref.ref(self)
        self.state = Vlan_State_255()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.vlan_id = Leafref(_meta={"mandatory": False},
            path="../config/vlan-id",
        )
        self.vlan_id._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "vlan_id"





class VlanTop_Vlans_233(BaseBinding):
    """
    Container for VLAN configuration and state
    variables
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.vlan = Vlans_Vlan_237()
        self.vlan._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanTop(BaseBinding):
    """
    Top-level grouping for VLAN configuration
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.vlans = VlanTop_Vlans_233()
        self.vlans._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Vlan_Config_278(VlanLogicalConfig):
    """
    Configuration parameters for VLANs
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
        




class Vlan_State_284(VlanLogicalState, VlanLogicalConfig):
    """
    State variables for VLANs
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
        




class VlanLogicalTop_Vlan_273(BaseBinding):
    """
    Enclosing container for VLAN interface-specific
    data on subinterfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Vlan_Config_278()
        self.config._parent = weakref.ref(self)
        self.state = Vlan_State_284()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanLogicalTop(BaseBinding):
    """
    Top-level grouping for VLAN data associated with a
    logical interface or subinterface
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.vlan = VlanLogicalTop_Vlan_273()
        self.vlan._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanRoutedConfig(BaseBinding):
    """
    Configuration data for routed vlans (SVI, IRB, etc.)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.vlan = Union(_meta={"mandatory": False},
            type_={
            "string": {}, 
            "uint16": {}
        },
        )
        self.vlan._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanRoutedState(BaseBinding):
    """
    Operational state data for routed vlan interfaces.
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
        




class RoutedVlan_Config_332(VlanRoutedConfig):
    """
    Configuration data for routed vlan interfaces
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
        




class RoutedVlan_State_339(VlanRoutedState, VlanRoutedConfig):
    """
    Operational state data 
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
        




class VlanRoutedTop_RoutedVlan_325(BaseBinding):
    """
    Top-level container for routed vlan interfaces.  These
    logical interfaces are also known as SVI (switched virtual
    interface), IRB (integrated routing and bridging), RVI
    (routed VLAN interface)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = RoutedVlan_Config_332()
        self.config._parent = weakref.ref(self)
        self.state = RoutedVlan_State_339()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class VlanRoutedTop(BaseBinding):
    """
    Top-level grouping for routed vlan logical interfaces
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.routed_vlan = VlanRoutedTop_RoutedVlan_325()
        self.routed_vlan._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
vlan = model_factory(VlanTop)


# Top-containers


# augments
class Augment_0(BaseAugment, VlanLogicalTop):
    """Adds VLAN settings to individual subinterfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        VlanLogicalTop.__init__(self)
        



# Load the augmentation
Augment_0()()

class Augment_1(BaseAugment, VlanRoutedTop):
    """Adds configuration and state for routed VLAN interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface']
        
        self._meta = {'when': u"oc-if:type = 'ift:l3ipvlan'"}

        
        BaseAugment.__init__(self)
        
        VlanRoutedTop.__init__(self)
        



# Load the augmentation
Augment_1()()

class Augment_2(BaseAugment, VlanEthernetTop):
    """Adds VLAN settings to individual Ethernet
interfaces"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-eth:ethernet']
        
        self._meta = {'when': u"oc-if:type = 'ift:ethernetCsmacd'"}

        
        BaseAugment.__init__(self)
        
        VlanEthernetTop.__init__(self)
        



# Load the augmentation
Augment_2()()

class Augment_3(BaseAugment, VlanEthernetTop):
    """Adds VLAN settings to a LAG interface"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-lag:aggregation']
        
        self._meta = {'when': u"oc-if:type = 'ift:ieee8023adLag'"}

        
        BaseAugment.__init__(self)
        
        VlanEthernetTop.__init__(self)
        



# Load the augmentation
Augment_3()()
