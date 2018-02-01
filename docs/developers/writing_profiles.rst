Writing Profiles
================

As it's been already mentioned, a profile consists of a bunch of YAML files that describe how to map native
configuration and how to translate an object into native configuration. In order to read native
configuration we will use **parsers**. To translate a YANG model into native configuration we will
use **translators**.

Both parsers and translators follow three basic rules:

#. One directory per module.
#. One file per model.
#. Exact same representation of the model inside the file:

For example::

    $ tree napalm_yang/mappings/eos/parsers/config
    napalm_yang/mappings/eos/parsers/config
    ├── napalm-if-ip
    │   └── secondary.yaml
    ├── openconfig-if-ip
    │   └── ipv4.yaml
    ├── openconfig-interfaces
    │   └── interfaces.yaml
    └── openconfig-vlan
        ├── routed-vlan.yaml
        └── vlan.yaml

    4 directories, 5 files
    $ cat napalm_yang/mappings/eos/parsers/config/openconfig-vlan/vlan.yaml
    ---
    metadata:
        (trimmed for brevity)

    vlan:
        (trimmed for brevity)
        config:
            (trimmed for brevity)
            vlan_id:
                (trimmed for brevity)

If we check the content of the file ``vlan.yaml`` we can clearly see two parts:

* **metadata** - This part specifies what parser or translator we want to use. There are several
  options available depending on the type of data we are parsing from or translating to.
  Additionally, we need to provide some options that the parser/translator might need. For example::

    metadata:
        processor: XMLParser
        execute:
            - method: _rpc
              args: []
              kwargs:
                  get: "<get-configuration/>"

In this case we are using the ``XMLParser`` parser. In order to get the data we need from the
device we have to call the method ``_rpc`` with the ``args`` and ``kwargs`` parameters. This is, 
by the way, an RPC call for a junos device.

**Note:** If a model is called by other models, like openconfig-if-ethernet is called by openconfig-interfaces,
there is no need to specify the execute section in the metadata, if the commands will be the same.
Since the first model executes the commands, the data from the commands will be shared with the 
models that the first model calls. While it will work it to specify the same commands in the metadata
section for the second model, it could cause the commands to be executed multiple times.

* **vlan** - This is the part that follows the model specification. In this case is ``vlan`` but in
  others it might be ``interfaces``, ``addressess`` or something else, this will be model dependent
  but it's basically whatever it's not ``metadata``. This part will follow the model specification
  and add rules on each attribute to tell the parser/translator what needs to be done. For
  example::

    vlan:
        _process: unnecessary
        config:
            _process: unnecessary
            vlan_id:
                _process:
                  - mode: xpath
                    xpath: "vlan-id"
                    from: "{{ parse_bookmarks['parent'] }}"

We have to specify the ``_process`` attribute at each step, which can either be ``unnecessary``, `` not_implemented`` or a list of rules:

* ``not_implemented`` means that we haven't added support to that field. In addition it will stop parsing that
  branch of the tree.
* ``unnecessary`` means that we don't need that field. This is common in containers as you usually don't
  need to process them at all.
* ``list`` of rules. See :ref:`parsers` and :ref:`translators`.

Something else worth noting is that each rule inside ``_process`` is evaluated as a
``jinja2`` template so you can do variable substitutions, evaluations, etc...
