from pyangbind.lib.serialise import pybindJSONDecoder
from napalm_yang.parser import Parser


def model_to_dict(model):
    def get_key(key, model, parent_defining_module):
        key = "{} {}".format(key, "[rw]" if model._is_config else "[ro]")

        if parent_defining_module != model._defining_module:
            key = "{}:{}".format(model._defining_module, key)
        return key

    if model._yang_type in ("container", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model}
    elif model._yang_type in ("list", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model._contained_class()}
    else:
        return model._yang_type


class Root(object):
    _yang_type = "container"
    _defining_module = ""

    def __init__(self):
        self._elements = {}

    def elements(self):
        return self._elements

    def add_model(self, model):
        try:
            model = model()
        except Exception:
            pass

        for k, v in model:
            self._elements[k] = v
            setattr(self, k, v)

    def get(self, filter=False):
        result = {}

        for k, v in self.elements().items():
            intermediate = v.get(filter=filter)
            if intermediate:
                result[k] = intermediate

        return result

    def __iter__(self):
        for k, v in self.elements().items():
            yield k, v

    def load_dict(self, data, overwrite=False):
        for k, v in data.items():
            if k not in self._elements.keys():
                raise AttributeError("Model {} is not loaded".format(k))
            attr = getattr(self, k)
            pybindJSONDecoder.load_json(v, None, None, obj=attr, overwrite=overwrite)

    def parse(self, profile, config):
        for k, v in self:
            parser = Parser(v, profile, config)
            parser.parse()
