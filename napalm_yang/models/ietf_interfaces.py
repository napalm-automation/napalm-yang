"""ietf-interfaces."""

from napalm_yang import yang_types

__module__ = "ietf-interfaces"

__namespace__ = "urn:ietf:params:xml:ns:yang:ietf-interfaces"

__prefix__ = "if"

__organization__ = "IETF NETMOD (NETCONF Data Modeling Language) Working Group"

__contact__ = """
WG Web:   <http://tools.ietf.org/wg/netmod/>
WG List:  <mailto:netmod@ietf.org>
WG Chair: Thomas Nadeau
          <mailto:tnadeau@lucidvision.com>
WG Chair: Juergen Schoenwaelder
          <mailto:j.schoenwaelder@jacobs-university.de>
Editor:   Martin Bjorklund
          <mailto:mbj@tail-f.com>
"""

__description__ = """
This module contains a collection of YANG definitions for
managing network interfaces.
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http://trustee.ietf.org/license-info).
This version of this YANG module is part of RFC 7223; see
the RFC itself for full legal notices.
"""


class Interface(yang_types.Base):
    """
    The list of configured interfaces on the device.
    The operational state of an interface is available in the
    /interfaces-state/interface list.  If the configuration of a
    system-controlled interface cannot be used by the system
    (e.g., the interface hardware present does not match the
    interface type), then the configuration is not applied to
    the system-controlled interface shown in the
    /interfaces-state/interface list.  If the configuration
    of a user-controlled interface cannot be used by the system,
    the configured interface is not instantiated in the
    /interfaces-state/interface list.
    """

    def __init__(self):
        """Main instantiator."""
        self.enabled == yang_types.Boolean(options={})
        self.link_up_down_trap_enable == yang_types.Enumeration(options={
              'enum': {
                  'disabled': 2,
                  'enabled': 1,
                 },
             })
        self.type == yang_types.Identityref(options={
              'base': 'interface-type',
             })
        self.name == yang_types.String(options={})
        self.description == yang_types.String(options={})

    @property
    def enabled(self):
        return self.enabled

    @enabled.setter
    def enabled(self, value):
        self.enabled = yang_types.Boolean(value, options={})

    @property
    def link_up_down_trap_enable(self):
        return self.link_up_down_trap_enable

    @link_up_down_trap_enable.setter
    def link_up_down_trap_enable(self, value):
        self.link_up_down_trap_enable = yang_types.Enumeration(value, options={
              'enum': {
                  'disabled': 2,
                  'enabled': 1,
                 },
             })

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, value):
        self.type = yang_types.Identityref(value, options={
              'base': 'interface-type',
             })

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = yang_types.String(value, options={})

    @property
    def description(self):
        return self.description

    @description.setter
    def description(self, value):
        self.description = yang_types.String(value, options={})


class InterfaceState(yang_types.Base):
    """
    The list of interfaces on the device.
    System-controlled interfaces created by the system are
    always present in this list, whether they are configured or
    not.
    """

    def __init__(self):
        """Main instantiator."""
        self.speed == yang_types.Gauge64(options={})
        self.name == yang_types.String(options={})
        self.oper_status == yang_types.Enumeration(options={
              'enum': {
                  'dormant': 5,
                  'lower-layer-down': 7,
                  'unknown': 4,
                  'testing': 3,
                  'up': 1,
                  'down': 2,
                  'not-present': 6,
                 },
             })
        self.phys_address == yang_types.PhysAddress(options={})
        self.type == yang_types.Identityref(options={
              'base': 'interface-type',
             })
        self.last_change == yang_types.DateAndTime(options={})
        self.admin_status == yang_types.Enumeration(options={
              'enum': {
                  'down': 2,
                  'testing': 3,
                  'up': 1,
                 },
             })
        self.if_index == yang_types.Int32(options={
              'range': '1..2147483647',
             })
        self.statistics == Statistics()

    @property
    def speed(self):
        return self.speed

    @speed.setter
    def speed(self, value):
        self.speed = yang_types.Gauge64(value, options={})

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = yang_types.String(value, options={})

    @property
    def oper_status(self):
        return self.oper_status

    @oper_status.setter
    def oper_status(self, value):
        self.oper_status = yang_types.Enumeration(value, options={
              'enum': {
                  'dormant': 5,
                  'lower-layer-down': 7,
                  'unknown': 4,
                  'testing': 3,
                  'up': 1,
                  'down': 2,
                  'not-present': 6,
                 },
             })

    @property
    def phys_address(self):
        return self.phys_address

    @phys_address.setter
    def phys_address(self, value):
        self.phys_address = yang_types.PhysAddress(value, options={})

    @property
    def type(self):
        return self.type

    @type.setter
    def type(self, value):
        self.type = yang_types.Identityref(value, options={
              'base': 'interface-type',
             })

    @property
    def last_change(self):
        return self.last_change

    @last_change.setter
    def last_change(self, value):
        self.last_change = yang_types.DateAndTime(value, options={})

    @property
    def admin_status(self):
        return self.admin_status

    @admin_status.setter
    def admin_status(self, value):
        self.admin_status = yang_types.Enumeration(value, options={
              'enum': {
                  'down': 2,
                  'testing': 3,
                  'up': 1,
                 },
             })

    @property
    def if_index(self):
        return self.if_index

    @if_index.setter
    def if_index(self, value):
        self.if_index = yang_types.Int32(value, options={
              'range': '1..2147483647',
             })

    @property
    def statistics(self):
        return self.statistics

    @statistics.setter
    def statistics(self, value):
        self.statistics = yang_types.Statistics(value)


