"""
This module defines configuration and operational state data
for transceivers (i.e., pluggable optics).  The module should be
used in conjunction with the platform model where other
physical entity data are represented.

In the platform model, a component of type=TRANSCEIVER is
expected to be a subcomponent of a PORT component.  This
module defines a concrete schema for the associated data for
components with type=TRANSCEIVER.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_transceiver = LocalNamespace()



# Imports
from napalm_yang import oc_opt_types
from napalm_yang import oc_types
from napalm_yang import oc_platform
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import oc_if

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.2.0")



__namespace__ = "http://openconfig.net/yang/platform/transceiver"
__yang_version__ = "1"
__prefix__ = "oc-transceiver"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
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

# Classes to support containers and lists



class OpticalPowerState_OutputPower_58(oc_types.AvgMinMaxInstantStatsPrecision2Dbm):
    """
    The output optical power of this port in units of 0.01dBm.
    If the port is an aggregate of multiple physical channels,
    this attribute is the total power or sum of all channels.
    Values include the instantaneous, average, minimum, and
    maximum statistics. If avg/min/max statistics are not
    supported, the target is expected to just supply the
    instant value
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
        




class OpticalPowerState_InputPower_71(oc_types.AvgMinMaxInstantStatsPrecision2Dbm):
    """
    The input optical power of this port in units of 0.01dBm.
    If the port is an aggregate of multiple physical channels,
    this attribute is the total power or sum of all channels.
    Values include the instantaneous, average, minimum, and
    maximum statistics. If avg/min/max statistics are not
    supported, the target is expected to just supply the
    instant value
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
        




class OpticalPowerState_LaserBiasCurrent_84(oc_types.AvgMinMaxInstantStatsPrecision2Ma):
    """
    The current applied by the system to the transmit laser to
    achieve the output power. The current is expressed in mA
    with up to two decimal precision. Values include the
    instantaneous, average, minimum, and maximum statistics.
    If avg/min/max statistics are not supported, the target is
    expected to just supply the instant value
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
        




class OpticalPowerState(BaseBinding):
    """
    Reusable leaves related to optical power state -- these
    are read-only state values. If avg/min/max statistics are
    not supported, the target is expected to just supply the
    instant value
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.output_power = OpticalPowerState_OutputPower_58()
        self.input_power = OpticalPowerState_InputPower_71()
        self.laser_bias_current = OpticalPowerState_LaserBiasCurrent_84()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class OutputOpticalFrequency(BaseBinding):
    """
    Reusable leaves related to optical output power -- this is
    typically configurable on line side and read-only on the
    client-side
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.output_frequency = oc_opt_types.FrequencyType(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PhysicalChannelConfig(BaseBinding):
    """
    Configuration data for physical client channels
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.index = Uint16(_meta={"mandatory": False},
            range_="0..max",
        )
        self.tx_laser = Boolean(_meta={"mandatory": False},
        )
        self.target_output_power = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.description = String(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PhysicalChannelState(OpticalPowerState, OutputOpticalFrequency):
    """
    Operational state data for client channels.
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
        




class Channel_Config_182(PhysicalChannelConfig):
    """
    Configuration data for physical channels
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
        




class Channel_State_189(PhysicalChannelState, PhysicalChannelConfig):
    """
    Operational state data for channels
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
        




class PhysicalChannels_Channel_167(List, BaseBinding):
    """
    List of client channels, keyed by index within a physical
    client port.  A physical port with a single channel would
    have a single zero-indexed element
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Channel_Config_182()
        self.state = Channel_State_189()
        # list
        # leaf
        self.index = Leafref(_meta={"mandatory": False},
            path="../config/index",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "index"





class PhysicalChannelTop_PhysicalChannels_163(BaseBinding):
    """
    Enclosing container for client channels
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.channel = PhysicalChannels_Channel_167()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PhysicalChannelTop(BaseBinding):
    """
    Top-level grouping for physical client channels
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.physical_channels = PhysicalChannelTop_PhysicalChannels_163()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PortTransceiverConfig(BaseBinding):
    """
    Configuration data for client port transceivers
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.form_factor_preconf = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Transceiver_Form_Factor_Type,
        )
        self.enabled = Boolean(_meta={"mandatory": False},
        )
        self.ethernet_pmd_preconf = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Ethernet_Pmd_Type,
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PortTransceiverState(BaseBinding):
    """
    Operational state data for client port transceivers
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.vendor = String(_meta={"mandatory": False},
            length="1..16",
        )
        self.form_factor = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Transceiver_Form_Factor_Type,
        )
        self.vendor_rev = String(_meta={"mandatory": False},
            length="1..2",
        )
        self.serial_no = String(_meta={"mandatory": False},
            length="1..16",
        )
        self.fault_condition = Boolean(_meta={"mandatory": False},
        )
        self.date_code = yang.DateAndTime(_meta={"mandatory": False},
        )
        self.otn_compliance_code = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Otn_Application_Code,
        )
        self.ethernet_pmd = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Ethernet_Pmd_Type,
        )
        self.vendor_part = String(_meta={"mandatory": False},
            length="1..16",
        )
        self.connector_type = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Fiber_Connector_Type,
        )
        self.internal_temp = Int16(_meta={"mandatory": False},
            range_="-40..125",
        )
        self.sonet_sdh_compliance_code = Identityref(_meta={"mandatory": False},
            base=oc_opt_types.Sonet_Application_Code,
        )
        self.present = Enumeration(_meta={"mandatory": False},
            enum={
            "NOT_PRESENT": {
                "info": {
                    "description": "Transceiver is not present on the port"
                }
            }, 
            "PRESENT": {
                "info": {
                    "description": "Transceiver is present on the port"
                }
            }
        },
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Transceiver_Config_403(PortTransceiverConfig):
    """
    Configuration data for client port transceivers
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
        




class Transceiver_State_410(PortTransceiverState, PortTransceiverConfig):
    """
    Operational state data for client port transceivers
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
        




class PortTransceiverTop_Transceiver_399(PhysicalChannelTop):
    """
    Top-level container for client port transceiver data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Transceiver_Config_403()
        self.state = Transceiver_State_410()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PortTransceiverTop(BaseBinding):
    """
    Top-level grouping for client port transceiver data
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.transceiver = PortTransceiverTop_Transceiver_399()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment):
    """Adds a reference from the base interface to its corresponding
physical channels."""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:state']
        
        self.physical_channel = Leafref(path = "/oc-platform:components/oc-platform:component[oc-platform:name=current()/../oc-platform:hardware-port]/oc-transceiver:transceiver/oc-transceiver:physical-channels/oc-transceiver:channel/oc-transceiver:index")
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        



class Augment_1(BaseAugment, PortTransceiverTop):
    """Adding transceiver data to physical inventory"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-platform:components', u'oc-platform:component']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        PortTransceiverTop.__init__(self)
        


