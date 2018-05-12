import pytest

import napalm_yang


class Tests(object):

    @pytest.mark.parametrize("module, models", napalm_yang.SUPPORTED_MODELS)
    def test_supported_models(self, module, models):
        obj = getattr(napalm_yang.models, module.replace("-", "_"), None)
        assert obj, "{} not supported"
        assert list(obj._pyangbind_elements.keys()) == models
