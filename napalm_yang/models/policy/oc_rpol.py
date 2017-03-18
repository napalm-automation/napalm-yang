"""
This module describes a YANG model for routing policy
configuration. It is a limited subset of all of the policy
configuration parameters available in the variety of vendor
implementations, but supports widely used constructs for managing
how routes are imported, exported, and modified across different
routing protocols.  This module is intended to be used in
conjunction with routing protocol configuration models (e.g.,
BGP) defined in other modules.

Route policy expression:

Policies are expressed as a set of top-level policy definitions,
each of which consists of a sequence of policy statements. Policy
statements consist of simple condition-action tuples. Conditions
may include mutiple match or comparison operations, and similarly
actions may be multitude of changes to route attributes or a
final disposition of accepting or rejecting the route.

Route policy evaluation:

Policy definitions are referenced in routing protocol
configurations using import and export configuration statements.
The arguments are members of an ordered list of named policy
definitions which comprise a policy chain, and optionally, an
explicit default policy action (i.e., reject or accept).

Evaluation of each policy definition proceeds by evaluating its
corresponding individual policy statements in order.  When a
condition statement in a policy statement is satisfied, the
corresponding action statement is executed.  If the action
statement has either accept-route or reject-route actions, policy
evaluation of the current policy definition stops, and no further
policy definitions in the chain are evaluated.

If the condition is not satisfied, then evaluation proceeds to
the next policy statement.  If none of the policy statement
conditions are satisfied, then evaluation of the current policy
definition stops, and the next policy definition in the chain is
evaluated.  When the end of the policy chain is reached, the
default route disposition action is performed (i.e., reject-route
unless an an alternate default action is specified for the
chain).

Policy 'subroutines' (or nested policies) are supported by
allowing policy statement conditions to reference another policy
definition which applies conditions and actions from the
referenced policy before returning to the calling policy
statement and resuming evaluation.  If the called policy
results in an accept-route (either explicit or by default), then
the subroutine returns an effective true value to the calling
policy.  Similarly, a reject-route action returns false.  If the
subroutine returns true, the calling policy continues to evaluate
the remaining conditions (using a modified route if the
subroutine performed any changes to the route).
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_rpol = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import inet
from napalm_yang import oc_if
from napalm_yang import oc_pol_types
# Imcludes

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.0.1")



__namespace__ = "http://openconfig.net/yang/routing-policy"
__yang_version__ = "1"
__prefix__ = "oc-rpol"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-05-12": {
        "revision": "2016-05-12"
    }
}


class PrefixTop(BaseBinding):
    """
    Top-level grouping for prefixes in a prefix list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.prefixes = PrefixTop_Prefixes_213()
        self.prefixes._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True

# extensions

# features


# typedef

class DefaultPolicyType(Enumeration):
    """
    type used to specify default route disposition in
    a policy chain
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "ACCEPT_ROUTE": {
        "info": {
            "description": "default policy to accept the route"
        }
    }, 
    "REJECT_ROUTE": {
        "info": {
            "description": "default policy to reject the route"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )


# Identities

# Classes to support containers and lists



class PrefixSetConfig(BaseBinding):
    """
    Configuration data for prefix sets used in policy
    definitions.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.prefix_set_name = String(_meta={"mandatory": False},
        )
        self.prefix_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixSetState(BaseBinding):
    """
    Operational state data for prefix sets
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
        




class PrefixSet_Config_148(PrefixSetConfig):
    """
    Configuration data for prefix sets
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
        




class PrefixSet_State_155(PrefixSetState, PrefixSetConfig):
    """
    Operational state data 
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
        




class PrefixSets_PrefixSet_135(List, PrefixTop):
    """
    List of the defined prefix sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = PrefixSet_Config_148()
        self.config._parent = weakref.ref(self)
        self.state = PrefixSet_State_155()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.prefix_set_name = Leafref(_meta={"mandatory": False},
            path="../config/prefix-set-name",
        )
        self.prefix_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "prefix_set_name"





