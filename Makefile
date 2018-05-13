PYBINDPLUGIN=$(shell /usr/bin/env python -c 'import pyangbind; import os; print("{}/plugin".format(os.path.dirname(pyangbind.__file__)))')

MODELS_PATH=napalm_yang/models

YANG_OC=yang_oc/release/models
YANG_IETF=yang_ietf/standard/ietf
YANG_NAPALM=yang_napalm

PYANGBIND=pyang --plugindir $(PYBINDPLUGIN) -f pybind --lax-quote-checks


clean:
	find $(MODELS_PATH)/* -d -type d -exec rm -rf '{}' \;

.PHONY: openconfig_tree
openconfig_tree:
	pyang -f tree \
		--path $(YANG_OC) \
		-f tree \
		$(YANG_OC)/network-instance/openconfig-network-instance.yang

.PHONY: models_openconfig
models_openconfig:
	rm -rf $(MODELS_PATH)/openconfig/
	$(PYANGBIND) \
		--path $(YANG_OC) \
		--split-class-dir=$(MODELS_PATH)/openconfig/ \
		$(YANG_OC)/network-instance/openconfig-network-instance.yang \
		$(YANG_OC)/interfaces/*.yang \
		$(YANG_OC)/platform/*.yang \
		$(YANG_OC)/vlan/*.yang \
		$(YANG_OC)/system/*.yang \
		$(YANG_NAPALM)/interfaces/*.yang

# .PHONY: models_ietf
# models_ietf:
#     rm -rf $(MODELS_PATH)/ietf/
#     $(PYANGBIND) \
#         --path $(YANG_IETF)/RFC \
#         --path $(YANG_IETF)/DRAFT \
#         --split-class-dir=$(MODELS_PATH)/ietf/ \
#         $(YANG_IETF)/RFC/ietf-yang-types.yang \
#         $(YANG_IETF)/RFC/ietf-interfaces@2014-05-08.yang \
#         $(YANG_IETF)/RFC/ietf-routing@2016-11-04.yang \
#         $(YANG_IETF)/DRAFT/ietf-pim*

.PHONY: submodule
submodule:
	git submodule update --init --recursive

.PHONY: templates
templates:
	rm -rf napalm_yang/mappings/dummy/
	python generate_templates.py

.PHONY: tests
tests:
	pytest

.PHONY: test_black
test_black:
	find . \
		-not -path "./.tox*" \
		-not -path "./napalm_yang/models*" \
		-not -path "./napalm_yang/mappings*" \
		-not -path "./yang_ietf*" \
		-not -path "./yang_oc*" \
		-name "*.py" \
		-exec black --check {} \+

.PHONY: test_sphinx
test_sphinx:
	sphinx-build -W -b html -d docs/_build/doctrees docs docs/_build/html

.PHONY: test_pylama
test_pylama:
	pylama .
