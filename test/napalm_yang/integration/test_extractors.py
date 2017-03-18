import napalm_yang

import pytest

import json

import os


BASE_PATH = os.path.dirname(__file__)


extractor_tests = [
    ("eos/default/config.txt", "eos", "eos/default/expected.json"),
    ("junos/default/config.txt", "junos", "junos/default/expected.json"),
]


def read_file_content(filename):
    full_path = os.path.join(BASE_PATH, "data", "extractor", filename)
    with open(full_path, "r") as f:
        return f.read()


class Tests(object):

    @pytest.mark.parametrize("config, profile, expected", extractor_tests)
    def test_extractor(self, config, profile, expected):
        testing_conf = read_file_content(config)
        testing = napalm_yang.BaseBinding()
        testing.add_model(napalm_yang.oc_if.interfaces())
        testing.get_config(config=testing_conf, profile=profile)

        expected_dict = json.loads(read_file_content(expected))

        #  print(json.dumps(testing.to_dict(), indent=4))
        assert testing.to_dict() == expected_dict
