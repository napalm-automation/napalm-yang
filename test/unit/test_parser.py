import os
from glob import glob

import napalm_yang

import pytest
import yaml


BASE_PATH = os.path.dirname(__file__)

test_parser = [x.split('/')[-1]
               for x in glob('{}/test_parser/*'.format(BASE_PATH))]


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

    @pytest.mark.parametrize("case", test_parser)
    def test_parser(self, case):
        with open("{}/test_parser/{}/mocked.txt".format(BASE_PATH, case), 'r') as f:
            mocked = f.read()
        with open("{}/test_parser/{}/example.yaml".format(BASE_PATH, case), 'r') as f:
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
        if example["processor"]["node_type"] == "list":
            for case, d in enumerate(example["data"]):
                processed = True
                parser.keys = d["keys"]
                parser.extra_vars = d["extra_vars"]
                bookmarks.update(d.get("bookmarks", {}))
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
        else:
            raise Exception(example["node_type"])
        assert processed
