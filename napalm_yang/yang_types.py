"""Yang Types"""
from builtins import super

from yang_base import YangType


class Identity(YangType):

    def __init__(self, value, base=None, description="", options=None):
        super().__init__(options)
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

    def __init__(self, options):
        super().__init__(options)
        self._enum = None
        self.options = options

    @property
    def enum(self):
        return self._enum

    @enum.setter
    def enum(self, value):
        if value in self.options.keys():
            self._enum = value
            self._value = self.options[self._enum].get('value', {'value': None})['value']
            self._value = int(self._value) if self._value is not None else None
        else:
            error_msg = "Wrong description for enumeration: {}\n.Accepted values are {}"
            raise ValueError(error_msg.format(value, self.options.keys()))

    @property
    def value(self):
        return self._value

    def __str__(self):
        return "{}, {}".format(self.enum, self.value)


class String(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, basestring):
            self._value = value
        else:
            raise ValueError("Wrong value for string: {}".format(value))


class Leafref(String):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value


class Yang_list(YangType):
    _type = None

    def __init__(self, value=None):
        self._value = value if value else {}
        same_type = all([isinstance(x, self._type) for x in self._value.values()])

        if not same_type:
            raise AttributeError("Some element of {} is not of type {}".format(self._type, value))

    @property
    def value(self):
        return self._value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        raise AttributeError("Type can't be changed once the object is created")

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
