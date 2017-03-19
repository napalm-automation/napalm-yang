PYBINDPLUGIN=$(shell /usr/bin/env python -c 'import pyangbind; import os; print "%s/plugin" % os.path.dirname(pyangbind.__file__)')

MODELS_PATH=napalm_yang/models

YANG_OC=yang_oc/release/models
YANG_IETF=yang_ietf/standard/ietf
YANG_NAPALM=yang_napalm

PYANGBING=pyang --plugindir $(PYBINDPLUGIN) -f pybind


clean:
	find $(MODELS_PATH)/* -d -type d -exec rm -rf '{}' \;

.PHONY: models_openconfig
models_openconfig:
	rm -rf $(MODELS_PATH)/openconfig/
	$(PYANGBING) \
		--path $(YANG_OC) \
		--split-class-dir=$(MODELS_PATH)/openconfig/ \
		$(YANG_OC)/bgp/*.yang \
		$(YANG_OC)/interfaces/*.yang \
		$(YANG_OC)/platform/*.yang \
		$(YANG_OC)/vlan/*.yang \
		$(YANG_NAPALM)/interfaces/*.yang

.PHONY: models_ietf
models_ietf:
	rm -rf $(MODELS_PATH)/ietf/
	$(PYANGBING) \
		--path $(YANG_IETF) \
		--split-class-dir=$(MODELS_PATH)/ietf/ \
		$(YANG_IETF)/DRAFT/ietf-pim*

.PHONY: submodule
submodule:
	git submodule update --init --recursive

.PHONY: tests
tests:
	python test.py
	py.test
