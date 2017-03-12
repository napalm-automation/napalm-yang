"""Base classes for Yang Types and bindings."""
import text_helpers

import napalm_yang
from napalm_yang import framework

import weakref


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
            if a == "_parent":
                continue

            attr = getattr(self, a)
            if issubclass(attr.__class__, BaseBinding) or issubclass(attr.__class__, YangType):
                yield a, attr

    def update_parent_refs(self):
        for k, v in self.items():
            v._parent = weakref.ref(self)
            v.update_parent_refs()

    def __eq__(self, other):
        return self.diff(other) == {}

    def __ne__(self, other):
        return not self.__eq__(other)

    def __setattr__(self, name, value):
        try:
            obj = getattr(self, name)
        except Exception:
            obj = None

        if name in self.__dict__:
            obj = getattr(self, name)

            if isinstance(obj, YangType) and isinstance(value, obj.__class__):
                pass
            elif isinstance(obj, YangType):
                obj(value)
                return
        object.__setattr__(self, name, value)

    @property
    def _parent(self):
        try:
            return self._parent_object()
        except AttributeError:
            return None

    @_parent.setter
    def _parent(self, parent):
        self._parent_object = parent

    def augment_model(self, augment):
        self_attr = self
        for p in augment.path:
            attr = p.split(":")

            if len(attr) == 1:
                attr = attr[0]
                yang_prefix = self_attr.yang_prefix
            else:
                yang_prefix, attr = attr

            self_attr = getattr(self_attr, text_helpers.safe_attr_name(attr))

            if not self_attr.yang_prefix == yang_prefix:
                return

        self_attr.add_model(augment, is_augment=True)

    def add_model(self, model, is_augment=False):
        """Merges model into existing object."""
        for k, v in model.items():
            if isinstance(v, YangType):
                v.yang_prefix = model.yang_prefix

            setattr(self, k, v)

            if is_augment:
                self._meta["augments"][k] = model

        if not is_augment:
            if model._meta["config"]:
                self._meta["config"] = True

    @property
    def yang_prefix(self):
        return self.__prefix__

    def model_to_dict(self):
        """Returns a dict with information about the model itself."""
        result = {}

        for attr_name, attr in self.items():
            if isinstance(attr, BaseBinding) or attr_name in self._meta["augments"]:
                key = "{}:{}".format(attr.yang_prefix, attr_name)
            else:
                key = attr_name

            result[key] = attr.model_to_dict()

        return result

    def to_dict(self):
        """Returns a dictionary with the data"""
        result = {}

        for attr_name, attr in self.items():
            res = attr.to_dict()
            if res:
                result[attr_name] = res

        return result

    def diff(self, other):
        result = {}

        for attr_name, attr in self.items():
            res = attr.diff(getattr(other, attr_name))
            if res:
                result[attr_name] = res

        return result

    def get_config(self, device=None, config=None, profile=None):
        profile = profile or device.profile

        if device:
            device.open()

        for k, v in self.items():
            framework.Parser(device, k, v).parse(config, profile)

        if device:
            device.close()

    def translate(self, device, merge=None, replace=None):
        translator = framework.Translator()
        for k, v in self.items():
            translator = framework.Translator(device, k, v, merge, replace,
                                              translator.translation).parse()

        return translator

    def load_dict(self, data):
        for k, v in data.items():
            attr = getattr(self, k)
            attr.load_dict(v)


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

    def update_parent_refs(self):
        pass

    def __eq__(self, other):
        return self.value == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __repr__(self):
        return "{}".format(self.__class__.__name__)

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
        if isinstance(self.value, YangType):
            return self.value.__nonzero__()
        else:
            return self.value is not None and not self._meta["mandatory"]

    def _verify_value(self, value):
        """
        Each type has to implement this method. The method returns whether the value is
        correct for the type.
        """
        raise NotImplementedError("{} is missing the implementation of this method".format(
                                                                    self.__class__.__name__))

    @property
    def _parent(self):
        try:
            return self.parent()
        except AttributeError:
            return None

    @_parent.setter
    def _parent(self, parent):
        self.parent = parent

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value is None or self._verify_value(value):
            self._value = value
        else:
            raise ValueError("Wrong value for {}: {}".format(self.__class__.__name__, value))

    def diff(self, other):
        if self.value != other.value:
            return {"mine": self.value, "other": other.value}
        else:
            return {}

    def model_to_dict(self):
        """Returns a dict with information about the model itself."""
        question = "" if self._meta["mandatory"] else "? "
        return "{}{}".format(question, self.__repr__())

    def to_dict(self):
        if isinstance(self.value, YangType):
            return self.value.to_dict()
        else:
            return self.value

    def load_dict(self, data):
        self(data)


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
