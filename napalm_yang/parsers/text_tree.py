from builtins import super
from collections import OrderedDict

from napalm_yang.parsers.jsonp import JSONParser


def _attach_data_to_path(obj, path, data, list_=False):
    if "#list" not in obj:
        obj["#list"] = []

    path = path.split(" ")
    o = obj
    first = True

    while True:
        o["#text"] = " ".join(path)
        p = path.pop(0)
        if not path:
            break
        else:
            if p not in o:
                o[p] = OrderedDict()
            o = o[p]

            if first and list_:
                obj["#list"].append({p: o})
                first = False
    if p in o:
        o[p].update(data)
    else:
        o[p] = data

    # We add a standalong flag to be able to distinguish this situation:
    # switchport
    # switchport mode access
    o[p]["#standalone"] = True


def parse_indented_config(config, current_indent=0, previous_indent=0, nested=False):
    """
    This methid basically reads a configuration that conforms to a very poor industry standard
    and returns a nested structure that behaves like a dict. For example:
        {'enable password whatever': {},
         'interface GigabitEthernet1': {
             'description "bleh"': {},
             'fake nested': {
                 'nested nested configuration': {}},
             'switchport mode trunk': {}},
         'interface GigabitEthernet2': {
             'no ip address': {}},
         'interface GigabitEthernet3': {
             'negotiation auto': {},
             'no ip address': {},
             'shutdown': {}},
         'interface Loopback0': {
             'description "blah"': {}}}
    """
    parsed = OrderedDict()
    while True:
        if not config:
            break
        line = config.pop(0)

        if line.startswith("!"):
            continue

        last = line.lstrip()
        leading_spaces = len(line) - len(last)

        #  print("current_indent:{}, previous:{}, leading:{} - {}".format(
        #        current_indent, previous_indent, leading_spaces, line))

        if leading_spaces > current_indent:
            current = parse_indented_config(config, leading_spaces, current_indent, True)
            _attach_data_to_path(parsed, last, current, nested)
        elif leading_spaces < current_indent:
            config.insert(0, line)
            break
        else:
            if not nested:
                current = parse_indented_config(config, leading_spaces, current_indent, True)
                _attach_data_to_path(parsed, last, current, nested)
            else:
                config.insert(0, line)
                break

    return parsed


class TextTree(JSONParser):

    def init_native(self, native):
        resp = []
        for n in native:
            if isinstance(n, dict):
                resp.append(n)
            else:
                resp.append(parse_indented_config(n.splitlines()))

        #  with open("/tmp/napalm-tree-parser", "w+") as f:
        #      import json
        #      f.write(json.dumps(resp[0]["interface"]["Ethernet1"], indent=4))
        #  raise Exception

        return resp

    def _parse_leaf_default(self, mapping, data, check_default=True, check_presence=False):
        extra_path = "#standalone" if check_presence else "#text"
        if "path" in mapping:
            mapping["path"] = "{}.{}".format(mapping["path"], extra_path)
        else:
            mapping["path"] = extra_path
        return super()._parse_leaf_default(mapping, data, check_default, check_presence)
