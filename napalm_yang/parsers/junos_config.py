from napalm_yang.jinja_filters.vlan_filters import vlan_range_to_oc
from napalm_yang.parsers.base import _resolve_path
from napalm_yang.parsers.jsonp import JSONParser


class JunosConfig(JSONParser):

    def openconfig_vlan_switched_vlan(self, parser):
        result = {"switched-vlan": {"config": {}}}
        config = result["switched-vlan"]["config"]

        try:
            d = _resolve_path(parser.bookmarks["parent"], ["unit", "family", "ethernet-switching"])
        except Exception:
            return
        vlans = _resolve_path(d, ["vlan", "members"])
        if isinstance(vlans, list):
            vlans = ",".join([v["#text"] for v in vlans])
        else:
            vlans = vlans["#text"]
            if vlans == "all":
                vlans = "1-4094"

        if d["interface-mode"]["#text"] == "trunk":
            config["interface-mode"] = "TRUNK"
            config["trunk-vlans"] = vlan_range_to_oc(vlans)
        else:
            config["interface-mode"] = "ACCESS"
            config["access-vlans"] = vlans
        parser.bookmarks["parent"] = result
