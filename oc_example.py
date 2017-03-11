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
        d.discard_config()
        d.close()

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
    d.close()


config_generation(j)
config_generation(e)


def merge_config(d, example):
    print("")
    print("MERGE CONFIGURATION GENERATION: {}".format(example))
    print("=============================================")

    d.open()
    running_config = napalm_yang.BaseBinding()
    running_config.add_model(napalm_yang.oc_if.interfaces())
    running_config.get_config(d)

    candidate_config = napalm_yang.BaseBinding()
    candidate_config.add_model(napalm_yang.oc_if.interfaces())
    candidate_config.get_config(d)

    if example == "eos_example":
        # Default mtu of Po1
        candidate_config.interfaces.interface["Port-Channel1"].config.mtu(None)

        # Eliminate lo1 and create lo0
        candidate_config.interfaces.interface.pop("Loopback1")
        loopback = candidate_config.interfaces.interface.get_element("Loopback0")
    elif example == "junos_example":
        # Default mtu of ge-0/0/1
        candidate_config.interfaces.interface["ge-0/0/1"].config.mtu(None)

        # Eliinat lo0.0 and create lo0.1
        lo = candidate_config.interfaces.interface["lo0"]
        lo.subinterfaces.subinterface.pop("0")
        loopback = lo.subinterfaces.subinterface.get_element("1")

    loopback.config.description("Creating new loopback interace")

    config = candidate_config.translate(d, merge=running_config)
    print(config)
    print("diff:")
    d.load_merge_candidate(config=config)
    print(d.compare_config())
    d.discard_config()
    d.close()


merge_config(e, "eos_example")
merge_config(j, "junos_example")


def replace_config(d, example):
    print("")
    print("REPLACE CONFIGURATION GENERATION: {}".format(example))
    print("====================================================")

    d.open()
    running_config = napalm_yang.BaseBinding()
    running_config.add_model(napalm_yang.oc_if.interfaces())
    running_config.get_config(d)

    candidate_config = napalm_yang.BaseBinding()
    candidate_config.add_model(napalm_yang.oc_if.interfaces())
    candidate_config.get_config(d)

    if example == "eos_example":
        # Default mtu of Po1
        candidate_config.interfaces.interface["Port-Channel1"].config.mtu(None)

        # Eliminate lo1 and create lo0
        candidate_config.interfaces.interface.pop("Loopback1")
        loopback = candidate_config.interfaces.interface.get_element("Loopback0")
    elif example == "junos_example":
        # Default mtu of ge-0/0/1
        candidate_config.interfaces.interface["ge-0/0/1"].config.mtu(None)

        # Eliinat lo0.0 and create lo0.1
        lo = candidate_config.interfaces.interface["lo0"]
        lo.subinterfaces.subinterface.pop("0")
        loopback = lo.subinterfaces.subinterface.get_element("1")

    loopback.config.description("Creating new loopback interace")

    config = candidate_config.translate(d, replace=running_config)
    print(config)
    print("diff:")
    d.load_merge_candidate(config=config)
    print(d.compare_config())
    d.discard_config()
    d.close()


#  replace_config(e, "eos_example")
#  replace_config(j, "junos_example")
