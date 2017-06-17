Translators
^^^^^^^^^^^

Translators are responsible for transforming a model into native configuration.

Special actions
===============

Most actions depend on the parser you are using, however, some are common to all of them:

unnecessary
-----------

This makes the parser skip the field and continue processing the tree.

not_implemented
---------------

This makes the parser stop processing the tree underneath this value. For example::

    field_1:
        process: unnecessary
    field_2:
        process: not_implemented
        subfield_1:
            process: ...
        subfield_2:
            process: ...
    field_3:
        ...

The ``not_implemented`` action will stop the parser from processing ``subfield_1`` and ``subfield_2``
and move directly onto ``field_3``.

gate
----

Works like ``not_implemented`` but accepts a condition. For example::

    protocols:
        protocol:
            bgp:
                _process:
                  - mode: gate
                    when: "{{ protocol_key != 'bgp bgp' }}"
                global:
                    ...

The snippet above will only process the ``bgp`` subtree if the condition is **not** met.

Special fields
==============

When translating an object, some fields might depend on the translator you are using but some will
available regardless. Some may be even be mandatory.

mode
----

* **mandatory**: yes
* **description**: which parsing/translation action to use for this particular field
* **example**: Translate description attribute of an interface to native configuration::

    description:
        _process:
            - mode: element
              value: "    description {{ model }}\n"
              negate: "    default description"

when
----

* **mandatory**: no
* **description**: the evaluation of this field will determine if the action is executed or
  skipped. This action is probably not very useful when parsing but it's available if you need it.
* **example**: configure ``switchport`` on IOS devices only if the interface is not a loopback
  or a management interface::

    ipv4:
        _process: unnecessary
        config:
            _process: unnecessary
            enabled:
                _process:
                    - mode: element
                      value: "    no switchport\n"
                      negate: "    switchport\n"
                      in: "interface.{{ interface_key }}"
                      when: "{{ model and interface_key[0:4] not in ['mana', 'loop'] }}"

in
--

* **mandatory**: no
* **description**: where to add the configuration. Sometimes the configuration might have to be
  installed on a different object from the one you are parsing. For example, when configuring a
  tagged subinterface on junos you will have to add also a ``vlan-tagging`` option on the parent
  interface. On ``IOS/EOS``, when configuring interfaces, you have to also add the configuration in
  the root of the configuration and not as a child of the parent interface::

    vlan:
        _process: unnecessary
        config:
            _process: unnecessary
            vlan_id:
                _process:
                    - mode: element
                      element: "vlan-tagging"
                      in: "interface.{{ interface_key }}" # <--- add element to parent interface
                      when: "{{ model > 0 }}"
                      value: null
                    - mode: element
                      element: "vlan-id"
                      when: "{{ model > 0 }}"

    (...)
    subinterface:
        _process:
            mode: container
            key_value: "interface {{ interface_key}}.{{ subinterface_key }}\n"
            negate: "no interface {{ interface_key}}.{{ subinterface_key }}\n"
            in: "interfaces"                            # <--- add element to root of configuration

.. note:: This field follows the same logic as the :ref:`yang_special_field_bookmarks` special field.

continue_negating
-----------------

* **mandatory**: no
* **description**: This option, when added to a container, will make the framework to also negate children.
* **example**: We can use as an example the "network-instances" model. In the model, BGP is inside the ``network-instance`` container, however, in EOS and other platforms that BGP configuration is decoupled from the VRF, so in order to tell the framework to delete also the direct children you will have to use this option. For example::

    network-instance:
        _process:
            - mode: container
              key_value: "vrf definition {{ network_instance_key }}\n"
              negate: "no vrf definition {{ network_instance_key }}\n"
              continue_negating: true
              end: "    exit\n"
              when: "{{ network_instance_key != 'global' }}"
        ...
        protocols:
            _process: unnecessary
            protocol:
                _process:
                  - mode: container
                    key_value: "router bgp {{ model.bgp.global_.config.as_ }}\n  vrf {{ network_instance_key}}\n"
                    negate: "router bgp {{ model.bgp.global_.config.as_ }}\n  no vrf {{ network_instance_key}}\n"
                    end: "    exit\n"
                    when: "{{ protocol_key == 'bgp bgp' and network_instance_key != 'global' }}"
                    replace: false
                    in: "network-instances"

The example above will generate::

    no vrf definition blah
    router bgp ASN
       no vrf blah

Without ``continue_negating`` it would just generate::

    no vrf definition blah

Special variables
=================

keys
----

See :ref:`yang_special_field_keys`.

model
-----

This is the current model/attribute being translated. You have the entire object at your disposal,
not only it's value so you can do things like::

    vlan_id:
        _process:
            - mode: element
              value: "    encapsulation dot1q vlan {{ model }}\n"

Or::

    config:
        _process: unnecessary
        ip:
            _process: unnecessary
        prefix_length:
            _process:
                - mode: element
                  value: "    ip address {{ model._parent.ip }}/{{ model }} {{ 'secondary' if model._parent.secondary else '' }}\n"
                  negate: "    default ip address {{ model._parent.ip }}/{{ model }}\n"
