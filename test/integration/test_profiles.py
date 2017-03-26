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


def pretty_json(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)


BASE_PATH = os.path.dirname(__file__)


test_profile_models = [
    ["ios", napalm_yang.models.openconfig_interfaces, "default"],
]


def read_file_content(profile, model, case, filename):
    full_path = os.path.join(BASE_PATH, "profiles_data",
                             profile, model._yang_name, case, filename)
    with open(full_path, "r") as f:
        return f.read()


def read_json(profile, model, case, filename):
    return json.loads(read_file_content(profile, model, case, filename))


class Tests(object):

    @pytest.mark.parametrize("profile, model, case", test_profile_models)
    def test_parse(self, profile, model, case):
        config_txt = read_file_content(profile, model, case, "config.txt")
        expected_json = read_json(profile, model, case, "expected.json")

        config = napalm_yang.base.Root()
        config.add_model(model)
        config.parse_config(config=config_txt, profile=[profile])

        expected = napalm_yang.base.Root()
        expected.add_model(model)
        expected.load_dict(expected_json)

        #  print(pretty_json(config.get(filter=True)))

        assert not napalm_yang.utils.diff(config, expected)
