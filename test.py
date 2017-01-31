from napalm_yang.models.interfaces import oc_if
from napalm_yang.models.acl import oc_acl

import random


oc_if = oc_if.Interfaces()
print(oc_if.model_to_text())


for eth_name in ["eth1", "eth2"]:
    eth = oc_if.interfaces.interface.new_element(eth_name)
    eth.config.description("This is a description for {}".format(eth_name))
    eth.config.enabled(random.choice([True, False]))
    eth.config.mtu(1500)
    # eth.config.type
    eth.state.description("This is a description for {}".format(eth_name))
    eth.state.counters.in_octets(random.randint(0, 999999))
    eth.state.oper_status("LOWER_LAYER_DOWN")
    eth.state.admin_status("UP")

print("\n=========================================\n")
print("Trying to set admin_status of eth2 to something wonky")
try:
    oc_if.interfaces.interface["eth2"].state.oper_status("WONKY")
except ValueError as e:
    print("ERROR!!!")
    print(e.message)

print("\n=========================================\n")
print("Trying to set description of eth2 to an int")
try:
    oc_if.interfaces.interface["eth2"].state.description(1)
except ValueError as e:
    print("ERROR!!!")
    print(e.message)

print("\n=========================================\n")
print("\nData:")
print(oc_if.data_to_text())

print("\n=========================================\n")

acl = oc_acl.Acl()
print(acl.model_to_text())
