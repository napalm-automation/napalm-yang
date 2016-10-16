"""Yang Types"""


class Base:
    pass


class YangType:

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.__str__())

    def __str__(self):
        return "{}".format(self.value)


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
