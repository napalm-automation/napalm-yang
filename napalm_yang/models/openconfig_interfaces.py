"""openconfig-interfaces."""

from napalm_yang import yang_types
from napalm_yang import yang_base
from napalm_yang import bindings

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
class InterfaceId(yang_types.String):
    """
    User-defined identifier for an interface, generally used to
    name a interface reference.  The id can be arbitrary but a
    useful convention is to use a combination of base interface
    name and subinterface index.
    """


# typedef
class BaseInterfaceRef(yang_types.Leafref):
    """
    Reusable type for by-name reference to a base interface.
    This type may be used in cases where ability to reference
    a subinterface is not required.
    """
    path = "{'options': {}, 'value': u'/OcIf:Interfaces/OcIf:Interface/OcIf:Name'}"


# discovered_classes
class InterfacesTop_Interfaces(yang_base.BaseBinding):
    """
    Top level container for interfaces, including configuration
    and state data.
    """
    config = False
    container = {}
    leaf = {}
    list = {u'interface': 'Interfaces_Interface'}
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
    list = {}
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
    list = {}
    uses = [u'interface-phys-config']


# discovered_classes
class Unnumbered_Config(yang_base.BaseBinding):
    """
    Configuration data for unnumbered interface
    """
    config = False
    container = {}
    leaf = {}
    list = {}
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
              'value': 'Leafref',
             },
          'description': {
              'options': {},
              'value': """The Index Number Of The Subinterface  Used To Address
The Logical Interface""",
             },
         },
     }
    list = {}
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
              'value': 'Leafref',
             },
          'description': {
              'options': {},
              'value': 'References The Configured Name Of The Interface',
             },
         },
     }
    list = {}
    uses = [u'subinterfaces-top', u'interface-phys-holdtime-top']


# discovered_classes
class Subinterface_Config(yang_base.BaseBinding):
    """
    Configurable items at the subinterface level
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'subinterfaces-config']


# discovered_classes
class Interface_State(yang_base.BaseBinding):
    """
    Operational state data at the global interface level
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'interface-common-state', u'interface-phys-config', u'interface-counters-state']


# discovered_classes
class InterfaceRef_Config(yang_base.BaseBinding):
    """
    Configured reference to interface / subinterface
    """
    config = False
    container = {}
    leaf = {}
    list = {}
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
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

The Total Number Of Octets Transmitted Out Of The
Interface, Including Framing Characters.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifhcoutoctets',
             },
         },
      'out-errors': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

For PacketOriented Interfaces, The Number Of Outbound
Packets That Could Not Be Transmitted Because Of Errors.
For CharacterOriented Or FixedLength Interfaces, The
Number Of Outbound Transmission Units That Could Not Be
Transmitted Because Of Errors.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifouterrors',
             },
         },
      'in-multicast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]


The Number Of Packets, Delivered By This SubLayer To A
Higher (Sub)Layer, That Were Addressed To A Multicast
Address At This SubLayer.  For A MacLayer Protocol,
This Includes Both Group And Functional Addresses.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': """Rfc 2863: The Interfaces Group Mib 
          Ifhcinmulticastpkts""",
             },
         },
      'out-unicast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Total Number Of Packets That HigherLevel Protocols
Requested Be Transmitted, And That Were Not Addressed
To A Multicast Or Broadcast Address At This SubLayer,
Including Those That Were Discarded Or Not Sent.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifhcoutucastpkts',
             },
         },
      'in-errors': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

For PacketOriented Interfaces, The Number Of Inbound
Packets That Contained Errors Preventing Them From Being
Deliverable To A HigherLayer Protocol.  For Character
Oriented Or FixedLength Interfaces, The Number Of
Inbound Transmission Units That Contained Errors
Preventing Them From Being Deliverable To A HigherLayer
Protocol.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifinerrors',
             },
         },
      'out-multicast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

The Total Number Of Packets That HigherLevel Protocols
Requested Be Transmitted, And That Were Addressed To A
Multicast Address At This SubLayer, Including Those
That Were Discarded Or Not Sent.  For A MacLayer
Protocol, This Includes Both Group And Functional
Addresses.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': """Rfc 2863: The Interfaces Group Mib 
          Ifhcoutmulticastpkts""",
             },
         },
      'in-discards': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

The Number Of Inbound Packets That Were Chosen To Be
Discarded Even Though No Errors Had Been Detected To
Prevent Their Being Deliverable To A HigherLayer
Protocol.  One Possible Reason For Discarding Such A
Packet Could Be To Free Up Buffer Space.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifindiscards',
             },
         },
      'last-clear': {
          'type': {
              'options': {},
              'value': 'Yang:DateAndTime',
             },
          'description': {
              'options': {},
              'value': """Indicates The Last Time The Interface Counters Were