class PrefixSetTop_PrefixSets_131(BaseBinding):
    """
    Enclosing container 
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.prefix_set = PrefixSets_PrefixSet_135()
        self.prefix_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixSetTop(BaseBinding):
    """
    Top-level data definitions for a list of IPv4 or IPv6
    prefixes which are matched as part of a policy
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.prefix_sets = PrefixSetTop_PrefixSets_131()
        self.prefix_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixConfig(BaseBinding):
    """
    Configuration data for a prefix definition
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.masklength_range = String(_meta={"mandatory": False},
            pattern="^([0-9]+\\.\\.[0-9]+)|exact$",
        )
        self.masklength_range._parent = weakref.ref(self)
        self.ip_prefix = inet.IpPrefix(_meta={"mandatory": True},
        )
        self.ip_prefix._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixState(BaseBinding):
    """
    Operational state data for prefix definitions
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
        




class Prefix_Config_239(PrefixConfig):
    """
    Configuration data for prefix definition
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
        




class Prefix_State_246(PrefixState, PrefixConfig):
    """
    Operational state data for prefix definition
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
        




class Prefixes_Prefix_218(List, BaseBinding):
    """
    List of prefixes in the prefix set
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Prefix_Config_239()
        self.config._parent = weakref.ref(self)
        self.state = Prefix_State_246()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.masklength_range = Leafref(_meta={"mandatory": False},
            path="../config/masklength-range",
        )
        self.masklength_range._parent = weakref.ref(self)
        self.ip_prefix = Leafref(_meta={"mandatory": False},
            path="../config/ip-prefix",
        )
        self.ip_prefix._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ip_prefix_masklength_range"





class PrefixTop_Prefixes_213(BaseBinding):
    """
    Enclosing container for the list of prefixes in a policy
    prefix list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.prefix = Prefixes_Prefix_218()
        self.prefix._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class NeighborSetConfig(BaseBinding):
    """
    Configuration data for neighbor set definitions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.neighbor_set_name = String(_meta={"mandatory": False},
        )
        self.neighbor_set_name._parent = weakref.ref(self)
        # leaflist
        self.address = LeafList(inet.IpAddressNoZone(_meta={"mandatory": False}, ))
        self.address._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class NeighborSetState(BaseBinding):
    """
    Operational state data for neighbor set definitions
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
        




class NeighborSet_Config_306(NeighborSetConfig):
    """
    Configuration data for neighbor sets.
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
        




class NeighborSet_State_313(NeighborSetState, NeighborSetConfig):
    """
    Operational state data for neighbor sets.
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
        




class NeighborSets_NeighborSet_293(List, BaseBinding):
    """
    List of defined neighbor sets for use in policies.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = NeighborSet_Config_306()
        self.config._parent = weakref.ref(self)
        self.state = NeighborSet_State_313()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.neighbor_set_name = Leafref(_meta={"mandatory": False},
            path="../config/neighbor-set-name",
        )
        self.neighbor_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "neighbor_set_name"





class NeighborSetTop_NeighborSets_288(BaseBinding):
    """
    Enclosing container for the list of neighbor set
    definitions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.neighbor_set = NeighborSets_NeighborSet_293()
        self.neighbor_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class NeighborSetTop(BaseBinding):
    """
    Top-level data definition for a list of IPv4 or IPv6
    neighbors which can be matched in a routing policy
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.neighbor_sets = NeighborSetTop_NeighborSets_288()
        self.neighbor_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TagSetConfig(BaseBinding):
    """
    Configuration data for tag set definitions.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.tag_set_name = String(_meta={"mandatory": False},
        )
        self.tag_set_name._parent = weakref.ref(self)
        # leaflist
        self.tag_value = LeafList(oc_pol_types.TagType(_meta={"mandatory": False}, ))
        self.tag_value._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class TagSetState(BaseBinding):
    """
    Operational state data for tag set definitions.
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
        




class TagSet_Config_372(TagSetConfig):
    """
    Configuration data for tag sets
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
        




