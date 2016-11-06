"""openconfig-interfaces."""

from napalm_yang import yang_types
from napalm_yang import yang_base

__module__ = "openconfig-interfaces"

__description__ = """Model for managing network interfaces and subinterfaces.  This
module also defines convenience types / groupings for other
models to create references to interfaces:

 base-interface-ref (type) -  reference to a base interface
 interface-ref (grouping) -  container for reference to a
   interface + subinterface
 interface-ref-state (grouping) - container for read-only
   (opstate) reference to interface + subinterface

This model reuses data items defined in the IETF YANG model for
interfaces described by RFC 7223 with an alternate structure
(particularly for operational state data) and and with
additional configuration items."""

__namespace__ = 'http://openconfig.net/yang/interfaces'

__yang_version__ = '1'

__prefix__ = 'oc-if'

__contact__ = """OpenConfig working group
netopenconfig@googlegroups.com"""

__organization__ = 'OpenConfig working group'


__openconfig_extensions__ = {
  'openconfig-version': '1.0.2',
 }

__revision__ = {
  '2016-05-26': {
      'description': {
          'options': {},
          'value': 'OpenConfig public release',
         },
      'reference': {
          'options': {},
          'value': '1.0.2',
         },
     },
 }


# typedef
class InterfaceId(yang_types.string):
    """
    User-defined identifier for an interface, generally used to
    name a interface reference.  The id can be arbitrary but a
    useful convention is to use a combination of base interface
    name and subinterface index.
    """


# typedef
class BaseInterfaceRef(yang_types.leafref):
    """
    Reusable type for by-name reference to a base interface.
    This type may be used in cases where ability to reference
    a subinterface is not required.
    """
    path = "{'options': {}, 'value': u'/oc-if:interfaces/oc-if:interface/oc-if:name'}"


# discovered_classes
class InterfacesTop_Interfaces(yang_base.BaseBinding):
    """
    Top level container for interfaces, including configuration
    and state data.
    """
    config = False
    container = {}
    leaf = {}
    list_ = {u'interface': 'interfaces_interface'}
    uses = []


# discovered_classes
class InterfacePhysHoldtimeTop_HoldTime(yang_base.BaseBinding):
    """
    Top-level container for hold-time settings to enable
    dampening advertisements of interface transitions.
    """
    config = False
    container = {'state': 'HoldTime_State', 'config': 'HoldTime_Config', }
    leaf = {}
    list_ = {}
    uses = []


# discovered_classes
class Interface_Config(yang_base.BaseBinding):
    """
    Configurable items at the global, physical interface
    level
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-phys-config']


# discovered_classes
class Unnumbered_Config(yang_base.BaseBinding):
    """
    Configuration data for unnumbered interface
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'sub-unnumbered-config']


# discovered_classes
class Subinterfaces_Subinterface(yang_base.BaseBinding):
    """
    The list of subinterfaces (logical interfaces) associated
    with a physical interface
    """
    config = False
    container = {'state': 'Subinterface_State', 'config': 'Subinterface_Config', }
    leaf = {
      'index': {
          'type': {
              'options': {
                  '../config/index': {},
                 },
              'value': 'leafref',
             },
          'description': {
              'options': {},
              'value': """The index number of the subinterface -- used to address
the logical interface""",
             },
         },
     }
    list_ = {}
    uses = []


# discovered_classes
class Interfaces_Interface(yang_base.BaseBinding):
    """
    The list of named interfaces on the device.
    """
    config = False
    container = {'state': 'Interface_State', 'config': 'Interface_Config', }
    leaf = {
      'name': {
          'type': {
              'options': {
                  '../config/name': {},
                 },
              'value': 'leafref',
             },
          'description': {
              'options': {},
              'value': 'References the configured name of the interface',
             },
         },
     }
    list_ = {}
    uses = [u'subinterfaces-top', u'interface-phys-holdtime-top']