Cleared.""",
             },
         },
      'in-unicast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Number Of Packets, Delivered By This SubLayer To A
Higher (Sub)Layer, That Were Not Addressed To A
Multicast Or Broadcast Address At This SubLayer.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifhcinucastpkts',
             },
         },
      'out-broadcast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Total Number Of Packets That HigherLevel Protocols
Requested Be Transmitted, And That Were Addressed To A
Broadcast Address At This SubLayer, Including Those
That Were Discarded Or Not Sent.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': """Rfc 2863: The Interfaces Group Mib 
          Ifhcoutbroadcastpkts""",
             },
         },
      'out-discards': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

The Number Of Outbound Packets That Were Chosen To Be
Discarded Even Though No Errors Had Been Detected To
Prevent Their Being Transmitted.  One Possible Reason
For Discarding Such A Packet Could Be To Free Up Buffer
Space.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifoutdiscards',
             },
         },
      'in-broadcast-pkts': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Number Of Packets, Delivered By This SubLayer To A
Higher (Sub)Layer, That Were Addressed To A Broadcast
Address At This SubLayer.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': """Rfc 2863: The Interfaces Group Mib 
          Ifhcinbroadcastpkts""",
             },
         },
      'in-unknown-protos': {
          'type': {
              'options': {},
              'value': 'Yang:Counter32',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]
Changed The Counter Type To Counter64.

For PacketOriented Interfaces, The Number Of Packets
Received Via The Interface That Were Discarded Because
Of An Unknown Or Unsupported Protocol.  For
CharacterOriented Or FixedLength Interfaces That
Support Protocol Multiplexing, The Number Of
Transmission Units Received Via The Interface That Were
Discarded Because Of An Unknown Or Unsupported Protocol.
For Any Interface That Does Not Support Protocol
Multiplexing, This Counter Is Not Present.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifinunknownprotos',
             },
         },
      'in-octets': {
          'type': {
              'options': {},
              'value': 'Yang:Counter64',
             },
          'description': {
              'options': {},
              'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Total Number Of Octets Received On The Interface,
Including Framing Characters.

Discontinuities In The Value Of This Counter Can Occur
At ReInitialization Of The Management System, And At
Other Times As Indicated By The Value Of
'DiscontinuityTime'.""",
             },
          'reference': {
              'options': {},
              'value': 'Rfc 2863: The Interfaces Group Mib  Ifhcinoctets',
             },
         },
     }
    list = {}
    uses = []


# discovered_classes
class InterfaceRefState_InterfaceRef(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'interface-ref-state-container']


# discovered_classes
class InterfaceRefStateContainer_State(yang_base.BaseBinding):
    """
    Operational state for interface-ref
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'interface-ref-common']


# discovered_classes
class Unnumbered_State(yang_base.BaseBinding):
    """
    Operational state data for unnumbered interfaces
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'sub-unnumbered-state', u'sub-unnumbered-config']


# discovered_classes
class HoldTime_Config(yang_base.BaseBinding):
    """
    Configuration data for interface hold-time settings.
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'interface-phys-holdtime-config']


# discovered_classes
class HoldTime_State(yang_base.BaseBinding):
    """
    Operational state data for interface hold-time.
    """
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = [u'interface-phys-holdtime-state', u'interface-phys-holdtime-config']


# discovered_classes
class Subinterface_State(yang_base.BaseBinding):
    """
    Operational state data for logical interfaces
    """
    config = False
    container = {}
    leaf = {}
    list = {}
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
    list = {u'subinterface': 'Subinterfaces_Subinterface'}
    uses = []


# discovered_classes
class InterfaceRef_InterfaceRef(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    config = False
    container = {'config': 'InterfaceRef_Config', }
    leaf = {}
    list = {}
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
    list = {}
    uses = [u'oc-if:interface-ref']


groupings = {
  'interface-phys-holdtime-top': {
      'info': {
          'description': """Top-level grouping for setting link transition
dampening on physical and other types of interfaces.""",
         },
      'container': {
          'hold-time': 'InterfacePhysHoldtimeTop_HoldTime',
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
          'interface-ref': 'InterfaceRefState_InterfaceRef',
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
          'interfaces': 'InterfacesTop_Interfaces',
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
                  'value': 'False',
                 },
              'type': {
                  'options': {},
                  'value': 'Boolean',
                 },
              'description': {
                  'options': {},
                  'value': """Indicates That The Subinterface Is Unnumbered.  By Default
The Subinterface Is Numbered, I.E., Expected To Have An
Ip Address Configuration.""",
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
                  'value': 'Uint32',
                 },
              'description': {
                  'options': {},
                  'value': """The Index Of The Subinterface, Or Logical Interface Number.
