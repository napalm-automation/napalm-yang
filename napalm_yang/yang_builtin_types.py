"""Yang Types"""
from builtins import super
import copy

from decimal import Decimal

import re

from napalm_yang.yang_base import YangType, BaseBinding


def value_in_pattern(pattern, value):
    if "^" not in pattern:
        pattern = "^{}".format(pattern)
    if "$" not in pattern:
        pattern = "{}$".format(pattern)

    pattern = re.compile(pattern)
    match = pattern.match(value)
    return match is not None


def value_in_range(range_, value, min_, max_, num_type=int):
    """Implements `range-stmt` as defined in rfc6020#section-12."""
    def _value_in_subrange(sr, v, min_, max_, num_type):
        valid = sr.split("..")

        if len(valid) == 1:
            return num_type(valid[0]) == v
        elif len(valid) == 2:
            min_ = num_type(min_) if valid[0] == "min" else num_type(valid[0])
            max_ = num_type(max_) if valid[1] == "max" else num_type(valid[1])
            return min_ <= v <= max_
        else:
            raise Exception("Invalid range: {}".format(sr))

    if isinstance(value, bool) or not (isinstance(value, num_type), isinstance(value, int)):
        # Bool is of type int as well and evaluates 1
        return False

    return any([_value_in_subrange(sr, value, min_, max_, num_type)
                for sr in range_.split("|")])


class Baseint(YangType):
    """Implements rfc6020 section-9.2."""
    num_type = int

    def __init__(self, range_=None, _meta=None):
        super().__init__(_meta)

        self.ranges = ["{}..{}".format(self.min, self.max)]

        if range_ is not None:
            self.ranges.append(range_)

    def _verify_value(self, value):
        min_, max_ = self.ranges[0].split("..")
        return all([value_in_range(r, value, min_, max_, self.num_type)
                    for r in self.ranges])


class Int8(Baseint):
    """Implements rfc6020 section-9.2."""
    min = -128
    max = 127


class Int16(Baseint):
    """Implements rfc6020 section-9.2."""
    min = -32768
    max = 32767


class Int32(Baseint):
    """Implements rfc6020 section-9.2."""
    min = -2147483648
    max = 2147483647


class Int64(Baseint):
    """Implements rfc6020 section-9.2."""
    min = Decimal('-9223372036854775808')
    max = 9223372036854775807


class Uint8(Baseint):
    """Implements rfc6020 section-9.2."""
    min = 0
    max = 255


class Uint16(Baseint):
    """Implements rfc6020 section-9.2."""
    min = 0
    max = 65535


class Uint32(Baseint):
    """Implements rfc6020 section-9.2."""
    min = 0
    max = 4294967295


class Uint64(Baseint):
    """Implements rfc6020 section-9.2."""
    num_type = long
    min = 0
    max = 18446744073709551615


class Decimal64(Baseint):
    """Implements rfc6020 section-9.3."""
    num_type = Decimal

    fraction_map = {
        "1": (Decimal('-922337203685477580.8'), Decimal('922337203685477580.7')),
        "2": (Decimal('-92233720368547758.08'), Decimal('92233720368547758.07')),
        "3": (Decimal('-9223372036854775.808'), Decimal('9223372036854775.807')),
        "4": (Decimal('-922337203685477.5808'), Decimal('922337203685477.5807')),
        "5": (Decimal('-92233720368547.75808'), Decimal('92233720368547.75807')),
        "6": (Decimal('-9223372036854.775808'), Decimal('9223372036854.775807')),
        "7": (Decimal('-922337203685.4775808'), Decimal('922337203685.4775807')),
        "8": (Decimal('-92233720368.54775808'), Decimal('92233720368.54775807')),
        "9": (Decimal('-9223372036.854775808'), Decimal('9223372036.854775807')),
        "10": (Decimal('-922337203.6854775808'), Decimal('922337203.6854775807')),
        "11": (Decimal('-92233720.36854775808'), Decimal('92233720.36854775807')),
        "12": (Decimal('-9223372.036854775808'), Decimal('9223372.036854775807')),
        "13": (Decimal('-922337.2036854775808'), Decimal('922337.2036854775807')),
        "14": (Decimal('-92233.72036854775808'), Decimal('92233.72036854775807')),
        "15": (Decimal('-9223.372036854775808'), Decimal('9223.372036854775807')),
        "16": (Decimal('-922.3372036854775808'), Decimal('922.3372036854775807')),
        "17": (Decimal('-92.23372036854775808'), Decimal('92.23372036854775807')),
        "18": (Decimal('-9.223372036854775808'), Decimal('9.223372036854775807')),
    }

    def __init__(self, fraction_digits=0, range_=None, _meta=None):
        try:
            self.min, self.max = self.fraction_map[str(fraction_digits)]
        except KeyError:
            raise ValueError("Wrong value ({}) for fraction_digits. Valid values are 1..18".format(
                fraction_digits))
        super().__init__(_meta=_meta, range_=range_)

    def _verify_value(self, value):
        value = Decimal(value)
        return super()._verify_value(value)


class String(YangType):
    """Implements rfc6020 section-9.4."""

    def __init__(self, _meta=None, pattern=None, length=None):
        super().__init__(_meta)
        self.pattern = pattern
        self.length = length

        self.ranges = ["0..18446744073709551615"]
        if length is not None:
            try:
                min_, max_ = self.ranges[0].split("..")
                min_ = int(min_)
                max_ = int(max_)
                self.ranges = [length]
            except:
                # If we get here it means we can't use length as new min|max
                self.ranges.append(length)

        if pattern is not None:
            self.patterns = [pattern]
        else:
            self.patterns = []

    def _verify_value(self, value):
        min_, max_ = self.ranges[0].split("..")

        if not isinstance(value, basestring):
            return False

        if not all([value_in_range(r, len(value), min_, max_)
                    for r in self.ranges]):
            return False

        if not all([value_in_pattern(p, value)
                    for p in self.patterns]):
            return False

        return True


