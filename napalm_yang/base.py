from pyangbind.lib.serialise import pybindJSONDecoder

from napalm_yang.parser import Parser
from napalm_yang.translator import Translator


class Root(object):
    _yang_type = "container"
    _defining_module = ""

    def __init__(self):
        self._elements = {}

    def elements(self):
        return self._elements
    "base",

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

    def parse_config(self, device=None, profile=None, config=None):
        for k, v in self:
            parser = Parser(v, device=device, profile=profile, config=config, is_config=True)
            parser.parse()

    def translate_config(self, profile, merge=None, replace=None):
        result = []
        for k, v in self:
            other_merge = getattr(merge, k) if merge else None
            other_replace = getattr(replace, k) if replace else None
            translator = Translator(v, profile, merge=other_merge, replace=other_replace)
            result.append(translator.translate())

        return "\n".join(result)
