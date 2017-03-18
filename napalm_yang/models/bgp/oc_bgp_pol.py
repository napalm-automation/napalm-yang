"""
This module contains data definitions for BGP routing policy.
It augments the base routing-policy module with BGP-specific
options for conditions and actions.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_bgp_pol = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import inet
from napalm_yang import oc_pol_types
from napalm_yang import oc_bgp_types
from napalm_yang import oc_rpol
# Imcludes

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.1.1")



__namespace__ = "http://openconfig.net/yang/bgp-policy"
__yang_version__ = "1"
__prefix__ = "oc-bgp-pol"
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

class BgpSetCommunityOptionType(Enumeration):
    """
    Type definition for options when setting the community
    attribute in a policy action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "ADD": {
        "info": {
            "description": "add the specified communities to the existing\ncommunity attribute"
        }
    }, 
    "REMOVE": {
        "info": {
            "description": "remove the specified communities from the\nexisting community attribute"
        }
    }, 
    "REPLACE": {
        "info": {
            "description": "replace the existing community attribute with\nthe specified communities. If an empty set is\nspecified, this removes the community attribute\nfrom the route."
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class BgpNextHopType(Union):
    """
    type definition for specifying next-hop in policy actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "enumeration": {
        "enum": {
            "SELF": {
                "info": {
                    "description": "special designation for local router's own\naddress, i.e., next-hop-self"
                }
            }
        }
    }, 
    "inet:ip-address-no-zone": {}
}, ):

        self.types = []
        self.types.append(inet.IpAddressNoZone({}))
        self.types.append(Enumeration({
    "enum": {
        "SELF": {
            "info": {
                "description": "special designation for local router's own\naddress, i.e., next-hop-self"
            }
        }
    }
}))
        

        super().__init__(_meta=_meta, type_ = type_, )

class BgpSetMedType(Union):
    """
    Type definition for specifying how the BGP MED can
    be set in BGP policy actions. The three choices are to set
    the MED directly, increment/decrement using +/- notation,
    and setting it to the IGP cost (predefined value).
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "enumeration": {
        "enum": {
            "IGP": {
                "info": {
                    "description": "set the MED value to the IGP cost toward the\nnext hop for the route"
                }
            }
        }
    }, 
    "string": {
        "pattern": "^[+-][0-9]+"
    }, 
    "uint32": {}
}, ):

        self.types = []
        self.types.append(String({
    "pattern": "^[+-][0-9]+"
}))
        self.types.append(Enumeration({
    "enum": {
        "IGP": {
            "info": {
                "description": "set the MED value to the IGP cost toward the\nnext hop for the route"
            }
        }
    }
}))
        self.types.append(Uint32({}))
        

        super().__init__(_meta=_meta, type_ = type_, )


# Identities

# Classes to support containers and lists



class MatchCommunityConfig(oc_rpol.MatchSetOptionsGroup):
    """
    Configuration data for match conditions on communities
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.community_set = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:defined-sets/oc-bgp-pol:bgp-defined-sets/oc-bgp-pol:community-sets/oc-bgp-pol:community-set/oc-bgp-pol:community-set-name",
        )
        self.community_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchCommunityState(BaseBinding):
    """
    Operational state data for match conditions on communities
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
        




class MatchCommunitySet_Config_135(MatchCommunityConfig):
    """
    Configuration data for match conditions on communities
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
        




class MatchCommunitySet_State_142(MatchCommunityState, MatchCommunityConfig):
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
        




class MatchCommunityTop_MatchCommunitySet_129(BaseBinding):
    """
    Top-level container for match conditions on communities.
    Match a referenced community-set according to the logic
    defined in the match-set-options leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchCommunitySet_Config_135()
        self.config._parent = weakref.ref(self)
        self.state = MatchCommunitySet_State_142()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchCommunityTop(BaseBinding):
    """
    Top-level grouping for match conditions on communities
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_community_set = MatchCommunityTop_MatchCommunitySet_129()
        self.match_community_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchExtCommunityConfig(oc_rpol.MatchSetOptionsGroup):
    """
    Configuration data for match conditions on extended
    communities
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ext_community_set = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:defined-sets/oc-bgp-pol:bgp-defined-sets/oc-bgp-pol:ext-community-sets/oc-bgp-pol:ext-community-set/oc-bgp-pol:ext-community-set-name",
        )
        self.ext_community_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchExtCommunityState(BaseBinding):
    """
    Operational state data for match conditions on extended
    communities
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
        




class MatchExtCommunitySet_Config_189(MatchExtCommunityConfig):
    """
    Configuration data for match conditions on extended
    communities
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
        




