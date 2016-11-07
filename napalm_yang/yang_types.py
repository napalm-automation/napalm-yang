"""Yang Types"""
from builtins import super

from yang_base import YangType


class boolean(YangType):

    def __init__(self, value, options=None):
        if value in [True, False]:
            self.value = value
        else:
            raise ValueError("Wrong value for boolean: {}".format(value))


class counter32(YangType):

    def __init__(self, value, options=None):
        if 0 <= value <= 4294967295:
            self.value = value
        else:
            raise ValueError("Wrong value for counter32: {}".format(value))


class counter64(YangType):

    def __init__(self, value, options=None):
        if 0 <= value <= 18446744073709551615:
            self.value = value
        else:
            raise ValueError("Wrong value for counter64: {}".format(value))


class enumeration(YangType):

    def __init__(self, options):
        self._enum = None
        self.map = options

    @property
    def enum(self):
        return self._enum

    @enum.setter
    def enum(self, value):
        if value in self.map.keys():
            self._enum = value
        else:
            error_msg = "Wrong description for enumeration: {}\n.Accepted values are {}"
            raise ValueError(error_msg.format(value, self.map.keys()))

    @property
    def value(self):
        try:
            return int(self.map[self._enum]['value']['value'])
        except KeyError:
            return None


class string(YangType):

    def __init__(self, value, options=None):
        if isinstance(value, basestring):
            self.value = value
        else:
            raise ValueError("Wrong value for string: {}".format(value))


class leafref(string):

    def __init__(self, value, options=None):
        super().__init__(value, options)