class TagSet_State_379(TagSetState, TagSetConfig):
    """
    Operational state data for tag sets
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
        




class TagSets_TagSet_359(List, BaseBinding):
    """
    List of tag set definitions.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = TagSet_Config_372()
        self.config._parent = weakref.ref(self)
        self.state = TagSet_State_379()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.tag_set_name = Leafref(_meta={"mandatory": False},
            path="../config/tag-set-name",
        )
        self.tag_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "tag_set_name"





class TagSetTop_TagSets_355(BaseBinding):
    """
    Enclosing container for the list of tag sets.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.tag_set = TagSets_TagSet_359()
        self.tag_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TagSetTop(BaseBinding):
    """
    Top-level data definitions for a list of tags which can
    be matched in policies
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.tag_sets = TagSetTop_TagSets_355()
        self.tag_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GenericDefinedSets(TagSetTop, NeighborSetTop, PrefixSetTop):
    """
    Data definitions for pre-defined sets of attributes used in
    policy match conditions.  These sets are generic and can
    be used in matching conditions in different routing
    protocols.
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
        




class MatchSetOptionsGroup(BaseBinding):
    """
    Grouping containing options relating to how a particular set
    should be matched
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.match_set_options = oc_pol_types.MatchSetOptionsType(_meta={"mandatory": False},
        )
        self.match_set_options._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchSetOptionsRestrictedGroup(BaseBinding):
    """
    Grouping for a restricted set of match operation modifiers
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.match_set_options = oc_pol_types.MatchSetOptionsRestrictedType(_meta={"mandatory": False},
        )
        self.match_set_options._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchInterfaceConditionConfig(oc_if.InterfaceRefCommon):
    """
    Configuration data for interface match condition
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
        




class MatchInterfaceConditionState(BaseBinding):
    """
    Operational state data for interface match condition
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
        




class MatchInterface_Config_452(MatchInterfaceConditionConfig):
    """
    Configuration data for interface match conditions
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
        




class MatchInterface_State_459(MatchInterfaceConditionState, MatchInterfaceConditionConfig):
    """
    Operational state data for interface match conditions
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
        




class MatchInterfaceConditionTop_MatchInterface_448(BaseBinding):
    """
    Top-level container for interface match conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchInterface_Config_452()
        self.config._parent = weakref.ref(self)
        self.state = MatchInterface_State_459()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchInterfaceConditionTop(BaseBinding):
    """
    Top-level grouping for the interface match condition
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_interface = MatchInterfaceConditionTop_MatchInterface_448()
        self.match_interface._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixSetConditionConfig(MatchSetOptionsRestrictedGroup):
    """
    Configuration data for prefix-set conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.prefix_set = Leafref(_meta={"mandatory": False},
            path="/routing-policy/defined-sets/prefix-sets/prefix-set/prefix-set-name",
        )
        self.prefix_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixSetConditionState(BaseBinding):
    """
    Operational state data for prefix-set conditions
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
        




class MatchPrefixSet_Config_504(PrefixSetConditionConfig):
    """
    Configuration data for a prefix-set condition
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
        




