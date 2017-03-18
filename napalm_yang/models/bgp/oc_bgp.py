"""
This module describes a YANG model for BGP protocol
configuration.It is a limited subset of all of the configuration
parameters available in the variety of vendor implementations,
hence it is expected that it would be augmented with vendor-
specific configuration data as needed. Additional modules or
submodules to handle other aspects of BGP configuration,
including policy, VRFs, VPNs, and additional address families
are also expected.

This model supports the following BGP configuration level
hierarchy:

 BGP
   |
   +-> [ global BGP configuration ]
     +-> AFI / SAFI global
   +-> peer group
     +-> [ peer group config ]
     +-> AFI / SAFI [ per-AFI overrides ]
   +-> neighbor
     +-> [ neighbor config ]
     +-> [ optional pointer to peer-group ]
     +-> AFI / SAFI [ per-AFI overrides ]
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_bgp = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import oc_rpol
# Imcludes
from openconfig_bgp_global import *

from openconfig_bgp_neighbor import *

from openconfig_bgp_peer_group import *

from openconfig_bgp_common_structure import *

from openconfig_bgp_common_multiprotocol import *

from openconfig_bgp_common import *


# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.1.1")



__namespace__ = "http://openconfig.net/yang/bgp"
__yang_version__ = "1"
__prefix__ = "oc-bgp"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-03-31": {
        "revision": "2016-03-31"
    }, 
    "2016-06-06": {
        "revision": "2016-06-06"
    }, 
    "2016-06-21": {
        "revision": "2016-06-21"
    }
}



# extensions

# features


# typedef


# Identities

# Classes to support containers and lists



class Bgp_Global_91(oc_rpol.ApplyPolicyGroup, BgpGlobalBase):
    """
    Global configuration for the BGP router
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
        




class Bgp_Neighbors_98(BgpNeighborList):
    """
    Configuration for BGP neighbors
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
        




class Bgp_PeerGroups_104(BgpPeerGroupList):
    """
    Configuration for BGP peer-groups
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
        




class BgpTop_Bgp_87(BaseBinding):
    """
    Top-level configuration and state for the BGP router
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.global_ = Bgp_Global_91()
        self.global_._parent = weakref.ref(self)
        self.neighbors = Bgp_Neighbors_98()
        self.neighbors._parent = weakref.ref(self)
        self.peer_groups = Bgp_PeerGroups_104()
        self.peer_groups._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpTop(BaseBinding):
    """
    Top-level grouping for the BGP model data
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.bgp = BgpTop_Bgp_87()
        self.bgp._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
bgp = model_factory(BgpTop)


# Top-containers


# augments