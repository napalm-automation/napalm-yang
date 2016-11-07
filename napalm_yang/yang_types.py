"""Yang Types"""
from builtins import super

from yang_base import YangType


class boolean(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value in [True, False]:
            self._value = value
        else:
            raise ValueError("Wrong value for boolean: {}".format(value))


class counter32(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if 0 <= value <= 4294967295 and not isinstance(value, bool):
            self._value = value
        else:
            raise ValueError("Wrong value for counter32: {}".format(value))


class counter64(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if 0 <= value <= 18446744073709551615 and not isinstance(value, bool):
            self._value = value
        else:
            raise ValueError("Wrong value for counter64: {}".format(value))


class enumeration(YangType):

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


class string(YangType):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if isinstance(value, basestring):
            self._value = value
        else:
            raise ValueError("Wrong value for string: {}".format(value))


class leafref(string):

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
