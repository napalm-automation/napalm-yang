import napalm_yang


class Tests(object):

    def test_resolve_path_dict(self):
        data = {
            "simple": {
                "path": 123
            }
        }
        path = "simple.path"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        assert result == 123

    def test_resolve_path_list(self):
        data = {
            "simple": [
                {"path": 123}
            ]
        }
        path = "simple.0.path"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        assert result == 123

    def test_extract_value_simple(self):
        data = {
            "group": {
                "group_1": {
                    "data": {"whatever": 1},
                    "subgroup": {
                        "subgroup_1": {"path": 2},
                        "subgroup_2": {"path": 3},
                    },
                },
                "group_2": {
                    "data": {"whatever": 4},
                    "subgroup": {
                        "subgroup_3": {"path": 5},
                        "subgroup_4": {"path": 6},
                    },
                }
            }
        }
        path = "group.?name"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        expected = [
            {'data': {'whatever': 1},
             'name': 'group_1',
             'subgroup': {'subgroup_1': {'path': 2}, 'subgroup_2': {'path': 3}}},
            {'data': {'whatever': 4},
             'name': 'group_2',
             'subgroup': {'subgroup_3': {'path': 5}, 'subgroup_4': {'path': 6}}}]
        assert result == expected or result == list(reversed(expected))

    def test_extract_value_nested(self):
        data = {
            "group": {
                "group_1": {
                    "data": {"whatever": 1},
                    "subgroup": {
                        "subgroup_1": {"path": 2},
                        "subgroup_2": {"path": 3},
                    },
                },
                "group_2": {
                    "data": {"whatever": 4},
                    "subgroup": {
                        "subgroup_3": {"path": 5},
                        "subgroup_4": {"path": 6},
                    },
                }
            }
        }
        path = "group.?name>group.subgroup.?subname"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        expected = [
            {'group': {'data': {'whatever': 1}},
             'name': 'group_1',
             'path': 2,
             'subname': 'subgroup_1'},
            {'group': {'data': {'whatever': 1}},
             'name': 'group_1',
             'path': 3,
             'subname': 'subgroup_2'},
            {'group': {'data': {'whatever': 4}},
             'name': 'group_2',
             'path': 5,
             'subname': 'subgroup_3'},
            {'group': {'data': {'whatever': 4}},
             'name': 'group_2',
             'path': 6,
             'subname': 'subgroup_4'}]
        assert sorted(result, key=lambda k: k['subname']) == expected

    def test_extract_value_nested_list(self):
        data = {
            "group": [{"name": "group_1",
                       "data": {"whatever": 1},
                       "subgroup": [{"name": "subgroup_1", "path": 2},
                                    {"name": "subgroup_2", "path": 3}]},
                      {"name": "group_2",
                       "data": {"whatever": 4},
                       "subgroup": [{"name": "subgroup_3", "path": 5},
                                    {"name": "subgroup_4", "path": 6}]}]}
        path = "group.?group:name.subgroup.?subgroup:name"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        expected = [
            {'data': {'whatever': 1}, 'group': 'group_1',
             'path': 2, 'subgroup': 'subgroup_1'},
            {'data': {'whatever': 1}, 'group': 'group_1',
             'path': 3, 'subgroup': 'subgroup_2'},
            {'data': {'whatever': 4}, 'group': 'group_2',
             'path': 5, 'subgroup': 'subgroup_3'},
            {'data': {'whatever': 4}, 'group': 'group_2',
             'path': 6, 'subgroup': 'subgroup_4'}]
        assert sorted(result, key=lambda k: k['subgroup']) == expected

    def test_junos_neighbor(self):
        data = {"group": [{"name": {"#text": "my_peers"},
                           "neighbor": [
                                {
                                    "name": {"#text": "192.168.100.2"},
                                    "description": {"#text": "adsasd"},
                                    "peer-as": {"#text": "65100"}
                                },
                                {
                                    "name": {"#text": "192.168.100.3"},
                                    "peer-as": {"#text": "65100"}}]},
                          {"name": {"#text": "my_other_peers"},
                           "neighbor": {
                              "name": {"#text": "172.20.0.1"},
                              "peer-as": {"#text": "65200"}}}]}
        path = "group.?peer_group:name.neighbor.?neighbor:name"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        expected = [
            {'neighbor': {'#text': '172.20.0.1'},
             'peer-as': {'#text': '65200'},
             'peer_group': {'#text': 'my_other_peers'}},
            {'description': {'#text': 'adsasd'},
             'neighbor': {'#text': '192.168.100.2'},
             'peer-as': {'#text': '65100'},
             'peer_group': {'#text': 'my_peers'}},
            {'neighbor': {'#text': '192.168.100.3'},
             'peer-as': {'#text': '65100'},
             'peer_group': {'#text': 'my_peers'}}]
        assert sorted(result, key=lambda k: k['neighbor']) == expected

    def test_ios_ip_addresses(self):
        data = {"ip": {"address": {"192.168.2.1": {
                                       "255.255.255.0": {
                                           "secondary": {"#standalone": True}}},
                                   "192.168.1.1": {
                                        "255.255.255.0": {"#standalone": True}},
                                   "172.20.0.1": {
                                        "255.255.255.0": {
                                            "secondary": {"#standalone": True}}}}}}

        path = "ip.address.?prefix.?mask"
        result = napalm_yang.parsers.base.BaseParser({}, {}).resolve_path(data, path)
        expected = [{'mask': '255.255.255.0',
                     'prefix': '172.20.0.1',
                     'secondary': {'#standalone': True}},
                    {'#standalone': True,
                     'mask': '255.255.255.0',
                     'prefix': '192.168.1.1'},
                    {'mask': '255.255.255.0',
                     'prefix': '192.168.2.1',
                     'secondary': {'#standalone': True}}]
        assert sorted(result, key=lambda k: k['prefix']) == expected
