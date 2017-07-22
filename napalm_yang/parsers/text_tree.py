#  from builtins import super
from collections import OrderedDict

from napalm_yang.parsers.jsonp import JSONParser


def _attach_data_to_path(obj, path, data):
    path = path.split(" ")

    while True:
        obj["#text"] = " ".join(path)
        p = path.pop(0)
        if not path:
            break
        else:
            if p not in obj:
                obj[p] = OrderedDict()
            obj = obj[p]
    obj[p] = data


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
            _attach_data_to_path(parsed, last, current)
        elif leading_spaces < current_indent:
            config.insert(0, line)
            break
        else:
            if not nested:
                current = parse_indented_config(config, leading_spaces, current_indent, True)
                _attach_data_to_path(parsed, last, current)
            else:
                config.insert(0, line)
                break

    return parsed


class TextTree(JSONParser):

    @classmethod
    def init_native(cls, native):
        resp = []
        for n in native:
            if isinstance(n, dict):
                resp.append(n)
            else:
                resp.append(parse_indented_config(n.splitlines()))
        return resp

    #  @classmethod
    #  def _parse_leaf_default(cls, mapping, data, check_default=True, check_presence=False):
    #      attribute = mapping.get("attribute", None)
    #      if attribute:
    #          attribute = "@{}".format(attribute)
    #          mapping["path"] = "{}.{}".format(mapping["path"], attribute)
    #      elif not check_presence:
    #          mapping["path"] = "{}.{}".format(mapping["path"], "#text")
    #      return super()._parse_leaf_default(mapping, data, check_default, check_presence)