# discovered_classes
class Subinterface_Config(yang_base.BaseBinding):
    """
    Configurable items at the subinterface level
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'subinterfaces-config']


# discovered_classes
class Interface_State(yang_base.BaseBinding):
    """
    Operational state data at the global interface level
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-common-state', u'interface-phys-config', u'interface-counters-state']


# discovered_classes
class InterfaceRef_Config(yang_base.BaseBinding):
    """
    Configured reference to interface / subinterface
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-ref-common']


# discovered_classes
class InterfaceCountersState_Counters(yang_base.BaseBinding):
    """
    A collection of interface-related statistics objects.
    """
    config = False
    container = {}
    leaf = {
      'out-octets': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

The total number of octets transmitted out of the
interface, including framing characters.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifHCOutOctets',
             },
         },
      'out-errors': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

For packet-oriented interfaces, the number of outbound
packets that could not be transmitted because of errors.
For character-oriented or fixed-length interfaces, the
number of outbound transmission units that could not be
transmitted because of errors.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifOutErrors',
             },
         },
      'in-multicast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]


The number of packets, delivered by this sub-layer to a
higher (sub-)layer, that were addressed to a multicast
address at this sub-layer.  For a MAC-layer protocol,
this includes both Group and Functional addresses.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': """RFC 2863: The Interfaces Group MIB -
          ifHCInMulticastPkts""",
             },
         },
      'out-unicast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]

The total number of packets that higher-level protocols
requested be transmitted, and that were not addressed
to a multicast or broadcast address at this sub-layer,
including those that were discarded or not sent.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifHCOutUcastPkts',
             },
         },
      'in-errors': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

For packet-oriented interfaces, the number of inbound
packets that contained errors preventing them from being
deliverable to a higher-layer protocol.  For character-
oriented or fixed-length interfaces, the number of
inbound transmission units that contained errors
preventing them from being deliverable to a higher-layer
protocol.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifInErrors',
             },
         },
      'out-multicast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

The total number of packets that higher-level protocols
requested be transmitted, and that were addressed to a
multicast address at this sub-layer, including those
that were discarded or not sent.  For a MAC-layer
protocol, this includes both Group and Functional
addresses.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': """RFC 2863: The Interfaces Group MIB -
          ifHCOutMulticastPkts""",
             },
         },
      'in-discards': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

The number of inbound packets that were chosen to be
discarded even though no errors had been detected to
prevent their being deliverable to a higher-layer
protocol.  One possible reason for discarding such a
packet could be to free up buffer space.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifInDiscards',
             },
         },
      'last-clear': {
          'type': {
              'options': {},
              'value': 'yang:date-and-time',
             },
          'description': {
              'options': {},
              'value': """Indicates the last time the interface counters were
cleared.""",
             },
         },
      'in-unicast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]

The number of packets, delivered by this sub-layer to a
higher (sub-)layer, that were not addressed to a
multicast or broadcast address at this sub-layer.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifHCInUcastPkts',
             },
         },
      'out-broadcast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]

The total number of packets that higher-level protocols
requested be transmitted, and that were addressed to a
broadcast address at this sub-layer, including those
that were discarded or not sent.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': """RFC 2863: The Interfaces Group MIB -
          ifHCOutBroadcastPkts""",
             },
         },
      'out-discards': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

The number of outbound packets that were chosen to be
discarded even though no errors had been detected to
prevent their being transmitted.  One possible reason
for discarding such a packet could be to free up buffer
space.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifOutDiscards',
             },
         },
      'in-broadcast-pkts': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]

The number of packets, delivered by this sub-layer to a
higher (sub-)layer, that were addressed to a broadcast
address at this sub-layer.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': """RFC 2863: The Interfaces Group MIB -
          ifHCInBroadcastPkts""",
             },
         },
      'in-unknown-protos': {
          'type': {
              'options': {},
              'value': 'yang:counter32',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]
Changed the counter type to counter64.

For packet-oriented interfaces, the number of packets
received via the interface that were discarded because
of an unknown or unsupported protocol.  For
character-oriented or fixed-length interfaces that
support protocol multiplexing, the number of
transmission units received via the interface that were
discarded because of an unknown or unsupported protocol.
For any interface that does not support protocol
multiplexing, this counter is not present.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifInUnknownProtos',
             },
         },
      'in-octets': {
          'type': {
              'options': {},
              'value': 'yang:counter64',
             },
          'description': {
              'options': {},
              'value': """[adapted from IETF interfaces model (RFC 7223)]

