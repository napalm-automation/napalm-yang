"""Yang Types"""
from builtins import super
import copy

from napalm_yang.yang_base import YangType, BaseBinding


class Identity(YangType):

    def __init__(self, value, base=None, description="", _meta=None):
        super().__init__(_meta)
        self.base = base
        self.description = description
        self.value = value


class Boolean(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value in [True, False]:
            self._value = value
        else:
            raise ValueError("Wrong value for boolean: {}".format(value))


class Baseint(YangType):
    min = 0
    max = 0

    def __init__(self, range=None, _meta=None):
        super().__init__(_meta)
        self.range = range

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self.min <= value <= self.max and not isinstance(value, bool):
            self._value = value
        else:
            raise ValueError("Wrong value for {}: {}".format(value, self.__class__.__name__))


class Int8(Baseint):
    min = -128
    max = 127


class Int16(Baseint):
    min = -32768
    max = 32767


class Int32(Baseint):
    min = -2147483648
    max = 2147483647


class Int64(Baseint):
    min = -9223372036854775808
    max = 9223372036854775807


class Uint8(Baseint):
    min = 0
    max = 255


class Uint16(Baseint):
    min = 0
    max = 65535


class Uint32(Baseint):
    min = 0
    max = 4294967295


class Uint64(Baseint):
    min = 0
    max = 18446744073709551615


class Counter32(Uint32):
    pass


class Counter64(Uint64):
    pass


class Enumeration(YangType):

    def __init__(self, enum, _meta=None):
        super().__init__(_meta)
        self.enum_map = enum
        self._meta["enum"] = None

    @property
    def enum(self):
        return self._meta["enum"]

    @enum.setter
    def enum(self, enum):
        raise AttributeError("Can't change enumeration once it's been initialized")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value in self.enum_map.keys():
            self._value = value

            if "value" in self.enum_map[value].keys():
                self._meta["enum_value"] = int(self.enum_map[value]['value'])
            else:
                self._meta["enum_value"] = sorted(self.enum_map.keys()).index(value)
        else:
            error_msg = "Wrong description for enumeration: {}\n.Accepted values are {}"
            raise ValueError(error_msg.format(value, self.enum_map.keys()))

    def __str__(self):
        return "{}, {}".format(self.enum, self.value)


class String(YangType):

    def __init__(self, _meta=None, pattern=None):
        super().__init__(_meta)

        self.pattern = pattern

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, basestring):
            self._value = value
        else:
            raise ValueError("Wrong value for string: {}".format(value))


class Identityref(String):

    def __init__(self, base, _meta=None):
        super().__init__(_meta)
        self.base = base

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Leafref(String):

    def __init__(self, path, _meta=None):
        super().__init__(_meta)
        self.path = path

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


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

    def new_element(self, name):
        self._value[name] = ListElement(self)
        return self._value[name]

    def data_representation(self):
        res = {}
        res["_meta"] = copy.deepcopy(self._meta) or {}
        res["list"] = {}

        for element, data in self.items():
            res["list"][element] = data.data_representation()
            res["list"][element]["_meta"] = copy.deepcopy(self._meta) or {}

        return res

    def __getitem__(self, name):
        return self._value.__getitem__(name)

    def __delitem__(self, name):
        self._value.__delitem__(name)

    def __setitem__(self, name, value):
        if not isinstance(value, self.type):
            raise AttributeError("{} is not of type {}".format(value, self.type))
        self._value.__setitem__(name, value)

    def __contains__(self, item):
        return self._value.__contains__(item)

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


class Timeticks(Uint32):
    pass


class DateAndTime(YangType):
    pass