class MatchPrefixSet_State_511(PrefixSetConditionState, PrefixSetConditionConfig):
    """
    Operational state data for a prefix-set condition
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
        




class PrefixSetConditionTop_MatchPrefixSet_499(BaseBinding):
    """
    Match a referenced prefix-set according to the logic
    defined in the match-set-options leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchPrefixSet_Config_504()
        self.config._parent = weakref.ref(self)
        self.state = MatchPrefixSet_State_511()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PrefixSetConditionTop(BaseBinding):
    """
    Top-level grouping for prefix-set conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_prefix_set = PrefixSetConditionTop_MatchPrefixSet_499()
        self.match_prefix_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class NeighborSetConditionConfig(MatchSetOptionsRestrictedGroup):
    """
    Configuration data for neighbor-set conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.neighbor_set = Leafref(_meta={"mandatory": False},
            path="/routing-policy/defined-sets/neighbor-sets/neighbor-set/neighbor-set-name",
        )
        self.neighbor_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class NeighborSetConditionState(BaseBinding):
    """
    Operational state data for neighbor-set conditions
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
        




class MatchNeighborSet_Config_556(NeighborSetConditionConfig):
    """
    Configuration data 
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
        




class MatchNeighborSet_State_563(NeighborSetConditionState, NeighborSetConditionConfig):
    """
    Operational state data 
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
        




class NeighborSetConditionTop_MatchNeighborSet_551(BaseBinding):
    """
    Match a referenced neighbor set according to the logic
    defined in the match-set-options-leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchNeighborSet_Config_556()
        self.config._parent = weakref.ref(self)
        self.state = MatchNeighborSet_State_563()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class NeighborSetConditionTop(BaseBinding):
    """
    Top-level grouping for neighbor-set conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_neighbor_set = NeighborSetConditionTop_MatchNeighborSet_551()
        self.match_neighbor_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TagSetConditionConfig(MatchSetOptionsRestrictedGroup):
    """
    Configuration data for tag-set condition statements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.tag_set = Leafref(_meta={"mandatory": False},
            path="/routing-policy/defined-sets/tag-sets/tag-set/tag-set-name",
        )
        self.tag_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TagSetConditionState(BaseBinding):
    """
    Operational state data for tag-set condition statements
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
        




class MatchTagSet_Config_607(TagSetConditionConfig):
    """
    Configuration data for tag-set conditions
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
        




class MatchTagSet_State_614(TagSetConditionState, TagSetConditionConfig):
    """
    Operational state data tag-set conditions
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
        




class TagSetConditionTop_MatchTagSet_602(BaseBinding):
    """
    Match a referenced tag set according to the logic defined
    in the match-options-set leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchTagSet_Config_607()
        self.config._parent = weakref.ref(self)
        self.state = MatchTagSet_State_614()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TagSetConditionTop(BaseBinding):
    """
    Top-level grouping for tag-set conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_tag_set = TagSetConditionTop_MatchTagSet_602()
        self.match_tag_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GenericConditions(TagSetConditionTop, NeighborSetConditionTop, PrefixSetConditionTop, MatchInterfaceConditionTop):
    """
    Condition statement definitions for checking
    membership in a generic defined set
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
        




class IgpGenericConditions(BaseBinding):
    """
    grouping for IGP policy conditions
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
        




class IgpConditions_IgpConditions_647(IgpGenericConditions):
    """
    Policy conditions for IGP attributes
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
        




class IgpConditions(BaseBinding):
    """
    grouping for IGP-specific policy conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.igp_conditions = IgpConditions_IgpConditions_647()
        self.igp_conditions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class GenericActions(BaseBinding):
    """
    Definitions for common set of policy action statements that
    manage the disposition or control flow of the policy
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
        




class IgpActionsConfig(BaseBinding):
    """
    Configuration data for IGP policy actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.set_tag = oc_pol_types.TagType(_meta={"mandatory": False},
        )
        self.set_tag._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IgpActionsState(BaseBinding):
    """
    Operational state data for IGP policy actions 
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
        




class IgpActions_Config_702(IgpActionsConfig):
    """
    Configuration data 
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
        




class IgpActions_State_709(IgpActionsState, IgpActionsConfig):
    """
    Operational state data 
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
        