The total number of octets received on the interface,
including framing characters.

Discontinuities in the value of this counter can occur
at re-initialization of the management system, and at
other times as indicated by the value of
'discontinuity-time'.""",
             },
          'reference': {
              'options': {},
              'value': 'RFC 2863: The Interfaces Group MIB - ifHCInOctets',
             },
         },
     }
    list_ = {}
    uses = []


# discovered_classes
class InterfaceRefState_InterfaceRef(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-ref-state-container']


# discovered_classes
class InterfaceRefStateContainer_State(yang_base.BaseBinding):
    """
    Operational state for interface-ref
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-ref-common']


# discovered_classes
class Unnumbered_State(yang_base.BaseBinding):
    """
    Operational state data for unnumbered interfaces
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'sub-unnumbered-state', u'sub-unnumbered-config']


# discovered_classes
class HoldTime_Config(yang_base.BaseBinding):
    """
    Configuration data for interface hold-time settings.
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-phys-holdtime-config']


# discovered_classes
class HoldTime_State(yang_base.BaseBinding):
    """
    Operational state data for interface hold-time.
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'interface-phys-holdtime-state', u'interface-phys-holdtime-config']


# discovered_classes
class Subinterface_State(yang_base.BaseBinding):
    """
    Operational state data for logical interfaces
    """
    config = False
    container = {}
    leaf = {}
    list_ = {}
    uses = [u'subinterfaces-config', u'subinterfaces-state']


# discovered_classes
class SubinterfacesTop_Subinterfaces(yang_base.BaseBinding):
    """
    Enclosing container for the list of subinterfaces associated
    with a physical interface
    """
    config = False
    container = {}
    leaf = {}
    list_ = {u'subinterface': 'subinterfaces_subinterface'}
    uses = []


# discovered_classes
class InterfaceRef_InterfaceRef(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    config = False
    container = {'config': 'InterfaceRef_Config', }
    leaf = {}
    list_ = {}
    uses = [u'interface-ref-state-container']


# discovered_classes
class SubUnnumberedTop_Unnumbered(yang_base.BaseBinding):
    """
    Top-level container for setting unnumbered interfaces.
    Includes reference the interface that provides the
    address information
    """
    config = False
    container = {'state': 'Unnumbered_State', 'config': 'Unnumbered_Config', }
    leaf = {}
    list_ = {}
    uses = [u'oc-if:interface-ref']


groupings = {
  'interface-phys-holdtime-top': {
      'info': {
          'description': """Top-level grouping for setting link transition
dampening on physical and other types of interfaces.""",
         },
      'container': {
          'hold-time': 'interface-phys-holdtime-top_hold-time',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interface-ref-state': {
      'info': {
          'description': """Reusable opstate w/container for a reference to an
interface or subinterface""",
         },
      'container': {
          'interface-ref': 'interface-ref-state_interface-ref',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interfaces-top': {
      'info': {
          'description': """Top-level grouping for interface configuration and
operational state data""",
         },
      'container': {
          'interfaces': 'interfaces-top_interfaces',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'sub-unnumbered-state': {
      'info': {
          'description': 'Operational state data unnumbered subinterfaces',
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'sub-unnumbered-config': {
      'info': {
          'description': 'Configuration data for unnumbered subinterfaces',
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {
          'enabled': {
              'default': {
                  'options': {},
                  'value': 'false',
                 },
              'type': {
                  'options': {},
                  'value': 'boolean',
                 },
              'description': {
                  'options': {},
                  'value': """Indicates that the subinterface is unnumbered.  By default
the subinterface is numbered, i.e., expected to have an
IP address configuration.""",
                 },
             },
         },
      'config': False,
     },
  'subinterfaces-config': {
      'info': {
          'description': 'Configuration data for subinterfaces',
         },
      'container': {},
      'list': {},
      'uses': {
          'interface-common-config': {},
         },
      'leaf': {
          'index': {
              'default': {
                  'options': {},
                  'value': '0',
                 },
              'type': {
                  'options': {},
                  'value': 'uint32',
                 },
              'description': {
                  'options': {},
                  'value': """The index of the subinterface, or logical interface number.
On systems with no support for subinterfaces, or not using
subinterfaces, this value should default to 0, i.e., the
default subinterface.""",
                 },
             },
         },
      'config': False,
     },
  'subinterfaces-state': {
      'info': {
          'description': 'Operational state data for subinterfaces',
         },
      'container': {},
      'list': {},
      'uses': {
          'interface-common-state': {},
          'interface-counters-state': {},
         },
      'leaf': {},
      'config': False,
     },
  'interface-common-state': {
      'info': {
          'description': """Operational state data (in addition to intended configuration)
at the global level for this interface""",
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {
          'ifindex': {
              'type': {
                  'options': {},
                  'value': 'uint32',
                 },
              'description': {
                  'options': {},
                  'value': """System assigned number for each interface.  Corresponds to
