"""
This module defines data related to packet header fields
used in matching operations, for example in ACLs.  When a
field is omitted from a match expression, the effect is a
wildcard ('any') for that field.
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports
from napalm_yang import oc_ext
from napalm_yang import yang
from napalm_yang import oc_pkt_match_types
from napalm_yang import inet

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()
openconfig_extensions.openconfig_version = "0.2.0"


__namespace__ = "http://openconfig.net/yang/header-fields"
__yang_version__ = "1"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-04-27": {
        "revision": "2016-04-27"
    }, 
    "2016-08-08": {
        "revision": "2016-08-08"
    }
}



# typedef


# Identities

# Classes to support containers and lists



class EthernetHeaderConfig(yang_base.BaseBinding):
    """
    Configuration data of fields in Ethernet header.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.source_mac_mask = yang.MacAddress(_meta={"mandatory": False}, )
        self.ethertype = oc_pkt_match_types.EthertypeType(_meta={"mandatory": False}, )
        self.source_mac = yang.MacAddress(_meta={"mandatory": False}, )
        self.destination_mac = yang.MacAddress(_meta={"mandatory": False}, )
        self.destination_mac_mask = yang.MacAddress(_meta={"mandatory": False}, )
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetHeaderState(yang_base.BaseBinding):
    """
    State information of fields in Ethernet header.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class L2_Config_94(EthernetHeaderConfig):
    """
    Configuration data
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class L2_State_100(EthernetHeaderState, EthernetHeaderConfig):
    """
    State Information.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class EthernetHeaderTop_L2_90(yang_base.BaseBinding):
    """
    Ethernet header fields
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = L2_Config_94()
        self.state = L2_State_100()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class EthernetHeaderTop(yang_base.BaseBinding):
    """
    Top level container for fields in Ethernet header.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.l2 = EthernetHeaderTop_L2_90()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpProtocolFieldsConfig(yang_base.BaseBinding):
    """
    Configuration data of IP protocol fields
    common to ipv4 and ipv6
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.protocol = oc_pkt_match_types.IpProtocolType(_meta={"mandatory": False}, )
        self.source_ip_flow_label = inet.Ipv6FlowLabel(_meta={"mandatory": False}, )
        self.destination_ip_address = inet.IpPrefix(_meta={"mandatory": False}, )
        self.dscp = inet.Dscp(_meta={"mandatory": False}, )
        self.ip_version = inet.IpVersion(_meta={"mandatory": False}, )
        self.source_ip_address = inet.IpPrefix(_meta={"mandatory": False}, )
        self.destination_ip_flow_label = inet.Ipv6FlowLabel(_meta={"mandatory": False}, )
        self.hop_limit = Uint8(_meta={"mandatory": False}, range="0..255")
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpProtocolFieldsState(yang_base.BaseBinding):
    """
    State information of IP header fields common to ipv4 and ipv6
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ip_Config_184(IpProtocolFieldsConfig):
    """
    Configuration data
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Ip_State_190(IpProtocolFieldsState, IpProtocolFieldsConfig):
    """
    State information
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class IpProtocolFieldsTop_Ip_180(yang_base.BaseBinding):
    """
    Top level container
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = Ip_Config_184()
        self.state = Ip_State_190()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class IpProtocolFieldsTop(yang_base.BaseBinding):
    """
    IP header fields common to ipv4 and ipv6
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.ip = IpProtocolFieldsTop_Ip_180()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TransportFieldsConfig(yang_base.BaseBinding):
    """
    Configuration data of transport-layer packet fields
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        self.destination_port = oc_pkt_match_types.PortNumRange(_meta={"mandatory": False}, )
        self.source_port = oc_pkt_match_types.PortNumRange(_meta={"mandatory": False}, )
        # leaflist
        self.tcp_flags = yang.LeafList(Identityref(_meta={"mandatory": False}, base="oc-pkt-match-types:TCP_FLAGS"))
        # Meta
        self._meta["config"] = True
        




class TransportFieldsState(yang_base.BaseBinding):
    """
    State data of transport-fields
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Transport_Config_239(TransportFieldsConfig):
    """
    Configuration data
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class Transport_State_245(TransportFieldsState, TransportFieldsConfig):
    """
    State data
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = False
        




class TransportFieldsTop_Transport_235(yang_base.BaseBinding):
    """
    Transport fields container
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.config = Transport_Config_239()
        self.state = Transport_State_245()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        




class TransportFieldsTop(yang_base.BaseBinding):
    """
    Destination transport-fields top level grouping
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        # container
        self.transport = TransportFieldsTop_Transport_235()
        # list
        # leaf
        # leaflist
        # Meta
        self._meta["config"] = True
        



# Top-uses
# Top-containers{}