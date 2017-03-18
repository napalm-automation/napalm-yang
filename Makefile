PYBINDPLUGIN=$(shell /usr/bin/env python -c 'import pyangbind; import os; print "%s/plugin" % os.path.dirname(pyangbind.__file__)')

MODELS_PATH=napalm_yang/models

YANG_OC=yang_oc/release/models
YANG_IETF=yang_ietf/standard/ietf
YANG_NAPALM=yang_napalm

PYANGBING=pyang --plugindir $(PYBINDPLUGIN) --path $(YANG_OC) --path $(YANG_IETF) --split-class-dir=$(MODELS_PATH) -f pybind


clean:
	find $(MODELS_PATH)/* -d -type d -exec rm -rf '{}' \;

.PHONY: models
models:
	$(PYANGBING) \
		$(YANG_OC)/bgp/*.yang \
		$(YANG_OC)/interfaces/*.yang \
		$(YANG_OC)/platform/*.yang \
		$(YANG_OC)/vlan/*.yang \
		$(YANG_NAPALM)/interfaces/*.yang

.PHONY: submodule
submodule:
	git submodule update --init --recursive

.PHONY: tests
tests:
	python test.py
	py.test
