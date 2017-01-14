Generating the models
=====================

	make submodule # Synch git submodules (IETF/OC models)
	make models    # Generating supported models


Structure
=========

	├── napalm_yang                    # napalm_yang library to be imported by napalm_base
	│   ├── __init__.py                # Main entry point for all the imports, provides namespace
	│   ├── models                     # OC/IETF models generated automagically
	│   ├── yang_base.py               # Base classes to use for bindings and data types
	│   ├── yang_types.py              # YANG builtin types
	├── pyang_plugin                   # pyang plugin to generate bindings
	├── test                           # Tests
	├── yang_ietf                      # Git submodule with IETF models
	└── yang_oc                        # Git submodule with OC models
