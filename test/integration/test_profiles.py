from __future__ import unicode_literals

from napalm_base import get_network_driver

import napalm_yang

import pytest

import json

import os
import sys


import logging
logger = logging.getLogger("napalm-yang")


device_configuration = {
    "junos": {
        'hostname': '127.0.0.1',
        'username': 'vagrant',
        'password': '',
        'optional_args': {'port': 12203, 'config_lock': False}
    }
}


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


#  config_logging()


def pretty_json(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)


BASE_PATH = os.path.dirname(__file__)


test_config_profile_models = [
    ["ios", napalm_yang.models.openconfig_interfaces, "default"],
    ["eos", napalm_yang.models.openconfig_network_instance, "default"],
    ["junos", napalm_yang.models.openconfig_network_instance, "default"],
]

test_state_profile_models = [
    ["junos", napalm_yang.models.openconfig_interfaces, "default"],
    #  ["eos", napalm_yang.models.openconfig_interfaces, "default"],
]


def read_file_content(profile, model, case, filename):
    full_path = os.path.join(BASE_PATH, "profiles_data",
                             profile, model._yang_name, case, filename)
    with open(full_path, "r") as f:
        return f.read()


def read_json(profile, model, case, filename):
    return json.loads(read_file_content(profile, model, case, filename))


class Tests(object):

    @pytest.mark.parametrize("profile, model, case", test_config_profile_models)
    def test_parse_config(self, profile, model, case):
        config_txt = read_file_content(profile, model, case, "config.txt")
        expected_json = read_json(profile, model, case, "expected.json")

        config = napalm_yang.base.Root()
        config.add_model(model)
        config.parse_config(native=[config_txt], profile=[profile])

        expected = napalm_yang.base.Root()
        expected.add_model(model)
        expected.load_dict(expected_json)

        #  print(pretty_json(config.get(filter=True)))

        assert not napalm_yang.utils.diff(config, expected)

    @pytest.mark.parametrize("profile, model, case", test_config_profile_models)
    def test_translate(self, profile, model, case):
        json_blob = read_json(profile, model, case, "expected.json")
        expected_translation = read_file_content(profile, model, case, "translation.txt")

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
    @pytest.mark.parametrize("profile, model, case", test_config_profile_models)
    def test_translate_merge(self, action, profile, model, case):
        json_running = read_json(profile, model, case, "expected.json")
        json_candidate = read_json(profile, model, case, "candidate.json")

        expected_translation = read_file_content(profile, model, case, "{}.txt".format(action))

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
            #  d.load_merge_candidate(config=configuration)
            #  print(d.compare_config())
            #  d.discard_config()

        assert configuration == expected_translation

    @pytest.mark.parametrize("profile, model, case", test_state_profile_models)
    def test_parse_state(self, profile, model, case):
        native = read_file_content(profile, model, case, "{}.native".format(model._yang_name))
        expected_json = read_json(profile, model, case, "{}.expected".format(model._yang_name))

        state = napalm_yang.base.Root()
        state.add_model(model)
        state.parse_state(native=[native], profile=[profile])

        expected = napalm_yang.base.Root()
        expected.add_model(model)
        expected.load_dict(expected_json)

        assert not napalm_yang.utils.diff(state, expected)
