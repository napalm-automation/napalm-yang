"""Base classes for Yang Types and bindings."""

import copy


def print_model(name, model, indentation=""):
    meta = model["_meta"]
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    print("{}+-- {} {}{}".format(indentation, mode, name, key))
    indentation = indentation + "|  "

    for attr, data in model.items():
        if attr == "_meta":
            continue

        sm = data.get("_meta")
        if sm["nested"]:
            print_model(attr, data, indentation)
        else:
            mandatory = "" if sm["mandatory"] else "?"
            body = "{}+-- {} {}{}".format(indentation, mode, attr, mandatory)
            spacing = " " * (60 - len(body))
            print("{}{}{}".format(body, spacing, sm["type"]))


def print_data(name, data, indentation=""):
    meta = data["_meta"]
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    print("{}+-- {} {}{}".format(indentation, mode, name, key))
    indentation = indentation + "|  "

    for attr, attr_data in data.items():
        if attr == "_meta":
            continue
        elif attr == "list":
            for e, d in attr_data.items():
                print_data(e, d, indentation)
        elif "value" in attr_data.keys():
            sm = attr_data["_meta"]

            if sm["type"] == "Enumeration":
                try:
                    value = "{} ({})".format(attr_data["value"], attr_data["enum_value"])
                except Exception:
                    raise Exception(attr_data)
            else:
                value = attr_data["value"]

            mandatory = "" if sm["mandatory"] else "?"
            body = "{}+-- {} {}{}".format(indentation, mode, attr, mandatory)
            spacing = " " * (60 - len(body))
            print("{}{}{}".format(body, spacing, value))
        else:
            print_data(attr, attr_data, indentation)


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

    def model_representation(self):
        """Returns a dict with information about the model itself."""
        result = {}
        result["_meta"] = copy.deepcopy(self._meta)
        result["_meta"]["nested"] = True

        for attr_name, attr in self.items():
            result[attr_name] = attr.model_representation()

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

    def print_model(self, indentation=""):
        print_model(self.__class__.__name__, self.model_representation())

    def print_data(self, indentation=""):
        print_data(self.__class__.__name__, self.data_representation())


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

    def __call__(self, *args):
        if len(args) == 0:
            return self.value
        elif len(args) == 1:
            self.value = args[0]
        else:
            raise Exception("Too many arguments passed")

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

    def model_representation(self):
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
