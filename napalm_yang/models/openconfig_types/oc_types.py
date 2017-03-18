"""
This module contains a set of general type definitions that
are used across OpenConfig models. It can be imported by modules
that make use of these types.
"""
from builtins import super
import weakref

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

oc_types = LocalNamespace()



# Imports
from napalm_yang import oc_ext
# Imcludes

# openconfig-extensions
openconfig_version = oc_ext.OpenconfigVersion("0.3.1")



__namespace__ = "http://openconfig.net/yang/openconfig-types"
__yang_version__ = "1"
__prefix__ = "oc-types"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-05-31": {
        "revision": "2016-05-31"
    }, 
    "2016-11-11": {
        "revision": "2016-11-11"
    }, 
    "2016-11-14": {
        "revision": "2016-11-14"
    }
}



# extensions

# features


# typedef

class Percentage(Uint8):
    """
    Integer indicating a percentage value
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, range_ = "0..100", ):

        super().__init__(_meta=_meta, range_ = range_, )

class StdRegexp(String):
    """
    This type definition is a placeholder for a standard
    definition of a regular expression that can be utilised in
    OpenConfig models. Further discussion is required to
    consider the type of regular expressions that are to be
    supported. An initial proposal is POSIX compatible.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, ):

        super().__init__(_meta=_meta, )

class Timeticks64(Uint64):
    """
    This type is based on the timeticks type defined in
    RFC 6991, but with 64-bit width.  It represents the time,
    modulo 2^64, in hundredths of a second between two epochs.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, ):

        super().__init__(_meta=_meta, )

class Ieeefloat32(Binary):
    """
    An IEEE 32-bit floating point number. The format of this number
    is of the form:
     1-bit  sign
     8-bit  exponent
     24-bit fraction
    The floating point value is calculated using:
     (-1)**S * 2**(Exponent-127) * (1+Fraction)
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, length = "32", ):

        super().__init__(_meta=_meta, length = length, )

class RoutingPassword(String):
    """
    This type is indicative of a password that is used within
    a routing protocol which can be returned in plain text to the
    NMS by the local system. Such passwords are typically stored
    as encrypted strings. Since the encryption used is generally
    well known, it is possible to extract the original value from
    the string - and hence this format is not considered secure.
    Leaves specified with this type should not be modified by
    the system, and should be returned to the end-user in plain
    text. This type exists to differentiate passwords, which
    may be sensitive, from other string leaves. It could, for
    example, be used by the NMS to censor this data when
    viewed by particular users.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None, ):

        super().__init__(_meta=_meta, )


# Identities
Address_Family = Identity(
    base=None,
    value="ADDRESS_FAMILY",
    description="""A base identity for all address families"""
    )

Ipv4 = Identity(
    base=Address_Family,
    value="IPV4",
    description="""The IPv4 address family"""
    )

Ipv6 = Identity(
    base=Address_Family,
    value="IPV6",
    description="""The IPv6 address family"""
    )


# Classes to support containers and lists



class AvgMinMaxStatsPrecision1(BaseBinding):
    """
    Common nodes for recording average, minimum, and
    maximum values for a statistic.  These values all have
    fraction-digits set to 1.
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
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
        self.min = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.min._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AvgMinMaxInstantStatsPrecision1(AvgMinMaxStatsPrecision1):
    """
    Common grouping for recording an instantaneous statistic value
    in addition to avg-min-max stats
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.instant = Decimal64(_meta={"mandatory": False},
            fraction_digits="1",
        )
        self.instant._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AvgMinMaxInstantStatsPrecision2Db(BaseBinding):
    """
    Common grouping for recording dB values with 2 decimal
    precision. Values include the instantaneous, average,
    minimum, and maximum statistics
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.max = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.max._parent = weakref.ref(self)
        self.avg = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.avg._parent = weakref.ref(self)
        self.instant = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.instant._parent = weakref.ref(self)
        self.min = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.min._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AvgMinMaxInstantStatsPrecision2Dbm(BaseBinding):
    """
    Common grouping for recording dBm values with 2 decimal
    precision. Values include the instantaneous, average,
    minimum, and maximum statistics
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.max = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.max._parent = weakref.ref(self)
        self.avg = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.avg._parent = weakref.ref(self)
        self.instant = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.instant._parent = weakref.ref(self)
        self.min = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.min._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        




class AvgMinMaxInstantStatsPrecision2Ma(BaseBinding):
    """
    Common grouping for recording mA values with 2 decimal
    precision. Values include the instantaneous, average,
    minimum, and maximum statistics
    """
    yang_prefix = __prefix__

    def __init__(self, _meta=None):
        self._meta = _meta or {}
        self._meta["when"] = ""
        
        super().__init__(_meta=_meta)
        # container
        # list
        # leaf
        self.max = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.max._parent = weakref.ref(self)
        self.avg = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.avg._parent = weakref.ref(self)
        self.instant = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.instant._parent = weakref.ref(self)
        self.min = Decimal64(_meta={"mandatory": False},
            fraction_digits="2",
        )
        self.min._parent = weakref.ref(self)
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses

# Top-containers


# augments