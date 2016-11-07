"""Base classes for Yang Types and bindings."""


class BaseBinding(object):
    """All YANG bindings inherit from this class."""
    pass


class YangType(object):
    """All YANG types inherit from this class."""

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.__str__())

    def __str__(self):
        return "{}".format(self.value)


def attach_childs(cls, ns):
    for k, v in cls.container.items():
        setattr(cls, k, ns[v]())