class MatchExtCommunitySet_State_197(MatchExtCommunityState, MatchExtCommunityConfig):
    """
    Operational state data for match conditions on extended
    communities
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
        




class MatchExtCommunityTop_MatchExtCommunitySet_184(BaseBinding):
    """
    Match a referenced extended community-set according to the
    logic defined in the match-set-options leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchExtCommunitySet_Config_189()
        self.config._parent = weakref.ref(self)
        self.state = MatchExtCommunitySet_State_197()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchExtCommunityTop(BaseBinding):
    """
    Top-level grouping for match conditions on extended
    communities
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_ext_community_set = MatchExtCommunityTop_MatchExtCommunitySet_184()
        self.match_ext_community_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchAsPathConfig(oc_rpol.MatchSetOptionsGroup):
    """
    Configuration data for match conditions on AS path set
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.as_path_set = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:defined-sets/oc-bgp-pol:bgp-defined-sets/oc-bgp-pol:as-path-sets/oc-bgp-pol:as-path-set/oc-bgp-pol:as-path-set-name",
        )
        self.as_path_set._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchAsPathState(BaseBinding):
    """
    Operational state data for match conditions on AS path set
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
        




class MatchAsPathSet_Config_240(MatchAsPathConfig):
    """
    Configuration data for match conditions on AS path set
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
        




class MatchAsPathSet_State_247(MatchAsPathState, MatchAsPathConfig):
    """
    Operational state data for match conditions on AS
    path set
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
        




class MatchAsPathTop_MatchAsPathSet_235(BaseBinding):
    """
    Match a referenced as-path set according to the logic
    defined in the match-set-options leaf
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = MatchAsPathSet_Config_240()
        self.config._parent = weakref.ref(self)
        self.state = MatchAsPathSet_State_247()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class MatchAsPathTop(BaseBinding):
    """
    Top-level grouping for match conditions on AS path set
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.match_as_path_set = MatchAsPathTop_MatchAsPathSet_235()
        self.match_as_path_set._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpMatchSetConditions(MatchAsPathTop, MatchExtCommunityTop, MatchCommunityTop):
    """
    Condition statement definitions for checking membership in a
    defined set
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
        




class CommunityCountConfig(oc_pol_types.AttributeCompareOperators):
    """
    Configuration data for community count condition
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
        




class CommunityCountState(BaseBinding):
    """
    Operational state data for community count condition
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
        




class CommunityCount_Config_292(CommunityCountConfig):
    """
    Configuration data for community count condition
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
        




class CommunityCount_State_299(CommunityCountState, CommunityCountConfig):
    """
    Operational state data for community count condition
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
        




class CommunityCountTop_CommunityCount_287(BaseBinding):
    """
    Value and comparison operations for conditions based on the
    number of communities in the route update
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = CommunityCount_Config_292()
        self.config._parent = weakref.ref(self)
        self.state = CommunityCount_State_299()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class CommunityCountTop(BaseBinding):
    """
    Top-level grouping for community count condition
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.community_count = CommunityCountTop_CommunityCount_287()
        self.community_count._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathLengthConfig(oc_pol_types.AttributeCompareOperators):
    """
    Configuration data for AS path length condition
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
        




class AsPathLengthState(BaseBinding):
    """
    Operational state data for AS path length condition
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
        




