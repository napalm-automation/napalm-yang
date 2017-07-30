from __future__ import unicode_literals

#  from napalm_base import get_network_driver

import napalm_yang
from napalm_base.mock import MockDriver

import pytest

import json

import os


#  napalm_yang.helpers.config_logging()


device_configuration = {
    "junos": {
        'hostname': '127.0.0.1',
        'username': 'vagrant',
        'password': '',
        'optional_args': {'port': 12203, 'config_lock': False}
    }
}


def pretty_json(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)


BASE_PATH = os.path.dirname(__file__)


test_parse_models = [
    ["ios", "config", napalm_yang.models.openconfig_network_instance, "default"],
    ["ios", "config", napalm_yang.models.openconfig_interfaces, "default"],
    ["eos", "config", napalm_yang.models.openconfig_network_instance, "default"],
    ["eos", "config", napalm_yang.models.openconfig_interfaces, "default"],
    ["eos", "config", napalm_yang.models.openconfig_interfaces, "l2_ports"],
    ["eos", "config", napalm_yang.models.openconfig_vlan, "default"],
    ["eos", "state", napalm_yang.models.openconfig_interfaces, "default"],
    ["junos", "config", napalm_yang.models.openconfig_network_instance, "default"],
    ["junos", "state", napalm_yang.models.openconfig_interfaces, "default"],
]


def read_file_content(base, profile, model, mode, case, filename):
    full_path = os.path.join(BASE_PATH, base,
                             profile, model._yang_name, mode, case, filename)
    with open(full_path, "r") as f:
        return f.read()


def read_json(base, profile, model, mode, case, filename):
    return json.loads(read_file_content(base, profile, model, mode, case, filename))


def load_json_model(base, profile, model, mode, case, filename):
    expected_json = read_json(base, profile, model, mode, case, "expected.json")
    expected = napalm_yang.base.Root()
    expected.add_model(model)
    expected.load_dict(expected_json)
    return expected


class Tests(object):

    @pytest.mark.parametrize("profile, mode, model, case", test_parse_models)
    def test_parse(self, profile, mode, model, case):
        expected = load_json_model("test_profiles", profile, model, mode, case, "expected.json")

        optional_args = {
            "path": os.path.join(BASE_PATH, "test_profiles",
                                 profile, model._yang_name, mode, case, "mocked"),
            "profile": profile if isinstance(profile, list) else [profile],
        }
        with MockDriver("hostname", "username", "password", optional_args=optional_args) as d:
            yang = napalm_yang.base.Root()
            yang.add_model(model)

            if mode == "config":
                yang.parse_config(device=d)
            else:
                yang.parse_state(device=d)

        #  print(pretty_json(yang.get(filter=True)))
        #  print(pretty_json(expected.get(filter=True)))
        assert not napalm_yang.utils.diff(yang, expected)

    @pytest.mark.parametrize("profile, mode, model, case", test_parse_models)
    def test_translate(self, profile, mode, model, case):
        if mode == "state":
            return

        json_blob = read_json("test_profiles", profile, model, mode, case, "expected.json")
        expected_translation = read_file_content("test_profiles", profile, model, mode, case,
                                                 "translation.txt")

        config = napalm_yang.base.Root()
        config.add_model(model)
        config.load_dict(json_blob)

        configuration = config.translate_config(profile=[profile])

        #  driver = get_network_driver(profile)
        #  with driver(**device_configuration[profile]) as d:
        #     d.load_merge_candidate(config=configuration)
        #     print(d.compare_config())

        assert configuration == expected_translation

    @pytest.mark.parametrize("action", ["merge", "replace"])
    @pytest.mark.parametrize("profile, mode, model, case", test_parse_models)
    def test_translate_merge(self, mode, action, profile, model, case):
        if mode == "state":
            return

        json_running = read_json("test_profiles", profile, model, mode, case, "expected.json")
        json_candidate = read_json("test_profiles", profile, model, mode, case, "candidate.json")

        expected_translation = read_file_content("test_profiles", profile, model, mode, case,
                                                 "{}.txt".format(action))

        candidate = napalm_yang.base.Root()
        candidate.add_model(model)
        candidate.load_dict(json_candidate)

        running = napalm_yang.base.Root()
        running.add_model(model)
        running.load_dict(json_running)

        if action == "merge":
            configuration = candidate.translate_config(profile=[profile], merge=running)
        elif action == "replace":
            configuration = candidate.translate_config(profile=[profile], replace=running)

        #  print(pretty_json(napalm_yang.utils.diff(candidate, running)))
        #  print(configuration)

        #  driver = get_network_driver(profile)
        #  with driver(**device_configuration[profile]) as d:
        #      d.load_merge_candidate(config=configuration)
        #      print(d.compare_config())
        #      d.discard_config()

        assert configuration == expected_translation
