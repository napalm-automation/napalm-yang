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

    def items(self):
        """Allows the user to iterate the container as if it was a dictionary."""
        attrs = dir(self)
        for a in attrs:
            attr = getattr(self, a)
            if issubclass(attr.__class__, BaseBinding) or issubclass(attr.__class__, YangType):
                yield a, attr

    def model_represenation(self):
        """Returns a dict with information about the model itself."""
        result = {}
        result["_meta"] = copy.deepcopy(self._meta)
        result["_meta"]["nested"] = True

        for attr_name, attr in self.items():
            result[attr_name] = attr.model_represenation()

        return result

    def data_representation(self):
        """Returns a dict with information about the data (if any) contained in the model."""
        result = {}

        for attr_name, attr in self.items():
            res = attr.data_representation()
            if res:
                result[attr_name] = res

        if result:
            result["_meta"] = copy.deepcopy(self._meta)
        return result


class YangType(object):
    """
    All YANG types inherit from this class.

    Notes:
    * Yang types are callable. When a parameter is passed, the type will set the parameter
      as its value. Without a paremeter it will return the value.
    * The value is stored in the attribute `_value` but it's set and accessed via the `value`
      property.
    * Most types inheriting from this class will mostly have to care about implementing
    the `_verify_value` class.
    """

    def __init__(self, _meta=None):
        # Actual value of the type, accessed via the value property
        self._value = None

        # Meta information about the type as defined by the model
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

    def _verify_value(self, value):
        """
        Each type has to implement this method. The method returns whether the value is
        correct for the type.
        """
        raise NotImplementedError("{} is missing the implementation of this method".format(
                                                                    self.__class__.__name__))

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._verify_value(value):
            self._value = value
        else:
            raise ValueError("Wrong value for {}: {}".format(value, self.__class__.__name__))

    def model_represenation(self):
        """Returns a dict with information about the model itself."""
        return {
            "_meta": {
                "type": self.__class__.__name__,
                "mandatory": self._meta["mandatory"],
                "nested": False,
            }
        }

    def data_representation(self):
        """Returns a dict with information about the data (if any) contained in the model."""
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
