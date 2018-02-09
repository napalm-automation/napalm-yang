import os
from glob import glob

import napalm_yang

import pytest
import yaml


BASE_PATH = os.path.dirname(__file__)

test_parser_list = [x.split('/')[-1]
                    for x in glob('{}/test_parser/list/*'.format(BASE_PATH))]
test_parser_leaf = [x.split('/')[-1]
                    for x in glob('{}/test_parser/leaf/*'.format(BASE_PATH))]
test_parser_container = [x.split('/')[-1]
                         for x in glob('{}/test_parser/container/*'.format(BASE_PATH))]


def to_dict(d):
    if isinstance(d, dict):
        d = dict(d)
        for k, v in d.items():
            d[k] = to_dict(v)
    elif isinstance(d, list):
        r = []
        for i in d:
            r.append(to_dict(i))
        d = r
    return d


class Tests(object):

    @pytest.mark.parametrize("case", test_parser_list)
    def test_parser_list(self, case):
        with open("{}/test_parser/list/{}/mocked.txt".format(BASE_PATH, case), 'r') as f:
            mocked = f.read()
        with open("{}/test_parser/list/{}/example.yaml".format(BASE_PATH, case), 'r') as f:
            example = yaml.load(f.read())

        parser = napalm_yang.parsers.get_parser(example["processor"]["name"])({}, {})
        mocked = parser.init_native([mocked])
        parent = mocked[0].get("some_configuration_block", mocked[0])
        bookmarks = {"root_{}".format(example["processor"]["root_name"]): mocked,
                     "parent": parent}

        #  import json
        #  print(json.dumps(to_dict(parent), indent=4))

        processed = False
        attribute = example["processor"]["attribute"]
        for case, d in enumerate(example["data"]):
            processed = True
            parser.keys = d["keys"]
            parser.extra_vars = d["extra_vars"]
            i = 0
            for k, b, e in parser.parse_list(attribute, example["rule"], bookmarks):
                assert k == example["expected"][case][i]["key"]
                b.pop("#list", None)
                assert b == example["expected"][case][i]["block"], \
                    "\n{}".format(yaml.safe_dump(to_dict(b), default_flow_style=False))
                assert e == example["expected"][case][i]["extra_vars"], \
                    "\n{}".format(yaml.safe_dump(to_dict(e), default_flow_style=False))
                i += 1
            assert i == len(example["expected"][case])
        assert processed

    @pytest.mark.parametrize("case", test_parser_leaf)
    def test_parser_leaf(self, case):
        with open("{}/test_parser/leaf/{}/mocked.txt".format(BASE_PATH, case), 'r') as f:
            mocked = f.read()
        with open("{}/test_parser/leaf/{}/example.yaml".format(BASE_PATH, case), 'r') as f:
            example = yaml.load(f.read())

        parser = napalm_yang.parsers.get_parser(example["processor"]["name"])({}, {})
        mocked = parser.init_native([mocked])
        parent = mocked[0].get("some_configuration_block", mocked[0])
        bookmarks = {"root_{}".format(example["processor"]["root_name"]): mocked,
                     "parent": parent}

        #  import json
        #  print(json.dumps(to_dict(parent), indent=4))

        processed = False
        attribute = example["processor"]["attribute"]
        for case, d in enumerate(example["data"]):
            processed = True
            #  parser.keys = d["keys"]
            #  parser.extra_vars = d["extra_vars"]
            i = 0
            for k, b, e in parser.parse_list(attribute, example["parent_rule"], bookmarks):
                bookmarks["parent"] = b
                r = parser.parse_leaf("aintmatter", example["rule"], bookmarks)
                assert r == example["expected"][case][i], example["blocks"][i]
                i += 1
        assert processed

    @pytest.mark.parametrize("case", test_parser_container)
    def test_parser_cointainer(self, case):
        with open("{}/test_parser/container/{}/mocked.txt".format(BASE_PATH, case), 'r') as f:
            mocked = f.read()
        with open("{}/test_parser/container/{}/example.yaml".format(BASE_PATH, case), 'r') as f:
            example = yaml.load(f.read())

        parser = napalm_yang.parsers.get_parser(example["processor"]["name"])({}, {})
        mocked = parser.init_native([mocked])
        parent = mocked[0].get("some_configuration_block", mocked[0])
        bookmarks = {"root_{}".format(example["processor"]["root_name"]): mocked,
                     "parent": parent}

        #  import json
        #  print(json.dumps(to_dict(parent), indent=4))

        processed = False
        for case, d in enumerate(example["data"]):
            processed = True
            #  parser.keys = d["keys"]
            #  parser.extra_vars = d["extra_vars"]
            d, extra_vars = parser.parse_container("aintmatter", example["rule"], bookmarks)
            assert d == example["expected"][case]["result"]
            assert extra_vars == example["expected"][case]["extra_vars"]
        assert processed
