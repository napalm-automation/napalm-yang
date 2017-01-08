"""
This module contains a collection of generally useful derived
YANG data types for Internet addresses and related things.
Copyright (c) 2013 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http://trustee.ietf.org/license-info).
This version of this YANG module is part of RFC 6991; see
the RFC itself for full legal notices.
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()


__namespace__ = "urn:ietf:params:xml:ns:yang:ietf-inet-types"
__contact__ = "WG Web:   <http://tools.ietf.org/wg/netmod/>\nWG List:  <mailto:netmod@ietf.org>\nWG Chair: David Kessens\n          <mailto:david.kessens@nsn.com>\nWG Chair: Juergen Schoenwaelder\n          <mailto:j.schoenwaelder@jacobs-university.de>\nEditor:   Juergen Schoenwaelder\n          <mailto:j.schoenwaelder@jacobs-university.de>"
__organization__ = "IETF NETMOD (NETCONF Data Modeling Language) Working Group"
__revision__ = {
    "2010-09-24": {
        "revision": "2010-09-24"
    }, 
    "2013-07-15": {
        "revision": "2013-07-15"
    }
}



# typedef

class Ipv4Prefix(yang_base.BaseBinding):
    """
    The ipv4-prefix type represents an IPv4 address prefix.
    The prefix length is given by the number following the
    slash character and must be less than or equal to 32.
    A prefix length value of n corresponds to an IP address
    mask that has n contiguous 1-bits from the most
    significant bit (MSB) and all other bits set to 0.
    The canonical format of an IPv4 prefix has all bits of
    the IPv4 address set to zero that are not part of the
    IPv4 prefix.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv4_prefix = yang.String(pattern="(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))", )


class Ipv6Prefix(yang_base.BaseBinding):
    """
    The ipv6-prefix type represents an IPv6 address prefix.
    The prefix length is given by the number following the
    slash character and must be less than or equal to 128.
    A prefix length value of n corresponds to an IP address
    mask that has n contiguous 1-bits from the most
    significant bit (MSB) and all other bits set to 0.
    The IPv6 address should have all bits that do not belong
    to the prefix set to zero.
    The canonical format of an IPv6 prefix has all bits of
    the IPv6 address set to zero that are not part of the
    IPv6 prefix.  Furthermore, the IPv6 address is represented
    as defined in Section 4 of RFC 5952.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv6_prefix = yang.String(pattern="((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))", )


class IpAddressNoZone(yang_base.BaseBinding):
    """
    The ip-address-no-zone type represents an IP address and is
    IP version neutral.  The format of the textual representation
    implies the IP version.  This type does not support scoped
    addresses since it does not allow zone identifiers in the
    address format.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ip_address_no_zone = yang.Union(type="defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'inet:ipv4-address-no-zone': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {}), u'inet:ipv6-address-no-zone': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {})})", )


class IpVersion(yang_base.BaseBinding):
    """
    This value represents the version of the IP protocol.
    In the value set and its semantics, this type is equivalent
    to the InetVersion textual convention of the SMIv2.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ip_version = yang.Enumeration(enum="defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'unknown': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {'info': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'description': u'An unknown or unspecified version of the Internet\nprotocol.'}), u'value': u'0'}), u'ipv4': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {'info': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'description': u'The IPv4 protocol as defined in RFC 791.'}), u'value': u'1'}), u'ipv6': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {'info': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'description': u'The IPv6 protocol as defined in RFC 2460.'}), u'value': u'2'})})", )


class Dscp(yang_base.BaseBinding):
    """
    The dscp type represents a Differentiated Services Code Point
    that may be used for marking packets in a traffic stream.
    In the value set and its semantics, this type is equivalent
    to the Dscp textual convention of the SMIv2.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.dscp = yang.Uint8(range="0..63", )


class IpPrefix(yang_base.BaseBinding):
    """
    The ip-prefix type represents an IP prefix and is IP
    version neutral.  The format of the textual representations
    implies the IP version.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ip_prefix = yang.Union(type="defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'inet:ipv6-prefix': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {}), u'inet:ipv4-prefix': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {})})", )


class Ipv6AddressNoZone(yang_base.BaseBinding):
    """
    An IPv6 address without a zone index.  This type, derived from
    ipv6-address, may be used in situations where the zone is
    known from the context and hence no zone index is needed.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv6_address_no_zone = yang.inet.Ipv6Address(pattern="[0-9a-fA-F:\.]*", )


class Uri(yang_base.BaseBinding):
    """
    The uri type represents a Uniform Resource Identifier
    (URI) as defined by STD 66.
    Objects using the uri type MUST be in US-ASCII encoding,
    and MUST be normalized as described by RFC 3986 Sections
    6.2.1, 6.2.2.1, and 6.2.2.2.  All unnecessary
    percent-encoding is removed, and all case-insensitive
    characters are set to lowercase except for hexadecimal
    digits, which are normalized to uppercase as described in
    Section 6.2.2.1.
    The purpose of this normalization is to help provide
    unique URIs.  Note that this normalization is not
    sufficient to provide uniqueness.  Two URIs that are
    textually distinct after this normalization may still be
    equivalent.
    Objects using the uri type may restrict the schemes that
    they permit.  For example, 'data:' and 'urn:' schemes
    might not be appropriate.
    A zero-length URI is not a valid URI.  This can be used to
    express 'URI absent' where required.
    In the value set and its semantics, this type is equivalent
    to the Uri SMIv2 textual convention defined in RFC 5017.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.uri = yang.String()


class PortNumber(yang_base.BaseBinding):
    """
    The port-number type represents a 16-bit port number of an
    Internet transport-layer protocol such as UDP, TCP, DCCP, or
    SCTP.  Port numbers are assigned by IANA.  A current list of
    all assignments is available from <http://www.iana.org/>.
    Note that the port number value zero is reserved by IANA.  In
    situations where the value zero does not make sense, it can
    be excluded by subtyping the port-number type.
    In the value set and its semantics, this type is equivalent
    to the InetPortNumber textual convention of the SMIv2.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.port_number = yang.Uint16(range="0..65535", )


