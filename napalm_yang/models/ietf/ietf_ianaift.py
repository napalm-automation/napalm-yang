"""
This YANG module defines YANG identities for IANA-registered
interface types.
This YANG module is maintained by IANA and reflects the
'ifType definitions' registry.
The latest revision of this YANG module can be obtained from
the IANA web site.
Requests for new values should be made to IANA via
email (iana@iana.org).
Copyright (c) 2014 IETF Trust and the persons identified as
authors of the code.  All rights reserved.
Redistribution and use in source and binary forms, with or
without modification, is permitted pursuant to, and subject
to the license terms contained in, the Simplified BSD License
set forth in Section 4.c of the IETF Trust's Legal Provisions
Relating to IETF Documents
(http://trustee.ietf.org/license-info).
The initial version of this YANG module is part of RFC 7224;
see the RFC itself for full legal notices.
"""
from builtins import super

from napalm_yang import *


class LocalNamespace(object):
    def __getattr__(self, name):
        import sys
        return globals()[name]

ianaift = LocalNamespace()



# Imports
from napalm_yang import if_

# openconfig-extensions



__namespace__ = "urn:ietf:params:xml:ns:yang:iana-if-type"
__prefix__ = "ianaift"
__contact__ = "        Internet Assigned Numbers Authority\nPostal: ICANN\n        4676 Admiralty Way, Suite 330\n        Marina del Rey, CA 90292\nTel:    +1 310 823 9358\n<mailto:iana@iana.org>"
__organization__ = "IANA"
__revision__ = {
    "2014-05-08": {
        "revision": "2014-05-08"
    }
}



# extensions

# features


# typedef


# Identities
IanaInterfaceType = Identity(
    base=if_.InterfaceType,
    value="iana-interface-type",
    description="""This identity is used as a base for all interface types
defined in the 'ifType definitions' registry."""
    )

