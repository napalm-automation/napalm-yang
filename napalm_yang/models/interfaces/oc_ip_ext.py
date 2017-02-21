"""
This module adds extensions to the base IP configuration and
operational state model to support additional use cases.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_ip_ext = LocalNamespace()



# Imports
from napalm_yang import oc_ext
from napalm_yang import oc_if
from napalm_yang import oc_ip

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("1.1.0")



__namespace__ = "http://openconfig.net/yang/interfaces/ip-ext"
__yang_version__ = "1"
__prefix__ = "oc-ip-ext"
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



class Ipv6AutoconfConfig(BaseBinding):
    """
    Configuration data for IPv6 address autoconfiguration
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.create_temporary_addresses = Boolean(_meta={"mandatory": False},
        )
        self.create_global_addresses = Boolean(_meta={"mandatory": False},
        )
        self.temporary_preferred_lifetime = Uint32(_meta={"mandatory": False},
        )
        self.temporary_valid_lifetime = Uint32(_meta={"mandatory": False},
        )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6AutoconfState(BaseBinding):
    """
    Operational state data for IPv6 address autoconfiguration
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
        




class Autoconf_Config_112(Ipv6AutoconfConfig):
    """
    [adapted from IETF IP model RFC 7277]

    Parameters to control the autoconfiguration of IPv6
    addresses, as described in RFC 4862.
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
        




class Autoconf_State_124(Ipv6AutoconfState, Ipv6AutoconfConfig):
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
        




class Ipv6AutoconfTop_Autoconf_108(BaseBinding):
    """
    Top-level container for IPv6 autoconf
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.config = Autoconf_Config_112()
        self.state = Autoconf_State_124()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ipv6AutoconfTop(BaseBinding):
    """
    Top-level grouping for IPv6 address autoconfiguration
    """
    prefix = __prefix__

    def __init__(self, _meta=None):
        super().__init__(_meta=_meta)
        # container
        self.autoconf = Ipv6AutoconfTop_Autoconf_108()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments
class Augment_0(BaseAugment, Ipv6AutoconfTop):
    """Adds address autoconfiguration to the base IP model"""
    prefix = __prefix__

    def __init__(self):
        
        self.path = [u'oc-if:interfaces', u'oc-if:interface', u'oc-if:subinterfaces', u'oc-if:subinterface', u'oc-ip:ipv6']
        
        self._meta = {'when': None}

        
        BaseAugment.__init__(self)
        
        Ipv6AutoconfTop.__init__(self)
        



# Load the augmentation
Augment_0()()
