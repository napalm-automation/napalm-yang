"""ietf-interfaces."""

__module__ = "ietf-interfaces"

__namespace__ = "urn:ietf:params:xml:ns:yang:ietf-interfaces"

__prefix__ = "if"

__organization__ = "IETF NETMOD (NETCONF Data Modeling Language) Working Group"

__contact__ = """WG Web:   <http://tools.ietf.org/wg/netmod/>
WG List:  <mailto:netmod@ietf.org>
WG Chair: Thomas Nadeau
          <mailto:tnadeau@lucidvision.com>
WG Chair: Juergen Schoenwaelder
          <mailto:j.schoenwaelder@jacobs-university.de>
Editor:   Martin Bjorklund
          <mailto:mbj@tail-f.com>"""

__description__ = """This module contains a collection of YANG definitions for
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
the RFC itself for full legal notices."""


    class interface:
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


    class interface-state:
    """
    The list of interfaces on the device.
System-controlled interfaces created by the system are
always present in this list, whether they are configured or
not.
    """


    class statistics:
    """
    A collection of interface-related statistics objects.
    """