class Statistics(yang_types.Base):
    """
    A collection of interface-related statistics objects.
    """

    def __init__(self):
        """Main instantiator."""
        self.out_octets == yang_types.Counter64(options={})
        self.discontinuity_time == yang_types.DateAndTime(options={})
        self.in_multicast_pkts == yang_types.Counter64(options={})
        self.out_unicast_pkts == yang_types.Counter64(options={})
        self.in_errors == yang_types.Counter32(options={})
        self.out_errors == yang_types.Counter32(options={})
        self.out_multicast_pkts == yang_types.Counter64(options={})
        self.in_discards == yang_types.Counter32(options={})
        self.in_unicast_pkts == yang_types.Counter64(options={})
        self.out_broadcast_pkts == yang_types.Counter64(options={})
        self.out_discards == yang_types.Counter32(options={})
        self.in_broadcast_pkts == yang_types.Counter64(options={})
        self.in_unknown_protos == yang_types.Counter32(options={})
        self.in_octets == yang_types.Counter64(options={})

    @property
    def out_octets(self):
        return self.out_octets

    @out_octets.setter
    def out_octets(self, value):
        self.out_octets = yang_types.Counter64(value, options={})

    @property
    def discontinuity_time(self):
        return self.discontinuity_time

    @discontinuity_time.setter
    def discontinuity_time(self, value):
        self.discontinuity_time = yang_types.DateAndTime(value, options={})

    @property
    def in_multicast_pkts(self):
        return self.in_multicast_pkts

    @in_multicast_pkts.setter
    def in_multicast_pkts(self, value):
        self.in_multicast_pkts = yang_types.Counter64(value, options={})

    @property
    def out_unicast_pkts(self):
        return self.out_unicast_pkts

    @out_unicast_pkts.setter
    def out_unicast_pkts(self, value):
        self.out_unicast_pkts = yang_types.Counter64(value, options={})

    @property
    def in_errors(self):
        return self.in_errors

    @in_errors.setter
    def in_errors(self, value):
        self.in_errors = yang_types.Counter32(value, options={})

    @property
    def out_errors(self):
        return self.out_errors

    @out_errors.setter
    def out_errors(self, value):
        self.out_errors = yang_types.Counter32(value, options={})

    @property
    def out_multicast_pkts(self):
        return self.out_multicast_pkts

    @out_multicast_pkts.setter
    def out_multicast_pkts(self, value):
        self.out_multicast_pkts = yang_types.Counter64(value, options={})

    @property
    def in_discards(self):
        return self.in_discards

    @in_discards.setter
    def in_discards(self, value):
        self.in_discards = yang_types.Counter32(value, options={})

    @property
    def in_unicast_pkts(self):
        return self.in_unicast_pkts

    @in_unicast_pkts.setter
    def in_unicast_pkts(self, value):
        self.in_unicast_pkts = yang_types.Counter64(value, options={})

    @property
    def out_broadcast_pkts(self):
        return self.out_broadcast_pkts

    @out_broadcast_pkts.setter
    def out_broadcast_pkts(self, value):
        self.out_broadcast_pkts = yang_types.Counter64(value, options={})

    @property
    def out_discards(self):
        return self.out_discards

    @out_discards.setter
    def out_discards(self, value):
        self.out_discards = yang_types.Counter32(value, options={})

    @property
    def in_broadcast_pkts(self):
        return self.in_broadcast_pkts

    @in_broadcast_pkts.setter
    def in_broadcast_pkts(self, value):
        self.in_broadcast_pkts = yang_types.Counter64(value, options={})

    @property
    def in_unknown_protos(self):
        return self.in_unknown_protos

    @in_unknown_protos.setter
    def in_unknown_protos(self, value):
        self.in_unknown_protos = yang_types.Counter32(value, options={})

    @property
    def in_octets(self):
        return self.in_octets

    @in_octets.setter
    def in_octets(self, value):
        self.in_octets = yang_types.Counter64(value, options={})