class AsPathLength_Config_333(AsPathLengthConfig):
    """
    Configuration data for AS path length condition
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
        




class AsPathLength_State_340(AsPathLengthState, AsPathLengthConfig):
    """
    Operational state data for AS path length condition
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
        




class AsPathLengthTop_AsPathLength_328(BaseBinding):
    """
    Value and comparison operations for conditions based on the
    length of the AS path in the route update
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = AsPathLength_Config_333()
        self.config._parent = weakref.ref(self)
        self.state = AsPathLength_State_340()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathLengthTop(BaseBinding):
    """
    Top-level grouping for AS path length condition
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.as_path_length = AsPathLengthTop_AsPathLength_328()
        self.as_path_length._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpConditionsConfig(BaseBinding):
    """
    Configuration data for BGP-specific policy conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.origin_eq = oc_bgp_types.BgpOriginAttrType(_meta={"mandatory": False},
        )
        self.origin_eq._parent = weakref.ref(self)
        self.route_type = Enumeration(_meta={"mandatory": False},
            enum={
            "EXTERNAL": {
                "info": {
                    "description": "route type is external"
                }
            }, 
            "INTERNAL": {
                "info": {
                    "description": "route type is internal"
                }
            }
        },
        )
        self.route_type._parent = weakref.ref(self)
        self.med_eq = Uint32(_meta={"mandatory": False},
        )
        self.med_eq._parent = weakref.ref(self)
        self.local_pref_eq = Uint32(_meta={"mandatory": False},
        )
        self.local_pref_eq._parent = weakref.ref(self)
        # leaflist
        self.afi_safi_in = LeafList(Identityref(_meta={"mandatory": False}, base="oc-bgp-types:AFI_SAFI_TYPE"))
        self.afi_safi_in._parent = weakref.ref(self)
        self.next_hop_in = LeafList(inet.IpAddressNoZone(_meta={"mandatory": False}, ))
        self.next_hop_in._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class BgpConditionsState(BaseBinding):
    """
    Operational state data for BGP-specific policy conditions
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
        




class BgpConditions_Config_423(BgpConditionsConfig):
    """
    Configuration data for BGP-specific policy conditions
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
        




class BgpConditions_State_430(BgpConditionsState, BgpConditionsConfig):
    """
    Operational state data for BGP-specific policy
    conditions
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
        




class BgpConditionsTop_BgpConditions_419(BgpMatchSetConditions, AsPathLengthTop, CommunityCountTop):
    """
    Top-level container 
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpConditions_Config_423()
        self.config._parent = weakref.ref(self)
        self.state = BgpConditions_State_430()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpConditionsTop(BaseBinding):
    """
    Top-level grouping for BGP-specific policy conditions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.bgp_conditions = BgpConditionsTop_BgpConditions_419()
        self.bgp_conditions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class CommunitySetConfig(BaseBinding):
    """
    Configuration data for BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.community_set_name = String(_meta={"mandatory": True},
        )
        self.community_set_name._parent = weakref.ref(self)
        # leaflist
        self.community_member = LeafList(Union(_meta={"mandatory": False}, type_={
            "oc-bgp-types:bgp-community-regexp-type": {}, 
            "oc-bgp-types:bgp-std-community-type": {}, 
            "oc-bgp-types:bgp-well-known-community-type": {}
        }))
        self.community_member._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class CommunitySetState(BaseBinding):
    """
    Operational state data for BGP community sets
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
        




class CommunitySet_Config_497(CommunitySetConfig):
    """
    Configuration data for BGP community sets
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
        




class CommunitySet_State_504(CommunitySetState, CommunitySetConfig):
    """
    Operational state data for BGP community sets
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
        




