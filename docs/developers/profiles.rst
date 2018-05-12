Profiles
--------

In order to correctly map YANG objects to native configuration and vice versa, ``napalm-yang`` uses the concept of **profiles**. Profiles, identify the type of device you are dealing with, which can vary depending on the OS, version and/or platform you are using.

If you are using a napalm driver and have access to your device, you will have access to the ``profile`` property which you can pass to any function that requires to know the profile. If you are not using a napalm driver or don't have access to the device, a profile is just a list of strings so you can just specify it directly. For example::

    # Without access to the device
    model.parse_config(profile=["junos"], config=my_configuration)
    
    # With access
    with driver(hostname, username, password) as d:
        model.parse_config(device=d)
    
    # With access but overriding profile
    with driver(hostname, username, password) as d:
        model.parse_config(device=d, profile=["junos13", "junos"])

.. note:: As you noticed a device may have multiple profiles. When that happens, each model that is
  parsed will loop through the profiles from left to right and use the first profile that
  implements that model (note that a YANG model is often comprised of multiple modules). This
  is useful as there might be small variances between different systems
  but not enough to justify reimplementing everything.

You can find the profiles `here <https://github.com/napalm-automation/napalm-yang/tree/develop/napalm_yang/mappings>`__ but what exactly is a profile? A profile is a bunch of YAML files that follows the structure of a YANG model and describes two things:

#. How to parse native configuration/state and map it into a model.
#. How to translate a model and map it into native configuration.

For example, `here <https://github.com/napalm-automation/napalm-yang/blob/develop/napalm_yang/mappings/eos/parsers/config/openconfig-interfaces/interfaces.yaml>`__ you can see how to map native configuration from an EOS device into the ``openconfig-interface`` model and `here <https://github.com/napalm-automation/napalm-yang/blob/develop/napalm_yang/mappings/eos/translators/openconfig-interfaces/interfaces.yaml>`__ how to map the model to native configuration.

As you can see it's not extremely difficult to understand what they are doing, in the next section we will learn how to write our own profiles.