class Ipv4AddressNoZone(yang_base.BaseBinding):
    """
    An IPv4 address without a zone index.  This type, derived from
    ipv4-address, may be used in situations where the zone is
    known from the context and hence no zone index is needed.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv4_address_no_zone = yang.inet.Ipv4Address(pattern="[0-9\.]*", )


class Host(yang_base.BaseBinding):
    """
    The host type represents either an IP address or a DNS
    domain name.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.host = yang.Union(type="defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'inet:domain-name': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {}), u'inet:ip-address': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {})})", )


class DomainName(yang_base.BaseBinding):
    """
    The domain-name type represents a DNS domain name.  The
    name SHOULD be fully qualified whenever possible.
    Internet domain names are only loosely specified.  Section
    3.5 of RFC 1034 recommends a syntax (modified in Section
    2.1 of RFC 1123).  The pattern above is intended to allow
    for current practice in domain name use, and some possible
    future expansion.  It is designed to hold various types of
    domain names, including names used for A or AAAA records
    (host names) and other records, such as SRV records.  Note
    that Internet host names have a stricter syntax (described
    in RFC 952) than the DNS recommendations in RFCs 1034 and
    1123, and that systems that want to store host names in
    schema nodes using the domain-name type are recommended to
    adhere to this stricter standard to ensure interoperability.
    The encoding of DNS names in the DNS protocol is limited
    to 255 characters.  Since the encoding consists of labels
    prefixed by a length bytes and there is a trailing NULL
    byte, only 253 characters can appear in the textual dotted
    notation.
    The description clause of schema nodes using the domain-name
    type MUST describe when and how these names are resolved to
    IP addresses.  Note that the resolution of a domain-name value
    may require to query multiple DNS records (e.g., A for IPv4
    and AAAA for IPv6).  The order of the resolution process and
    which DNS record takes precedence can either be defined
    explicitly or may depend on the configuration of the
    resolver.
    Domain-name values use the US-ASCII encoding.  Their canonical
    format uses lowercase US-ASCII characters.  Internationalized
    domain names MUST be A-labels as per RFC 5890.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.domain_name = yang.String(pattern="((([a-zA-Z0-9_]([a-zA-Z0-9\-_]){0,61})?[a-zA-Z0-9]\.)*([a-zA-Z0-9_]([a-zA-Z0-9\-_]){0,61})?[a-zA-Z0-9]\.?)|\.", length="1..253", )


class Ipv6FlowLabel(yang_base.BaseBinding):
    """
    The ipv6-flow-label type represents the flow identifier or Flow
    Label in an IPv6 packet header that may be used to
    discriminate traffic flows.
    In the value set and its semantics, this type is equivalent
    to the IPv6FlowLabel textual convention of the SMIv2.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv6_flow_label = yang.Uint32(range="0..1048575", )


class IpAddress(yang_base.BaseBinding):
    """
    The ip-address type represents an IP address and is IP
    version neutral.  The format of the textual representation
    implies the IP version.  This type supports scoped addresses
    by allowing zone identifiers in the address format.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ip_address = yang.Union(type="defaultdict(<function _nested_default_dict at 0x10e1c8578>, {u'inet:ipv6-address': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {}), u'inet:ipv4-address': defaultdict(<function _nested_default_dict at 0x10e1c8578>, {})})", )


class Ipv6Address(yang_base.BaseBinding):
    """
    The ipv6-address type represents an IPv6 address in full,
    mixed, shortened, and shortened-mixed notation.  The IPv6
    address may include a zone index, separated by a % sign.
    The zone index is used to disambiguate identical address
    values.  For link-local addresses, the zone index will
    typically be the interface index number or the name of an
    interface.  If the zone index is not present, the default
    zone of the device will be used.
    The canonical format of IPv6 addresses uses the textual
    representation defined in Section 4 of RFC 5952.  The
    canonical format for the zone index is the numerical
    format as described in Section 11.2 of RFC 4007.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv6_address = yang.String(pattern="((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\p{N}\p{L}]+)?", )


class Ipv4Address(yang_base.BaseBinding):
    """
    The ipv4-address type represents an IPv4 address in
    dotted-quad notation.  The IPv4 address may include a zone
    index, separated by a % sign.
    The zone index is used to disambiguate identical address
    values.  For link-local addresses, the zone index will
    typically be the interface index number or the name of an
    interface.  If the zone index is not present, the default
    zone of the device will be used.
    The canonical format for the zone index is the numerical
    format
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.ipv4_address = yang.String(pattern="(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\p{N}\p{L}]+)?", )


class AsNumber(yang_base.BaseBinding):
    """
    The as-number type represents autonomous system numbers
    which identify an Autonomous System (AS).  An AS is a set
    of routers under a single technical administration, using
    an interior gateway protocol and common metrics to route
    packets within the AS, and using an exterior gateway
    protocol to route packets to other ASes.  IANA maintains
    the AS number space and has delegated large parts to the
    regional registries.
    Autonomous system numbers were originally limited to 16
    bits.  BGP extensions have enlarged the autonomous system
    number space to 32 bits.  This type therefore uses an uint32
    base type without a range restriction in order to support
    a larger autonomous system number space.
    In the value set and its semantics, this type is equivalent
    to the InetAutonomousSystemNumber textual convention of
    the SMIv2.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.as_number = yang.Uint32()



# Identities

# Classes to support containers and lists


# Top-uses
# Top-containers{}