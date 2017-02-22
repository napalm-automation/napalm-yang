from napalm_base import get_network_driver

import napalm_yang


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

"""
junos = get_network_driver("junos")
j = junos(**junos_configuration)
j.open()

# Let's parse the configuration
j_running = j.parse_config("interfaces")

# Print the exact model as defined by OC
# This is mostly informative, as quick reference
print(j_running.model_to_text())

# We can get a representation of the data in text
print(j_running.data_to_text())

# Translate model
new_config = j.translate_model(j_running, "interfaces")
print(new_config)

# Change a description and Translate model
j_running.interfaces.interface["lo0"].config.description("asadqweqwe")
new_config = j.translate_model(j_running, "interfaces")
print(new_config)
"""

# Connect to devices
#  eos = get_network_driver("eos")
#  e = eos(**eos_configuration)
#  e.open()

# Let's create the running configuration object
running = napalm_yang.BaseBinding()
print(running.model_to_text())  # Empty model

# We can now load the interfaces into it
running.add_model(napalm_yang.oc_if.interfaces)
running.add_model(napalm_yang.oc_vlan.vlan)
running.add_model(napalm_yang.oc_platform.platform)
print(running.model_to_text())  # Should've interfaces model and all of the augmentations

running.interfaces.interface.new_element("test")
running.interfaces.interface["test"].config.description("asds")
print(running.data_to_text())


# Get current interfaces configuration
#  running = e.parse_config("interfaces")

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
