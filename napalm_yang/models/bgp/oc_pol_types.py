"""
This module contains general data definitions for use in routing
policy.  It can be imported by modules that contain protocol-
specific policy conditions and actions.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_pol_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
# Imcludes

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.0.1")



__namespace__ = "http://openconfig.net/yang/policy-types"
__yang_version__ = "1"
__prefix__ = "oc-pol-types"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-05-12": {
        "revision": "2016-05-12"
    }
}



# extensions

# features


# typedef

class MatchSetOptionsType(Enumeration):
    """
    Options that govern the behavior of a match statement.  The
    default behavior is ANY, i.e., the given value matches any
    of the members of the defined set
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "ALL": {
        "info": {
            "description": "match is true if given value matches all\nmembers of the defined set"
        }
    }, 
    "ANY": {
        "info": {
            "description": "match is true if given value matches any member\nof the defined set"
        }
    }, 
    "INVERT": {
        "info": {
            "description": "match is true if given value does not match any\nmember of the defined set"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class MatchSetOptionsRestrictedType(Enumeration):
    """
    Options that govern the behavior of a match statement.  The
    default behavior is ANY, i.e., the given value matches any
    of the members of the defined set.  Note this type is a
    restricted version of the match-set-options-type.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "ANY": {
        "info": {
            "description": "match is true if given value matches any member\nof the defined set"
        }
    }, 
    "INVERT": {
        "info": {
            "description": "match is true if given value does not match any\nmember of the defined set"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class TagType(Union):
    """
    type for expressing route tags on a local system,
    including IS-IS and OSPF; may be expressed as either decimal or
    hexidecimal integer
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "uint32": {}, 
    "yang:hex-string": {}
}, ):

        self.types = []
        self.types.append(Uint32({}))
        self.types.append(yang.HexString({}))
        

        super().__init__(_meta=_meta, type_ = type_, )


# Identities
Attribute_Comparison = Identity(
    base=None,
    value="ATTRIBUTE_COMPARISON",
    description="""base type for supported comparison operators on route
attributes"""
    )

Attribute_Eq = Identity(
    base=Attribute_Comparison,
    value="ATTRIBUTE_EQ",
    description="""== comparison"""
    )

Attribute_Ge = Identity(
    base=Attribute_Comparison,
    value="ATTRIBUTE_GE",
    description=""">= comparison"""
    )

Attribute_Le = Identity(
    base=Attribute_Comparison,
    value="ATTRIBUTE_LE",
    description="""<= comparison"""
    )

Install_Protocol_Type = Identity(
    base=None,
    value="INSTALL_PROTOCOL_TYPE",
    description="""Base type for protocols which can install prefixes into the
RIB"""
    )

Bgp = Identity(
    base=Install_Protocol_Type,
    value="BGP",
    description="""BGP"""
    )

Isis = Identity(
    base=Install_Protocol_Type,
    value="ISIS",
    description="""IS-IS"""
    )

Ospf = Identity(
    base=Install_Protocol_Type,
    value="OSPF",
    description="""OSPFv2"""
    )

Ospf3 = Identity(
    base=Install_Protocol_Type,
    value="OSPF3",
    description="""OSPFv3"""
    )

Static = Identity(
    base=Install_Protocol_Type,
    value="STATIC",
    description="""Locally-installed static route"""
    )

Directly_Connected = Identity(
    base=Install_Protocol_Type,
    value="DIRECTLY_CONNECTED",
    description="""A directly connected route"""
    )

Local_Aggregate = Identity(
    base=Install_Protocol_Type,
    value="LOCAL_AGGREGATE",
    description="""Locally defined aggregate route"""
    )


# Classes to support containers and lists



class AttributeCompareOperators(BaseBinding):
    """
    common definitions for comparison operations in
    condition statements
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.operator = Identityref(_meta={"mandatory": False},
            base=Attribute_Comparison,
        )
        self.operator._parent = weakref.ref(self)
        self.value = Uint32(_meta={"mandatory": False},
        )
        self.value._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments