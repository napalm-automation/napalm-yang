"""Base classes for Yang Types and bindings."""

import copy


class BaseBinding(object):
    """All YANG bindings inherit from this class."""

    def __init__(self, _meta=None):
        self._meta = {
            "config": False,
        }
        if _meta:
            self._meta.update(_meta)

    def model_represenation(self):
        attrs = dir(self)

        result = {}
        result["_meta"] = copy.deepcopy(self._meta)
        result["_meta"]["nested"] = True

        for a in attrs:
            attr = getattr(self, a)
            if issubclass(attr.__class__, BaseBinding) or issubclass(attr.__class__, YangType):
                result[a] = attr.model_represenation()

        return result

    def data_representation(self):
        attrs = dir(self)

        result = {}

        for a in attrs:
            attr = getattr(self, a)
            if issubclass(attr.__class__, BaseBinding) or issubclass(attr.__class__, YangType):
                res = attr.data_representation()
                if res:
                    result[a] = res

        if result:
            result["_meta"] = copy.deepcopy(self._meta)
        return result


class YangType(object):
    """All YANG types inherit from this class."""

    def __init__(self, _meta=None):
        self._value = None

        self._meta = {
            "config": False,
            "mandatory": False
        }
        if _meta:
            self._meta.update(_meta)

    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.__str__())

    def __str__(self):
        return "{}".format(self.value)

    def __call__(self, value=None):
        if value is not None:
            self.value = value
        else:
            return self.value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def model_represenation(self):
        return {
            "_meta": {
                "type": self.__class__.__name__,
                "mandatory": self._meta["mandatory"],
                "nested": False,
            }
        }

    def data_representation(self):
        res = {"value": self.value}
        res["_meta"] = copy.deepcopy(self._meta)
        res["_meta"]["type"] = self.__class__.__name__
        res["_meta"]["nested"] = False
        if res["value"] is not None or res["_meta"]["mandatory"]:
            return res
        else:
            return {}


class Extension(YangType):
    """An base class to create extensions"""
    # TBD
    pass