class Boolean(YangType):
    """Implements rfc6020 section-9.5."""

    def _verify_value(self, value):
        if isinstance(value, basestring):
            if value == "true":
                value = True
            elif value == "false":
                value = False
        elif not isinstance(value, (basestring, bool)):
            return False
        return value in [True, False]

    def __str__(self):
        """Lexical form"""
        return "true" if self.value else "false"


class Enumeration(YangType):
    """
    Implements rfc6020 section-9.6.

    Note: Do not mistake what we call here value (the real value for the object) and
    what the value of an enum is (which we store under `self.enum_value` which
    is an optional statement.
    """

    def __init__(self, enum, _meta=None):
        super().__init__(_meta)
        self.enum = enum
        self._meta["enum"] = None
        self.enum_value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value in self.enum.keys():
            self._value = value

            if "value" in self.enum[value].keys():
                self.enum_value = int(self.enum[value]['value'])
            else:
                self.enum_value = sorted(self.enum.keys()).index(value)
        else:
            error_msg = "Wrong description for enumeration: {}\n.Accepted values are {}"
            raise ValueError(error_msg.format(value, self.enum.keys()))

    def data_representation(self):
        """Returns a dict with information about the model itself."""
        model = super().data_representation()
        model["enum_value"] = self.enum_value
        return model


class Bits(YangType):
    """
    Implements rfc6020 section-9.7.

    TBD
    """
    pass


class Binary(YangType):
    """
    Implements rfc6020 section-9.8.

    TBD
    """
    pass


class Leafref(String):
    """
    Implements rfc6020 section-9.9.


    TBD Use path to validate when importing/exporting from/to JSON/XML
    """

    def __init__(self, path, _meta=None):
        super().__init__(_meta)
        self.path = path

    def _verify_value(self, value):
        return True


class Identityref(String):
    """
    Implements rfc6020 section-9.10.


    TBD Use path to validate when importing/exporting from/to JSON/XML
    """

    def __init__(self, base, _meta=None):
        super().__init__(_meta)
        self.base = base

    def _verify_value(self, value):
        if not isinstance(value, Identity):
            return False
        else:
            return self.base == value.base


class Empty(YangType):
    """
    Implements rfc6020 section-9.11.

    TBD
    """
    pass


class Union(YangType):
    """
    Implements rfc6020 section-9.12.

    TBD
    """
    def __init__(self, type_, _meta=None):
        super().__init__(_meta)
        self._value = None

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        valid = False
        for t in self.types:
            try:
                t(value)
                self._value = t
                valid = True
            except ValueError:
                pass
        if not valid:
            raise ValueError("Value '{}' is not valid for any of the types '{}'".format(value,
                                                                                        self.types))


class InstanceIdentifier(YangType):
    """
    Implements rfc6020 section-9.13.

    TBD
    """
    pass


class Identity(YangType):

    def __init__(self, value, base=None, description="", _meta=None):
        super().__init__(_meta)
        self.base = base
        self.description = description
        self.value = value

    def _verify_value(self, value):
        return True


class ListElement(BaseBinding):
    def __init__(self, parent):
        super().__init__(parent._meta)
        self.type = parent.__class__.__name__

        self._meta = copy.deepcopy(parent._meta)

        attrs = dir(parent)
        for a in attrs:
            attr = getattr(parent, a)
            if issubclass(attr.__class__, BaseBinding) or issubclass(attr.__class__, YangType):
                setattr(self, a, copy.deepcopy(attr))


class List(BaseBinding):

    def __init__(self, _meta=None):
        super().__init__(_meta)
        self._value = {}

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        raise ValueError("You can't set a value to a list. Use new_element method")

    def new_element(self, name):
        """Force the ceration of a new element."""
        self._value[name] = ListElement(self)
        return self._value[name]

    def get_element(self, name):
        """Returns an existing element if it exists or create a new one."""
        if name not in self._value:
            return self.new_element(name)
        else:
            return self._value[name]

    def model_represenation(self):
        return ListElement(self).model_represenation()

    def data_representation(self):
        res = {}
        res["_meta"] = copy.deepcopy(self._meta) or {}
        res["list"] = {}

        for element, data in self.items():
            res["list"][element] = data.data_representation()
            res["list"][element]["_meta"] = copy.deepcopy(self._meta) or {}

        return res

    def __contains__(self, key):
        return key in self._value

    def __getitem__(self, name):
        return self._value.__getitem__(name)

    def __delitem__(self, name):
        self._value.__delitem__(name)

    def __setitem__(self, name, value):
        if not isinstance(value, self.type):
            raise AttributeError("{} is not of type {}".format(value, self.type))
        self._value.__setitem__(name, value)

    def __iter__(self):
        return self._value.__iter__()

    def __len__(self):
        return len(self._value)

    def items(self):
        return self._value.items()

    def keys(self):
        return self._value.keys()

    def values(self):
        return self._value.values()


class BaseTypeDef(YangType):
    pass


class Feature(YangType):

    def __init__(self, name, _meta=None):
        super().__init__(_meta)
        self._value = name


class LeafList(YangType):

    def __init__(self, type, _meta=None):
        super().__init__(_meta)
        self._value = type