On Systems With No Support For Subinterfaces, Or Not Using
Subinterfaces, This Value Should Default To 0, I.E., The
Default Subinterface.""",
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
                  'value': 'Uint32',
                 },
              'description': {
                  'options': {},
                  'value': """System Assigned Number For Each Interface.  Corresponds To
Ifindex Object In Snmp Interface Mib""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863  The Interfaces Group Mib',
                 },
             },
          'oper-status': {
              'mandatory': {
                  'options': {},
                  'value': 'True',
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
                  'value': 'Enumeration',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Current Operational State Of The Interface.

This Leaf Has The Same Semantics As Ifoperstatus.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Ifoperstatus',
                 },
             },
          'last-change': {
              'type': {
                  'options': {},
                  'value': 'Yang:Timeticks',
                 },
              'description': {
                  'options': {},
                  'value': """Date And Time Of The Last State Change Of The Interface
(E.G., UpToDown Transition).   This Corresponds To The
Iflastchange Object In The Standard Interface Mib.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Iflastchange',
                 },
             },
          'admin-status': {
              'mandatory': {
                  'options': {},
                  'value': 'True',
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
                  'value': 'Enumeration',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Desired State Of The Interface.  In Rfc 7223 This Leaf
Has The Same Read Semantics As Ifadminstatus.  Here, It
Reflects The Administrative State As Set By Enabling Or
Disabling The Interface.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Ifadminstatus',
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
                  'value': 'True',
                 },
              'type': {
                  'options': {
                      'ietf-if:interface-type': {},
                     },
                  'value': 'Identityref',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Type Of The Interface.

When An Interface Entry Is Created, A Server May
Initialize The Type Leaf With A Valid Value, E.G., If It
Is Possible To Derive The Type From The Name Of The
Interface.

If A Client Tries To Set The Type Of An Interface To A
Value That Can Never Be Used By The System, E.G., If The
Type Is Not Supported Or If The Type Does Not Match The
Name Of The Interface, The Server Must Reject The Request.
A Netconf Server Must Reply With An RpcError With The
ErrorTag 'InvalidValue' In This Case.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Iftype',
                 },
             },
          'mtu': {
              'type': {
                  'options': {},
                  'value': 'Uint16',
                 },
              'description': {
                  'options': {},
                  'value': """Set The Max Transmission Unit Size In Octets
For The Physical Interface.  If This Is Not Set, The Mtu Is
Set To The Operational Default  E.G., 1514 Bytes On An
Ethernet Interface.""",
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
                  'value': 'Leafref',
                 },
              'description': {
                  'options': {},
                  'value': """Reference To A Base Interface.  If A Reference To A
Subinterface Is Required, This Leaf Must Be Specified
To Indicate The Base Interface.""",
                 },
             },
          'subinterface': {
              'type': {
                  'options': {
                      '/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index': {},
                     },
                  'value': 'Leafref',
                 },
              'description': {
                  'options': {},
                  'value': """Reference To A Subinterface  This Requires The Base
Interface To Be Specified Using The Interface Leaf In
This Container.  If Only A Reference To A Base Interface
Is Requuired, This Leaf Should Not Be Set.""",
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
          'subinterfaces': 'SubinterfacesTop_Subinterfaces',
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
          'unnumbered': 'SubUnnumberedTop_Unnumbered',
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
                  'value': 'Milliseconds',
                 },
              'default': {
                  'options': {},
                  'value': '0',
                 },
              'type': {
                  'options': {},
                  'value': 'Uint32',
                 },
              'description': {
                  'options': {},
                  'value': """Dampens Advertisement When The Interface Transitions From
Up To Down.  A Zero Value Means Dampening Is Turned Off,
I.E., Immediate Notification.""",
                 },
             },
          'up': {
              'units': {
                  'options': {},
                  'value': 'Milliseconds',
                 },
              'default': {
                  'options': {},
                  'value': '0',
                 },
              'type': {
                  'options': {},
                  'value': 'Uint32',
                 },
              'description': {
                  'options': {},
                  'value': """Dampens Advertisement When The Interface
Transitions From Down To Up.  A Zero Value Means Dampening
Is Turned Off, I.E., Immediate Notification.""",
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
          'state': 'InterfaceRefStateContainer_State',
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
                  'value': 'True',
                 },
              'type': {
                  'options': {},
                  'value': 'Boolean',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

This Leaf Contains The Configured, Desired State Of The
Interface.

Systems That Implement The IfMib Use The Value Of This
Leaf In The 'Running' Datastore To Set
IfMib.Ifadminstatus To 'Up' Or 'Down' After An Ifentry
Has Been Initialized, As Described In Rfc 2863.

Changes In This Leaf In The 'Running' Datastore Are
Reflected In Ifadminstatus, But If Ifadminstatus Is
Changed Over Snmp, This Leaf Is Not Affected.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Ifadminstatus',
                 },
             },
          'name': {
              'type': {
                  'options': {},
                  'value': 'String',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

The Name Of The Interface.

A Device May Restrict The Allowed Values For This Leaf,
Possibly Depending On The Type Of The Interface.
For SystemControlled Interfaces, This Leaf Is The
DeviceSpecific Name Of The Interface.  The 'Config False'
List Interfaces/Interface[Name]/State Contains The Currently
Existing Interfaces On The Device.

If A Client Tries To Create Configuration For A
SystemControlled Interface That Is Not Present In The
Corresponding State List, The Server May Reject
The Request If The Implementation Does Not Support
PreProvisioning Of Interfaces Or If The Name Refers To
An Interface That Can Never Exist In The System.  A
Netconf Server Must Reply With An RpcError With The
ErrorTag 'InvalidValue' In This Case.

The Ietf Model In Rfc 7223 Provides Yang Features For The
Following (I.E., PreProvisioning And ArbitraryNames),
However They Are Omitted Here:

 If The Device Supports PreProvisioning Of Interface
 Configuration, The 'PreProvisioning' Feature Is
 Advertised.

 If The Device Allows Arbitrarily Named UserControlled
 Interfaces, The 'ArbitraryNames' Feature Is Advertised.

When A Configured UserControlled Interface Is Created By
The System, It Is Instantiated With The Same Name In The
/Interfaces/Interface[Name]/State List.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 7223: A Yang Data Model For Interface Management',
                 },
             },
          'description': {
              'type': {
                  'options': {},
                  'value': 'String',
                 },
              'description': {
                  'options': {},
                  'value': """[Adapted From Ietf Interfaces Model (Rfc 7223)]

A Textual Description Of The Interface.

A Server Implementation May Map This Leaf To The Ifalias
Mib Object.  Such An Implementation Needs To Use Some
Mechanism To Handle The Differences In Size And Characters
Allowed Between This Leaf And Ifalias.  The Definition Of
Such A Mechanism Is Outside The Scope Of This Document.

Since Ifalias Is Defined To Be Stored In NonVolatile
Storage, The Mib Implementation Must Map Ifalias To The
Value Of 'Description' In The Persistently Stored
Datastore.

Specifically, If The Device Supports ':Startup', When
Ifalias Is Read The Device Must Return The Value Of
'Description' In The 'Startup' Datastore, And When It Is
Written, It Must Be Written To The 'Running' And 'Startup'
Datastores.  Note That It Is Up To The Implementation To

Decide Whether To Modify This Single Leaf In 'Startup' Or
Perform An Implicit CopyConfig From 'Running' To
'Startup'.

If The Device Does Not Support ':Startup', Ifalias Must
Be Mapped To The 'Description' Leaf In The 'Running'
Datastore.""",
                 },
              'reference': {
                  'options': {},
                  'value': 'Rfc 2863: The Interfaces Group Mib  Ifalias',
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
          'interface-ref': 'InterfaceRef_InterfaceRef',
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
          'counters': 'InterfaceCountersState_Counters',
         },
      'list': {},
      'uses': {},
      'leaf': {},
      'config': False,
     },
 }


class Interfaces(InterfacesTop_Interfaces):
    """
    Top-level grouping for interface configuration and
    operational state data
    """
    pass


bindings.attach_childs(InterfacesTop_Interfaces, globals())
bindings.attach_childs(InterfacePhysHoldtimeTop_HoldTime, globals())
bindings.attach_childs(Interface_Config, globals())
bindings.attach_childs(Unnumbered_Config, globals())
bindings.attach_childs(Subinterfaces_Subinterface, globals())
bindings.attach_childs(Interfaces_Interface, globals())
bindings.attach_childs(Subinterface_Config, globals())
bindings.attach_childs(Interface_State, globals())
bindings.attach_childs(InterfaceRef_Config, globals())
bindings.attach_childs(InterfaceCountersState_Counters, globals())
bindings.attach_childs(InterfaceRefState_InterfaceRef, globals())
bindings.attach_childs(InterfaceRefStateContainer_State, globals())
bindings.attach_childs(Unnumbered_State, globals())
bindings.attach_childs(HoldTime_Config, globals())
bindings.attach_childs(HoldTime_State, globals())
bindings.attach_childs(Subinterface_State, globals())
bindings.attach_childs(SubinterfacesTop_Subinterfaces, globals())
bindings.attach_childs(InterfaceRef_InterfaceRef, globals())
bindings.attach_childs(SubUnnumberedTop_Unnumbered, globals())
bindings.attach_childs(Interfaces, globals())