Other = Identity(
    base=IanaInterfaceType,
    value="other",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Regular1822 = Identity(
    base=IanaInterfaceType,
    value="regular1822",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Hdh1822 = Identity(
    base=IanaInterfaceType,
    value="hdh1822",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Ddnx25 = Identity(
    base=IanaInterfaceType,
    value="ddnX25",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Rfc877X25 = Identity(
    base=IanaInterfaceType,
    value="rfc877x25",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Ethernetcsmacd = Identity(
    base=IanaInterfaceType,
    value="ethernetCsmacd",
    description="""For all Ethernet-like interfaces, regardless of speed,
as per RFC 3635."""
    )

Iso88023Csmacd = Identity(
    base=IanaInterfaceType,
    value="iso88023Csmacd",
    description="""Deprecated via RFC 3635.
Use ethernetCsmacd(6) instead."""
    )

Iso88024Tokenbus = Identity(
    base=IanaInterfaceType,
    value="iso88024TokenBus",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Iso88025Tokenring = Identity(
    base=IanaInterfaceType,
    value="iso88025TokenRing",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Iso88026Man = Identity(
    base=IanaInterfaceType,
    value="iso88026Man",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Starlan = Identity(
    base=IanaInterfaceType,
    value="starLan",
    description="""Deprecated via RFC 3635.
Use ethernetCsmacd(6) instead."""
    )

Proteon10Mbit = Identity(
    base=IanaInterfaceType,
    value="proteon10Mbit",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Proteon80Mbit = Identity(
    base=IanaInterfaceType,
    value="proteon80Mbit",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Hyperchannel = Identity(
    base=IanaInterfaceType,
    value="hyperchannel",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Fddi = Identity(
    base=IanaInterfaceType,
    value="fddi",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Lapb = Identity(
    base=IanaInterfaceType,
    value="lapb",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Sdlc = Identity(
    base=IanaInterfaceType,
    value="sdlc",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Ds1 = Identity(
    base=IanaInterfaceType,
    value="ds1",
    description="""DS1-MIB."""
    )

E1 = Identity(
    base=IanaInterfaceType,
    value="e1",
    description="""Obsolete; see DS1-MIB."""
    )

Basicisdn = Identity(
    base=IanaInterfaceType,
    value="basicISDN",
    description="""No longer used.  See also RFC 2127."""
    )

Primaryisdn = Identity(
    base=IanaInterfaceType,
    value="primaryISDN",
    description="""No longer used.  See also RFC 2127."""
    )

Proppointtopointserial = Identity(
    base=IanaInterfaceType,
    value="propPointToPointSerial",
    description="""Proprietary serial."""
    )

Ppp = Identity(
    base=IanaInterfaceType,
    value="ppp",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Softwareloopback = Identity(
    base=IanaInterfaceType,
    value="softwareLoopback",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Eon = Identity(
    base=IanaInterfaceType,
    value="eon",
    description="""CLNP over IP."""
    )

Ethernet3Mbit = Identity(
    base=IanaInterfaceType,
    value="ethernet3Mbit",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Nsip = Identity(
    base=IanaInterfaceType,
    value="nsip",
    description="""XNS over IP."""
    )

Slip = Identity(
    base=IanaInterfaceType,
    value="slip",
    description="""Generic SLIP."""
    )

Ultra = Identity(
    base=IanaInterfaceType,
    value="ultra",
    description="""Ultra Technologies."""
    )

Ds3 = Identity(
    base=IanaInterfaceType,
    value="ds3",
    description="""DS3-MIB."""
    )

Sip = Identity(
    base=IanaInterfaceType,
    value="sip",
    description="""SMDS, coffee."""
    )

Framerelay = Identity(
    base=IanaInterfaceType,
    value="frameRelay",
    description="""DTE only."""
    )

Rs232 = Identity(
    base=IanaInterfaceType,
    value="rs232",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Para = Identity(
    base=IanaInterfaceType,
    value="para",
    description="""Parallel-port."""
    )

Arcnet = Identity(
    base=IanaInterfaceType,
    value="arcnet",
    description="""ARCnet."""
    )

Arcnetplus = Identity(
    base=IanaInterfaceType,
    value="arcnetPlus",
    description="""ARCnet Plus."""
    )

Atm = Identity(
    base=IanaInterfaceType,
    value="atm",
    description="""ATM cells."""
    )

Miox25 = Identity(
    base=IanaInterfaceType,
    value="miox25",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Sonet = Identity(
    base=IanaInterfaceType,
    value="sonet",
    description="""SONET or SDH."""
    )

X25Ple = Identity(
    base=IanaInterfaceType,
    value="x25ple",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Iso88022Llc = Identity(
    base=IanaInterfaceType,
    value="iso88022llc",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Localtalk = Identity(
    base=IanaInterfaceType,
    value="localTalk",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Smdsdxi = Identity(
    base=IanaInterfaceType,
    value="smdsDxi",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Framerelayservice = Identity(
    base=IanaInterfaceType,
    value="frameRelayService",
    description="""FRNETSERV-MIB."""
    )

V35 = Identity(
    base=IanaInterfaceType,
    value="v35",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Hssi = Identity(
    base=IanaInterfaceType,
    value="hssi",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Hippi = Identity(
    base=IanaInterfaceType,
    value="hippi",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Modem = Identity(
    base=IanaInterfaceType,
    value="modem",
    description="""Generic modem."""
    )

Aal5 = Identity(
    base=IanaInterfaceType,
    value="aal5",
    description="""AAL5 over ATM."""
    )

Sonetpath = Identity(
    base=IanaInterfaceType,
    value="sonetPath",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Sonetvt = Identity(
    base=IanaInterfaceType,
    value="sonetVT",
    description="""defaultdict(<function _nested_default_dict at 0x10fc3c5f0>, {})"""
    )

Smdsicip = Identity(
    base=IanaInterfaceType,
    value="smdsIcip",
    description="""SMDS InterCarrier Interface."""
    )

Propvirtual = Identity(
    base=IanaInterfaceType,
    value="propVirtual",
    description="""Proprietary virtual/internal."""
    )

Propmultiplexor = Identity(
    base=IanaInterfaceType,
    value="propMultiplexor",
    description="""Proprietary multiplexing."""
    )

Ieee80212 = Identity(
    base=IanaInterfaceType,
    value="ieee80212",
    description="""100BaseVG."""
    )

Fibrechannel = Identity(
    base=IanaInterfaceType,
    value="fibreChannel",
    description="""Fibre Channel."""
    )

Hippiinterface = Identity(
    base=IanaInterfaceType,
    value="hippiInterface",
    description="""HIPPI interfaces."""
    )

Framerelayinterconnect = Identity(
    base=IanaInterfaceType,
    value="frameRelayInterconnect",
    description="""Obsolete; use either
frameRelay(32) or frameRelayService(44)."""
    )

Aflane8023 = Identity(
    base=IanaInterfaceType,
    value="aflane8023",
    description="""ATM Emulated LAN for 802.3."""
    )

Aflane8025 = Identity(
    base=IanaInterfaceType,
    value="aflane8025",
    description="""ATM Emulated LAN for 802.5."""
    )

Cctemul = Identity(
    base=IanaInterfaceType,
    value="cctEmul",
    description="""ATM Emulated circuit."""
    )

Fastether = Identity(
    base=IanaInterfaceType,
    value="fastEther",
    description="""Obsoleted via RFC 3635.
ethernetCsmacd(6) should be used instead."""
    )

Isdn = Identity(
    base=IanaInterfaceType,
    value="isdn",
    description="""ISDN and X.25."""
    )

V11 = Identity(
    base=IanaInterfaceType,
    value="v11",
    description="""CCITT V.11/X.21."""
    )

V36 = Identity(
    base=IanaInterfaceType,
    value="v36",
    description="""CCITT V.36."""
    )

G703At64K = Identity(
    base=IanaInterfaceType,
    value="g703at64k",
    description="""CCITT G703 at 64Kbps."""
    )

G703At2Mb = Identity(
    base=IanaInterfaceType,
    value="g703at2mb",
    description="""Obsolete; see DS1-MIB."""
    )

Qllc = Identity(
    base=IanaInterfaceType,
    value="qllc",
    description="""SNA QLLC."""
    )

Fastetherfx = Identity(
    base=IanaInterfaceType,
    value="fastEtherFX",
    description="""Obsoleted via RFC 3635.
ethernetCsmacd(6) should be used instead."""
    )

Channel = Identity(
    base=IanaInterfaceType,
    value="channel",
    description="""Channel."""
    )

Ieee80211 = Identity(
    base=IanaInterfaceType,
    value="ieee80211",
    description="""Radio spread spectrum."""
    )

Ibm370Parchan = Identity(
    base=IanaInterfaceType,
    value="ibm370parChan",
    description="""IBM System 360/370 OEMI Channel."""
    )

Escon = Identity(
    base=IanaInterfaceType,
    value="escon",
    description="""IBM Enterprise Systems Connection."""
    )

Dlsw = Identity(
    base=IanaInterfaceType,
    value="dlsw",
    description="""Data Link Switching."""
    )

Isdns = Identity(
    base=IanaInterfaceType,
    value="isdns",
    description="""ISDN S/T interface."""
    )

Isdnu = Identity(
    base=IanaInterfaceType,
    value="isdnu",
    description="""ISDN U interface."""
    )

Lapd = Identity(
    base=IanaInterfaceType,
    value="lapd",
    description="""Link Access Protocol D."""
    )

Ipswitch = Identity(
    base=IanaInterfaceType,
    value="ipSwitch",
    description="""IP Switching Objects."""
    )

Rsrb = Identity(
    base=IanaInterfaceType,
    value="rsrb",
    description="""Remote Source Route Bridging."""
    )

Atmlogical = Identity(
    base=IanaInterfaceType,
    value="atmLogical",
    description="""ATM Logical Port."""
    )

Ds0 = Identity(
    base=IanaInterfaceType,
    value="ds0",
    description="""Digital Signal Level 0."""
    )

Ds0Bundle = Identity(
    base=IanaInterfaceType,
    value="ds0Bundle",
    description="""Group of ds0s on the same ds1."""
    )

Bsc = Identity(
    base=IanaInterfaceType,
    value="bsc",
    description="""Bisynchronous Protocol."""
    )

Async = Identity(
    base=IanaInterfaceType,
    value="async",
    description="""Asynchronous Protocol."""
    )

Cnr = Identity(
    base=IanaInterfaceType,
    value="cnr",
    description="""Combat Net Radio."""
    )

Iso88025Dtr = Identity(
    base=IanaInterfaceType,
    value="iso88025Dtr",
    description="""ISO 802.5r DTR."""
    )

Eplrs = Identity(
    base=IanaInterfaceType,
    value="eplrs",
    description="""Ext Pos Loc Report Sys."""
    )

Arap = Identity(
    base=IanaInterfaceType,
    value="arap",
    description="""Appletalk Remote Access Protocol."""
    )

Propcnls = Identity(
    base=IanaInterfaceType,
    value="propCnls",
    description="""Proprietary Connectionless Protocol."""
    )

Hostpad = Identity(
    base=IanaInterfaceType,
    value="hostPad",
    description="""CCITT-ITU X.29 PAD Protocol."""
    )

Termpad = Identity(
    base=IanaInterfaceType,
    value="termPad",
    description="""CCITT-ITU X.3 PAD Facility."""
    )

Framerelaympi = Identity(
    base=IanaInterfaceType,
    value="frameRelayMPI",
    description="""Multiproto Interconnect over FR."""
    )

X213 = Identity(
    base=IanaInterfaceType,
    value="x213",
    description="""CCITT-ITU X213."""
    )

Adsl = Identity(
    base=IanaInterfaceType,
    value="adsl",
    description="""Asymmetric Digital Subscriber Loop."""
    )

Radsl = Identity(
    base=IanaInterfaceType,
    value="radsl",
    description="""Rate-Adapt. Digital Subscriber Loop."""
    )

Sdsl = Identity(
    base=IanaInterfaceType,
    value="sdsl",
    description="""Symmetric Digital Subscriber Loop."""
    )

Vdsl = Identity(
    base=IanaInterfaceType,
    value="vdsl",
    description="""Very H-Speed Digital Subscrib. Loop."""
    )

Iso88025Crfpint = Identity(
    base=IanaInterfaceType,
    value="iso88025CRFPInt",
    description="""ISO 802.5 CRFP."""
    )

Myrinet = Identity(
    base=IanaInterfaceType,
    value="myrinet",
    description="""Myricom Myrinet."""
    )

Voiceem = Identity(
    base=IanaInterfaceType,
    value="voiceEM",
    description="""Voice recEive and transMit."""
    )

Voicefxo = Identity(
    base=IanaInterfaceType,
    value="voiceFXO",
    description="""Voice Foreign Exchange Office."""
    )

Voicefxs = Identity(
    base=IanaInterfaceType,
    value="voiceFXS",
    description="""Voice Foreign Exchange Station."""
    )

Voiceencap = Identity(
    base=IanaInterfaceType,
    value="voiceEncap",
    description="""Voice encapsulation."""
    )

Voiceoverip = Identity(
    base=IanaInterfaceType,
    value="voiceOverIp",
    description="""Voice over IP encapsulation."""
    )

Atmdxi = Identity(
    base=IanaInterfaceType,
    value="atmDxi",
    description="""ATM DXI."""
    )

Atmfuni = Identity(
    base=IanaInterfaceType,
    value="atmFuni",
    description="""ATM FUNI."""
    )

Atmima = Identity(
    base=IanaInterfaceType,
    value="atmIma",
    description="""ATM IMA."""
    )

Pppmultilinkbundle = Identity(
    base=IanaInterfaceType,
    value="pppMultilinkBundle",
    description="""PPP Multilink Bundle."""
    )

Ipovercdlc = Identity(
    base=IanaInterfaceType,
    value="ipOverCdlc",
    description="""IBM ipOverCdlc."""
    )

Ipoverclaw = Identity(
    base=IanaInterfaceType,
    value="ipOverClaw",
    description="""IBM Common Link Access to Workstn."""
    )

Stacktostack = Identity(
    base=IanaInterfaceType,
    value="stackToStack",
    description="""IBM stackToStack."""
    )

Virtualipaddress = Identity(
    base=IanaInterfaceType,
    value="virtualIpAddress",
    description="""IBM VIPA."""
    )

Mpc = Identity(
    base=IanaInterfaceType,
    value="mpc",
    description="""IBM multi-protocol channel support."""
    )

Ipoveratm = Identity(
    base=IanaInterfaceType,
    value="ipOverAtm",
    description="""IBM ipOverAtm."""
    )

Iso88025Fiber = Identity(
    base=IanaInterfaceType,
    value="iso88025Fiber",
    description="""ISO 802.5j Fiber Token Ring."""
    )

Tdlc = Identity(
    base=IanaInterfaceType,
    value="tdlc",
    description="""IBM twinaxial data link control."""
    )

Gigabitethernet = Identity(
    base=IanaInterfaceType,
    value="gigabitEthernet",
    description="""Obsoleted via RFC 3635.
ethernetCsmacd(6) should be used instead."""
    )

Hdlc = Identity(
    base=IanaInterfaceType,
    value="hdlc",
    description="""HDLC."""
    )

Lapf = Identity(
    base=IanaInterfaceType,
    value="lapf",
    description="""LAP F."""
    )

V37 = Identity(
    base=IanaInterfaceType,
    value="v37",
    description="""V.37."""
    )

X25Mlp = Identity(
    base=IanaInterfaceType,
    value="x25mlp",
    description="""Multi-Link Protocol."""
    )

X25Huntgroup = Identity(
    base=IanaInterfaceType,
    value="x25huntGroup",
    description="""X25 Hunt Group."""
    )

Transphdlc = Identity(
    base=IanaInterfaceType,
    value="transpHdlc",
    description="""Transp HDLC."""
    )

Interleave = Identity(
    base=IanaInterfaceType,
    value="interleave",
    description="""Interleave channel."""
    )

Fast = Identity(
    base=IanaInterfaceType,
    value="fast",
    description="""Fast channel."""
    )

Ip = Identity(
    base=IanaInterfaceType,
    value="ip",
    description="""IP (for APPN HPR in IP networks)."""
    )

Docscablemaclayer = Identity(
    base=IanaInterfaceType,
    value="docsCableMaclayer",
    description="""CATV Mac Layer."""
    )

Docscabledownstream = Identity(
    base=IanaInterfaceType,
    value="docsCableDownstream",
    description="""CATV Downstream interface."""
    )

Docscableupstream = Identity(
    base=IanaInterfaceType,
    value="docsCableUpstream",
    description="""CATV Upstream interface."""
    )

A12Mppswitch = Identity(
    base=IanaInterfaceType,
    value="a12MppSwitch",
    description="""Avalon Parallel Processor."""
    )

Tunnel = Identity(
    base=IanaInterfaceType,
    value="tunnel",
    description="""Encapsulation interface."""
    )

Coffee = Identity(
    base=IanaInterfaceType,
    value="coffee",
    description="""Coffee pot."""
    )

Ces = Identity(
    base=IanaInterfaceType,
    value="ces",
    description="""Circuit Emulation Service."""
    )

Atmsubinterface = Identity(
    base=IanaInterfaceType,
    value="atmSubInterface",
    description="""ATM Sub Interface."""
    )

L2Vlan = Identity(
    base=IanaInterfaceType,
    value="l2vlan",
    description="""Layer 2 Virtual LAN using 802.1Q."""
    )

L3Ipvlan = Identity(
    base=IanaInterfaceType,
    value="l3ipvlan",
    description="""Layer 3 Virtual LAN using IP."""
    )

L3Ipxvlan = Identity(
    base=IanaInterfaceType,
    value="l3ipxvlan",
    description="""Layer 3 Virtual LAN using IPX."""
    )

Digitalpowerline = Identity(
    base=IanaInterfaceType,
    value="digitalPowerline",
    description="""IP over Power Lines."""
    )

Mediamailoverip = Identity(
    base=IanaInterfaceType,
    value="mediaMailOverIp",
    description="""Multimedia Mail over IP."""
    )

Dtm = Identity(
    base=IanaInterfaceType,
    value="dtm",
    description="""Dynamic synchronous Transfer Mode."""
    )

Dcn = Identity(
    base=IanaInterfaceType,
    value="dcn",
    description="""Data Communications Network."""
    )

Ipforward = Identity(
    base=IanaInterfaceType,
    value="ipForward",
    description="""IP Forwarding Interface."""
    )

Msdsl = Identity(
    base=IanaInterfaceType,
    value="msdsl",
    description="""Multi-rate Symmetric DSL."""
    )

Ieee1394 = Identity(
    base=IanaInterfaceType,
    value="ieee1394",
    description="""IEEE1394 High Performance Serial Bus."""
    )

IfGsn = Identity(
    base=IanaInterfaceType,
    value="if-gsn",
    description="""HIPPI-6400."""
    )

Dvbrccmaclayer = Identity(
    base=IanaInterfaceType,
    value="dvbRccMacLayer",
    description="""DVB-RCC MAC Layer."""
    )

Dvbrccdownstream = Identity(
    base=IanaInterfaceType,
    value="dvbRccDownstream",
    description="""DVB-RCC Downstream Channel."""
    )

Dvbrccupstream = Identity(
    base=IanaInterfaceType,
    value="dvbRccUpstream",
    description="""DVB-RCC Upstream Channel."""
    )

Atmvirtual = Identity(
    base=IanaInterfaceType,
    value="atmVirtual",
    description="""ATM Virtual Interface."""
    )

Mplstunnel = Identity(
    base=IanaInterfaceType,
    value="mplsTunnel",
    description="""MPLS Tunnel Virtual Interface."""
    )

Srp = Identity(
    base=IanaInterfaceType,
    value="srp",
    description="""Spatial Reuse Protocol."""
    )

Voiceoveratm = Identity(
    base=IanaInterfaceType,
    value="voiceOverAtm",
    description="""Voice over ATM."""
    )

Voiceoverframerelay = Identity(
    base=IanaInterfaceType,
    value="voiceOverFrameRelay",
    description="""Voice Over Frame Relay."""
    )

Idsl = Identity(
    base=IanaInterfaceType,
    value="idsl",
    description="""Digital Subscriber Loop over ISDN."""
    )

Compositelink = Identity(
    base=IanaInterfaceType,
    value="compositeLink",
    description="""Avici Composite Link Interface."""
    )

Ss7Siglink = Identity(
    base=IanaInterfaceType,
    value="ss7SigLink",
    description="""SS7 Signaling Link."""
    )

Propwirelessp2P = Identity(
    base=IanaInterfaceType,
    value="propWirelessP2P",
    description="""Prop. P2P wireless interface."""
    )

Frforward = Identity(
    base=IanaInterfaceType,
    value="frForward",
    description="""Frame Forward Interface."""
    )

Rfc1483 = Identity(
    base=IanaInterfaceType,
    value="rfc1483",
    description="""Multiprotocol over ATM AAL5."""
    )

Usb = Identity(
    base=IanaInterfaceType,
    value="usb",
    description="""USB Interface."""
    )

Ieee8023Adlag = Identity(
    base=IanaInterfaceType,
    value="ieee8023adLag",
    description="""IEEE 802.3ad Link Aggregate."""
    )

Bgppolicyaccounting = Identity(
    base=IanaInterfaceType,
    value="bgppolicyaccounting",
    description="""BGP Policy Accounting."""
    )

Frf16Mfrbundle = Identity(
    base=IanaInterfaceType,
    value="frf16MfrBundle",
    description="""FRF.16 Multilink Frame Relay."""
    )

H323Gatekeeper = Identity(
    base=IanaInterfaceType,
    value="h323Gatekeeper",
    description="""H323 Gatekeeper."""
    )

H323Proxy = Identity(
    base=IanaInterfaceType,
    value="h323Proxy",
    description="""H323 Voice and Video Proxy."""
    )

Mpls = Identity(
    base=IanaInterfaceType,
    value="mpls",
    description="""MPLS."""
    )

Mfsiglink = Identity(
    base=IanaInterfaceType,
    value="mfSigLink",
    description="""Multi-frequency signaling link."""
    )

Hdsl2 = Identity(
    base=IanaInterfaceType,
    value="hdsl2",
    description="""High Bit-Rate DSL - 2nd generation."""
    )

Shdsl = Identity(
    base=IanaInterfaceType,
    value="shdsl",
    description="""Multirate HDSL2."""
    )

Ds1Fdl = Identity(
    base=IanaInterfaceType,
    value="ds1FDL",
    description="""Facility Data Link (4Kbps) on a DS1."""
    )

Pos = Identity(
    base=IanaInterfaceType,
    value="pos",
    description="""Packet over SONET/SDH Interface."""
    )

Dvbasiin = Identity(
    base=IanaInterfaceType,
    value="dvbAsiIn",
    description="""DVB-ASI Input."""
    )

Dvbasiout = Identity(
    base=IanaInterfaceType,
    value="dvbAsiOut",
    description="""DVB-ASI Output."""
    )

Plc = Identity(
    base=IanaInterfaceType,
    value="plc",
    description="""Power Line Communications."""
    )

Nfas = Identity(
    base=IanaInterfaceType,
    value="nfas",
    description="""Non-Facility Associated Signaling."""
    )

Tr008 = Identity(
    base=IanaInterfaceType,
    value="tr008",
    description="""TR008."""
    )

Gr303Rdt = Identity(
    base=IanaInterfaceType,
    value="gr303RDT",
    description="""Remote Digital Terminal."""
    )

Gr303Idt = Identity(
    base=IanaInterfaceType,
    value="gr303IDT",
    description="""Integrated Digital Terminal."""
    )

Isup = Identity(
    base=IanaInterfaceType,
    value="isup",
    description="""ISUP."""
    )

Propdocswirelessmaclayer = Identity(
    base=IanaInterfaceType,
    value="propDocsWirelessMaclayer",
    description="""Cisco proprietary Maclayer."""
    )

Propdocswirelessdownstream = Identity(
    base=IanaInterfaceType,
    value="propDocsWirelessDownstream",
    description="""Cisco proprietary Downstream."""
    )

Propdocswirelessupstream = Identity(
    base=IanaInterfaceType,
    value="propDocsWirelessUpstream",
    description="""Cisco proprietary Upstream."""
    )

Hiperlan2 = Identity(
    base=IanaInterfaceType,
    value="hiperlan2",
    description="""HIPERLAN Type 2 Radio Interface."""
    )

Propbwap2Mp = Identity(
    base=IanaInterfaceType,
    value="propBWAp2Mp",
    description="""PropBroadbandWirelessAccesspt2Multipt (use of this value
for IEEE 802.16 WMAN interfaces as per IEEE Std 802.16f
is deprecated, and ieee80216WMAN(237) should be used
instead)."""
    )

Sonetoverheadchannel = Identity(
    base=IanaInterfaceType,
    value="sonetOverheadChannel",
    description="""SONET Overhead Channel."""
    )

Digitalwrapperoverheadchannel = Identity(
    base=IanaInterfaceType,
    value="digitalWrapperOverheadChannel",
    description="""Digital Wrapper."""
    )

Aal2 = Identity(
    base=IanaInterfaceType,
    value="aal2",
    description="""ATM adaptation layer 2."""
    )

Radiomac = Identity(
    base=IanaInterfaceType,
    value="radioMAC",
    description="""MAC layer over radio links."""
    )

Atmradio = Identity(
    base=IanaInterfaceType,
    value="atmRadio",
    description="""ATM over radio links."""
    )

Imt = Identity(
    base=IanaInterfaceType,
    value="imt",
    description="""Inter-Machine Trunks."""
    )

Mvl = Identity(
    base=IanaInterfaceType,
    value="mvl",
    description="""Multiple Virtual Lines DSL."""
    )

Reachdsl = Identity(
    base=IanaInterfaceType,
    value="reachDSL",
    description="""Long Reach DSL."""
    )

Frdlciendpt = Identity(
    base=IanaInterfaceType,
    value="frDlciEndPt",
    description="""Frame Relay DLCI End Point."""
    )

Atmvciendpt = Identity(
    base=IanaInterfaceType,
    value="atmVciEndPt",
    description="""ATM VCI End Point."""
    )

Opticalchannel = Identity(
    base=IanaInterfaceType,
    value="opticalChannel",
    description="""Optical Channel."""
    )

Opticaltransport = Identity(
    base=IanaInterfaceType,
    value="opticalTransport",
    description="""Optical Transport."""
    )

Propatm = Identity(
    base=IanaInterfaceType,
    value="propAtm",
    description="""Proprietary ATM."""
    )

Voiceovercable = Identity(
    base=IanaInterfaceType,
    value="voiceOverCable",
    description="""Voice Over Cable Interface."""
    )

Infiniband = Identity(
    base=IanaInterfaceType,
    value="infiniband",
    description="""Infiniband."""
    )

Telink = Identity(
    base=IanaInterfaceType,
    value="teLink",
    description="""TE Link."""
    )

Q2931 = Identity(
    base=IanaInterfaceType,
    value="q2931",
    description="""Q.2931."""
    )

Virtualtg = Identity(
    base=IanaInterfaceType,
    value="virtualTg",
    description="""Virtual Trunk Group."""
    )

Siptg = Identity(
    base=IanaInterfaceType,
    value="sipTg",
    description="""SIP Trunk Group."""
    )

Sipsig = Identity(
    base=IanaInterfaceType,
    value="sipSig",
    description="""SIP Signaling."""
    )

Docscableupstreamchannel = Identity(
    base=IanaInterfaceType,
    value="docsCableUpstreamChannel",
    description="""CATV Upstream Channel."""
    )

Econet = Identity(
    base=IanaInterfaceType,
    value="econet",
    description="""Acorn Econet."""
    )

Pon155 = Identity(
    base=IanaInterfaceType,
    value="pon155",
    description="""FSAN 155Mb Symetrical PON interface."""
    )

Pon622 = Identity(
    base=IanaInterfaceType,
    value="pon622",
    description="""FSAN 622Mb Symetrical PON interface."""
    )

Bridge = Identity(
    base=IanaInterfaceType,
    value="bridge",
    description="""Transparent bridge interface."""
    )

Linegroup = Identity(
    base=IanaInterfaceType,
    value="linegroup",
    description="""Interface common to multiple lines."""
    )

Voiceemfgd = Identity(
    base=IanaInterfaceType,
    value="voiceEMFGD",
    description="""Voice E&M Feature Group D."""
    )

Voicefgdeana = Identity(
    base=IanaInterfaceType,
    value="voiceFGDEANA",
    description="""Voice FGD Exchange Access North American."""
    )

Voicedid = Identity(
    base=IanaInterfaceType,
    value="voiceDID",
    description="""Voice Direct Inward Dialing."""
    )

Mpegtransport = Identity(
    base=IanaInterfaceType,
    value="mpegTransport",
    description="""MPEG transport interface."""
    )

Sixtofour = Identity(
    base=IanaInterfaceType,
    value="sixToFour",
    description="""6to4 interface (DEPRECATED)."""
    )

Gtp = Identity(
    base=IanaInterfaceType,
    value="gtp",
    description="""GTP (GPRS Tunneling Protocol)."""
    )

Pdnetherloop1 = Identity(
    base=IanaInterfaceType,
    value="pdnEtherLoop1",
    description="""Paradyne EtherLoop 1."""
    )

Pdnetherloop2 = Identity(
    base=IanaInterfaceType,
    value="pdnEtherLoop2",
    description="""Paradyne EtherLoop 2."""
    )

Opticalchannelgroup = Identity(
    base=IanaInterfaceType,
    value="opticalChannelGroup",
    description="""Optical Channel Group."""
    )

Homepna = Identity(
    base=IanaInterfaceType,
    value="homepna",
    description="""HomePNA ITU-T G.989."""
    )

Gfp = Identity(
    base=IanaInterfaceType,
    value="gfp",
    description="""Generic Framing Procedure (GFP)."""
    )

Ciscoislvlan = Identity(
    base=IanaInterfaceType,
    value="ciscoISLvlan",
    description="""Layer 2 Virtual LAN using Cisco ISL."""
    )

Actelismetaloop = Identity(
    base=IanaInterfaceType,
    value="actelisMetaLOOP",
    description="""Acteleis proprietary MetaLOOP High Speed Link."""
    )

Fciplink = Identity(
    base=IanaInterfaceType,
    value="fcipLink",
    description="""FCIP Link."""
    )

Rpr = Identity(
    base=IanaInterfaceType,
    value="rpr",
    description="""Resilient Packet Ring Interface Type."""
    )

Qam = Identity(
    base=IanaInterfaceType,
    value="qam",
    description="""RF Qam Interface."""
    )

Lmp = Identity(
    base=IanaInterfaceType,
    value="lmp",
    description="""Link Management Protocol."""
    )

Cblvectastar = Identity(
    base=IanaInterfaceType,
    value="cblVectaStar",
    description="""Cambridge Broadband Networks Limited VectaStar."""
    )

Docscablemcmtsdownstream = Identity(
    base=IanaInterfaceType,
    value="docsCableMCmtsDownstream",
    description="""CATV Modular CMTS Downstream Interface."""
    )

Adsl2 = Identity(
    base=IanaInterfaceType,
    value="adsl2",
    description="""Asymmetric Digital Subscriber Loop Version 2
(DEPRECATED/OBSOLETED - please use adsl2plus(238)
instead)."""
    )

Macseccontrolledif = Identity(
    base=IanaInterfaceType,
    value="macSecControlledIF",
    description="""MACSecControlled."""
    )

Macsecuncontrolledif = Identity(
    base=IanaInterfaceType,
    value="macSecUncontrolledIF",
    description="""MACSecUncontrolled."""
    )

Aviciopticalether = Identity(
    base=IanaInterfaceType,
    value="aviciOpticalEther",
    description="""Avici Optical Ethernet Aggregate."""
    )

Atmbond = Identity(
    base=IanaInterfaceType,
    value="atmbond",
    description="""atmbond."""
    )

Voicefgdos = Identity(
    base=IanaInterfaceType,
    value="voiceFGDOS",
    description="""Voice FGD Operator Services."""
    )

Mocaversion1 = Identity(
    base=IanaInterfaceType,
    value="mocaVersion1",
    description="""MultiMedia over Coax Alliance (MoCA) Interface
as documented in information provided privately to IANA."""
    )

Ieee80216Wman = Identity(
    base=IanaInterfaceType,
    value="ieee80216WMAN",
    description="""IEEE 802.16 WMAN interface."""
    )

Adsl2Plus = Identity(
    base=IanaInterfaceType,
    value="adsl2plus",
    description="""Asymmetric Digital Subscriber Loop Version 2 -
Version 2 Plus and all variants."""
    )

Dvbrcsmaclayer = Identity(
    base=IanaInterfaceType,
    value="dvbRcsMacLayer",
    description="""DVB-RCS MAC Layer."""
    )

Dvbtdm = Identity(
    base=IanaInterfaceType,
    value="dvbTdm",
    description="""DVB Satellite TDM."""
    )

Dvbrcstdma = Identity(
    base=IanaInterfaceType,
    value="dvbRcsTdma",
    description="""DVB-RCS TDMA."""
    )

X86Laps = Identity(
    base=IanaInterfaceType,
    value="x86Laps",
    description="""LAPS based on ITU-T X.86/Y.1323."""
    )

Wwanpp = Identity(
    base=IanaInterfaceType,
    value="wwanPP",
    description="""3GPP WWAN."""
    )

Wwanpp2 = Identity(
    base=IanaInterfaceType,
    value="wwanPP2",
    description="""3GPP2 WWAN."""
    )

Voiceebs = Identity(
    base=IanaInterfaceType,
    value="voiceEBS",
    description="""Voice P-phone EBS physical interface."""
    )

Ifpwtype = Identity(
    base=IanaInterfaceType,
    value="ifPwType",
    description="""Pseudowire interface type."""
    )

Ilan = Identity(
    base=IanaInterfaceType,
    value="ilan",
    description="""Internal LAN on a bridge per IEEE 802.1ap."""
    )

Pip = Identity(
    base=IanaInterfaceType,
    value="pip",
    description="""Provider Instance Port on a bridge per IEEE 802.1ah PBB."""
    )

Aluelp = Identity(
    base=IanaInterfaceType,
    value="aluELP",
    description="""Alcatel-Lucent Ethernet Link Protection."""
    )

Gpon = Identity(
    base=IanaInterfaceType,
    value="gpon",
    description="""Gigabit-capable passive optical networks (G-PON) as per
ITU-T G.948."""
    )

Vdsl2 = Identity(
    base=IanaInterfaceType,
    value="vdsl2",
    description="""Very high speed digital subscriber line Version 2
(as per ITU-T Recommendation G.993.2)."""
    )

Capwapdot11Profile = Identity(
    base=IanaInterfaceType,
    value="capwapDot11Profile",
    description="""WLAN Profile Interface."""
    )

Capwapdot11Bss = Identity(
    base=IanaInterfaceType,
    value="capwapDot11Bss",
    description="""WLAN BSS Interface."""
    )

Capwapwtpvirtualradio = Identity(
    base=IanaInterfaceType,
    value="capwapWtpVirtualRadio",
    description="""WTP Virtual Radio Interface."""
    )

Bits = Identity(
    base=IanaInterfaceType,
    value="bits",
    description="""bitsport."""
    )

Docscableupstreamrfport = Identity(
    base=IanaInterfaceType,
    value="docsCableUpstreamRfPort",
    description="""DOCSIS CATV Upstream RF Port."""
    )

Cabledownstreamrfport = Identity(
    base=IanaInterfaceType,
    value="cableDownstreamRfPort",
    description="""CATV downstream RF Port."""
    )

Vmwarevirtualnic = Identity(
    base=IanaInterfaceType,
    value="vmwareVirtualNic",
    description="""VMware Virtual Network Interface."""
    )

Ieee802154 = Identity(
    base=IanaInterfaceType,
    value="ieee802154",
    description="""IEEE 802.15.4 WPAN interface."""
    )

Otnodu = Identity(
    base=IanaInterfaceType,
    value="otnOdu",
    description="""OTN Optical Data Unit."""
    )

Otnotu = Identity(
    base=IanaInterfaceType,
    value="otnOtu",
    description="""OTN Optical channel Transport Unit."""
    )

Ifvfitype = Identity(
    base=IanaInterfaceType,
    value="ifVfiType",
    description="""VPLS Forwarding Instance Interface Type."""
    )

G9981 = Identity(
    base=IanaInterfaceType,
    value="g9981",
    description="""G.998.1 bonded interface."""
    )

G9982 = Identity(
    base=IanaInterfaceType,
    value="g9982",
    description="""G.998.2 bonded interface."""
    )

G9983 = Identity(
    base=IanaInterfaceType,
    value="g9983",
    description="""G.998.3 bonded interface."""
    )

Aluepon = Identity(
    base=IanaInterfaceType,
    value="aluEpon",
    description="""Ethernet Passive Optical Networks (E-PON)."""
    )

Aluepononu = Identity(
    base=IanaInterfaceType,
    value="aluEponOnu",
    description="""EPON Optical Network Unit."""
    )

Alueponphysicaluni = Identity(
    base=IanaInterfaceType,
    value="aluEponPhysicalUni",
    description="""EPON physical User to Network interface."""
    )

Alueponlogicallink = Identity(
    base=IanaInterfaceType,
    value="aluEponLogicalLink",
    description="""The emulation of a point-to-point link over the EPON
layer."""
    )

Alugpononu = Identity(
    base=IanaInterfaceType,
    value="aluGponOnu",
    description="""GPON Optical Network Unit."""
    )

Alugponphysicaluni = Identity(
    base=IanaInterfaceType,
    value="aluGponPhysicalUni",
    description="""GPON physical User to Network interface."""
    )

Vmwarenicteam = Identity(
    base=IanaInterfaceType,
    value="vmwareNicTeam",
    description="""VMware NIC Team."""
    )


# Classes to support containers and lists


# Top-uses

# Top-containers