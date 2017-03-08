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

oc_vlan_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.0.2")



__namespace__ = "http://openconfig.net/yang/vlan-types"
__yang_version__ = "1"
__prefix__ = "oc-vlan-types"
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

class VlanId(Uint16):
    """
    Type definition representing a single-tagged VLAN
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, range_ = "1..4094", ):

        super().__init__(_meta=_meta, range_ = range_, )

class VlanRange(String):
    """
    Type definition representing a range of single-tagged
    VLANs. A range is specified as x..y where x and y are
    valid VLAN IDs (1 <= vlan-id <= 4094). The range is
    assumed to be inclusive, such that any VLAN-ID matching
    x <= VLAN-ID <= y falls within the range.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, pattern = "(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])", ):

        super().__init__(_meta=_meta, pattern = pattern, )

class QinqId(String):
    """
    Type definition representing a single double-tagged/QinQ VLAN
    identifier. The format of a QinQ VLAN-ID is x.y where X is the
    'outer' VLAN identifier, and y is the 'inner' VLAN identifier.
    Both x and y must be valid VLAN IDs (1 <= vlan-id <= 4094)
    with the exception that y may be equal to a wildcard (*). In
    cases where y is set to the wildcard, this represents all inner
    VLAN identifiers where the outer VLAN identifier is equal to
    x
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, pattern = "(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)", ):

        super().__init__(_meta=_meta, pattern = pattern, )

class QinqIdRange(Union):
    """
    A type definition representing a range of double-tagged/QinQ
    VLAN identifiers. The format of a QinQ VLAN-ID range can be
    specified in three formats. Where the range is outer VLAN IDs
    the range is specified as x..y.z. In this case outer VLAN
    identifiers meeting the criteria x <= outer-vlan-id <= y are
    accepted iff the inner VLAN-ID is equal to y - or any inner-tag
    if the wildcard is specified. Alternatively the range can be
    specified as x.y..z. In this case only VLANs with an
    outer-vlan-id qual to x are accepted (x may again be the
    wildcard). Inner VLANs are accepted if they meet the inequality
    y <= inner-vlan-id <= z.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "string": {
        "pattern": "(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)"
    }
}, ):

        self.types = []
        self.types.append(String({
    "pattern": "(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.\\.(409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])\\.((409[0-4]|40[0-8][0-9]|[1-3][0-9]{3}|[1-9][0-9]{1,2}|[1-9])|\\*)"
}))
        

        super().__init__(_meta=_meta, type_ = type_, )

class VlanModeType(Enumeration):
    """
    VLAN interface mode (trunk or access)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "ACCESS": {
        "info": {
            "description": "Access mode VLAN interface (No 802.1q header)"
        }
    }, 
    "TRUNK": {
        "info": {
            "description": "Trunk mode VLAN interface"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )

class VlanRef(Union):
    """
    Reference to a VLAN by name or id
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, type_ = {
    "string": {}, 
    "vlan-id": {}
}, ):

        self.types = []
        self.types.append(VlanId({}))
        self.types.append(String({}))
        

        super().__init__(_meta=_meta, type_ = type_, )


# Identities
Tpid_Types = Identity(
    base=None,
    value="TPID_TYPES",
    description="""Base identity for TPID values that can override the VLAN
ethertype value"""
    )

Tpid_0X8100 = Identity(
    base=Tpid_Types,
    value="TPID_0x8100",
    description="""Default TPID value for 802.1q single-tagged VLANs."""
    )

Tpid_0X8A88 = Identity(
    base=Tpid_Types,
    value="TPID_0x8A88",
    description="""TPID value for 802.1ad provider bridging, Q-in-Q,
or stacked VLANs"""
    )

Tpid_0X9100 = Identity(
    base=Tpid_Types,
    value="TPID_0x9100",
    description="""Alternate TPID value"""
    )

Tpid_0X9200 = Identity(
    base=Tpid_Types,
    value="TPID_0X9200",
    description="""Alternate TPID value"""
    )


# Classes to support containers and lists


# Top-uses

# Top-containers


# augments