ifIndex object in SNMP Interface MIB""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863 - The Interfaces Group MIB',
                 },
             },
          'oper-status': {
              'mandatory': {
                  'options': {},
                  'value': 'true',
                 },
              'type': {
                  'options': {
                      'DORMANT': {
                          'description': {
                              'options': {},
                              'value': 'Waiting for some external event.',
                             },
                          'value': {
                              'options': {},
                              'value': '5',
                             },
                         },
                      'LOWER_LAYER_DOWN': {
                          'description': {
                              'options': {},
                              'value': 'Down due to state of lower-layer interface(s).',
                             },
                          'value': {
                              'options': {},
                              'value': '7',
                             },
                         },
                      'UNKNOWN': {
                          'description': {
                              'options': {},
                              'value': 'Status cannot be determined for some reason.',
                             },
                          'value': {
                              'options': {},
                              'value': '4',
                             },
                         },
                      'TESTING': {
                          'description': {
                              'options': {},
                              'value': """In some test mode.  No operational packets can
be passed.""",
                             },
                          'value': {
                              'options': {},
                              'value': '3',
                             },
                         },
                      'UP': {
                          'description': {
                              'options': {},
                              'value': 'Ready to pass packets.',
                             },
                          'value': {
                              'options': {},
                              'value': '1',
                             },
                         },
                      'DOWN': {
                          'description': {
                              'options': {},
                              'value': 'The interface does not pass any packets.',
                             },
                          'value': {
                              'options': {},
                              'value': '2',
                             },
                         },
                      'NOT_PRESENT': {
                          'description': {
                              'options': {},
                              'value': 'Some component (typically hardware) is missing.',
                             },
                          'value': {
                              'options': {},
                              'value': '6',
                             },
                         },
                     },
                  'value': 'enumeration',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

The current operational state of the interface.

This leaf has the same semantics as ifOperStatus.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifOperStatus',
                 },
             },
          'last-change': {
              'type': {
                  'options': {},
                  'value': 'yang:timeticks',
                 },
              'description': {
                  'options': {},
                  'value': """Date and time of the last state change of the interface
(e.g., up-to-down transition).   This corresponds to the
ifLastChange object in the standard interface MIB.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifLastChange',
                 },
             },
          'admin-status': {
              'mandatory': {
                  'options': {},
                  'value': 'true',
                 },
              'type': {
                  'options': {
                      'DOWN': {
                          'description': {
                              'options': {},
                              'value': 'Not ready to pass packets and not in some test mode.',
                             },
                         },
                      'TESTING': {
                          'description': {
                              'options': {},
                              'value': 'In some test mode.',
                             },
                         },
                      'UP': {
                          'description': {
                              'options': {},
                              'value': 'Ready to pass packets.',
                             },
                         },
                     },
                  'value': 'enumeration',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

The desired state of the interface.  In RFC 7223 this leaf
has the same read semantics as ifAdminStatus.  Here, it
reflects the administrative state as set by enabling or
disabling the interface.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifAdminStatus',
                 },
             },
         },
      'config': False,
     },
  'interface-phys-config': {
      'info': {
          'description': 'Configuration data for physical interfaces',
         },
      'container': {},
      'list': {},
      'uses': {
          'interface-common-config': {},
         },
      'leaf': {
          'type': {
              'mandatory': {
                  'options': {},
                  'value': 'true',
                 },
              'type': {
                  'options': {
                      'ietf-if:interface-type': {},
                     },
                  'value': 'identityref',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

The type of the interface.

When an interface entry is created, a server MAY
initialize the type leaf with a valid value, e.g., if it
is possible to derive the type from the name of the
interface.

If a client tries to set the type of an interface to a
value that can never be used by the system, e.g., if the
type is not supported or if the type does not match the
name of the interface, the server MUST reject the request.
A NETCONF server MUST reply with an rpc-error with the
error-tag 'invalid-value' in this case.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifType',
                 },
             },
          'mtu': {
              'type': {
                  'options': {},
                  'value': 'uint16',
                 },
              'description': {
                  'options': {},
                  'value': """Set the max transmission unit size in octets
for the physical interface.  If this is not set, the mtu is
set to the operational default -- e.g., 1514 bytes on an
Ethernet interface.""",
                 },
             },
         },
      'config': False,
     },
  'interface-ref-common': {
      'info': {
          'description': 'Reference leafrefs to interface / subinterface',
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {
          'interface': {
              'type': {
                  'options': {
                      '/oc-if:interfaces/oc-if:interface/oc-if:name': {},
                     },
                  'value': 'leafref',
                 },
              'description': {
                  'options': {},
                  'value': """Reference to a base interface.  If a reference to a
subinterface is required, this leaf must be specified
to indicate the base interface.""",
                 },
             },
          'subinterface': {
              'type': {
                  'options': {
                      '/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index': {},
                     },
                  'value': 'leafref',
                 },
              'description': {
                  'options': {},
                  'value': """Reference to a subinterface -- this requires the base
interface to be specified using the interface leaf in
this container.  If only a reference to a base interface
is requuired, this leaf should not be set.""",
                 },
             },
         },
      'config': False,
     },
  'subinterfaces-top': {
      'info': {
          'description': """Subinterface data for logical interfaces associated with a
given interface""",
         },
      'container': {
          'subinterfaces': 'subinterfaces-top_subinterfaces',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'sub-unnumbered-top': {
      'info': {
          'description': 'Top-level grouping unnumbered subinterfaces',
         },
      'container': {
          'unnumbered': 'sub-unnumbered-top_unnumbered',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interface-phys-holdtime-config': {
      'info': {
          'description': """Configuration data for interface hold-time settings --
applies to physical interfaces.""",
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {
          'down': {
              'units': {
                  'options': {},
                  'value': 'milliseconds',
                 },
              'default': {
                  'options': {},
                  'value': '0',
                 },
              'type': {
                  'options': {},
                  'value': 'uint32',
                 },
              'description': {
                  'options': {},
                  'value': """Dampens advertisement when the interface transitions from
up to down.  A zero value means dampening is turned off,
i.e., immediate notification.""",
                 },
             },
          'up': {
              'units': {
                  'options': {},
                  'value': 'milliseconds',
                 },
              'default': {
                  'options': {},
                  'value': '0',
                 },
              'type': {
                  'options': {},
                  'value': 'uint32',
                 },
              'description': {
                  'options': {},
                  'value': """Dampens advertisement when the interface
transitions from down to up.  A zero value means dampening
is turned off, i.e., immediate notification.""",
                 },
             },
         },
      'config': False,
     },
  'interface-ref-state-container': {
      'info': {
          'description': """Reusable opstate w/container for a reference to an
interface or subinterface""",
         },
      'container': {
          'state': 'interface-ref-state-container_state',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interface-common-config': {
      'info': {
          'description': """Configuration data data nodes common to physical interfaces
and subinterfaces""",
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {
          'enabled': {
              'default': {
                  'options': {},
                  'value': 'true',
                 },
              'type': {
                  'options': {},
                  'value': 'boolean',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

This leaf contains the configured, desired state of the
interface.

Systems that implement the IF-MIB use the value of this
leaf in the 'running' datastore to set
IF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry
has been initialized, as described in RFC 2863.

Changes in this leaf in the 'running' datastore are
reflected in ifAdminStatus, but if ifAdminStatus is
changed over SNMP, this leaf is not affected.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifAdminStatus',
                 },
             },
          'name': {
              'type': {
                  'options': {},
                  'value': 'string',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

The name of the interface.

A device MAY restrict the allowed values for this leaf,
possibly depending on the type of the interface.
For system-controlled interfaces, this leaf is the
device-specific name of the interface.  The 'config false'
list interfaces/interface[name]/state contains the currently
existing interfaces on the device.

If a client tries to create configuration for a
system-controlled interface that is not present in the
corresponding state list, the server MAY reject
the request if the implementation does not support
pre-provisioning of interfaces or if the name refers to
an interface that can never exist in the system.  A
NETCONF server MUST reply with an rpc-error with the
error-tag 'invalid-value' in this case.

The IETF model in RFC 7223 provides YANG features for the
following (i.e., pre-provisioning and arbitrary-names),
however they are omitted here:

 If the device supports pre-provisioning of interface
 configuration, the 'pre-provisioning' feature is
 advertised.

 If the device allows arbitrarily named user-controlled
 interfaces, the 'arbitrary-names' feature is advertised.

When a configured user-controlled interface is created by
the system, it is instantiated with the same name in the
/interfaces/interface[name]/state list.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 7223: A YANG Data Model for Interface Management',
                 },
             },
          'description': {
              'type': {
                  'options': {},
                  'value': 'string',
                 },
              'description': {
                  'options': {},
                  'value': """[adapted from IETF interfaces model (RFC 7223)]

A textual description of the interface.

A server implementation MAY map this leaf to the ifAlias
MIB object.  Such an implementation needs to use some
mechanism to handle the differences in size and characters
allowed between this leaf and ifAlias.  The definition of
such a mechanism is outside the scope of this document.

Since ifAlias is defined to be stored in non-volatile
storage, the MIB implementation MUST map ifAlias to the
value of 'description' in the persistently stored
datastore.

Specifically, if the device supports ':startup', when
ifAlias is read the device MUST return the value of
'description' in the 'startup' datastore, and when it is
written, it MUST be written to the 'running' and 'startup'
datastores.  Note that it is up to the implementation to

decide whether to modify this single leaf in 'startup' or
perform an implicit copy-config from 'running' to
'startup'.

If the device does not support ':startup', ifAlias MUST
be mapped to the 'description' leaf in the 'running'
datastore.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'RFC 2863: The Interfaces Group MIB - ifAlias',
                 },
             },
         },
      'config': False,
     },
  'interface-ref': {
      'info': {
          'description': """Reusable definition for a reference to an interface or
subinterface""",
         },
      'container': {
          'interface-ref': 'interface-ref_interface-ref',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interface-phys-holdtime-state': {
      'info': {
          'description': 'Operational state data for interface hold-time.',
         },
      'container': {},
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
  'interface-counters-state': {
      'info': {
          'description': """Operational state representing interface counters
and statistics.  Some of these are adapted from RFC 7223""",
         },
      'container': {
          'counters': 'interface-counters-state_counters',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
 }


class Interfaces(yang_base.BaseBinding):
    """
    Top-level grouping for interface configuration and
    operational state data
    """
    uses = ['interfaces-top_interfaces']
