"""
This module defines data types (e.g., YANG identities)
to support the OpenConfig component inventory model.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_platform_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.5.0")



__namespace__ = "http://openconfig.net/yang/platform-types"
__yang_version__ = "1"
__prefix__ = "oc-platform-types"
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
Openconfig_Hardware_Component = Identity(
    base=None,
    value="OPENCONFIG_HARDWARE_COMPONENT",
    description="""Base identity for hardware related components in a managed
device.  Derived identities are partially based on contents
of the IANA Entity MIB."""
    )

Openconfig_Software_Component = Identity(
    base=None,
    value="OPENCONFIG_SOFTWARE_COMPONENT",
    description="""Base identity for software-related components in a managed
device"""
    )

Chassis = Identity(
    base=Openconfig_Hardware_Component,
    value="CHASSIS",
    description="""Chassis component, typically with multiple slots / shelves"""
    )

Backplane = Identity(
    base=Openconfig_Hardware_Component,
    value="BACKPLANE",
    description="""Backplane component for aggregating traffic, typically
contained in a chassis component"""
    )

Power_Supply = Identity(
    base=Openconfig_Hardware_Component,
    value="POWER_SUPPLY",
    description="""Component that is supplying power to the device"""
    )

Fan = Identity(
    base=Openconfig_Hardware_Component,
    value="FAN",
    description="""Cooling fan, or could be some other heat-reduction component"""
    )

Sensor = Identity(
    base=Openconfig_Hardware_Component,
    value="SENSOR",
    description="""Physical sensor, e.g., a temperature sensor in a chassis"""
    )

Module = Identity(
    base=Openconfig_Hardware_Component,
    value="MODULE",
    description="""Replaceable hardware module, e.g., a daughtercard"""
    )

Linecard = Identity(
    base=Openconfig_Hardware_Component,
    value="LINECARD",
    description="""Linecard component, typically inserted into a chassis slot"""
    )

Port = Identity(
    base=Openconfig_Hardware_Component,
    value="PORT",
    description="""Physical port, e.g., for attaching pluggables and networking
cables"""
    )

Transceiver = Identity(
    base=Openconfig_Hardware_Component,
    value="TRANSCEIVER",
    description="""Pluggable module present in a port"""
    )

Cpu = Identity(
    base=Openconfig_Hardware_Component,
    value="CPU",
    description="""Processing unit, e.g., a management processor"""
    )

Operating_System = Identity(
    base=Openconfig_Software_Component,
    value="OPERATING_SYSTEM",
    description="""Operating system running on a component"""
    )


# Classes to support containers and lists



class AvgMinMaxInstantStatsPrecision1Celsius(BaseBinding):
    """
    Common grouping for recording temperature values in
    Celsius with 1 decimal precision. Values include the
    instantaneous, average, minimum, and maximum statistics
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.max = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.max._parent = weakref.ref(self)
        self.avg = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.avg._parent = weakref.ref(self)
        self.instant = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.instant._parent = weakref.ref(self)
        self.min = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.min._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments