MODELS_PATH=napalm_yang/models

YANG_OC=yang_oc/release/models
YANG_IETF=yang_ietf/standard/ietf

PYANG=pyang -V --napalm-path=$(MODELS_PATH) --plugindir pyang_plugin --format napalm --path $(YANG_OC)

clean:
	find $(MODELS_PATH)/* -d -type d -exec rm -rf '{}' \;

.PHONY: models
models: clean
	$(PYANG) --napalm-module=ietf $(YANG_IETF)/RFC/ietf-inet-types.yang
	$(PYANG) --napalm-module=ietf $(YANG_IETF)/RFC/ietf-interfaces@2014-05-08.yang
	$(PYANG) --napalm-module=ietf $(YANG_IETF)/RFC/ietf-yang-types@2013-07-15.yang
	$(PYANG) --napalm-module=acl $(YANG_OC)/acl/*.yang
	$(PYANG) --napalm-module=interfaces $(YANG_OC)/interfaces/openconfig-interfaces.yang
	$(PYANG) --napalm-module=openconfig_extensions $(YANG_OC)/openconfig-extensions.yang

.PHONY: submodule
submodule:
	git submodule update --init --recursive

.PHONY: tests
tests:
	python test.py
	py.test