class CommunitySets_CommunitySet_484(List, BaseBinding):
    """
    List of defined BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = CommunitySet_Config_497()
        self.config._parent = weakref.ref(self)
        self.state = CommunitySet_State_504()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.community_set_name = Leafref(_meta={"mandatory": False},
            path="../config/community-set-name",
        )
        self.community_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "community_set_name"





class CommunitySetTop_CommunitySets_480(BaseBinding):
    """
    Enclosing container for list of defined BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.community_set = CommunitySets_CommunitySet_484()
        self.community_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class CommunitySetTop(BaseBinding):
    """
    Top-level grouping for BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.community_sets = CommunitySetTop_CommunitySets_480()
        self.community_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ExtCommunitySetConfig(BaseBinding):
    """
    Configuration data for extended BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ext_community_set_name = String(_meta={"mandatory": False},
        )
        self.ext_community_set_name._parent = weakref.ref(self)
        # leaflist
        self.ext_community_member = LeafList(Union(_meta={"mandatory": False}, type_={
            "oc-bgp-types:bgp-community-regexp-type": {}, 
            "oc-bgp-types:bgp-ext-community-type": {}
        }))
        self.ext_community_member._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class ExtCommunitySetState(BaseBinding):
    """
    Operational state data for extended BGP community sets
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
        




class ExtCommunitySet_Config_566(ExtCommunitySetConfig):
    """
    Configuration data for extended BGP community sets
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
        




class ExtCommunitySet_State_573(ExtCommunitySetState, ExtCommunitySetConfig):
    """
    Operational state data for extended BGP community sets
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
        




class ExtCommunitySets_ExtCommunitySet_553(List, BaseBinding):
    """
    List of defined extended BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = ExtCommunitySet_Config_566()
        self.config._parent = weakref.ref(self)
        self.state = ExtCommunitySet_State_573()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.ext_community_set_name = Leafref(_meta={"mandatory": False},
            path="../config/ext-community-set-name",
        )
        self.ext_community_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "ext_community_set_name"





class ExtCommunitySetTop_ExtCommunitySets_548(BaseBinding):
    """
    Enclosing container for list of extended BGP community
    sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.ext_community_set = ExtCommunitySets_ExtCommunitySet_553()
        self.ext_community_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class ExtCommunitySetTop(BaseBinding):
    """
    Top-level grouping for extended BGP community sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ext_community_sets = ExtCommunitySetTop_ExtCommunitySets_548()
        self.ext_community_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathSetConfig(BaseBinding):
    """
    Configuration data for AS path sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.as_path_set_name = String(_meta={"mandatory": False},
        )
        self.as_path_set_name._parent = weakref.ref(self)
        # leaflist
        self.as_path_set_member = LeafList(String(_meta={"mandatory": False}, ))
        self.as_path_set_member._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class AsPathSetState(BaseBinding):
    """
    Operational state data for AS path sets
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
        




class AsPathSet_Config_632(AsPathSetConfig):
    """
    Configuration data for AS path sets
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
        




class AsPathSet_State_639(AsPathSetState, AsPathSetConfig):
    """
    Operational state data for AS path sets
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
        




class AsPathSets_AsPathSet_619(List, BaseBinding):
    """
    List of defined AS path sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = AsPathSet_Config_632()
        self.config._parent = weakref.ref(self)
        self.state = AsPathSet_State_639()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        self.as_path_set_name = Leafref(_meta={"mandatory": False},
            path="../config/as-path-set-name",
        )
        self.as_path_set_name._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "as_path_set_name"





class AsPathSetTop_AsPathSets_615(BaseBinding):
    """
    Enclosing container for list of define AS path sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        self.as_path_set = AsPathSets_AsPathSet_619()
        self.as_path_set._parent = weakref.ref(self)
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathSetTop(BaseBinding):
    """
    Top-level grouping for AS path sets
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.as_path_sets = AsPathSetTop_AsPathSets_615()
        self.as_path_sets._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class DefinedSets_BgpDefinedSets_659(AsPathSetTop, ExtCommunitySetTop, CommunitySetTop):
    """
    BGP-related set definitions for policy match conditions
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
        




class AsPathPrependConfig(BaseBinding):
    """
    Configuration data for the AS path prepend action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.repeat_n = Uint8(_meta={"mandatory": False},
            range_="1..max",
        )
        self.repeat_n._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathPrependState(BaseBinding):
    """
    Operational state data for the AS path prepend action
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
        




