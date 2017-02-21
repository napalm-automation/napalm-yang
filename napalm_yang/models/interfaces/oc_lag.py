"""
Model for managing aggregated (aka bundle, LAG) interfaces.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_lag = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import oc_eth
from napalm_yang import oc_if
from napalm_yang import ift

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.1.0")



__namespace__ = "http://openconfig.net/yang/interfaces/aggregate"
__yang_version__ = "1"
__prefix__ = "oc-lag"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-12-22": {
        "revision": "2016-12-22"
    }
}



# extensions

# features


# typedef

class AggregationType(Enumeration):
    """
    Type to define the lag-type, i.e., how the LAG is
    defined and managed
    """
    prefix = __prefix__

    def __init__(self, _meta=None, enum = {
    "LACP": {
        "info": {
            "description": "LAG managed by LACP"
        }
    }, 
    "STATIC": {
        "info": {
            "description": "Statically configured bundle / LAG"
        }
    }
}, ):

        super().__init__(_meta=_meta, enum = enum, )


# Identities

# Classes to support containers and lists



class AggregationLogicalConfig(BaseBinding):
    """
    Configuration data for aggregate interfaces
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.min_links = Uint16(_meta={"mandatory": False},
        )
        self.lag_type = AggregationType(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AggregationLogicalState(BaseBinding):
    """
    Operational state data for aggregate interfaces
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.lag_speed = Uint32(_meta={"mandatory": False},
        )
        # leaflist
        self.member = LeafList(oc_if.BaseInterfaceRef(_meta={"mandatory": False}, ))
        # Meta
        self._meta["config"] = True
        




class Aggregation_Config_116(AggregationLogicalConfig):
    """
    Configuration variables for logical aggregate /
    LAG interfaces
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
        




class Aggregation_State_124(AggregationLogicalState, AggregationLogicalConfig):
    """
    Operational state variables for logical
    aggregate / LAG interfaces
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
        




class AggregationLogicalTop_Aggregation_110(BaseBinding):
    """
    Options for logical interfaces representing
    aggregates
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Aggregation_Config_116()
        self.state = Aggregation_State_124()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AggregationLogicalTop(BaseBinding):
    """
    Top-level data definitions for LAGs
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.aggregation = AggregationLogicalTop_Aggregation_110()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetIfAggregationConfig(BaseBinding):
    """
    Adds configuration items for Ethernet interfaces
    belonging to a logical aggregate / LAG
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.aggregate_id = Leafref(_meta={"mandatory": False},
            path="/oc-if:interfaces/oc-if:interface/oc-if:name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment, AggregationLogicalTop):
    """Adds LAG configuration to the interface module"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface']
        
        self._meta = {'when': u"oc-if:type = 'ift:ieee8023adLag'"}

        
        BaseAugment.__init__(self)
        
        AggregationLogicalTop.__init__(self)
        



class Augment_1(BaseAugment, EthernetIfAggregationConfig):
    """Adds LAG settings to individual Ethernet
interfaces"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-eth:ethernet', u'oc-eth:state']
        
        self._meta = {'when': u"oc-if:type = 'ift:ethernetCsmacd'"}

        
        BaseAugment.__init__(self)
        
        EthernetIfAggregationConfig.__init__(self)
        



class Augment_2(BaseAugment, EthernetIfAggregationConfig):
    """Adds LAG settings to individual Ethernet
interfaces"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-eth:ethernet', u'oc-eth:config']
        
        self._meta = {'when': u"oc-if:type = 'ift:ethernetCsmacd'"}

        
        BaseAugment.__init__(self)
        
        EthernetIfAggregationConfig.__init__(self)
        


