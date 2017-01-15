"""
This module contains a collection of generally useful derived
YANG data types.
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
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

yang = LocalNamespace()



# Imports

# openconfig-extensions



__namespace__ = "urn:ietf:params:xml:ns:yang:ietf-yang-types"
__prefix__ = "yang"
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



# extensions

# features


# typedef

class Counter32(Uint32):
    """
    The counter32 type represents a non-negative integer
    that monotonically increases until it reaches a
    maximum value of 2^32-1 (4294967295 decimal), when it
    wraps around and starts increasing again from zero.
    Counters have no defined 'initial' value, and thus, a
    single value of a counter has (in general) no information
    content.  Discontinuities in the monotonically increasing
    value normally occur at re-initialization of the
    management system, and at other times as specified in the
    description of a schema node using this type.  If such
    other times can occur, for example, the creation of
    a schema node of type counter32 at times other than
    re-initialization, then a corresponding schema node
    should be defined, with an appropriate type, to indicate
    the last discontinuity.
    The counter32 type should not be used for configuration
    schema nodes.  A default statement SHOULD NOT be used in
    combination with the type counter32.
    In the value set and its semantics, this type is equivalent
    to the Counter32 type of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class ZeroBasedCounter32(yang.Counter32):
    """
    The zero-based-counter32 type represents a counter32
    that has the defined 'initial' value zero.
    A schema node of this type will be set to zero (0) on creation
    and will thereafter increase monotonically until it reaches
    a maximum value of 2^32-1 (4294967295 decimal), when it
    wraps around and starts increasing again from zero.
    Provided that an application discovers a new schema node
    of this type within the minimum time to wrap, it can use the
    'initial' value as a delta.  It is important for a management
    station to be aware of this minimum time and the actual time
    between polls, and to discard data if the actual time is too
    long or there is no defined minimum time.
    In the value set and its semantics, this type is equivalent
    to the ZeroBasedCounter32 textual convention of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class Counter64(Uint64):
    """
    The counter64 type represents a non-negative integer
    that monotonically increases until it reaches a
    maximum value of 2^64-1 (18446744073709551615 decimal),
    when it wraps around and starts increasing again from zero.
    Counters have no defined 'initial' value, and thus, a
    single value of a counter has (in general) no information
    content.  Discontinuities in the monotonically increasing
    value normally occur at re-initialization of the
    management system, and at other times as specified in the
    description of a schema node using this type.  If such
    other times can occur, for example, the creation of
    a schema node of type counter64 at times other than
    re-initialization, then a corresponding schema node
    should be defined, with an appropriate type, to indicate
    the last discontinuity.
    The counter64 type should not be used for configuration
    schema nodes.  A default statement SHOULD NOT be used in
    combination with the type counter64.
    In the value set and its semantics, this type is equivalent
    to the Counter64 type of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class ZeroBasedCounter64(yang.Counter64):
    """
    The zero-based-counter64 type represents a counter64 that
    has the defined 'initial' value zero.
    A schema node of this type will be set to zero (0) on creation
    and will thereafter increase monotonically until it reaches
    a maximum value of 2^64-1 (18446744073709551615 decimal),
    when it wraps around and starts increasing again from zero.
    Provided that an application discovers a new schema node
    of this type within the minimum time to wrap, it can use the
    'initial' value as a delta.  It is important for a management
    station to be aware of this minimum time and the actual time
    between polls, and to discard data if the actual time is too
    long or there is no defined minimum time.
    In the value set and its semantics, this type is equivalent
    to the ZeroBasedCounter64 textual convention of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class Gauge32(Uint32):
    """
    The gauge32 type represents a non-negative integer, which
    may increase or decrease, but shall never exceed a maximum
    value, nor fall below a minimum value.  The maximum value
    cannot be greater than 2^32-1 (4294967295 decimal), and
    the minimum value cannot be smaller than 0.  The value of
    a gauge32 has its maximum value whenever the information
    being modeled is greater than or equal to its maximum
    value, and has its minimum value whenever the information
    being modeled is smaller than or equal to its minimum value.
    If the information being modeled subsequently decreases
    below (increases above) the maximum (minimum) value, the
    gauge32 also decreases (increases).
    In the value set and its semantics, this type is equivalent
    to the Gauge32 type of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class Gauge64(Uint64):
    """
    The gauge64 type represents a non-negative integer, which
    may increase or decrease, but shall never exceed a maximum
    value, nor fall below a minimum value.  The maximum value
    cannot be greater than 2^64-1 (18446744073709551615), and
    the minimum value cannot be smaller than 0.  The value of
    a gauge64 has its maximum value whenever the information
    being modeled is greater than or equal to its maximum
    value, and has its minimum value whenever the information
    being modeled is smaller than or equal to its minimum value.
    If the information being modeled subsequently decreases
    below (increases above) the maximum (minimum) value, the
    gauge64 also decreases (increases).
    In the value set and its semantics, this type is equivalent
    to the CounterBasedGauge64 SMIv2 textual convention defined
    in RFC 2856
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class ObjectIdentifier(String):
    """
    The object-identifier type represents administratively
    assigned names in a registration-hierarchical-name tree.
    Values of this type are denoted as a sequence of numerical
    non-negative sub-identifier values.  Each sub-identifier
    value MUST NOT exceed 2^32-1 (4294967295).  Sub-identifiers
    are separated by single dots and without any intermediate
    whitespace.
    The ASN.1 standard restricts the value space of the first
    sub-identifier to 0, 1, or 2.  Furthermore, the value space
    of the second sub-identifier is restricted to the range
    0 to 39 if the first sub-identifier is 0 or 1.  Finally,
    the ASN.1 standard requires that an object identifier
    has always at least two sub-identifiers.  The pattern
    captures these restrictions.
    Although the number of sub-identifiers is not limited,
    module designers should realize that there may be
    implementations that stick with the SMIv2 limit of 128
    sub-identifiers.
    This type is a superset of the SMIv2 OBJECT IDENTIFIER type
    since it is not restricted to 128 sub-identifiers.  Hence,
    this type SHOULD NOT be used to represent the SMIv2 OBJECT
    IDENTIFIER type; the object-identifier-128 type SHOULD be
    used instead.
    """
    def __init__(self, _meta=None, pattern = "(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class ObjectIdentifier128(ObjectIdentifier):
    """
    This type represents object-identifiers restricted to 128
    sub-identifiers.
    In the value set and its semantics, this type is equivalent
    to the OBJECT IDENTIFIER type of the SMIv2.
    """
    def __init__(self, _meta=None, pattern = "\\d*(\\.\\d*){1,127}", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class YangIdentifier(String):
    """
    A YANG identifier string as defined by the 'identifier'
    rule in Section 12 of RFC 6020.  An identifier must
    start with an alphabetic character or an underscore
    followed by an arbitrary sequence of alphabetic or
    numeric characters, underscores, hyphens, or dots.
    A YANG identifier MUST NOT start with any possible
    combination of the lowercase or uppercase character
    sequence 'xml'.
    """
    def __init__(self, _meta=None, pattern = "[a-zA-Z_][a-zA-Z0-9\\-_.]*", length = "1..max", ):
        super().__init__(_meta=_meta, pattern = pattern, length = length, )

class DateAndTime(String):
    """
    The date-and-time type is a profile of the ISO 8601
    standard for representation of dates and times using the
    Gregorian calendar.  The profile is defined by the
    date-time production in Section 5.6 of RFC 3339.
    The date-and-time type is compatible with the dateTime XML
    schema type with the following notable exceptions:
    (a) The date-and-time type does not allow negative years.
    (b) The date-and-time time-offset -00:00 indicates an unknown
        time zone (see RFC 3339) while -00:00 and +00:00 and Z
        all represent the same time zone in dateTime.
    (c) The canonical format (see below) of data-and-time values
        differs from the canonical format used by the dateTime XML
        schema type, which requires all times to be in UTC using
        the time-offset 'Z'.
    This type is not equivalent to the DateAndTime textual
    convention of the SMIv2 since RFC 3339 uses a different
    separator between full-date and full-time and provides
    higher resolution of time-secfrac.
    The canonical format for date-and-time values with a known time
    zone uses a numeric time zone offset that is calculated using
    the device's configured known offset to UTC time.  A change of
    the device's offset to UTC time will cause date-and-time values
    to change accordingly.  Such changes might happen periodically
    in case a server follows automatically daylight saving time
    (DST) time zone offset changes.  The canonical format for
    date-and-time values with an unknown time zone (usually
    referring to the notion of local time) uses the time-offset
    -00:00.
    """
    def __init__(self, _meta=None, pattern = "\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class Timeticks(Uint32):
    """
    The timeticks type represents a non-negative integer that
    represents the time, modulo 2^32 (4294967296 decimal), in
    hundredths of a second between two epochs.  When a schema
    node is defined that uses this type, the description of
    the schema node identifies both of the reference epochs.
    In the value set and its semantics, this type is equivalent
    to the TimeTicks type of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class Timestamp(yang.Timeticks):
    """
    The timestamp type represents the value of an associated
    timeticks schema node at which a specific occurrence
    happened.  The specific occurrence must be defined in the
    description of any schema node defined using this type.  When
    the specific occurrence occurred prior to the last time the
    associated timeticks attribute was zero, then the timestamp
    value is zero.  Note that this requires all timestamp values
    to be reset to zero when the value of the associated timeticks
    attribute reaches 497+ days and wraps around to zero.
    The associated timeticks schema node must be specified
    in the description of any schema node using this type.
    In the value set and its semantics, this type is equivalent
    to the TimeStamp textual convention of the SMIv2.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class PhysAddress(String):
    """
    Represents media- or physical-level addresses represented
    as a sequence octets, each octet represented by two hexadecimal
    numbers.  Octets are separated by colons.  The canonical
    representation uses lowercase characters.
    In the value set and its semantics, this type is equivalent
    to the PhysAddress textual convention of the SMIv2.
    """
    def __init__(self, _meta=None, pattern = "([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class MacAddress(String):
    """
    The mac-address type represents an IEEE 802 MAC address.
    The canonical representation uses lowercase characters.
    In the value set and its semantics, this type is equivalent
    to the MacAddress textual convention of the SMIv2.
    """
    def __init__(self, _meta=None, pattern = "[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class Xpath10(String):
    """
    This type represents an XPATH 1.0 expression.
    When a schema node is defined that uses this type, the
    description of the schema node MUST specify the XPath
    context in which the XPath expression is evaluated.
    """
    def __init__(self, _meta=None, ):
        super().__init__(_meta=_meta, )

class HexString(String):
    """
    A hexadecimal string with octets represented as hex digits
    separated by colons.  The canonical representation uses
    lowercase characters.
    """
    def __init__(self, _meta=None, pattern = "([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class Uuid(String):
    """
    A Universally Unique IDentifier in the string representation
    defined in RFC 4122.  The canonical representation uses
    lowercase characters.
    The following is an example of a UUID in string representation:
    f81d4fae-7dec-11d0-a765-00a0c91e6bf6
    """
    def __init__(self, _meta=None, pattern = "[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}", ):
        super().__init__(_meta=_meta, pattern = pattern, )

class DottedQuad(String):
    """
    An unsigned 32-bit number expressed in the dotted-quad
    notation, i.e., four octets written as decimal numbers
    and separated with the '.' (full stop) character.
    """
    def __init__(self, _meta=None, pattern = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])", ):
        super().__init__(_meta=_meta, pattern = pattern, )


# Identities

# Classes to support containers and lists


# Top-uses

# Top-containers