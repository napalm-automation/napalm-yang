"""Base classes for Yang Types and bindings."""
import text_helpers
import copy

import napalm_yang
from napalm_yang import parsers

import os


def model_to_text(name, model, indentation="", augment=""):
    text = ""
    meta = model["_meta"]
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    text += "{}+-- {} {}{}\n".format(indentation, mode, name, key)
    text += augment
    indentation = indentation + "|  "

    for attr, data in model.items():
        if attr == "_meta":
            continue

        sm = data.get("_meta")
        if attr in model["_meta"]["augments"].keys():
            when = model["_meta"]["augments"][attr].when or "always"
            augment = "{}|    \ [augment] {} - when: {}\n".format(
                indentation,
                model["_meta"]["augments"][attr].prefix,
                when,
            )
        else:
            augment = ""
        if sm["nested"]:
            text += model_to_text(attr, data, indentation, augment)
        else:
            mandatory = "" if sm["mandatory"] else "?"
            body = "{}+-- {} {}{}".format(indentation, mode, attr, mandatory)
            spacing = " " * (60 - len(body))
            text += "{}{}{}\n".format(body, spacing, sm["type"])
            text += augment

    return text


def data_to_text(name, data, indentation=""):
    text = ""
    try:
        meta = data["_meta"]
    except Exception:
        print(name, data)
        raise
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    text += "{}+-- {} {}{}\n".format(indentation, mode, name, key)
    indentation = indentation + "|  "

    for attr, attr_data in data.items():
        if attr == "_meta":
            continue
        elif attr == "list":
            for e, d in attr_data.items():
                text += data_to_text(e, d, indentation)
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
            text += "{}{}{}\n".format(body, spacing, value)
        else:
            text += data_to_text(attr, attr_data, indentation)

    return text


class BaseBinding(object):
    """All YANG bindings inherit from this class."""
    __prefix__ = None

    def __init__(self, _meta=None):
        self._meta = {
            "config": False,
            "augments": {},
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

    def __eq__(self, other):
        return self.diff(other) == {}

    def augment_model(self, augment):
        self_attr = self
        for p in augment.path:
            attr = p.split(":")

            if len(attr) == 1:
                attr = attr[0]
                prefix = self_attr.prefix
            else:
                prefix, attr = attr

            self_attr = getattr(self_attr, text_helpers.safe_attr_name(attr))

            if not self_attr.prefix == prefix:
                return

        self_attr.add_model(augment, is_augment=True)

    def add_model(self, model, is_augment=False):
        """Merges model into existing object."""
        for k, v in model.items():
            setattr(self, k, v)

            if is_augment:
                self._meta["augments"][k] = model

        if not is_augment:
            if model._meta["config"]:
                self._meta["config"] = True

    @property
    def prefix(self):
        return self.__prefix__

    def model_to_dict(self):
        """Returns a dict with information about the model itself."""
        result = {}
        result["_meta"] = copy.deepcopy(self._meta)
        result["_meta"]["nested"] = True

        for attr_name, attr in self.items():
            result[attr_name] = attr.model_to_dict()

        return result

    def data_to_dict(self):
        """Returns a dict with information about the data (if any) contained in the model."""
        result = {}

        for attr_name, attr in self.items():
            res = attr.data_to_dict()
            if res:
                result[attr_name] = res

        if result:
            result["_meta"] = copy.deepcopy(self._meta)
        return result

    def model_to_text(self, indentation=""):
        return model_to_text(self.__class__.__name__, self.model_to_dict())

    def data_to_text(self, indentation=""):
        return data_to_text(self.__class__.__name__, self.data_to_dict())

    def diff(self, other):
        result = {}

        for attr_name, attr in self.items():
            res = attr.diff(getattr(other, attr_name))
            if res:
                result[attr_name] = res

        return result


        if os.path.exists(full_path):
            return full_path
        else:
            raise IOError("Couldn't find file with mocked data: {}".format(full_path))

    def get_config(self, device):
        for k, v in self.items():
            parsers.parse(device, k, v)


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

    def __nonzero__(self):
        return bool(self.value)

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

    def diff(self, other):
        if self.value != other.value:
            return {"mine": self.value, "other": other.value}
        else:
            return {}

    def model_to_dict(self):
        """Returns a dict with information about the model itself."""
        return {
            "_meta": {
                "type": self.__class__.__name__,
                "mandatory": self._meta["mandatory"],
                "nested": False,
            }
        }

    def data_to_dict(self):
        """Returns a dict with information about the data (if any) contained in the model."""
        res = {"value": self.value}
        res["_meta"] = copy.deepcopy(self._meta)
        res["_meta"]["type"] = self.__class__.__name__
        res["_meta"]["nested"] = False
        if res["value"] or res["_meta"]["mandatory"]:
            return res
        else:
            return {}


class Extension(YangType):
    """A base class to create extensions"""
    # TBD
    pass


class BaseAugment(BaseBinding):
    """A base class for augments."""
    when = None
    path = None

    def __call__(self):
        module, model = self.path[0].split(":")

        module = getattr(napalm_yang, text_helpers.safe_attr_name(module))
        model = getattr(module, text_helpers.safe_attr_name(model))
        model.augment(self)


def model_factory(model):
    class ModelFactory(model):
        augments = []

        def augment(self, augment):
            self.augments.append(augment)

        def __call__(self):
            m = model()
            for augment in self.augments:
                m.augment_model(augment)
            return m

    return ModelFactory()
