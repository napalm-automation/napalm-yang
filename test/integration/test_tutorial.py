from __future__ import unicode_literals

import napalm_yang

import pytest

import json

import os
import sys


import logging
logger = logging.getLogger("napalm-yang")


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


#  config_logging()


BASE_PATH = os.path.dirname(__file__)


#  test_populating_from_file = ["eos", "junos"]
test_populating_from_file = ["eos"]


def read_file_content(filename):
    full_path = os.path.join(BASE_PATH, "data", filename)
    with open(full_path, "r") as f:
        return f.read()


def read_json(filename):
    return json.loads(read_file_content(filename))


class Tests(object):

    def test_create_binding(self):
        config = napalm_yang.base.Root()

        # Adding models to the object
        config.add_model(napalm_yang.models.openconfig_interfaces)
        config.add_model(napalm_yang.models.openconfig_vlan)

        assert napalm_yang.utils.model_to_dict(config) == read_json("test_create_binding.expected")

    def test_populate_models_programmatically(self):
        config = napalm_yang.base.Root()
        config.add_model(napalm_yang.models.openconfig_interfaces)

        et1 = config.interfaces.interface.add("et1")
        et1.config.description = "My description"
        et1.config.mtu = 1500
        assert et1.config.description == "My description"
        assert et1.config.mtu == 1500

        config.interfaces.interface.add("et2")
        config.interfaces.interface["et2"].config.description = "Another description"
        config.interfaces.interface["et2"].config.mtu = 9000
        assert config.interfaces.interface["et2"].config.description == "Another description"
        assert config.interfaces.interface["et2"].config.mtu == 9000

        assert config.get(filter=True) == \
            read_json("test_populate_models_programmatically.expected")

        with pytest.raises(ValueError):
            et1.config.mtu = -1

        assert_against = [
            ("et1", 'My description'),
            ('et2', 'Another description'),
        ]
        for iface, data in config.interfaces.interface.items():
            expected = assert_against.pop(0)
            assert iface == expected[0]
            assert data.config.description == expected[1]

        assert not assert_against, "We didn't iterate over all the interfaces"

        assert config.interfaces.interface.keys() == ['et1', 'et2']
        config.interfaces.interface.delete("et1")
        assert config.interfaces.interface.keys() == ['et2']

    def test_populating_from_a_dict(self):
        config = napalm_yang.base.Root()
        config.add_model(napalm_yang.models.openconfig_vlan)

        vlans_dict = {
            "vlans": {"vlan": {100: {
                                    "config": {
                                        "vlan_id": 100, "name": "production"}},
                               200: {
                                    "config": {
                                        "vlan_id": 200, "name": "dev"}}}}}
        config.load_dict(vlans_dict)
        assert config.vlans.vlan.keys() == [200, 100]
        assert config.vlans.vlan[100].config.name == "production"
        assert config.vlans.vlan[200].config.name == "dev"

    @pytest.mark.parametrize("profile", test_populating_from_file)
    def test_populating_from_file(self, profile):
        config_path = "test_populating_from_file/{}/config.txt".format(profile)
        expected_path = "test_populating_from_file/{}/expected.json".format(profile)

        config = napalm_yang.base.Root()
        config.add_model(napalm_yang.models.openconfig_interfaces)

        config.parse_config(config=read_file_content(config_path), profile=profile)

        assert config.get(filter=True) == read_json(expected_path)

    def test_translating_models(self):
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

        expected_junos = read_file_content("test_translating_models_junos.expected")
        expected_eos = read_file_content("test_translating_models_eos.expected")

        assert candidate.translate_config(profile="junos") == expected_junos
        assert candidate.translate_config(profile="eos") == expected_eos

    def test_advanced_manipulation_junos(self):
        profile = "junos"

        config_file = "test_advanced_manipulation/{}/config.txt".format(profile)
        merge_file = "test_advanced_manipulation/{}/merge.expected".format(profile)
        replace_file = "test_advanced_manipulation/{}/replace.expected".format(profile)

        candidate = napalm_yang.base.Root()
        candidate.add_model(napalm_yang.models.openconfig_interfaces)
        candidate.parse_config(config=read_file_content(config_file), profile=profile)

        # now let's do a few changes, let's remove lo0.0 and create lo0.1
        candidate.interfaces.interface["lo0"].subinterfaces.subinterface.delete("0")
        lo1 = candidate.interfaces.interface["lo0"].subinterfaces.subinterface.add("1")
        lo1.config.description = "new loopback"

        # Let's also default the mtu of ge-0/0/0 which is set to 1400
        candidate.interfaces.interface["ge-0/0/0"].config._unset_mtu()

        # We will also need a running configuration to compare against
        running = napalm_yang.base.Root()
        running.add_model(napalm_yang.models.openconfig_interfaces)
        running.parse_config(config=read_file_content(config_file), profile=profile)

        merge_config = candidate.translate_config(profile=profile, merge=running)
        assert merge_config == read_file_content(merge_file)

        replace_config = candidate.translate_config(profile=profile, replace=running)
        assert replace_config == read_file_content(replace_file)

    def test_advanced_manipulation_eos(self):
        profile = "eos"

        config_file = "test_advanced_manipulation/{}/config.txt".format(profile)
        merge_file = "test_advanced_manipulation/{}/merge.expected".format(profile)
        replace_file = "test_advanced_manipulation/{}/replace.expected".format(profile)

        candidate = napalm_yang.base.Root()
        candidate.add_model(napalm_yang.models.openconfig_interfaces)
        candidate.parse_config(config=read_file_content(config_file), profile=profile)

        # now let's do a few changes, let's remove lo1 and create lo0
        candidate.interfaces.interface.delete("Loopback1")
        lo0 = candidate.interfaces.interface.add("Loopback0")
        lo0.config.description = "new loopback"

        # Let's also default the mtu of ge-0/0/0 which is set to 1400
        candidate.interfaces.interface["Port-Channel1"].config._unset_mtu()

        # We will also need a running configuration to compare against
        running = napalm_yang.base.Root()
        running.add_model(napalm_yang.models.openconfig_interfaces)
        running.parse_config(config=read_file_content(config_file), profile=profile)

        merge_config = candidate.translate_config(profile=profile, merge=running)
        assert merge_config == read_file_content(merge_file)

        replace_config = candidate.translate_config(profile=profile, replace=running)
        assert replace_config == read_file_content(replace_file)

    def test_diffing_objects(self):
        profile = "eos"

        config_file = "test_diffing_objects/config.txt"
        expected_file = "test_diffing_objects/expected.json"

        candidate = napalm_yang.base.Root()
        candidate.add_model(napalm_yang.models.openconfig_interfaces)
        candidate.parse_config(config=read_file_content(config_file), profile=profile)

        # now let's do a few changes, let's remove lo1 and create lo0
        candidate.interfaces.interface.delete("Loopback1")
        lo0 = candidate.interfaces.interface.add("Loopback0")
        lo0.config.description = "new loopback"

        # Let's also default the mtu of ge-0/0/0 which is set to 1400
        candidate.interfaces.interface["Port-Channel1"].config._unset_mtu()

        # We will also need a running configuration to compare against
        running = napalm_yang.base.Root()
        running.add_model(napalm_yang.models.openconfig_interfaces)
        running.parse_config(config=read_file_content(config_file), profile=profile)

        assert napalm_yang.utils.diff(candidate, running) == read_json(expected_file)
