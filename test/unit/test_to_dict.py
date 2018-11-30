import json
import os

import napalm_yang


BASE_PATH = os.path.join(os.path.dirname(__file__), "test_to_dict")


class Tests(object):
    def test_to_dict(self):
        root = napalm_yang.base.Root()
        root.add_model(napalm_yang.models.openconfig_interfaces)
        with open(os.path.join(BASE_PATH, "data.json"), "r") as f:
            root.load_dict(json.load(f))

        assert root.to_dict() == {
            "interfaces": {
                "interface": {
                    "Ethernet1": {
                        "name": "Ethernet1",
                        "config": {"type": "ethernetCsmacd", "enabled": True},
                        "ethernet": {
                            "switched_vlan": {
                                "config": {
                                    "interface_mode": "TRUNK",
                                    "native_vlan": 30,
                                    "access_vlan": 1,
                                    "trunk_vlans": ["20..22", 40],
                                }
                            }
                        },
                        "routed_vlan": {"ipv4": {"config": {"enabled": False}}},
                    },
                    "Ethernet2": {
                        "name": "Ethernet2",
                        "config": {"type": "ethernetCsmacd", "enabled": True},
                        "ethernet": {
                            "switched_vlan": {
                                "config": {
                                    "interface_mode": "ACCESS",
                                    "native_vlan": 1,
                                    "access_vlan": 30,
                                    "trunk_vlans": ["1..4094"],
                                }
                            }
                        },
                        "routed_vlan": {"ipv4": {"config": {"enabled": False}}},
                    },
                    "Management1": {
                        "name": "Management1",
                        "config": {
                            "type": "ethernetCsmacd",
                            "mtu": 1500,
                            "enabled": True,
                        },
                        "routed_vlan": {
                            "ipv4": {
                                "addresses": {
                                    "address": {
                                        "10.0.2.15": {
                                            "ip": "10.0.2.15",
                                            "config": {
                                                "ip": "10.0.2.15",
                                                "prefix_length": 24,
                                                "secondary": False,
                                            },
                                        }
                                    }
                                },
                                "config": {"enabled": True},
                            }
                        },
                    },
                }
            }
        }
