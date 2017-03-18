"""
This sub-module contains groupings that are common across multiple BGP
contexts and provide structure around other primitive groupings.
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
# Imcludes
from openconfig_bgp_common import *

from openconfig_bgp_common_multiprotocol import *


# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("2.1.1")



__prefix__ = "oc-bgp"
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


# Identities

# Classes to support containers and lists



class LoggingOptions_Config_42(BgpCommonNeighborGroupLoggingOptionsConfig):
    """
    Configuration parameters enabling or modifying logging
    for events relating to the BGPgroup
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
        




class LoggingOptions_State_48(BgpCommonNeighborGroupLoggingOptionsConfig):
    """
    State information relating to logging for the BGP neighbor
    or group
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
        




class BgpCommonStructureNeighborGroupLoggingOptions_LoggingOptions_38(BaseBinding):
    """
    Logging options for events related to the BGP neighbor or
    group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = LoggingOptions_Config_42()
        self.config._parent = weakref.ref(self)
        self.state = LoggingOptions_State_48()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonStructureNeighborGroupLoggingOptions(BaseBinding):
    """
    Structural grouping used to include error handling configuration and
    state for both BGP neighbors and groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.logging_options = BgpCommonStructureNeighborGroupLoggingOptions_LoggingOptions_38()
        self.logging_options._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EbgpMultihop_Config_66(BgpCommonNeighborGroupMultihopConfig):
    """
    Configuration parameters relating to eBGP multihop for the
    BGP group
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
        




class EbgpMultihop_State_72(BgpCommonNeighborGroupMultihopConfig):
    """
    State information for eBGP multihop, for the BGP neighbor
    or group
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
        




class BgpCommonStructureNeighborGroupEbgpMultihop_EbgpMultihop_63(BaseBinding):
    """
    eBGP multi-hop parameters for the BGPgroup
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = EbgpMultihop_Config_66()
        self.config._parent = weakref.ref(self)
        self.state = EbgpMultihop_State_72()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonStructureNeighborGroupEbgpMultihop(BaseBinding):
    """
    Structural grouping used to include eBGP multihop configuration and
    state for both BGP neighbors and peer groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.ebgp_multihop = BgpCommonStructureNeighborGroupEbgpMultihop_EbgpMultihop_63()
        self.ebgp_multihop._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class RouteReflector_Config_90(BgpCommonNeighborGroupRouteReflectorConfig):
    """
    Configuraton parameters relating to route reflection
    for the BGPgroup
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
        




class RouteReflector_State_96(BgpCommonNeighborGroupRouteReflectorConfig):
    """
    State information relating to route reflection for the
    BGPgroup
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
        




class BgpCommonStructureNeighborGroupRouteReflector_RouteReflector_87(BaseBinding):
    """
    Route reflector parameters for the BGPgroup
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = RouteReflector_Config_90()
        self.config._parent = weakref.ref(self)
        self.state = RouteReflector_State_96()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonStructureNeighborGroupRouteReflector(BaseBinding):
    """
    Structural grouping used to include route reflector configuration and
    state for both BGP neighbors and peer groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.route_reflector = BgpCommonStructureNeighborGroupRouteReflector_RouteReflector_87()
        self.route_reflector._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AsPathOptions_Config_115(BgpCommonNeighborGroupAsPathOptionsConfig):
    """
    Configuration parameters relating to AS_PATH manipulation
    for the BGP peer or group
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
        




class AsPathOptions_State_121(BgpCommonNeighborGroupAsPathOptionsConfig):
    """
    State information relating to the AS_PATH manipulation
    mechanisms for the BGP peer or group
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
        




class BgpCommonStructureNeighborGroupAsPathOptions_AsPathOptions_111(BaseBinding):
    """
    AS_PATH manipulation parameters for the BGP neighbor or
    group
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = AsPathOptions_Config_115()
        self.config._parent = weakref.ref(self)
        self.state = AsPathOptions_State_121()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonStructureNeighborGroupAsPathOptions(BaseBinding):
    """
    Structural grouping used to include AS_PATH manipulation configuration
    and state for both BGP neighbors and peer groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.as_path_options = BgpCommonStructureNeighborGroupAsPathOptions_AsPathOptions_111()
        self.as_path_options._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AddPaths_Config_140(BgpCommonNeighborGroupAddPathsConfig):
    """
    Configuration parameters relating to ADD_PATHS
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
        




class AddPaths_State_145(BgpCommonNeighborGroupAddPathsConfig):
    """
    State information associated with ADD_PATHS
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
        




class BgpCommonStructureNeighborGroupAddPaths_AddPaths_136(BaseBinding):
    """
    Parameters relating to the advertisement and receipt of
    multiple paths for a single NLRI (add-paths)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.config = AddPaths_Config_140()
        self.config._parent = weakref.ref(self)
        self.state = AddPaths_State_145()
        self.state._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class BgpCommonStructureNeighborGroupAddPaths(BaseBinding):
    """
    Structural grouping used to include ADD-PATHs configuration and state
    for both BGP neighbors and peer groups
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        self.add_paths = BgpCommonStructureNeighborGroupAddPaths_AddPaths_136()
        self.add_paths._parent = weakref.ref(self)
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments