"""
Model for managing network interfaces and subinterfaces.  This
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
additional configuration items.

{
    "container": {
        "hold-time_config_332": {
            "info": {
                "description": "Configuration data for interface hold-time settings."
            }, 
            "leaf": {
                "down": {
                    "default": "0", 
                    "info": {
                        "description": "Dampens advertisement when the interface transitions from\nup to down.  A zero value means dampening is turned off,\ni.e., immediate notification."
                    }, 
                    "type": {
                        "uint32": {}
                    }, 
                    "units": "milliseconds"
                }, 
                "up": {
                    "default": "0", 
                    "info": {
                        "description": "Dampens advertisement when the interface\ntransitions from down to up.  A zero value means dampening\nis turned off, i.e., immediate notification."
                    }, 
                    "type": {
                        "uint32": {}
                    }, 
                    "units": "milliseconds"
                }
            }
        }, 
        "hold-time_state_339": {
            "config": "false", 
            "info": {
                "description": "Operational state data for interface hold-time."
            }, 
            "leaf": {
                "down": {
                    "default": "0", 
                    "info": {
                        "description": "Dampens advertisement when the interface transitions from\nup to down.  A zero value means dampening is turned off,\ni.e., immediate notification."
                    }, 
                    "type": {
                        "uint32": {}
                    }, 
                    "units": "milliseconds"
                }, 
                "up": {
                    "default": "0", 
                    "info": {
                        "description": "Dampens advertisement when the interface\ntransitions from down to up.  A zero value means dampening\nis turned off, i.e., immediate notification."
                    }, 
                    "type": {
                        "uint32": {}
                    }, 
                    "units": "milliseconds"
                }
            }
        }, 
        "interface-counters-state_counters_475": {
            "info": {
                "description": "A collection of interface-related statistics objects."
            }, 
            "leaf": {
                "in-broadcast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe number of packets, delivered by this sub-layer to a\nhigher (sub-)layer, that were addressed to a broadcast\naddress at this sub-layer.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-discards": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nThe number of inbound packets that were chosen to be\ndiscarded even though no errors had been detected to\nprevent their being deliverable to a higher-layer\nprotocol.  One possible reason for discarding such a\npacket could be to free up buffer space.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-errors": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nFor packet-oriented interfaces, the number of inbound\npackets that contained errors preventing them from being\ndeliverable to a higher-layer protocol.  For character-\noriented or fixed-length interfaces, the number of\ninbound transmission units that contained errors\npreventing them from being deliverable to a higher-layer\nprotocol.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-multicast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\n\nThe number of packets, delivered by this sub-layer to a\nhigher (sub-)layer, that were addressed to a multicast\naddress at this sub-layer.  For a MAC-layer protocol,\nthis includes both Group and Functional addresses.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-octets": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe total number of octets received on the interface,\nincluding framing characters.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-unicast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe number of packets, delivered by this sub-layer to a\nhigher (sub-)layer, that were not addressed to a\nmulticast or broadcast address at this sub-layer.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "in-unknown-protos": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nFor packet-oriented interfaces, the number of packets\nreceived via the interface that were discarded because\nof an unknown or unsupported protocol.  For\ncharacter-oriented or fixed-length interfaces that\nsupport protocol multiplexing, the number of\ntransmission units received via the interface that were\ndiscarded because of an unknown or unsupported protocol.\nFor any interface that does not support protocol\nmultiplexing, this counter is not present.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter32": {}
                    }
                }, 
                "last-clear": {
                    "info": {
                        "description": "Indicates the last time the interface counters were\ncleared."
                    }, 
                    "type": {
                        "yang:date-and-time": {}
                    }
                }, 
                "out-broadcast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe total number of packets that higher-level protocols\nrequested be transmitted, and that were addressed to a\nbroadcast address at this sub-layer, including those\nthat were discarded or not sent.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "out-discards": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nThe number of outbound packets that were chosen to be\ndiscarded even though no errors had been detected to\nprevent their being transmitted.  One possible reason\nfor discarding such a packet could be to free up buffer\nspace.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "out-errors": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nFor packet-oriented interfaces, the number of outbound\npackets that could not be transmitted because of errors.\nFor character-oriented or fixed-length interfaces, the\nnumber of outbound transmission units that could not be\ntransmitted because of errors.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "out-multicast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nThe total number of packets that higher-level protocols\nrequested be transmitted, and that were addressed to a\nmulticast address at this sub-layer, including those\nthat were discarded or not sent.  For a MAC-layer\nprotocol, this includes both Group and Functional\naddresses.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "out-octets": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\nChanged the counter type to counter64.\n\nThe total number of octets transmitted out of the\ninterface, including framing characters.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "out-unicast-pkts": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe total number of packets that higher-level protocols\nrequested be transmitted, and that were not addressed\nto a multicast or broadcast address at this sub-layer,\nincluding those that were discarded or not sent.\n\nDiscontinuities in the value of this counter can occur\nat re-initialization of the management system, and at\nother times as indicated by the value of\n'discontinuity-time'."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }
            }
        }, 
        "interface-phys-holdtime-top_hold-time_327": {
            "container": {
                "container": [
                    [
                        "state", 
                        "hold-time_state_339"
                    ], 
                    [
                        "config", 
                        "hold-time_config_332"
                    ]
                ]
            }, 
            "info": {
                "description": "Top-level container for hold-time settings to enable\ndampening advertisements of interface transitions."
            }
        }, 
        "interface-ref-state-container_state_103": {
            "config": "false", 
            "info": {
                "description": "Operational state for interface-ref"
            }, 
            "leaf": {
                "interface": {
                    "info": {
                        "description": "Reference to a base interface.  If a reference to a\nsubinterface is required, this leaf must be specified\nto indicate the base interface."
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/oc-if:interfaces/oc-if:interface/oc-if:name"
                        }
                    }
                }, 
                "subinterface": {
                    "info": {
                        "description": "Reference to a subinterface -- this requires the base\ninterface to be specified using the interface leaf in\nthis container.  If only a reference to a base interface\nis requuired, this leaf should not be set."
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index"
                        }
                    }
                }
            }
        }, 
        "interface-ref-state_interface-ref_137": {
            "container": {
                "container": [
                    [
                        "state", 
                        "interface-ref-state-container_state_103"
                    ]
                ]
            }, 
            "info": {
                "description": "Reference to an interface or subinterface"
            }
        }, 
        "interface-ref_config_121": {
            "info": {
                "description": "Configured reference to interface / subinterface"
            }, 
            "leaf": {
                "interface": {
                    "info": {
                        "description": "Reference to a base interface.  If a reference to a\nsubinterface is required, this leaf must be specified\nto indicate the base interface."
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/oc-if:interfaces/oc-if:interface/oc-if:name"
                        }
                    }
                }, 
                "subinterface": {
                    "info": {
                        "description": "Reference to a subinterface -- this requires the base\ninterface to be specified using the interface leaf in\nthis container.  If only a reference to a base interface\nis requuired, this leaf should not be set."
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index"
                        }
                    }
                }
            }
        }, 
        "interface-ref_interface-ref_117": {
            "container": {
                "container": [
                    [
                        "config", 
                        "interface-ref_config_121"
                    ], 
                    [
                        "state", 
                        "interface-ref-state-container_state_103"
                    ]
                ]
            }, 
            "info": {
                "description": "Reference to an interface or subinterface"
            }
        }, 
        "interface_config_905": {
            "info": {
                "description": "Configurable items at the global, physical interface\nlevel"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nA textual description of the interface.\n\nA server implementation MAY map this leaf to the ifAlias\nMIB object.  Such an implementation needs to use some\nmechanism to handle the differences in size and characters\nallowed between this leaf and ifAlias.  The definition of\nsuch a mechanism is outside the scope of this document.\n\nSince ifAlias is defined to be stored in non-volatile\nstorage, the MIB implementation MUST map ifAlias to the\nvalue of 'description' in the persistently stored\ndatastore.\n\nSpecifically, if the device supports ':startup', when\nifAlias is read the device MUST return the value of\n'description' in the 'startup' datastore, and when it is\nwritten, it MUST be written to the 'running' and 'startup'\ndatastores.  Note that it is up to the implementation to\n\ndecide whether to modify this single leaf in 'startup' or\nperform an implicit copy-config from 'running' to\n'startup'.\n\nIf the device does not support ':startup', ifAlias MUST\nbe mapped to the 'description' leaf in the 'running'\ndatastore."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "enabled": {
                    "default": "true", 
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThis leaf contains the configured, desired state of the\ninterface.\n\nSystems that implement the IF-MIB use the value of this\nleaf in the 'running' datastore to set\nIF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry\nhas been initialized, as described in RFC 2863.\n\nChanges in this leaf in the 'running' datastore are\nreflected in ifAdminStatus, but if ifAdminStatus is\nchanged over SNMP, this leaf is not affected."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }, 
                "mtu": {
                    "info": {
                        "description": "Set the max transmission unit size in octets\nfor the physical interface.  If this is not set, the mtu is\nset to the operational default -- e.g., 1514 bytes on an\nEthernet interface."
                    }, 
                    "type": {
                        "uint16": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe name of the interface.\n\nA device MAY restrict the allowed values for this leaf,\npossibly depending on the type of the interface.\nFor system-controlled interfaces, this leaf is the\ndevice-specific name of the interface.  The 'config false'\nlist interfaces/interface[name]/state contains the currently\nexisting interfaces on the device.\n\nIf a client tries to create configuration for a\nsystem-controlled interface that is not present in the\ncorresponding state list, the server MAY reject\nthe request if the implementation does not support\npre-provisioning of interfaces or if the name refers to\nan interface that can never exist in the system.  A\nNETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case.\n\nThe IETF model in RFC 7223 provides YANG features for the\nfollowing (i.e., pre-provisioning and arbitrary-names),\nhowever they are omitted here:\n\n If the device supports pre-provisioning of interface\n configuration, the 'pre-provisioning' feature is\n advertised.\n\n If the device allows arbitrarily named user-controlled\n interfaces, the 'arbitrary-names' feature is advertised.\n\nWhen a configured user-controlled interface is created by\nthe system, it is instantiated with the same name in the\n/interfaces/interface[name]/state list."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "type": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe type of the interface.\n\nWhen an interface entry is created, a server MAY\ninitialize the type leaf with a valid value, e.g., if it\nis possible to derive the type from the name of the\ninterface.\n\nIf a client tries to set the type of an interface to a\nvalue that can never be used by the system, e.g., if the\ntype is not supported or if the type does not match the\nname of the interface, the server MUST reject the request.\nA NETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "identityref": {
                            "base": "ietf-if:interface-type"
                        }
                    }
                }
            }
        }, 
        "interface_state_913": {
            "config": "false", 
            "container": {
                "container": [
                    [
                        "counters", 
                        "interface-counters-state_counters_475"
                    ]
                ]
            }, 
            "info": {
                "description": "Operational state data at the global interface level"
            }, 
            "leaf": {
                "admin-status": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe desired state of the interface.  In RFC 7223 this leaf\nhas the same read semantics as ifAdminStatus.  Here, it\nreflects the administrative state as set by enabling or\ndisabling the interface."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "enumeration": {
                            "enum": {
                                "DOWN": {
                                    "info": {
                                        "description": "Not ready to pass packets and not in some test mode."
                                    }
                                }, 
                                "TESTING": {
                                    "info": {
                                        "description": "In some test mode."
                                    }
                                }, 
                                "UP": {
                                    "info": {
                                        "description": "Ready to pass packets."
                                    }
                                }
                            }
                        }
                    }
                }, 
                "description": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nA textual description of the interface.\n\nA server implementation MAY map this leaf to the ifAlias\nMIB object.  Such an implementation needs to use some\nmechanism to handle the differences in size and characters\nallowed between this leaf and ifAlias.  The definition of\nsuch a mechanism is outside the scope of this document.\n\nSince ifAlias is defined to be stored in non-volatile\nstorage, the MIB implementation MUST map ifAlias to the\nvalue of 'description' in the persistently stored\ndatastore.\n\nSpecifically, if the device supports ':startup', when\nifAlias is read the device MUST return the value of\n'description' in the 'startup' datastore, and when it is\nwritten, it MUST be written to the 'running' and 'startup'\ndatastores.  Note that it is up to the implementation to\n\ndecide whether to modify this single leaf in 'startup' or\nperform an implicit copy-config from 'running' to\n'startup'.\n\nIf the device does not support ':startup', ifAlias MUST\nbe mapped to the 'description' leaf in the 'running'\ndatastore."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "enabled": {
                    "default": "true", 
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThis leaf contains the configured, desired state of the\ninterface.\n\nSystems that implement the IF-MIB use the value of this\nleaf in the 'running' datastore to set\nIF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry\nhas been initialized, as described in RFC 2863.\n\nChanges in this leaf in the 'running' datastore are\nreflected in ifAdminStatus, but if ifAdminStatus is\nchanged over SNMP, this leaf is not affected."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }, 
                "ifindex": {
                    "info": {
                        "description": "System assigned number for each interface.  Corresponds to\nifIndex object in SNMP Interface MIB"
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }, 
                "last-change": {
                    "info": {
                        "description": "Date and time of the last state change of the interface\n(e.g., up-to-down transition).   This corresponds to the\nifLastChange object in the standard interface MIB."
                    }, 
                    "type": {
                        "yang:timeticks": {}
                    }
                }, 
                "mtu": {
                    "info": {
                        "description": "Set the max transmission unit size in octets\nfor the physical interface.  If this is not set, the mtu is\nset to the operational default -- e.g., 1514 bytes on an\nEthernet interface."
                    }, 
                    "type": {
                        "uint16": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe name of the interface.\n\nA device MAY restrict the allowed values for this leaf,\npossibly depending on the type of the interface.\nFor system-controlled interfaces, this leaf is the\ndevice-specific name of the interface.  The 'config false'\nlist interfaces/interface[name]/state contains the currently\nexisting interfaces on the device.\n\nIf a client tries to create configuration for a\nsystem-controlled interface that is not present in the\ncorresponding state list, the server MAY reject\nthe request if the implementation does not support\npre-provisioning of interfaces or if the name refers to\nan interface that can never exist in the system.  A\nNETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case.\n\nThe IETF model in RFC 7223 provides YANG features for the\nfollowing (i.e., pre-provisioning and arbitrary-names),\nhowever they are omitted here:\n\n If the device supports pre-provisioning of interface\n configuration, the 'pre-provisioning' feature is\n advertised.\n\n If the device allows arbitrarily named user-controlled\n interfaces, the 'arbitrary-names' feature is advertised.\n\nWhen a configured user-controlled interface is created by\nthe system, it is instantiated with the same name in the\n/interfaces/interface[name]/state list."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "oper-status": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe current operational state of the interface.\n\nThis leaf has the same semantics as ifOperStatus."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "enumeration": {
                            "enum": {
                                "DORMANT": {
                                    "info": {
                                        "description": "Waiting for some external event."
                                    }, 
                                    "value": "5"
                                }, 
                                "DOWN": {
                                    "info": {
                                        "description": "The interface does not pass any packets."
                                    }, 
                                    "value": "2"
                                }, 
                                "LOWER_LAYER_DOWN": {
                                    "info": {
                                        "description": "Down due to state of lower-layer interface(s)."
                                    }, 
                                    "value": "7"
                                }, 
                                "NOT_PRESENT": {
                                    "info": {
                                        "description": "Some component (typically hardware) is missing."
                                    }, 
                                    "value": "6"
                                }, 
                                "TESTING": {
                                    "info": {
                                        "description": "In some test mode.  No operational packets can\nbe passed."
                                    }, 
                                    "value": "3"
                                }, 
                                "UNKNOWN": {
                                    "info": {
                                        "description": "Status cannot be determined for some reason."
                                    }, 
                                    "value": "4"
                                }, 
                                "UP": {
                                    "info": {
                                        "description": "Ready to pass packets."
                                    }, 
                                    "value": "1"
                                }
                            }
                        }
                    }
                }, 
                "type": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe type of the interface.\n\nWhen an interface entry is created, a server MAY\ninitialize the type leaf with a valid value, e.g., if it\nis possible to derive the type from the name of the\ninterface.\n\nIf a client tries to set the type of an interface to a\nvalue that can never be used by the system, e.g., if the\ntype is not supported or if the type does not match the\nname of the interface, the server MUST reject the request.\nA NETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "identityref": {
                            "base": "ietf-if:interface-type"
                        }
                    }
                }
            }
        }, 
        "interfaces-top_interfaces_878": {
            "info": {
                "description": "Top level container for interfaces, including configuration\nand state data."
            }, 
            "list": {
                "list": [
                    [
                        "interface", 
                        "interfaces_interface_884"
                    ]
                ]
            }
        }, 
        "sub-unnumbered-top_unnumbered_773": {
            "container": {
                "container": [
                    [
                        "state", 
                        "unnumbered_state_786"
                    ], 
                    [
                        "config", 
                        "unnumbered_config_779"
                    ]
                ]
            }, 
            "info": {
                "description": "Top-level container for setting unnumbered interfaces.\nIncludes reference the interface that provides the\naddress information"
            }
        }, 
        "subinterface_config_853": {
            "info": {
                "description": "Configurable items at the subinterface level"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nA textual description of the interface.\n\nA server implementation MAY map this leaf to the ifAlias\nMIB object.  Such an implementation needs to use some\nmechanism to handle the differences in size and characters\nallowed between this leaf and ifAlias.  The definition of\nsuch a mechanism is outside the scope of this document.\n\nSince ifAlias is defined to be stored in non-volatile\nstorage, the MIB implementation MUST map ifAlias to the\nvalue of 'description' in the persistently stored\ndatastore.\n\nSpecifically, if the device supports ':startup', when\nifAlias is read the device MUST return the value of\n'description' in the 'startup' datastore, and when it is\nwritten, it MUST be written to the 'running' and 'startup'\ndatastores.  Note that it is up to the implementation to\n\ndecide whether to modify this single leaf in 'startup' or\nperform an implicit copy-config from 'running' to\n'startup'.\n\nIf the device does not support ':startup', ifAlias MUST\nbe mapped to the 'description' leaf in the 'running'\ndatastore."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "enabled": {
                    "default": "true", 
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThis leaf contains the configured, desired state of the\ninterface.\n\nSystems that implement the IF-MIB use the value of this\nleaf in the 'running' datastore to set\nIF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry\nhas been initialized, as described in RFC 2863.\n\nChanges in this leaf in the 'running' datastore are\nreflected in ifAdminStatus, but if ifAdminStatus is\nchanged over SNMP, this leaf is not affected."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }, 
                "index": {
                    "default": "0", 
                    "info": {
                        "description": "The index of the subinterface, or logical interface number.\nOn systems with no support for subinterfaces, or not using\nsubinterfaces, this value should default to 0, i.e., the\ndefault subinterface."
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe name of the interface.\n\nA device MAY restrict the allowed values for this leaf,\npossibly depending on the type of the interface.\nFor system-controlled interfaces, this leaf is the\ndevice-specific name of the interface.  The 'config false'\nlist interfaces/interface[name]/state contains the currently\nexisting interfaces on the device.\n\nIf a client tries to create configuration for a\nsystem-controlled interface that is not present in the\ncorresponding state list, the server MAY reject\nthe request if the implementation does not support\npre-provisioning of interfaces or if the name refers to\nan interface that can never exist in the system.  A\nNETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case.\n\nThe IETF model in RFC 7223 provides YANG features for the\nfollowing (i.e., pre-provisioning and arbitrary-names),\nhowever they are omitted here:\n\n If the device supports pre-provisioning of interface\n configuration, the 'pre-provisioning' feature is\n advertised.\n\n If the device allows arbitrarily named user-controlled\n interfaces, the 'arbitrary-names' feature is advertised.\n\nWhen a configured user-controlled interface is created by\nthe system, it is instantiated with the same name in the\n/interfaces/interface[name]/state list."
                    }, 
                    "type": {
                        "string": {}
                    }
                }
            }
        }, 
        "subinterface_state_860": {
            "config": "false", 
            "container": {
                "container": [
                    [
                        "counters", 
                        "interface-counters-state_counters_475"
                    ]
                ]
            }, 
            "info": {
                "description": "Operational state data for logical interfaces"
            }, 
            "leaf": {
                "admin-status": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe desired state of the interface.  In RFC 7223 this leaf\nhas the same read semantics as ifAdminStatus.  Here, it\nreflects the administrative state as set by enabling or\ndisabling the interface."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "enumeration": {
                            "enum": {
                                "DOWN": {
                                    "info": {
                                        "description": "Not ready to pass packets and not in some test mode."
                                    }
                                }, 
                                "TESTING": {
                                    "info": {
                                        "description": "In some test mode."
                                    }
                                }, 
                                "UP": {
                                    "info": {
                                        "description": "Ready to pass packets."
                                    }
                                }
                            }
                        }
                    }
                }, 
                "description": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nA textual description of the interface.\n\nA server implementation MAY map this leaf to the ifAlias\nMIB object.  Such an implementation needs to use some\nmechanism to handle the differences in size and characters\nallowed between this leaf and ifAlias.  The definition of\nsuch a mechanism is outside the scope of this document.\n\nSince ifAlias is defined to be stored in non-volatile\nstorage, the MIB implementation MUST map ifAlias to the\nvalue of 'description' in the persistently stored\ndatastore.\n\nSpecifically, if the device supports ':startup', when\nifAlias is read the device MUST return the value of\n'description' in the 'startup' datastore, and when it is\nwritten, it MUST be written to the 'running' and 'startup'\ndatastores.  Note that it is up to the implementation to\n\ndecide whether to modify this single leaf in 'startup' or\nperform an implicit copy-config from 'running' to\n'startup'.\n\nIf the device does not support ':startup', ifAlias MUST\nbe mapped to the 'description' leaf in the 'running'\ndatastore."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "enabled": {
                    "default": "true", 
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThis leaf contains the configured, desired state of the\ninterface.\n\nSystems that implement the IF-MIB use the value of this\nleaf in the 'running' datastore to set\nIF-MIB.ifAdminStatus to 'up' or 'down' after an ifEntry\nhas been initialized, as described in RFC 2863.\n\nChanges in this leaf in the 'running' datastore are\nreflected in ifAdminStatus, but if ifAdminStatus is\nchanged over SNMP, this leaf is not affected."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }, 
                "ifindex": {
                    "info": {
                        "description": "System assigned number for each interface.  Corresponds to\nifIndex object in SNMP Interface MIB"
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }, 
                "index": {
                    "default": "0", 
                    "info": {
                        "description": "The index of the subinterface, or logical interface number.\nOn systems with no support for subinterfaces, or not using\nsubinterfaces, this value should default to 0, i.e., the\ndefault subinterface."
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }, 
                "last-change": {
                    "info": {
                        "description": "Date and time of the last state change of the interface\n(e.g., up-to-down transition).   This corresponds to the\nifLastChange object in the standard interface MIB."
                    }, 
                    "type": {
                        "yang:timeticks": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe name of the interface.\n\nA device MAY restrict the allowed values for this leaf,\npossibly depending on the type of the interface.\nFor system-controlled interfaces, this leaf is the\ndevice-specific name of the interface.  The 'config false'\nlist interfaces/interface[name]/state contains the currently\nexisting interfaces on the device.\n\nIf a client tries to create configuration for a\nsystem-controlled interface that is not present in the\ncorresponding state list, the server MAY reject\nthe request if the implementation does not support\npre-provisioning of interfaces or if the name refers to\nan interface that can never exist in the system.  A\nNETCONF server MUST reply with an rpc-error with the\nerror-tag 'invalid-value' in this case.\n\nThe IETF model in RFC 7223 provides YANG features for the\nfollowing (i.e., pre-provisioning and arbitrary-names),\nhowever they are omitted here:\n\n If the device supports pre-provisioning of interface\n configuration, the 'pre-provisioning' feature is\n advertised.\n\n If the device allows arbitrarily named user-controlled\n interfaces, the 'arbitrary-names' feature is advertised.\n\nWhen a configured user-controlled interface is created by\nthe system, it is instantiated with the same name in the\n/interfaces/interface[name]/state list."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "oper-status": {
                    "info": {
                        "description": "[adapted from IETF interfaces model (RFC 7223)]\n\nThe current operational state of the interface.\n\nThis leaf has the same semantics as ifOperStatus."
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "enumeration": {
                            "enum": {
                                "DORMANT": {
                                    "info": {
                                        "description": "Waiting for some external event."
                                    }, 
                                    "value": "5"
                                }, 
                                "DOWN": {
                                    "info": {
                                        "description": "The interface does not pass any packets."
                                    }, 
                                    "value": "2"
                                }, 
                                "LOWER_LAYER_DOWN": {
                                    "info": {
                                        "description": "Down due to state of lower-layer interface(s)."
                                    }, 
                                    "value": "7"
                                }, 
                                "NOT_PRESENT": {
                                    "info": {
                                        "description": "Some component (typically hardware) is missing."
                                    }, 
                                    "value": "6"
                                }, 
                                "TESTING": {
                                    "info": {
                                        "description": "In some test mode.  No operational packets can\nbe passed."
                                    }, 
                                    "value": "3"
                                }, 
                                "UNKNOWN": {
                                    "info": {
                                        "description": "Status cannot be determined for some reason."
                                    }, 
                                    "value": "4"
                                }, 
                                "UP": {
                                    "info": {
                                        "description": "Ready to pass packets."
                                    }, 
                                    "value": "1"
                                }
                            }
                        }
                    }
                }
            }
        }, 
        "subinterfaces-top_subinterfaces_832": {
            "info": {
                "description": "Enclosing container for the list of subinterfaces associated\nwith a physical interface"
            }, 
            "list": {
                "list": [
                    [
                        "subinterface", 
                        "subinterfaces_subinterface_837"
                    ]
                ]
            }
        }, 
        "unnumbered_config_779": {
            "info": {
                "description": "Configuration data for unnumbered interface"
            }, 
            "leaf": {
                "enabled": {
                    "default": "false", 
                    "info": {
                        "description": "Indicates that the subinterface is unnumbered.  By default\nthe subinterface is numbered, i.e., expected to have an\nIP address configuration."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }
            }
        }, 
        "unnumbered_state_786": {
            "config": "false", 
            "info": {
                "description": "Operational state data for unnumbered interfaces"
            }, 
            "leaf": {
                "enabled": {
                    "default": "false", 
                    "info": {
                        "description": "Indicates that the subinterface is unnumbered.  By default\nthe subinterface is numbered, i.e., expected to have an\nIP address configuration."
                    }, 
                    "type": {
                        "boolean": {}
                    }
                }
            }
        }
    }, 
    "identity": {}, 
    "import": {
        "ietf-interfaces": {
            "info": {
                "prefix": "ietf-if"
            }
        }, 
        "ietf-yang-types": {
            "info": {
                "prefix": "yang"
            }
        }, 
        "openconfig-extensions": {
            "info": {
                "prefix": "oc-ext"
            }
        }
    }, 
    "info": {
        "contact": "OpenConfig working group\nnetopenconfig@googlegroups.com", 
        "namespace": "http://openconfig.net/yang/interfaces", 
        "openconfig-extensions": {
            "openconfig-version": "1.0.2"
        }, 
        "organization": "OpenConfig working group", 
        "revision": {
            "2016-05-26": {
                "revision": "2016-05-26"
            }
        }, 
        "yang-version": "1"
    }, 
    "list": {
        "interfaces_interface_884": {
            "container": {
                "container": [
                    [
                        "state", 
                        "interface_state_913"
                    ], 
                    [
                        "config", 
                        "interface_config_905"
                    ], 
                    [
                        "hold-time", 
                        "interface-phys-holdtime-top_hold-time_327"
                    ], 
                    [
                        "subinterfaces", 
                        "subinterfaces-top_subinterfaces_832"
                    ]
                ]
            }, 
            "info": {
                "description": "The list of named interfaces on the device."
            }, 
            "key": "name", 
            "leaf": {
                "name": {
                    "info": {
                        "description": "References the configured name of the interface"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/name"
                        }
                    }
                }
            }
        }, 
        "subinterfaces_subinterface_837": {
            "container": {
                "container": [
                    [
                        "state", 
                        "subinterface_state_860"
                    ], 
                    [
                        "config", 
                        "subinterface_config_853"
                    ]
                ]
            }, 
            "info": {
                "description": "The list of subinterfaces (logical interfaces) associated\nwith a physical interface"
            }, 
            "key": "index", 
            "leaf": {
                "index": {
                    "info": {
                        "description": "The index number of the subinterface -- used to address\nthe logical interface"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/index"
                        }
                    }
                }
            }
        }
    }, 
    "order": [
        [
            "container", 
            "interface-ref-state-container_state_103"
        ], 
        [
            "container", 
            "interface-ref_config_121"
        ], 
        [
            "container", 
            "interface-ref_interface-ref_117"
        ], 
        [
            "container", 
            "interface-ref-state_interface-ref_137"
        ], 
        [
            "container", 
            "hold-time_config_332"
        ], 
        [
            "container", 
            "hold-time_state_339"
        ], 
        [
            "container", 
            "interface-phys-holdtime-top_hold-time_327"
        ], 
        [
            "container", 
            "interface-counters-state_counters_475"
        ], 
        [
            "container", 
            "unnumbered_config_779"
        ], 
        [
            "container", 
            "unnumbered_state_786"
        ], 
        [
            "container", 
            "sub-unnumbered-top_unnumbered_773"
        ], 
        [
            "container", 
            "subinterface_config_853"
        ], 
        [
            "container", 
            "subinterface_state_860"
        ], 
        [
            "list", 
            "subinterfaces_subinterface_837"
        ], 
        [
            "container", 
            "subinterfaces-top_subinterfaces_832"
        ], 
        [
            "container", 
            "interface_config_905"
        ], 
        [
            "container", 
            "interface_state_913"
        ], 
        [
            "list", 
            "interfaces_interface_884"
        ], 
        [
            "container", 
            "interfaces-top_interfaces_878"
        ]
    ], 
    "top": {
        "container": {
            "container": [
                [
                    "interfaces", 
                    "interfaces-top_interfaces_878"
                ]
            ]
        }
    }, 
    "typedef": {
        "base-interface-ref": {
            "info": {
                "description": "Reusable type for by-name reference to a base interface.\nThis type may be used in cases where ability to reference\na subinterface is not required."
            }, 
            "type": {
                "leafref": {
                    "path": "/oc-if:interfaces/oc-if:interface/oc-if:name"
                }
            }
        }, 
        "interface-id": {
            "info": {
                "description": "User-defined identifier for an interface, generally used to\nname a interface reference.  The id can be arbitrary but a\nuseful convention is to use a combination of base interface\nname and subinterface index."
            }, 
            "type": {
                "string": {}
            }
        }
    }
}
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports
from napalm_yang.openconfig_extensions import oc_ext
from napalm_yang.ietf_yang_types import yang
from napalm_yang.ietf_interfaces import ietf_if

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()
openconfig_extensions.openconfig_version = "1.0.2"


__namespace__ = "http://openconfig.net/yang/interfaces"
__yang_version__ = "1"
__contact__ = "OpenConfig working group\nnetopenconfig@googlegroups.com"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-05-26": {
        "revision": "2016-05-26"
    }
}



# typedef

class InterfaceId(yang_base.BaseBinding):
    """
    User-defined identifier for an interface, generally used to
    name a interface reference.  The id can be arbitrary but a
    useful convention is to use a combination of base interface
    name and subinterface index.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.interface_id = yang.String()


class BaseInterfaceRef(yang_base.BaseBinding):
    """
    Reusable type for by-name reference to a base interface.
    This type may be used in cases where ability to reference
    a subinterface is not required.
    """
    def __init__(self, _meta=None):
        super().__init__(_meta)
        self.base_interface_ref = yang.Leafref(path="/oc-if:interfaces/oc-if:interface/oc-if:name")



# Identities

# Classes to support containers and lists
class InterfaceRefStateContainer_State_103(yang_base.BaseBinding):
    """
    Operational state for interface-ref
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.interface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface/oc-if:name")
        self.subinterface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index")
        # Meta
        self._meta["config"] = False
        

class InterfaceRef_Config_121(yang_base.BaseBinding):
    """
    Configured reference to interface / subinterface
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.interface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface/oc-if:name")
        self.subinterface = Leafref(_meta={"mandatory": False}, path="/oc-if:interfaces/oc-if:interface[oc-if:name=current()/../interface]/oc-if:subinterfaces/oc-if:subinterface/oc-if:index")
        # Meta
        self._meta["config"] = True
        

class InterfaceRef_InterfaceRef_117(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    def __init__(self):
        super().__init__()
        # container
        self.config = InterfaceRef_Config_121()
        self.state = InterfaceRefStateContainer_State_103()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class InterfaceRefState_InterfaceRef_137(yang_base.BaseBinding):
    """
    Reference to an interface or subinterface
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = InterfaceRefStateContainer_State_103()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class HoldTime_Config_332(yang_base.BaseBinding):
    """
    Configuration data for interface hold-time settings.
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.down = Uint32(_meta={"mandatory": False}, )
        self.up = Uint32(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class HoldTime_State_339(yang_base.BaseBinding):
    """
    Operational state data for interface hold-time.
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.down = Uint32(_meta={"mandatory": False}, )
        self.up = Uint32(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class InterfacePhysHoldtimeTop_HoldTime_327(yang_base.BaseBinding):
    """
    Top-level container for hold-time settings to enable
    dampening advertisements of interface transitions.
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = HoldTime_State_339()
        self.config = HoldTime_Config_332()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class InterfaceCountersState_Counters_475(yang_base.BaseBinding):
    """
    A collection of interface-related statistics objects.
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.out_octets = yang.Counter64(_meta={"mandatory": False}, )
        self.in_errors = yang.Counter64(_meta={"mandatory": False}, )
        self.in_discards = yang.Counter64(_meta={"mandatory": False}, )
        self.out_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_errors = yang.Counter64(_meta={"mandatory": False}, )
        self.out_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_multicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.last_clear = yang.DateAndTime(_meta={"mandatory": False}, )
        self.in_unicast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.out_discards = yang.Counter64(_meta={"mandatory": False}, )
        self.in_broadcast_pkts = yang.Counter64(_meta={"mandatory": False}, )
        self.in_unknown_protos = yang.Counter32(_meta={"mandatory": False}, )
        self.in_octets = yang.Counter64(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class Unnumbered_Config_779(yang_base.BaseBinding):
    """
    Configuration data for unnumbered interface
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class Unnumbered_State_786(yang_base.BaseBinding):
    """
    Operational state data for unnumbered interfaces
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class SubUnnumberedTop_Unnumbered_773(yang_base.BaseBinding):
    """
    Top-level container for setting unnumbered interfaces.
    Includes reference the interface that provides the
    address information
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Unnumbered_State_786()
        self.config = Unnumbered_Config_779()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class Subinterface_Config_853(yang_base.BaseBinding):
    """
    Configurable items at the subinterface level
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.index = Uint32(_meta={"mandatory": False}, )
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class Subinterface_State_860(yang_base.BaseBinding):
    """
    Operational state data for logical interfaces
    """
    def __init__(self):
        super().__init__()
        # container
        self.counters = InterfaceCountersState_Counters_475()
        # list
        # leaf
        self.index = Uint32(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        self.oper_status = Enumeration(_meta={"mandatory": True}, enum={
            "DORMANT": {
                "info": {
                    "description": "Waiting for some external event."
                }, 
                "value": "5"
            }, 
            "DOWN": {
                "info": {
                    "description": "The interface does not pass any packets."
                }, 
                "value": "2"
            }, 
            "LOWER_LAYER_DOWN": {
                "info": {
                    "description": "Down due to state of lower-layer interface(s)."
                }, 
                "value": "7"
            }, 
            "NOT_PRESENT": {
                "info": {
                    "description": "Some component (typically hardware) is missing."
                }, 
                "value": "6"
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode.  No operational packets can\nbe passed."
                }, 
                "value": "3"
            }, 
            "UNKNOWN": {
                "info": {
                    "description": "Status cannot be determined for some reason."
                }, 
                "value": "4"
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }, 
                "value": "1"
            }
        })
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.ifindex = Uint32(_meta={"mandatory": False}, )
        self.last_change = yang.Timeticks(_meta={"mandatory": False}, )
        self.admin_status = Enumeration(_meta={"mandatory": True}, enum={
            "DOWN": {
                "info": {
                    "description": "Not ready to pass packets and not in some test mode."
                }
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode."
                }
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }
            }
        })
        self.name = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class Subinterfaces_Subinterface_837(yang.List):
    """
    The list of subinterfaces (logical interfaces) associated
    with a physical interface
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Subinterface_State_860()
        self.config = Subinterface_Config_853()
        # list
        # leaf
        self.index = Leafref(_meta={"mandatory": False}, path="../config/index")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "index"


class SubinterfacesTop_Subinterfaces_832(yang_base.BaseBinding):
    """
    Enclosing container for the list of subinterfaces associated
    with a physical interface
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.subinterface = Subinterfaces_Subinterface_837()
        # leaf
        # Meta
        self._meta["config"] = True
        

class Interface_Config_905(yang_base.BaseBinding):
    """
    Configurable items at the global, physical interface
    level
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.type = Identityref(_meta={"mandatory": True}, base="ietf-if:interface-type")
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        self.mtu = Uint16(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class Interface_State_913(yang_base.BaseBinding):
    """
    Operational state data at the global interface level
    """
    def __init__(self):
        super().__init__()
        # container
        self.counters = InterfaceCountersState_Counters_475()
        # list
        # leaf
        self.description = String(_meta={"mandatory": False}, )
        self.admin_status = Enumeration(_meta={"mandatory": True}, enum={
            "DOWN": {
                "info": {
                    "description": "Not ready to pass packets and not in some test mode."
                }
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode."
                }
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }
            }
        })
        self.oper_status = Enumeration(_meta={"mandatory": True}, enum={
            "DORMANT": {
                "info": {
                    "description": "Waiting for some external event."
                }, 
                "value": "5"
            }, 
            "DOWN": {
                "info": {
                    "description": "The interface does not pass any packets."
                }, 
                "value": "2"
            }, 
            "LOWER_LAYER_DOWN": {
                "info": {
                    "description": "Down due to state of lower-layer interface(s)."
                }, 
                "value": "7"
            }, 
            "NOT_PRESENT": {
                "info": {
                    "description": "Some component (typically hardware) is missing."
                }, 
                "value": "6"
            }, 
            "TESTING": {
                "info": {
                    "description": "In some test mode.  No operational packets can\nbe passed."
                }, 
                "value": "3"
            }, 
            "UNKNOWN": {
                "info": {
                    "description": "Status cannot be determined for some reason."
                }, 
                "value": "4"
            }, 
            "UP": {
                "info": {
                    "description": "Ready to pass packets."
                }, 
                "value": "1"
            }
        })
        self.enabled = Boolean(_meta={"mandatory": False}, )
        self.mtu = Uint16(_meta={"mandatory": False}, )
        self.ifindex = Uint32(_meta={"mandatory": False}, )
        self.last_change = yang.Timeticks(_meta={"mandatory": False}, )
        self.type = Identityref(_meta={"mandatory": True}, base="ietf-if:interface-type")
        self.name = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class Interfaces_Interface_884(yang.List):
    """
    The list of named interfaces on the device.
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Interface_State_913()
        self.config = Interface_Config_905()
        self.hold_time = InterfacePhysHoldtimeTop_HoldTime_327()
        self.subinterfaces = SubinterfacesTop_Subinterfaces_832()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False}, path="../config/name")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"


class InterfacesTop_Interfaces_878(yang_base.BaseBinding):
    """
    Top level container for interfaces, including configuration
    and state data.
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.interface = Interfaces_Interface_884()
        # leaf
        # Meta
        self._meta["config"] = True
        


# Top level
class Interfaces(InterfacesTop_Interfaces_878):
    """Top level class"""
    pass
