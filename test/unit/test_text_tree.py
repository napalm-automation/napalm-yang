from glob import glob

import json
import os

import pytest

import napalm_yang


BASE_PATH = os.path.dirname(__file__)
test_case_text_parser = [
    x.split("/")[-1] for x in glob("{}/text_tree/*".format(BASE_PATH))
]


class Tests(object):

    @pytest.mark.parametrize("case", test_case_text_parser)
    def test_text_tree_parser(self, case):
        path = os.path.join(BASE_PATH, "text_tree", case, "config.txt")
        expected = os.path.join(BASE_PATH, "text_tree", case, "expected.json")

        with open(path, "r") as f:
            original = [f.read()]

        parsed = napalm_yang.parsers.text_tree.TextTree({}, {}).init_native(original)

        #  with open(expected, 'w') as f:
        #      f.write(result)

        with open(expected, "r") as f:
            expected = json.load(f)

        assert parsed == expected
