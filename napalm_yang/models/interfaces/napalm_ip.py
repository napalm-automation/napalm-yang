"""
This module defines some augmentations to the interface's IP model of OC
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

napalm_ip = LocalNamespace()



# Imports
from napalm_yang import oc_if
from napalm_yang import oc_ip
from napalm_yang import oc_vlan

# openconfig-extensions



__namespace__ = "https://github.com/napalm-automation/napalm-yang/yang_napalm/interfaces"
__yang_version__ = "1"
__prefix__ = "napalm-ip"
__contact__ = "napalm-automation@googlegroups.com"
__organization__ = "NAPALM Automation"
__revision__ = {
    "2017-03-17": {
        "revision": "2017-03-17"
    }
}



# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class SecondaryTop(BaseBinding):
    """
    Add secondary statement
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.secondary = Boolean(_meta={"mandatory": False},
        )
        self.secondary._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment, SecondaryTop):
    """Add secondary statement to routed VLANs' IPs"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-vlan:routed-vlan', u'oc-ip:ipv4', u'oc-ip:addresses', u'oc-ip:address', u'oc-ip:config']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        SecondaryTop.__init__(self)
        



# Load the augmentation
Augment_0()()

class Augment_1(BaseAugment, SecondaryTop):
    """Add secondary statement to subinterfaces' IPs"""
    yang_prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv4', u'oc-ip:addresses', u'oc-ip:address', u'oc-ip:config']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        SecondaryTop.__init__(self)
        



# Load the augmentation
Augment_1()()
