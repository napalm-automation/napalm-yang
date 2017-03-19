from napalm_yang import models
from napalm_yang import base

import json
import sys

import logging
logger = logging.getLogger("napalm-yang")


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


config_logging()


def pretty_print(dictionary):
    print(json.dumps(dictionary, sort_keys=True, indent=4))


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

with open("interactive_demo/eos.config", "r") as f:
    configuration = [{"show running-config all": f.read()}]

#  config.interfaces.interface.delete("eth1")
#  config.parse(profile="eos", config=configuration)
#  pretty_print(config.get(filter=True))

# JUNOS
with open("interactive_demo/junos.config", "r") as f:
    configuration = f.read()

config = base.Root()
config.add_model(models.openconfig_interfaces)
config.parse(profile="junos", config=configuration)
pretty_print(config.get(filter=True))
