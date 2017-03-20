from napalm_base import get_network_driver

import napalm_yang

import json
import sys

import logging
logger = logging.getLogger("napalm-yang")


junos_configuration = {
    'hostname': '127.0.0.1',
    'username': 'vagrant',
    'password': '',
    'optional_args': {'port': 12203}
}

eos_configuration = {
    'hostname': '127.0.0.1',
    'username': 'vagrant',
    'password': 'vagrant',
    'optional_args': {'port': 12443}
}

junos = get_network_driver("junos")
junos_device = junos(**junos_configuration)

eos = get_network_driver("eos")
eos_device = eos(**eos_configuration)


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


# config_logging()


def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))


"""
config = base.Root()
config.add_model(models.openconfig_interfaces)
config.add_model(models.openconfig_vlan)

pretty_print(base.model_to_dict(config))

# Populating models

et1 = config.interfaces.interface.add("eth1")
et1.config.description = "My description"
et1.config.mtu = 1500

pretty_print(et1.get(filter=True))

config.interfaces.interface.add("eth2")
config.interfaces.interface["eth2"].config.description = "Another description"
config.interfaces.interface["eth2"].config.mtu = 9000

pretty_print(config.get(filter=True))

try:
    et1.config.mtu = -1
except ValueError as e:
    print(e.message["error-string"])

# Iterating
for iface in config.interfaces.interface:
    print(iface, config.interfaces.interface[iface].config.description)


# We can also delete interfaces
print(config.interfaces.interface.keys())
config.interfaces.interface.delete("eth2")
print(config.interfaces.interface.keys())

# Populating the model from a dict
vlans_dict = {
    "vlans": {"vlan": {100: {
                            "config": {
                                "vlan_id": 100, "name": "production"}},
                       200: {
                            "config": {
                                "vlan_id": 200, "name": "dev"}}}}}

config.load_dict(vlans_dict)
pretty_print(config.vlans.get(filter=True))
"""


def test_config_load_and_translation(vendor):
    if vendor == "eos":
        device = eos_device
    elif vendor == "junos":
        device = junos_device
    #  with open("interactive_demo/{}.config".format(vendor), "r") as f:
    #      configuration = f.read()

    config = napalm_yang.base.Root()
    config.add_model(napalm_yang.models.openconfig_interfaces)
    device.open()
    config.parse_config(device=device)

    pretty_print(config.get(filter=True))

    text = config.translate_config(vendor)
    print(text)

    device.load_merge_candidate(config=text)
    print(device.compare_config())
    device.discard_config()

    device.close()


#  test_config_load_and_translation("junos")
#  test_config_load_and_translation("eos")

def test_junos(replace):
    junos_device.open()

    # first let's create a candidate config by retrieving the current state of the device
    candidate = napalm_yang.base.Root()
    candidate.add_model(napalm_yang.models.openconfig_interfaces)
    candidate.parse_config(device=junos_device)

    # now let's do a few changes, let's remove lo0.0 and create lo0.1
    candidate.interfaces.interface["lo0"].subinterfaces.subinterface.delete("0")
    lo1 = candidate.interfaces.interface["lo0"].subinterfaces.subinterface.add("1")
    lo1.config.description = "new loopback"

    # Let's also default the mtu of ge-0/0/0 which is set to 1400
    candidate.interfaces.interface["ge-0/0/0"].config._unset_mtu()

    # We will also need a running configuration to compare against
    running = napalm_yang.base.Root()
    running.add_model(napalm_yang.models.openconfig_interfaces)
    running.parse_config(device=junos_device)

    if replace:
        config = candidate.translate_config(profile=junos_device.profile, replace=running)
    else:
        config = candidate.translate_config(profile=junos_device.profile, merge=running)
    print(config)

    junos_device.load_merge_candidate(config=config)
    print(junos_device.compare_config())
    junos_device.discard_config()

    junos_device.close()


#  test_junos(replace=False)
#  test_junos(replace=True)


def test_eos(replace):
    eos_device.open()

    # first let's create a candidate config by retrieving the current state of the device
    candidate = napalm_yang.base.Root()
    candidate.add_model(napalm_yang.models.openconfig_interfaces)
    candidate.parse_config(device=eos_device)

    pretty_print(candidate.get(filter=True))

    # now let's do a few changes, let's remove lo1 and create lo0
    candidate.interfaces.interface.delete("Loopback1")
    lo0 = candidate.interfaces.interface.add("Loopback0")
    lo0.config.description = "new loopback"

    # Let's also default the mtu of ge-0/0/0 which is set to 1400
    candidate.interfaces.interface["Port-Channel1"].config._unset_mtu()

    # We will also need a running configuration to compare against
    running = napalm_yang.base.Root()
    running.add_model(napalm_yang.models.openconfig_interfaces)
    running.parse_config(device=eos_device)

    if replace:
        config = candidate.translate_config(profile=eos_device.profile, replace=running)
    else:
        config = candidate.translate_config(profile=eos_device.profile, merge=running)
    print(config)

    eos_device.load_merge_candidate(config=config)
    print(eos_device.compare_config())
    eos_device.discard_config()

    eos_device.close()


#  test_eos(replace=False)
test_eos(replace=True)


def test_config_load_file(vendor):
    with open("interactive_demo/{}.config".format(vendor), "r") as f:
        configuration = f.read()
    if vendor == "eos":
        pass
    elif vendor == "junos":
        configuration = [configuration]

    config = napalm_yang.base.Root()
    config.add_model(napalm_yang.models.openconfig_interfaces)
    config.parse_config(config=configuration, profile="junos")

    pretty_print(config.get(filter=True))


#  test_config_load_file("junos")
#  test_config_load_file("eos")


def test():
    candidate = napalm_yang.base.Root()
    candidate.add_model(napalm_yang.models.openconfig_interfaces())

    def create_iface(candidate, name, description, mtu, prefix, prefix_length):
        interface = candidate.interfaces.interface.add(name)
        interface.config.description = description
        interface.config.mtu = mtu
        ip = interface.routed_vlan.ipv4.addresses.address.add(prefix)
        ip.config.ip = prefix
        ip.config.prefix_length = prefix_length

    create_iface(candidate, "et1", "Uplink1", 9000, "192.168.1.1", 24)
    create_iface(candidate, "et2", "Uplink2", 9000, "192.168.2.1", 24)

    pretty_print(candidate.get(filter=True))
    print(candidate.translate_config(profile=junos_device.profile))


#  test()
