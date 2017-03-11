from napalm_base import get_network_driver

import napalm_yang

import sys

import logging
logger = logging.getLogger("napalm-yang")


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


#  config_logging()


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
j = junos(**junos_configuration)

eos = get_network_driver("eos")
e = eos(**eos_configuration)


def test_config_dict(device):
    with open(device) as d:
        running_config = napalm_yang.BaseBinding()
        running_config.add_model(napalm_yang.oc_if.interfaces())

        running_config.get_config(d)

        print(running_config.data_to_text())
        print("========================")
        config = running_config.translate(d)
        print(config)
        d.load_merge_candidate(config=config)
        print(d.compare_config())

        config_dict = {
            "interfaces": {
                "interface": {
                    "lo0": {
                        "config": {
                            "description": "New description"
                        },
                        "subinterfaces": {
                            "subinterface": {
                                "0": {
                                    "ipv4": {
                                        "addresses": {
                                            "address": {
                                                "10.0.0.1/24": {
                                                    "config": {
                                                        "ip": "10.0.0.1",
                                                        "prefix_length": 24
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        running_config.load_dict(config_dict)
        config = running_config.translate(d)
        print(config)

        d.load_merge_candidate(config=config)
        print(d.compare_config())

#  test_config_dict(j)


def translate_junos_to_eos():
    """
    eos = get_network_driver("eos")
    e = eos(**eos_configuration)
    e.open()
    print(j_running.data_to_text())
    config = j_running.translate(e)
    print(config)
    """
    pass


def config_generation(d):
    print("")
    print("CONFIGURATION GENERATION")
    print("========================")
    d.open()
    running_config = napalm_yang.BaseBinding()
    running_config.add_model(napalm_yang.oc_if.interfaces())
    running_config.get_config(d)
    config = running_config.translate(d)
    print(config)


config_generation(e)


def merge_config(d):
    print("")
    print("MERGE CONFIGURATION GENERATION")
    print("==============================")
    d.open()
    running_config = napalm_yang.BaseBinding()
    running_config.add_model(napalm_yang.oc_if.interfaces())
    running_config.get_config(d)

    candidate_config = napalm_yang.BaseBinding()
    candidate_config.add_model(napalm_yang.oc_if.interfaces())
    candidate_config.get_config(d)

    # Eliminate lo1 and create lo0
    candidate_config.interfaces.interface.pop("Loopback1")
    loopback = candidate_config.interfaces.interface.get_element("Loopback0")
    loopback.config.description("Creating new loopback interace")

    # Default mtu of Po1
    candidate_config.interfaces.interface["Port-Channel1"].config.mtu(None)

    config = candidate_config.translate(d, merge=running_config)
    print(config)
    print("diff:")
    e.load_merge_candidate(config=config)
    print(e.compare_config())
    e.discard_config()


merge_config(e)


def replace_config(d):
    print("")
    print("REPLACE CONFIGURATION GENERATION")
    print("================================")
    d.open()
    running_config = napalm_yang.BaseBinding()
    running_config.add_model(napalm_yang.oc_if.interfaces())
    running_config.get_config(d)

    candidate_config = napalm_yang.BaseBinding()
    candidate_config.add_model(napalm_yang.oc_if.interfaces())
    candidate_config.get_config(d)

    # Eliminate lo1 and create lo0
    candidate_config.interfaces.interface.pop("Loopback1")
    loopback = candidate_config.interfaces.interface.get_element("Loopback0")
    loopback.config.description("Creating new loopback interace")

    # Default mtu of Po1
    candidate_config.interfaces.interface["Port-Channel1"].config.mtu(None)

    config = candidate_config.translate(d, replace=running_config)
    print(config)
    print("diff:")
    e.load_merge_candidate(config=config)
    print(e.compare_config())
    e.discard_config()


replace_config(e)


"""
# Let's create the running configuration object
running = napalm_yang.BaseBinding()
print(running.model_to_text())  # Empty model

# We can now load the interfaces into it
running.add_model(napalm_yang.oc_if.interfaces())
running.add_model(napalm_yang.oc_vlan.vlan())
running.add_model(napalm_yang.oc_platform.platform())
print(running.model_to_text())  # Should've interfaces model and all of the augmentations

running.interfaces.interface.new_element("test")
running.interfaces.interface["test"].config.description("asds")
print(running.data_to_text())

candidate = napalm_yang.BaseBinding()
candidate.add_model(napalm_yang.oc_if.interfaces())
candidate.interfaces.interface.new_element("qweqwe")
candidate.interfaces.interface["qweqwe"].config.description("poi")
print(candidate.data_to_text())
print(running.data_to_text())

# Get current configuration for loaded models
config = napalm_yang.BaseBinding()
config.add_model(napalm_yang.oc_if.interfaces())
#  print(config.model_to_text())
config.get_config(e)

print(config.data_to_text())
"""

"""
# Print the exact model as defined by OC
# This is mostly informative, as quick reference
print(running.model_to_text())

# We can get a representation of the data in text
print(running.data_to_text())

# Or as a dict
pprint.pprint(running.data_to_dict())

# We can also translate the object backto native configuration
print(e.translate_model(running, "interfaces"))

# Let's change some configuration
candidate = e.parse_config("interfaces")
candidate.interfaces.interface["Management1"].config.description("Connected to oob1:et2")
candidate.interfaces.interface["Ethernet2"].config.description("Connected to spine")
candidate.interfaces.interface["Port-Channel1"].config.description("Connected to blah")
candidate.interfaces.interface["Ethernet1"].config.enabled(False)

# Let's create a new loopback interface
candidate.interfaces.interface.new_element("Loopback0")
candidate.interfaces.interface["Loopback0"].name("Loopback0")
candidate.interfaces.interface["Loopback0"].config.name("Loopback0")
candidate.interfaces.interface["Loopback0"].config.description("loopback0")
candidate.interfaces.interface["Loopback0"].config.enabled(True)
candidate.interfaces.interface["Loopback0"].config.mtu(1500)
candidate.interfaces.interface["Loopback0"].hold_time.config.up(0)
candidate.interfaces.interface["Loopback0"].hold_time.config.down(0)
candidate.interfaces.interface["Loopback0"].config.type_(napalm_yang.ianaift.Softwareloopback)

# Let's remove et2.1 and loq
candidate.interfaces.interface["Ethernet2"].subinterfaces.subinterface.pop("Ethernet2.1")
candidate.interfaces.interface.pop("Loopback1")

# Let's see a diff of the running and the candidate configuration
pprint.pprint(running.diff(candidate))

# Let's turn this into native configuration
new_config = e.translate_model(candidate, "interfaces")
print(new_config)

# Let's turn this into a native merge
merge = e.merge_model(candidate, running, "interfaces")
print(merge)

# Merge it into the device
e.load_merge_candidate(config=merge)

# See the diff matches our expectations
print(e.compare_config())


#  # Let's commit the configuration now
#  e.commit_config()

#  # if now get a new running and candidate config, let's compare it with out previous candidate
#  running = e.parse_config("interfaces")
#  pprint.pprint(running.diff(candidate))
"""
