from napalm_yang.models.interfaces import oc_if
from napalm_yang.models.acl import oc_acl

import random


def print_model(name, model, indentation=""):
    meta = model["_meta"]
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    print("{}+-- {} {}{}".format(indentation, mode, name, key))
    indentation = indentation + "|  "

    for attr, data in model.items():
        if attr == "_meta":
            continue

        sm = data.get("_meta")
        if sm["nested"]:
            print_model(attr, data, indentation)
        else:
            mandatory = "" if sm["mandatory"] else "?"
            body = "{}+-- {} {}{}".format(indentation, mode, attr, mandatory)
            spacing = " " * (60 - len(body))
            print("{}{}{}".format(body, spacing, sm["type"]))


def print_data(name, data, indentation=""):
    meta = data["_meta"]
    mode = "rw" if meta["config"] else "ro"
    key = "* [{}]".format(meta.get("key", "")) if meta.get("key", "") else ""
    print("{}+-- {} {}{}".format(indentation, mode, name, key))
    indentation = indentation + "|  "

    for attr, attr_data in data.items():
        if attr == "_meta":
            continue
        elif attr == "list":
            for e, d in attr_data.items():
                print_data(e, d, indentation)
        elif "value" in attr_data.keys():
            sm = attr_data["_meta"]

            if sm["type"] == "Enumeration":
                value = "{} ({})".format(attr_data["value"], sm["enum_value"])
            else:
                value = attr_data["value"]

            mandatory = "" if sm["mandatory"] else "?"
            body = "{}+-- {} {}{}".format(indentation, mode, attr, mandatory)
            spacing = " " * (60 - len(body))
            print("{}{}{}".format(body, spacing, value))
        else:
            print_data(attr, attr_data, indentation)


oc_if = oc_if.Interfaces()
model = oc_if.model_represenation()
print_model("openconfig-interfaces", model)


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
data = oc_if.data_representation()
print_data("interfaces", data)

print("\n=========================================\n")

acl = oc_acl.Acl()
model = acl.model_represenation()
print_model("acls", model)
