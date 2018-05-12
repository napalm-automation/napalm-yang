from __future__ import unicode_literals

import pytest


import napalm_yang

import json
import os
import sys


import logging

logger = logging.getLogger("napalm-yang")


def config_logging():
    logger.setLevel(logging.DEBUG)
    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")
    ch.setFormatter(formatter)
    logger.addHandler(ch)


#  config_logging()


def pretty_json(dictionary):
    return json.dumps(dictionary, sort_keys=True, indent=4)


BASE_PATH = os.path.dirname(__file__)


test_validate = [
    ["ios", napalm_yang.models.openconfig_interfaces, "default", True],
    ["ios", napalm_yang.models.openconfig_interfaces, "default_fail", False],
]


def read_file_content(profile, model, case, filename):
    full_path = os.path.join(BASE_PATH, "validate", profile, case, filename)
    with open(full_path, "r") as f:
        return f.read()


def read_json(profile, model, case, filename):
    return json.loads(read_file_content(profile, model, case, filename))


class Tests(object):

    @pytest.mark.parametrize("profile, model, case, result", test_validate)
    def test_validate(self, profile, model, case, result):
        data_file = "candidate.json"
        validate_file = "validate.yaml"

        data = read_json(profile, model, case, data_file)

        config = napalm_yang.base.Root()
        config.add_model(napalm_yang.models.openconfig_interfaces)
        config.load_dict(data)

        #  print(pretty_json(config.to_dict(filter=True)))

        validation_file = os.path.join(
            BASE_PATH, "validate", profile, case, validate_file
        )

        report = config.compliance_report(validation_file)

        assert report["complies"] == result, report
