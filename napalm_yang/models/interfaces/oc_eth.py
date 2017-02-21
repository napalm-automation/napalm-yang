"""
Model for managing Ethernet interfaces -- augments the IETF YANG
model for interfaces described by RFC 7223
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_eth = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import oc_if
from napalm_yang import ift

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.1.0")



__namespace__ = "http://openconfig.net/yang/interfaces/ethernet"
__yang_version__ = "1"
__prefix__ = "oc-eth"
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


# Identities
Ethernet_Speed = Identity(
    base=None,
    value="ETHERNET_SPEED",
    description="""base type to specify available Ethernet link
speeds"""
    )

Speed_10Mb = Identity(
    base=Ethernet_Speed,
    value="SPEED_10MB",
    description="""10 Mbps Ethernet"""
    )

Speed_100Mb = Identity(
    base=Ethernet_Speed,
    value="SPEED_100MB",
    description="""100 Mbps Ethernet"""
    )

Speed_1Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_1GB",
    description="""1 GBps Ethernet"""
    )

Speed_10Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_10GB",
    description="""10 GBps Ethernet"""
    )

Speed_25Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_25GB",
    description="""25 GBps Ethernet"""
    )

Speed_40Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_40GB",
    description="""40 GBps Ethernet"""
    )

Speed_50Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_50GB",
    description="""50 GBps Ethernet"""
    )

Speed_100Gb = Identity(
    base=Ethernet_Speed,
    value="SPEED_100GB",
    description="""100 GBps Ethernet"""
    )

Speed_Unknown = Identity(
    base=Ethernet_Speed,
    value="SPEED_UNKNOWN",
    description="""Interface speed is unknown.  Systems may report
speed UNKNOWN when an interface is down or unpopuplated (e.g.,
pluggable not present)."""
    )


# Classes to support containers and lists



class EthernetInterfaceConfig(BaseBinding):
    """
    Configuration items for Ethernet interfaces
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.auto_negotiate = Boolean(_meta={"mandatory": False},
        )
        self.enable_flow_control = Boolean(_meta={"mandatory": False},
        )
        self.port_speed = Identityref(_meta={"mandatory": False},
            base=Ethernet_Speed,
        )
        self.mac_address = yang.MacAddress(_meta={"mandatory": False},
        )
        self.duplex_mode = Enumeration(_meta={"mandatory": False},
            enum={
            "FULL": {
                "info": {
                    "description": "Full duplex mode"
                }
            }, 
            "HALF": {
                "info": {
                    "description": "Half duplex mode"
                }
            }
        },
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetInterfaceStateCounters(BaseBinding):
    """
    Ethernet-specific counters and statistics
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.in_fragment_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_oversize_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_8021q_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_8021q_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_mac_pause_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_jabber_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_crc_errors = yang.Counter64(_meta={"mandatory": False},
        )
        self.in_mac_control_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_mac_control_frames = yang.Counter64(_meta={"mandatory": False},
        )
        self.out_mac_pause_frames = yang.Counter64(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetInterfaceState_Counters_288(EthernetInterfaceStateCounters):
    """
    Ethernet interface counters
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
        




class EthernetInterfaceState(BaseBinding):
    """
    Grouping for defining Ethernet-specific operational state
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.counters = EthernetInterfaceState_Counters_288()
        # list
        # leaf
        self.hw_mac_address = yang.MacAddress(_meta={"mandatory": False},
        )
        self.negotiated_port_speed = Identityref(_meta={"mandatory": False},
            base=Ethernet_Speed,
        )
        self.effective_speed = Uint32(_meta={"mandatory": False},
        )
        self.negotiated_duplex_mode = Enumeration(_meta={"mandatory": False},
            enum={
            "FULL": {
                "info": {
                    "description": "Full duplex mode"
                }
            }, 
            "HALF": {
                "info": {
                    "description": "Half duplex mode"
                }
            }
        },
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ethernet_Config_307(EthernetInterfaceConfig):
    """
    Configuration data for ethernet interfaces
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
        




class Ethernet_State_314(EthernetInterfaceState, EthernetInterfaceConfig):
    """
    State variables for Ethernet interfaces
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
        




class EthernetTop_Ethernet_302(BaseBinding):
    """
    Top-level container for ethernet configuration
    and state
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Ethernet_Config_307()
        self.state = Ethernet_State_314()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetTop(BaseBinding):
    """
    top-level Ethernet config and state containers
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.ethernet = EthernetTop_Ethernet_302()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment, EthernetTop):
    """Adds addtional Ethernet-specific configuration to
interfaces model"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        EthernetTop.__init__(self)
        


