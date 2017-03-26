[![PyPI](https://img.shields.io/pypi/v/napalm-yang.svg)](https://pypi.python.org/pypi/napalm-yang)

[![PyPI](https://img.shields.io/pypi/dm/napalm-yang.svg)](https://pypi.python.org/pypi/napalm-yang)

[![Build Status](https://travis-ci.org/napalm-automation/napalm-yang.svg?branch=master)](https://travis-ci.org/napalm-automation/napalm-yang)

[![Coverage Status](https://coveralls.io/repos/github/napalm-automation/napalm-yang/badge.svg?branch=develop)](https://coveralls.io/github/napalm-automation/napalm-yang?branch=develop)

Generating the models
=====================

    make clean     # Remove automatically generated models
	make submodule # Synch git submodules (IETF/OC models)
	make models    # Generating supported models
    make tests     # Run tests


Structure
=========

	├── napalm_yang                    # napalm_yang library to be imported by napalm_base
	│   ├── __init__.py                # Main entry point for all the imports, provides namespace
	│   ├── models                     # OC/IETF models generated automagically
	│   ├── yang_base.py               # Base classes to use for bindings and data types
	│   ├── yang_builtin_types.py      # YANG builtin types
	├── pyang_plugin                   # pyang plugin to generate bindings
	├── test                           # Tests
	├── yang_ietf                      # Git submodule with IETF models
	└── yang_oc                        # Git submodule with OC models
