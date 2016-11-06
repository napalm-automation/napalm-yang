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

    def __init__(self, description, options):
        self.map = options['enum']
        if description in options['enum'].keys():
            self.description = description
        else:
            error_msg = "Wrong description for enumeration: {}\n.Accepted values are {}"
            raise ValueError(error_msg.format(description, options['enum'].keys()))

    @property
    def value(self):
        return self.map[self.description]


class string(YangType):
    # TODO ensure py3 compatibility

    def __init__(self, value, options=None):
        if isinstance(value, basestring):
            self.value = value
        else:
            raise ValueError("Wrong value for string: {}".format(value))


class leafref(string):

    def __init__(self, value, options=None):
        super().__init__(value, options)