class SetAsPathPrepend_Config_698(AsPathPrependConfig):
    """
    Configuration data for the AS path prepend action
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
        




class SetAsPathPrepend_State_706(AsPathPrependState, AsPathPrependConfig):
    """
    Operational state data for the AS path prepend action
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
        




class AsPathPrependTop_SetAsPathPrepend_693(BaseBinding):
    """
    action to prepend local AS number to the AS-path a
    specified number of times
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = SetAsPathPrepend_Config_698()
        self.config._parent = weakref.ref(self)
        self.state = SetAsPathPrepend_State_706()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathPrependTop(BaseBinding):
    """
    Top-level grouping for the AS path prepend action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.set_as_path_prepend = AsPathPrependTop_SetAsPathPrepend_693()
        self.set_as_path_prepend._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityActionCommon(BaseBinding):
    """
    Common leaves for set-community and set-ext-community
    actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.options = BgpSetCommunityOptionType(_meta={"mandatory": False},
        )
        self.options._parent = weakref.ref(self)
        self.method = Enumeration(_meta={"mandatory": False},
            enum={
            "INLINE": {
                "info": {
                    "description": "The extended communities are specified inline as a\nlist"
                }
            }, 
            "REFERENCE": {
                "info": {
                    "description": "The extended communities are specified by referencing a\ndefined ext-community set"
                }
            }
        },
        )
        self.method._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityInlineConfig(BaseBinding):
    """
    Configuration data for inline specification of set-community
    action
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
        self.communities = LeafList(Union(_meta={"mandatory": False}, type_={
            "oc-bgp-types:bgp-std-community-type": {}, 
            "oc-bgp-types:bgp-well-known-community-type": {}
        }))
        self.communities._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class SetCommunityInlineState(BaseBinding):
    """
    Operational state data or inline specification of
    set-community action
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
        




class Inline_Config_787(SetCommunityInlineConfig):
    """
    Configuration data or inline specification of set-community
    action
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
        




class Inline_State_795(SetCommunityInlineState, SetCommunityInlineConfig):
    """
    Operational state data or inline specification of
    set-community action
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
        




class SetCommunityInlineTop_Inline_778(BaseBinding):
    """
    Set the community values for the action inline with
    a list.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../config/method=INLINE"
        
        super().__init__(_meta=_meta)
        # container
        self.config = Inline_Config_787()
        self.config._parent = weakref.ref(self)
        self.state = Inline_State_795()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityInlineTop(BaseBinding):
    """
    Top-level grouping or inline specification of set-community
    action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.inline = SetCommunityInlineTop_Inline_778()
        self.inline._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityReferenceConfig(BaseBinding):
    """
    Configuration data for referening a community-set in the
    set-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.community_set_ref = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:defined-sets/oc-bgp-pol:bgp-defined-sets/oc-bgp-pol:community-sets/oc-bgp-pol:community-set/oc-bgp-pol:community-set-name",
        )
        self.community_set_ref._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityReferenceState(BaseBinding):
    """
    Operational state data for referening a community-set in the
    set-community action
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
        




class Reference_Config_846(SetCommunityReferenceConfig):
    """
    Configuration data for referening a community-set in the
    set-community action
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
        




class Reference_State_854(SetCommunityReferenceState, SetCommunityReferenceConfig):
    """
    Operational state data for referening a community-set
    in the set-community action
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
        




class SetCommunityReferenceTop_Reference_837(BaseBinding):
    """
    Provide a reference to a defined community set for the
    set-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../config/method=REFERENCE"
        
        super().__init__(_meta=_meta)
        # container
        self.config = Reference_Config_846()
        self.config._parent = weakref.ref(self)
        self.state = Reference_State_854()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityReferenceTop(BaseBinding):
    """
    Top-level grouping for referening a community-set in the
    set-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.reference = SetCommunityReferenceTop_Reference_837()
        self.reference._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityActionConfig(SetCommunityActionCommon):
    """
    Configuration data for the set-community action
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
        




