.. _parsers:

Parsers
=======

Parsers are responsible for mapping native configuration/data to a YANG model.

Processing data
---------------

The first thing you have to know is what type of data you are dealing with and then select the appropiate parser. Each one initializes the data and makes it available in similar ways but you have to be aware of the particularities of each one.

You can select the parser with the metadata field:

.. code-block:: yaml

    ---
    metadata:
        processor: TextTree
        execute:
            - method: cli
              kwargs:
                  commands: ["show running-config all"]

That block not only specifies which parser to use but how to retrieve the data necessary for the parser to
operate for that particular model.

Available processors are:

.. toctree::
   :maxdepth: 1

   JSONParser
   XMLParser
   TextTree

Rule Directives
---------------

.. include:: dynamic_directives.rst

Keys
----

When a list is traversed you will always have available a key with name ``$(attribute)_key``. In
addition, you will have ``parent_key`` as the key of the immediate parent object. `Example <https://github.com/napalm-automation/napalm-yang/blob/develop/napalm_yang/mappings/eos/parsers/config/openconfig-interfaces/interfaces.yaml#L63>`_.

Bookmarks
---------

Bookmarks are points of interest in the configuration. Usually, you will be gathering blocks of
configurations and parsing on those as you progress. However, sometimes the data you need is somewhere else.
For those cases you can use the bookmarks within the ``from`` field to pick the correct block of
configuration.

Bookmarks are created automatically according to these rules:

* At the begining of each model a bookmark of name ``root_$first_attribute_name`` will point to the list of data that the parser requires. `Example <https://github.com/napalm-automation/napalm-yang/blob/develop/napalm_yang/mappings/eos/parsers/config/openconfig-interfaces/interfaces.yaml#L14>`_
* When a container is traversed, a bookmark will be created with name ``$attribure_name``
* When a list is traveresed, each element of the list will have its own bookmark with name ``$attribute_name.$key``.

``extra_vars``
--------------

The ``regexp`` directive lets you capture any arbitary amount of information you want. All captured
groups will be avaible to you inside the ``extra_vars.$attribute`` (``$attribute`` is the attribute where the
additional information was captured). `Example <https://github.com/napalm-automation/napalm-yang/blob/develop/napalm_yang/mappings/eos/parsers/config/openconfig-if-ip/ipv4.yaml#L27>`_.

Examples
--------

.. toctree::
   :maxdepth: 1

   examples_list
   examples_leaf
