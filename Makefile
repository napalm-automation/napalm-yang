MODELS_PATH=napalm_yang/models
PYANG=pyang -V --plugindir pyang_plugin --format napalm --path yang_models/public/release/models/ --napalm-path=$(MODELS_PATH)

clean:
	find $(MODELS_PATH)/* -d -type d -exec rm -rf '{}' \;

.PHONY: models
models:
	# $(PYANG) yang_models/public/release/models/acl/openconfig-acl.yang
	$(PYANG) yang_models/public/release/models/interfaces/openconfig-interfaces.yang