class IgpActionsTop_IgpActions_697(BaseBinding):
    """
    Actions to set IGP route attributes; these actions
    apply to multiple IGPs
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = IgpActions_Config_702()
        self.config._parent = weakref.ref(self)
        self.state = IgpActions_State_709()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IgpActionsTop(BaseBinding):
    """
    Top-level grouping 
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.igp_actions = IgpActionsTop_IgpActions_697()
        self.igp_actions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyConditionsConfig(BaseBinding):
    """
    Configuration data for general policy conditions, i.e., those
    not related to match-sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.call_policy = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:policy-definitions/oc-rpol:policy-definition/oc-rpol:name",
        )
        self.call_policy._parent = weakref.ref(self)
        self.install_protocol_eq = Identityref(_meta={"mandatory": False},
            base=oc_pol_types.Install_Protocol_Type,
        )
        self.install_protocol_eq._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyConditionsState(BaseBinding):
    """
    Operational state data for policy conditions
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
        




class Conditions_Config_774(PolicyConditionsConfig):
    """
    Configuration data for policy conditions
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
        




class Conditions_State_781(PolicyConditionsState, PolicyConditionsConfig):
    """
    Operational state data for policy conditions
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
        




class PolicyConditionsTop_Conditions_770(IgpConditions, GenericConditions):
    """
    Condition statements for the current policy statement
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Conditions_Config_774()
        self.config._parent = weakref.ref(self)
        self.state = Conditions_State_781()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyConditionsTop(BaseBinding):
    """
    Top-level grouping for policy conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.conditions = PolicyConditionsTop_Conditions_770()
        self.conditions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyStatementsConfig(BaseBinding):
    """
    Configuration data for policy statements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.name = String(_meta={"mandatory": False},
        )
        self.name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyStatementsState(BaseBinding):
    """
    Operational state data for policy statements
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
        




class PolicyActionsConfig(GenericActions):
    """
    Configuration data for policy actions
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
        




class PolicyActionsState(BaseBinding):
    """
    Operational state data for policy actions
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
        




class Actions_Config_834(PolicyActionsConfig):
    """
    Configuration data for policy actions
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
        




class Actions_State_841(PolicyActionsState, PolicyActionsConfig):
    """
    Operational state data for policy actions
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
        




class PolicyActionsTop_Actions_830(IgpActionsTop):
    """
    Top-level container for policy action statements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = Actions_Config_834()
        self.config._parent = weakref.ref(self)
        self.state = Actions_State_841()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyActionsTop(BaseBinding):
    """
    Top-level grouping for policy actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.actions = PolicyActionsTop_Actions_830()
        self.actions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Statement_Config_884(PolicyStatementsConfig):
    """
    Configuration data for policy statements
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
        




class Statement_State_891(PolicyStatementsState, PolicyStatementsConfig):
    """
    Operational state data for policy statements
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
        




class Statements_Statement_864(List, PolicyActionsTop, PolicyConditionsTop):
    """
    Policy statements group conditions and actions
    within a policy definition.  They are evaluated in
    the order specified (see the description of policy
    evaluation at the top of this module.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        self._meta["ordered_by"] = "user"
        super().__init__(_meta=_meta)
        # container
        self.config = Statement_Config_884()
        self.config._parent = weakref.ref(self)
        self.state = Statement_State_891()
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





class PolicyStatementsTop_Statements_860(BaseBinding):
    """
    Enclosing container for policy statements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.statement = Statements_Statement_864()
        self.statement._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyStatementsTop(BaseBinding):
    """
    Top-level grouping for the policy statements list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.statements = PolicyStatementsTop_Statements_860()
        self.statements._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class DefinedSetsTop_DefinedSets_912(GenericDefinedSets):
    """
    Predefined sets of attributes used in policy match
    statements
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
        




class DefinedSetsTop(BaseBinding):
    """
    Top-level grouping for defined set definitions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.defined_sets = DefinedSetsTop_DefinedSets_912()
        self.defined_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyDefinitionsConfig(BaseBinding):
    """
    Configuration data for policy definitions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.name = String(_meta={"mandatory": False},
        )
        self.name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyDefinitionsState(BaseBinding):
    """
    Operational state data for policy definitions
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
        




class PolicyDefinition_Config_963(PolicyDefinitionsConfig):
    """
    Configuration data for policy defintions
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
        




