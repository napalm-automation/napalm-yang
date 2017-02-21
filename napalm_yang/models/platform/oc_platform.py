"""
This module defines a data model for representing a system
component inventory, which can include hardware or software
elements arranged in an arbitrary structure. The primary
relationship supported by the model is containment, e.g.,
components containing subcomponents.

It is expected that this model reflects every field replacable
unit on the device at a minimum (i.e., additional information
may be supplied about non-replacable components).

Every element in the inventory is termed a 'component' with each
component expected to have a unique name and type, and optionally
a unique system-assigned identifier and FRU number.  The
uniqueness is guaranteed by the system within the device.

Components may have properties defined by the system that are
modeled as a list of key-value pairs. These may or may not be
user-configurable.  The model provides a flag for the system
to optionally indicate which properties are user configurable.

Each component also has a list of 'subcomponents' which are
references to other components. Appearance in a list of
subcomponents indicates a containment relationship as described
above.  For example, a linecard component may have a list of
references to port components that reside on the linecard.

This schema is generic to allow devices to express their own
platform-specific structure.  It may be augmented by additional
component type-specific schemas that provide a common structure
for well-known component types.  In these cases, the system is
expected to populate the common component schema, and may
optionally also represent the component and its properties in the
generic structure.

The properties for each component may include dynamic values,
e.g., in the 'state' part of the schema.  For example, a CPU
component may report its utilization, temperature, or other
physical properties.  The intent is to capture all platform-
specific physical data in one location, including inventory
(presence or absence of a component) and state (physical
attributes or status).
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_platform = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import oc_if
from napalm_yang import oc_platform_types

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.5.0")



__namespace__ = "http://openconfig.net/yang/platform"
__yang_version__ = "1"
__prefix__ = "oc-platform"
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



class PlatformComponentPropertiesConfig(BaseBinding):
    """
    System-defined configuration data for component properties
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.name = String(_meta={"mandatory": False},
        )
        self.value = Union(_meta={"mandatory": False},
            type_={
            "boolean": {}, 
            "decimal64": {
                "fraction-digits": "2"
            }, 
            "int64": {}, 
            "string": {}, 
            "uint64": {}
        },
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentPropertiesState(BaseBinding):
    """
    Operational state data for component properties
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.configurable = Boolean(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Property_Config_136(PlatformComponentPropertiesConfig):
    """
    Configuration data for each property
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
        




class Property_State_143(PlatformComponentPropertiesState, PlatformComponentPropertiesConfig):
    """
    Operational state data for each property
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
        




class Properties_Property_123(List, BaseBinding):
    """
    List of system properties for the component
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Property_Config_136()
        self.state = Property_State_143()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class PlatformComponentPropertiesTop_Properties_119(BaseBinding):
    """
    Enclosing container 
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.property = Properties_Property_123()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentPropertiesTop(BaseBinding):
    """
    Top-level grouping 
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.properties = PlatformComponentPropertiesTop_Properties_119()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformSubcomponentRefConfig(BaseBinding):
    """
    Configuration data for subcomponent references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../../../../../component/config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformSubcomponentRefState(BaseBinding):
    """
    Operational state data for subcomponent references
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
        




class Subcomponent_Config_197(PlatformSubcomponentRefConfig):
    """
    Configuration data 
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
        




class Subcomponent_State_204(PlatformSubcomponentRefState, PlatformSubcomponentRefConfig):
    """
    Operational state data 
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
        




class Subcomponents_Subcomponent_184(List, BaseBinding):
    """
    List of subcomponent references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Subcomponent_Config_197()
        self.state = Subcomponent_State_204()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class PlatformSubcomponentRefTop_Subcomponents_180(BaseBinding):
    """
    Enclosing container for subcomponent references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.subcomponent = Subcomponents_Subcomponent_184()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformSubcomponentRefTop(BaseBinding):
    """
    Top-level grouping for list of subcomponent references
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.subcomponents = PlatformSubcomponentRefTop_Subcomponents_180()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentConfig(BaseBinding):
    """
    Configuration data for components
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.name = String(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentState(BaseBinding):
    """
    Operational state data for device components.
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.description = String(_meta={"mandatory": False},
        )
        self.serial_no = String(_meta={"mandatory": False},
        )
        self.part_no = String(_meta={"mandatory": False},
        )
        self.mfg_name = String(_meta={"mandatory": False},
        )
        self.version = String(_meta={"mandatory": False},
        )
        self.type_ = Union(_meta={"mandatory": False},
            type_={
            "identityref": {
                "base": "oc-platform-types:OPENCONFIG_HARDWARE_COMPONENT"
            }
        },
        )
        self.id = String(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentTempState_Temperature_295(oc_platform_types.AvgMinMaxInstantStatsPrecision1Celsius):
    """
    Temperature in degrees Celsius of the component. Values include
    the instantaneous, average, minimum, and maximum statistics. If
    avg/min/max statistics are not supported, the target is expected
    to just supply the instant value
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
        




class PlatformComponentTempState(BaseBinding):
    """
    Temperature state data for device components
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.temperature = PlatformComponentTempState_Temperature_295()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Component_Config_327(PlatformComponentConfig):
    """
    Configuration data for each component
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
        




class Component_State_334(PlatformComponentTempState, PlatformComponentState, PlatformComponentConfig):
    """
    Operational state data for each component
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
        




class Components_Component_314(List, PlatformSubcomponentRefTop, PlatformComponentPropertiesTop):
    """
    List of components, keyed by component name.
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Component_Config_327()
        self.state = Component_State_334()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False},
            path="../config/name",
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"





class PlatformComponentTop_Components_310(BaseBinding):
    """
    Enclosing container for the components in the system.
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        self.component = Components_Component_314()
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class PlatformComponentTop(BaseBinding):
    """
    Top-level grouping for components in the device inventory
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.components = PlatformComponentTop_Components_310()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
platform = PlatformComponentTop()


# Top-containers


# augments
class Augment_0(BaseAugment):
    """Adds a reference from the base interface to the corresponding
port component in the device inventory."""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:state']
        
        self.hardware_port = Leafref(path = "/oc-platform:components/oc-platform:component/oc-platform:name")
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        