class SetCommunityActionState(BaseBinding):
    """
    Operational state data for the set-community action
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
        




class SetCommunity_Config_891(SetCommunityActionConfig):
    """
    Configuration data for the set-community action
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
        




class SetCommunity_State_898(SetCommunityActionState, SetCommunityActionConfig):
    """
    Operational state data for the set-community action
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
        




class SetCommunityActionTop_SetCommunity_884(SetCommunityReferenceTop, SetCommunityInlineTop):
    """
    Action to set the community attributes of the route, along
    with options to modify how the community is modified.
    Communities may be set using an inline list OR
    reference to an existing defined set (not both).
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = SetCommunity_Config_891()
        self.config._parent = weakref.ref(self)
        self.state = SetCommunity_State_898()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetCommunityActionTop(BaseBinding):
    """
    Top-level grouping for the set-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.set_community = SetCommunityActionTop_SetCommunity_884()
        self.set_community._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityInlineConfig(BaseBinding):
    """
    Configuration data for inline specification of
    set-ext-community action
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
        self.communities = LeafList(Union(_meta={"mandatory": False}, type_={
            "oc-bgp-types:bgp-ext-community-type": {}, 
            "oc-bgp-types:bgp-well-known-community-type": {}
        }))
        self.communities._parent = weakref.ref(self)
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityInlineState(BaseBinding):
    """
    Operational state data or inline specification of
    set-ext-community action
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
        




class Inline_Config_950(SetExtCommunityInlineConfig):
    """
    Configuration data or inline specification of
    set-ext-community action
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
        




class Inline_State_958(SetExtCommunityInlineState, SetExtCommunityInlineConfig):
    """
    Operational state data or inline specification of
    set-ext-community action
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
        




class SetExtCommunityInlineTop_Inline_941(BaseBinding):
    """
    Set the extended community values for the action inline with
    a list.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../config/method=INLINE"
        
        super().__init__(_meta=_meta)
        # container
        self.config = Inline_Config_950()
        self.config._parent = weakref.ref(self)
        self.state = Inline_State_958()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityInlineTop(BaseBinding):
    """
    Top-level grouping or inline specification of set-ext-community
    action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.inline = SetExtCommunityInlineTop_Inline_941()
        self.inline._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityReferenceConfig(BaseBinding):
    """
    Configuration data for referening a extended community-set
    in the set-ext-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.ext_community_set_ref = Leafref(_meta={"mandatory": False},
            path="/oc-rpol:routing-policy/oc-rpol:defined-sets/oc-bgp-pol:bgp-defined-sets/oc-bgp-pol:ext-community-sets/oc-bgp-pol:ext-community-set/oc-bgp-pol:ext-community-set-name",
        )
        self.ext_community_set_ref._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityReferenceState(BaseBinding):
    """
    Operational state data for referening an extended
    community-set in the set-ext-community action
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
        




class Reference_Config_1011(SetExtCommunityReferenceConfig):
    """
    Configuration data for referening an extended
    community-set in the set-ext-community action
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
        




class Reference_State_1019(SetExtCommunityReferenceState, SetExtCommunityReferenceConfig):
    """
    Operational state data for referening an extended
    community-set in the set-ext-community action
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
        




class SetExtCommunityReferenceTop_Reference_1002(BaseBinding):
    """
    Provide a reference to an extended community set for the
    set-ext-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = "../config/method=REFERENCE"
        
        super().__init__(_meta=_meta)
        # container
        self.config = Reference_Config_1011()
        self.config._parent = weakref.ref(self)
        self.state = Reference_State_1019()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityReferenceTop(BaseBinding):
    """
    Top-level grouping for referening an extended community-set
    in the set-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.reference = SetExtCommunityReferenceTop_Reference_1002()
        self.reference._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityActionConfig(SetCommunityActionCommon):
    """
    Configuration data for the set-ext-community action
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
        




class SetExtCommunityActionState(BaseBinding):
    """
    Operational state data for the set-ext-community action
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
        




class SetExtCommunity_Config_1057(SetExtCommunityActionConfig):
    """
    Configuration data for the set-ext-community action
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
        




class SetExtCommunity_State_1064(SetExtCommunityActionState, SetExtCommunityActionConfig):
    """
    Operational state data for the set-ext-community action
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
        




class SetExtCommunityActionTop_SetExtCommunity_1049(SetExtCommunityReferenceTop, SetExtCommunityInlineTop):
    """
    Action to set the extended community attributes of the
    route, along with options to modify how the community is
    modified. Extended communities may be set using an inline
    list OR a reference to an existing defined set (but not
    both).
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = SetExtCommunity_Config_1057()
        self.config._parent = weakref.ref(self)
        self.state = SetExtCommunity_State_1064()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class SetExtCommunityActionTop(BaseBinding):
    """
    Top-level grouping for the set-ext-community action
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.set_ext_community = SetExtCommunityActionTop_SetExtCommunity_1049()
        self.set_ext_community._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpActionsConfig(BaseBinding):
    """
    Configuration data for BGP-specific actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.set_next_hop = BgpNextHopType(_meta={"mandatory": False},
        )
        self.set_next_hop._parent = weakref.ref(self)
        self.set_med = BgpSetMedType(_meta={"mandatory": False},
        )
        self.set_med._parent = weakref.ref(self)
        self.set_local_pref = Uint32(_meta={"mandatory": False},
        )
        self.set_local_pref._parent = weakref.ref(self)
        self.set_route_origin = oc_bgp_types.BgpOriginAttrType(_meta={"mandatory": False},
        )
        self.set_route_origin._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpActionsState(BaseBinding):
    """
    Operational state data for BGP-specific actions
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
        




class BgpActions_Config_1120(BgpActionsConfig):
    """
    Configuration data for BGP-specific actions
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
        




class BgpActions_State_1127(BgpActionsState, BgpActionsConfig):
    """
    Operational state data for BGP-specific actions
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
        




class BgpActionsTop_BgpActions_1116(SetExtCommunityActionTop, SetCommunityActionTop, AsPathPrependTop):
    """
    Top-level container for BGP-specific actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = BgpActions_Config_1120()
        self.config._parent = weakref.ref(self)
        self.state = BgpActions_State_1127()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpActionsTop(BaseBinding):
    """
    Top-level grouping for BGP-specific actions
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.bgp_actions = BgpActionsTop_BgpActions_1116()
        self.bgp_actions._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment):
    """adds BGP defined sets container to routing policy
model"""
    yang_prefix = __prefix__

    def __init__(self):
        self.bgp_defined_sets = DefinedSets_BgpDefinedSets_659()
        self.bgp_defined_sets._parent = weakref.ref(self)
        

        
        self.path = [u'oc-rpol:routing-policy', u'oc-rpol:defined-sets']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        



# Load the augmentation
Augment_0()()

class Augment_1(BaseAugment, BgpActionsTop):
    """BGP policy actions added to routing policy
module"""
    yang_prefix = __prefix__

    def __init__(self):
        

        
        self.path = [u'oc-rpol:routing-policy', u'oc-rpol:policy-definitions', u'oc-rpol:policy-definition', u'oc-rpol:statements', u'oc-rpol:statement', u'oc-rpol:actions']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        BgpActionsTop.__init__(self)
        



# Load the augmentation
Augment_1()()

class Augment_2(BaseAugment, BgpConditionsTop):
    """BGP policy conditions added to routing policy module"""
    yang_prefix = __prefix__

    def __init__(self):
        

        
        self.path = [u'oc-rpol:routing-policy', u'oc-rpol:policy-definitions', u'oc-rpol:policy-definition', u'oc-rpol:statements', u'oc-rpol:statement', u'oc-rpol:conditions']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        BgpConditionsTop.__init__(self)
        



# Load the augmentation
Augment_2()()