class PolicyDefinition_State_970(PolicyDefinitionsState, PolicyDefinitionsConfig):
    """
    Operational state data for policy definitions
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
        




class PolicyDefinitions_PolicyDefinition_947(List, PolicyStatementsTop):
    """
    List of top-level policy definitions, keyed by unique
    name.  These policy definitions are expected to be
    referenced (by name) in policy chains specified in import
    or export configuration statements.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = PolicyDefinition_Config_963()
        self.config._parent = weakref.ref(self)
        self.state = PolicyDefinition_State_970()
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





class PolicyDefinitionsTop_PolicyDefinitions_942(BaseBinding):
    """
    Enclosing container for the list of top-level policy
     definitions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.policy_definition = PolicyDefinitions_PolicyDefinition_947()
        self.policy_definition._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PolicyDefinitionsTop(BaseBinding):
    """
    Top-level grouping for the policy definition list
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.policy_definitions = PolicyDefinitionsTop_PolicyDefinitions_942()
        self.policy_definitions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class RoutingPolicyTop_RoutingPolicy_990(PolicyDefinitionsTop, DefinedSetsTop):
    """
    Top-level container for all routing policy configuration
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
        




class RoutingPolicyTop(BaseBinding):
    """
    Top level container for OpenConfig routing policy
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.routing_policy = RoutingPolicyTop_RoutingPolicy_990()
        self.routing_policy._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ApplyPolicyImportConfig(BaseBinding):
    """
    Configuration data for applying import policies
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.default_import_policy = DefaultPolicyType(_meta={"mandatory": False},
        )
        self.default_import_policy._parent = weakref.ref(self)
        # leaflist
        self.import_policy = LeafList(Leafref(_meta={"mandatory": False}, path="/oc-rpol:routing-policy/oc-rpol:policy-definitions/oc-rpol:policy-definition/oc-rpol:name"))
        self.import_policy._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class ApplyPolicyExportConfig(BaseBinding):
    """
    Configuration data for applying export policies
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.default_export_policy = DefaultPolicyType(_meta={"mandatory": False},
        )
        self.default_export_policy._parent = weakref.ref(self)
        # leaflist
        self.export_policy = LeafList(Leafref(_meta={"mandatory": False}, path="/oc-rpol:routing-policy/oc-rpol:policy-definitions/oc-rpol:policy-definition/oc-rpol:name"))
        self.export_policy._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class ApplyPolicyConfig(ApplyPolicyExportConfig, ApplyPolicyImportConfig):
    """
    Configuration data for routing policies
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
        




class ApplyPolicyState(BaseBinding):
    """
    Operational state associated with routing policy
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
        




class ApplyPolicy_Config_1093(ApplyPolicyConfig):
    """
    Policy configuration data.
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
        




class ApplyPolicy_State_1100(ApplyPolicyState, ApplyPolicyConfig):
    """
    Operational state for routing policy
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
        




class ApplyPolicyGroup_ApplyPolicy_1086(BaseBinding):
    """
    Anchor point for routing policies in the model.
    Import and export policies are with respect to the local
    routing table, i.e., export (send) and import (receive),
    depending on the context.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = ApplyPolicy_Config_1093()
        self.config._parent = weakref.ref(self)
        self.state = ApplyPolicy_State_1100()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ApplyPolicyGroup(BaseBinding):
    """
    Top level container for routing policy applications. This
    grouping is intended to be used in routing models where
    needed.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.apply_policy = ApplyPolicyGroup_ApplyPolicy_1086()
        self.apply_policy._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
routing = model_factory(RoutingPolicyTop)


# Top-containers


# augments
