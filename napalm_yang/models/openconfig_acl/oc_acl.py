"""
This module defines configuration and operational state
data for network access control lists (i.e., filters, rules,
etc.).  ACLs are organized into ACL sets, with each set
containing one or more ACL entries.  ACL sets are identified
by a unique name, while each entry within a set is assigned
a sequence-id that determines the order in which the ACL
rules are applied to a packet.

The model allows individual ACL rules to combine match criteria
from various fields in the packet, along with an action that
defines how matching packets should be handled.  Note that some
device implementations may require separate entries for match
criteria that cross protocol layers, e.g., MAC layer and IP
layer matches.

{
    "container": {
        "access-list-entries-top_acl-entries_304": {
            "info": {
                "description": "Access list entries container"
            }, 
            "list": {
                "list": [
                    [
                        "acl-entry", 
                        "acl-entries_acl-entry_308"
                    ]
                ]
            }
        }, 
        "acl-entry_config_321": {
            "info": {
                "description": "Access list entries config"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "A user-defined description, or comment, for this Access List\nEntry."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "sequence-id": {
                    "info": {
                        "description": "The sequence id determines the order in which ACL entries\nare applied.  The sequence id must be unique for each entry\nin an ACL set.  Target devices should apply the ACL entry\nrules in the order determined by sequence id, rather than\nthe relying only on order in the list."
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }
            }
        }, 
        "acl-entry_state_327": {
            "config": "false", 
            "info": {
                "description": "State information for ACL entries"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "A user-defined description, or comment, for this Access List\nEntry."
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "matched-octets": {
                    "info": {
                        "description": "Count of the number of octets (bytes) matching the current\nACL entry.\n\nAn implementation should provide this counter on a\nper-interface per-ACL-entry if possible.\n\nIf an implementation only supports ACL counters per entry\n(i.e., not broken out per interface), then the value\nshould be equal to the aggregate count across all interfaces.\n\nAn implementation that provides counters per entry per\ninterface is not required to also provide an aggregate count,\ne.g., per entry -- the user is expected to be able implement\nthe required aggregation if such a count is needed."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "matched-packets": {
                    "info": {
                        "description": "Count of the number of packets matching the current ACL\nentry.\n\nAn implementation should provide this counter on a\nper-interface per-ACL-entry if possible.\n\nIf an implementation only supports ACL counters per entry\n(i.e., not broken out per interface), then the value\nshould be equal to the aggregate count across all interfaces.\n\nAn implementation that provides counters per entry per\ninterface is not required to also provide an aggregate count,\ne.g., per entry -- the user is expected to be able implement\nthe required aggregation if such a count is needed."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "sequence-id": {
                    "info": {
                        "description": "The sequence id determines the order in which ACL entries\nare applied.  The sequence id must be unique for each entry\nin an ACL set.  Target devices should apply the ACL entry\nrules in the order determined by sequence id, rather than\nthe relying only on order in the list."
                    }, 
                    "type": {
                        "uint32": {}
                    }
                }
            }
        }, 
        "acl-entry_state_458": {
            "config": "false", 
            "info": {
                "description": "Operational state data for per-interface ACL entries"
            }, 
            "leaf": {
                "matched-octets": {
                    "info": {
                        "description": "Count of the number of octets (bytes) matching the current\nACL entry.\n\nAn implementation should provide this counter on a\nper-interface per-ACL-entry if possible.\n\nIf an implementation only supports ACL counters per entry\n(i.e., not broken out per interface), then the value\nshould be equal to the aggregate count across all interfaces.\n\nAn implementation that provides counters per entry per\ninterface is not required to also provide an aggregate count,\ne.g., per entry -- the user is expected to be able implement\nthe required aggregation if such a count is needed."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "matched-packets": {
                    "info": {
                        "description": "Count of the number of packets matching the current ACL\nentry.\n\nAn implementation should provide this counter on a\nper-interface per-ACL-entry if possible.\n\nIf an implementation only supports ACL counters per entry\n(i.e., not broken out per interface), then the value\nshould be equal to the aggregate count across all interfaces.\n\nAn implementation that provides counters per entry per\ninterface is not required to also provide an aggregate count,\ne.g., per entry -- the user is expected to be able implement\nthe required aggregation if such a count is needed."
                    }, 
                    "type": {
                        "yang:counter64": {}
                    }
                }, 
                "sequence-id": {
                    "info": {
                        "description": "Reference to an entry in the ACL set applied to an\ninterface"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/acl/acl-sets/acl-set[name=current()/../../../../set-name]/acl-entries/acl-entry/sequence-id"
                        }
                    }
                }
            }
        }, 
        "acl-interfaces-top_interfaces_619": {
            "info": {
                "description": "Enclosing container for the list of interfaces on which\nACLs are set"
            }, 
            "list": {
                "list": [
                    [
                        "interface", 
                        "interfaces_interface_624"
                    ]
                ]
            }
        }, 
        "acl-set-top_acl-sets_372": {
            "info": {
                "description": "Access list entries variables enclosing container"
            }, 
            "list": {
                "list": [
                    [
                        "acl-set", 
                        "acl-sets_acl-set_376"
                    ]
                ]
            }
        }, 
        "acl-set_config_390": {
            "info": {
                "description": "Access list config"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "Description, or comment, for the ACL set"
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "The name of the access-list set"
                    }, 
                    "type": {
                        "string": {}
                    }
                }
            }
        }, 
        "acl-set_state_396": {
            "config": "false", 
            "info": {
                "description": "Access list state information"
            }, 
            "leaf": {
                "description": {
                    "info": {
                        "description": "Description, or comment, for the ACL set"
                    }, 
                    "type": {
                        "string": {}
                    }
                }, 
                "name": {
                    "info": {
                        "description": "The name of the access-list set"
                    }, 
                    "type": {
                        "string": {}
                    }
                }
            }
        }, 
        "acl-top_acl_684": {
            "container": {
                "container": [
                    [
                        "state", 
                        "acl_state_696"
                    ], 
                    [
                        "config", 
                        "acl_config_689"
                    ], 
                    [
                        "acl-sets", 
                        "acl-set-top_acl-sets_372"
                    ], 
                    [
                        "interfaces", 
                        "acl-interfaces-top_interfaces_619"
                    ]
                ]
            }, 
            "info": {
                "description": "Top level enclosing container for ACL model config\nand operational state data"
            }
        }, 
        "acl_config_689": {
            "info": {
                "description": "Global config data for ACLs"
            }
        }, 
        "acl_state_696": {
            "config": "false", 
            "info": {
                "description": "Global operational state data for ACLs"
            }, 
            "leaf": {
                "counter-capability": {
                    "info": {
                        "description": "System reported indication of how ACL counters are reported\nby the target"
                    }, 
                    "type": {
                        "identityref": {
                            "base": "ACL_COUNTER_CAPABILITY"
                        }
                    }
                }
            }
        }, 
        "action-top_actions_203": {
            "container": {
                "container": [
                    [
                        "state", 
                        "actions_state_214"
                    ], 
                    [
                        "config", 
                        "actions_config_208"
                    ]
                ]
            }, 
            "info": {
                "description": "Enclosing container for list of ACL actions associated\nwith an entry"
            }
        }, 
        "actions_config_208": {
            "info": {
                "description": "Config data for ACL actions"
            }, 
            "leaf": {
                "forwarding-action": {
                    "info": {
                        "description": "Specifies the forwarding action.  One forwarding action\nmust be specified for each ACL entry"
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "identityref": {
                            "base": "FORWARDING_ACTION"
                        }
                    }
                }, 
                "log-action": {
                    "default": "LOG_NONE", 
                    "info": {
                        "description": "Specifies the log action and destination for\nmatched packets.  The default is not to log the\npacket."
                    }, 
                    "type": {
                        "identityref": {
                            "base": "LOG_ACTION"
                        }
                    }
                }
            }
        }, 
        "actions_state_214": {
            "config": "false", 
            "info": {
                "description": "State information for ACL actions"
            }, 
            "leaf": {
                "forwarding-action": {
                    "info": {
                        "description": "Specifies the forwarding action.  One forwarding action\nmust be specified for each ACL entry"
                    }, 
                    "mandatory": "true", 
                    "type": {
                        "identityref": {
                            "base": "FORWARDING_ACTION"
                        }
                    }
                }, 
                "log-action": {
                    "default": "LOG_NONE", 
                    "info": {
                        "description": "Specifies the log action and destination for\nmatched packets.  The default is not to log the\npacket."
                    }, 
                    "type": {
                        "identityref": {
                            "base": "LOG_ACTION"
                        }
                    }
                }
            }
        }, 
        "egress-acl-set_config_575": {
            "info": {
                "description": "Configuration data "
            }, 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to the ACL set applied on egress"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/acl/acl-sets/acl-set/config/name"
                        }
                    }
                }
            }
        }, 
        "egress-acl-set_state_582": {
            "config": "false", 
            "info": {
                "description": "Operational state data for interface egress ACLs"
            }, 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to the ACL set applied on egress"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/acl/acl-sets/acl-set/config/name"
                        }
                    }
                }
            }
        }, 
        "ingress-acl-set_config_512": {
            "info": {
                "description": "Configuration data "
            }, 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to the ACL set applied on ingress"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/acl/acl-sets/acl-set/config/name"
                        }
                    }
                }
            }
        }, 
        "ingress-acl-set_state_519": {
            "config": "false", 
            "info": {
                "description": "Operational state data for interface ingress ACLs"
            }, 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to the ACL set applied on ingress"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "/acl/acl-sets/acl-set/config/name"
                        }
                    }
                }
            }
        }, 
        "input-interface-top_input-interface_140": {
            "container": {
                "container": [
                    [
                        "state", 
                        "input-interface_state_150"
                    ], 
                    [
                        "config", 
                        "input-interface_config_144"
                    ]
                ]
            }, 
            "info": {
                "description": "Input interface container"
            }
        }, 
        "input-interface_config_144": {
            "info": {
                "description": "Config data"
            }
        }, 
        "input-interface_state_150": {
            "config": "false", 
            "info": {
                "description": "State information"
            }
        }, 
        "interface-acl-entries-top_acl-entries_437": {
            "config": "false", 
            "info": {
                "description": "Enclosing container for list of references to ACLs"
            }, 
            "list": {
                "list": [
                    [
                        "acl-entry", 
                        "acl-entries_acl-entry_442"
                    ]
                ]
            }
        }, 
        "interface-egress-acl-top_egress-acl-sets_557": {
            "info": {
                "description": "Enclosing container the list of egress ACLs on the\ninterface"
            }, 
            "list": {
                "list": [
                    [
                        "egress-acl-set", 
                        "egress-acl-sets_egress-acl-set_562"
                    ]
                ]
            }
        }, 
        "interface-ingress-acl-top_ingress-acl-sets_494": {
            "info": {
                "description": "Enclosing container the list of ingress ACLs on the\ninterface"
            }, 
            "list": {
                "list": [
                    [
                        "ingress-acl-set", 
                        "ingress-acl-sets_ingress-acl-set_499"
                    ]
                ]
            }
        }, 
        "interface_config_637": {
            "info": {
                "description": "Configuration for ACL per-interface data"
            }, 
            "leaf": {
                "id": {
                    "info": {
                        "description": "User-defined identifier for the interface -- a common\nconvention could be '<if name>.<subif index>'"
                    }, 
                    "type": {
                        "oc-if:interface-id": {}
                    }
                }
            }
        }, 
        "interface_state_644": {
            "config": "false", 
            "info": {
                "description": "Operational state for ACL per-interface data"
            }, 
            "leaf": {
                "id": {
                    "info": {
                        "description": "User-defined identifier for the interface -- a common\nconvention could be '<if name>.<subif index>'"
                    }, 
                    "type": {
                        "oc-if:interface-id": {}
                    }
                }
            }
        }
    }, 
    "identity": {
        "ACCEPT": {
            "base": "FORWARDING_ACTION", 
            "info": {
                "description": "Accept the packet"
            }
        }, 
        "ACL_COUNTER_CAPABILITY": {
            "info": {
                "description": "Base identity for system to indicate how it is able to report\ncounters"
            }
        }, 
        "AGGREGATE_ONLY": {
            "base": "ACL_COUNTER_CAPABILITY", 
            "info": {
                "description": "ACL counters are aggregated over all interfaces, and reported\nonly per ACL entry"
            }
        }, 
        "DROP": {
            "base": "FORWARDING_ACTION", 
            "info": {
                "description": "Drop packet without sending any ICMP error message"
            }
        }, 
        "FORWARDING_ACTION": {
            "info": {
                "description": "Base identity for actions in the forwarding category"
            }
        }, 
        "INTERFACE_AGGREGATE": {
            "base": "ACL_COUNTER_CAPABILITY", 
            "info": {
                "description": "ACL counters are reported per interface, and also aggregated\nand reported per ACL entry."
            }
        }, 
        "INTERFACE_ONLY": {
            "base": "ACL_COUNTER_CAPABILITY", 
            "info": {
                "description": "ACL counters are available and reported only per interface"
            }
        }, 
        "LOG_ACTION": {
            "info": {
                "description": "Base identity for defining the destination for logging\nactions"
            }
        }, 
        "LOG_NONE": {
            "base": "LOG_ACTION", 
            "info": {
                "description": "No logging"
            }
        }, 
        "LOG_SYSLOG": {
            "base": "LOG_ACTION", 
            "info": {
                "description": "Log the packet in Syslog"
            }
        }, 
        "REJECT": {
            "base": "FORWARDING_ACTION", 
            "info": {
                "description": "Drop the packet and send an ICMP error message to the source"
            }
        }
    }, 
    "import": {
        "ietf-yang-types": {
            "info": {
                "prefix": "yang"
            }
        }, 
        "openconfig-extensions": {
            "info": {
                "prefix": "oc-ext"
            }
        }, 
        "openconfig-interfaces": {
            "info": {
                "prefix": "oc-if"
            }
        }, 
        "openconfig-packet-match": {
            "info": {
                "prefix": "oc-match"
            }
        }
    }, 
    "info": {
        "contact": "OpenConfig working group\nwww.openconfig.net", 
        "namespace": "http://openconfig.net/yang/acl", 
        "openconfig-extensions": {
            "openconfig-version": "0.2.0"
        }, 
        "organization": "OpenConfig working group", 
        "revision": {
            "2016-01-22": {
                "revision": "2016-01-22"
            }, 
            "2016-08-08": {
                "revision": "2016-08-08"
            }
        }, 
        "yang-version": "1"
    }, 
    "list": {
        "acl-entries_acl-entry_308": {
            "container": {
                "container": [
                    [
                        "state", 
                        "acl-entry_state_327"
                    ], 
                    [
                        "config", 
                        "acl-entry_config_321"
                    ], 
                    [
                        "input-interface", 
                        "input-interface-top_input-interface_140"
                    ], 
                    [
                        "actions", 
                        "action-top_actions_203"
                    ]
                ]
            }, 
            "info": {
                "description": "List of ACL entries comprising an ACL set"
            }, 
            "key": "sequence-id", 
            "leaf": {
                "sequence-id": {
                    "info": {
                        "description": "references the list key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/sequence-id"
                        }
                    }
                }
            }
        }, 
        "acl-entries_acl-entry_442": {
            "container": {
                "container": [
                    [
                        "state", 
                        "acl-entry_state_458"
                    ]
                ]
            }, 
            "info": {
                "description": "List of ACL entries assigned to an interface"
            }, 
            "key": "sequence-id", 
            "leaf": {
                "sequence-id": {
                    "info": {
                        "description": "Reference to per-interface acl entry key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../state/sequence-id"
                        }
                    }
                }
            }
        }, 
        "acl-sets_acl-set_376": {
            "container": {
                "container": [
                    [
                        "state", 
                        "acl-set_state_396"
                    ], 
                    [
                        "config", 
                        "acl-set_config_390"
                    ], 
                    [
                        "acl-entries", 
                        "access-list-entries-top_acl-entries_304"
                    ]
                ]
            }, 
            "info": {
                "description": "List of ACL sets, each comprising of a list of ACL\nentries"
            }, 
            "key": "name", 
            "leaf": {
                "name": {
                    "info": {
                        "description": "Reference to the name list key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/name"
                        }
                    }
                }
            }
        }, 
        "egress-acl-sets_egress-acl-set_562": {
            "container": {
                "container": [
                    [
                        "state", 
                        "egress-acl-set_state_582"
                    ], 
                    [
                        "config", 
                        "egress-acl-set_config_575"
                    ], 
                    [
                        "acl-entries", 
                        "interface-acl-entries-top_acl-entries_437"
                    ]
                ]
            }, 
            "info": {
                "description": "List of egress ACLs on the interface"
            }, 
            "key": "set-name", 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to set name list key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/set-name"
                        }
                    }
                }
            }
        }, 
        "ingress-acl-sets_ingress-acl-set_499": {
            "container": {
                "container": [
                    [
                        "state", 
                        "ingress-acl-set_state_519"
                    ], 
                    [
                        "config", 
                        "ingress-acl-set_config_512"
                    ], 
                    [
                        "acl-entries", 
                        "interface-acl-entries-top_acl-entries_437"
                    ]
                ]
            }, 
            "info": {
                "description": "List of ingress ACLs on the interface"
            }, 
            "key": "set-name", 
            "leaf": {
                "set-name": {
                    "info": {
                        "description": "Reference to set name list key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/set-name"
                        }
                    }
                }
            }
        }, 
        "interfaces_interface_624": {
            "container": {
                "container": [
                    [
                        "state", 
                        "interface_state_644"
                    ], 
                    [
                        "config", 
                        "interface_config_637"
                    ], 
                    [
                        "ingress-acl-sets", 
                        "interface-ingress-acl-top_ingress-acl-sets_494"
                    ], 
                    [
                        "egress-acl-sets", 
                        "interface-egress-acl-top_egress-acl-sets_557"
                    ]
                ]
            }, 
            "info": {
                "description": "List of interfaces on which ACLs are set"
            }, 
            "key": "id", 
            "leaf": {
                "id": {
                    "info": {
                        "description": "Reference to the interface id list key"
                    }, 
                    "type": {
                        "leafref": {
                            "path": "../config/id"
                        }
                    }
                }
            }
        }
    }, 
    "order": [
        [
            "container", 
            "input-interface_config_144"
        ], 
        [
            "container", 
            "input-interface_state_150"
        ], 
        [
            "container", 
            "input-interface-top_input-interface_140"
        ], 
        [
            "container", 
            "actions_config_208"
        ], 
        [
            "container", 
            "actions_state_214"
        ], 
        [
            "container", 
            "action-top_actions_203"
        ], 
        [
            "container", 
            "acl-entry_config_321"
        ], 
        [
            "container", 
            "acl-entry_state_327"
        ], 
        [
            "list", 
            "acl-entries_acl-entry_308"
        ], 
        [
            "container", 
            "access-list-entries-top_acl-entries_304"
        ], 
        [
            "container", 
            "acl-set_config_390"
        ], 
        [
            "container", 
            "acl-set_state_396"
        ], 
        [
            "list", 
            "acl-sets_acl-set_376"
        ], 
        [
            "container", 
            "acl-set-top_acl-sets_372"
        ], 
        [
            "container", 
            "acl-entry_state_458"
        ], 
        [
            "list", 
            "acl-entries_acl-entry_442"
        ], 
        [
            "container", 
            "interface-acl-entries-top_acl-entries_437"
        ], 
        [
            "container", 
            "ingress-acl-set_config_512"
        ], 
        [
            "container", 
            "ingress-acl-set_state_519"
        ], 
        [
            "list", 
            "ingress-acl-sets_ingress-acl-set_499"
        ], 
        [
            "container", 
            "interface-ingress-acl-top_ingress-acl-sets_494"
        ], 
        [
            "container", 
            "egress-acl-set_config_575"
        ], 
        [
            "container", 
            "egress-acl-set_state_582"
        ], 
        [
            "list", 
            "egress-acl-sets_egress-acl-set_562"
        ], 
        [
            "container", 
            "interface-egress-acl-top_egress-acl-sets_557"
        ], 
        [
            "container", 
            "interface_config_637"
        ], 
        [
            "container", 
            "interface_state_644"
        ], 
        [
            "list", 
            "interfaces_interface_624"
        ], 
        [
            "container", 
            "acl-interfaces-top_interfaces_619"
        ], 
        [
            "container", 
            "acl_config_689"
        ], 
        [
            "container", 
            "acl_state_696"
        ], 
        [
            "container", 
            "acl-top_acl_684"
        ]
    ], 
    "top": {
        "container": {
            "container": [
                [
                    "acl", 
                    "acl-top_acl_684"
                ]
            ]
        }
    }, 
    "typedef": {}
}
"""
from napalm_yang import yang_base
from napalm_yang.ietf_yang_types.yang import *

# Imports
from napalm_yang.openconfig_extensions import oc_ext
from napalm_yang.ietf_yang_types import yang
from napalm_yang.openconfig_interfaces import oc_if
from napalm_yang.openconfig_packet_match import oc_match

# openconfig-extensions
openconfig_extensions = oc_ext.OpenConfigExtensions()
openconfig_extensions.openconfig_version = "0.2.0"


__namespace__ = "http://openconfig.net/yang/acl"
__yang_version__ = "1"
__contact__ = "OpenConfig working group\nwww.openconfig.net"
__organization__ = "OpenConfig working group"
__revision__ = {
    "2016-01-22": {
        "revision": "2016-01-22"
    }, 
    "2016-08-08": {
        "revision": "2016-08-08"
    }
}



# typedef


# Identities
DROP = yang.Identity(
    base="FORWARDING_ACTION",
    value="DROP",
    description="""Drop packet without sending any ICMP error message"""
    )

ACCEPT = yang.Identity(
    base="FORWARDING_ACTION",
    value="ACCEPT",
    description="""Accept the packet"""
    )

FORWARDING_ACTION = yang.Identity(
    base="None",
    value="FORWARDING_ACTION",
    description="""Base identity for actions in the forwarding category"""
    )

INTERFACE_ONLY = yang.Identity(
    base="ACL_COUNTER_CAPABILITY",
    value="INTERFACE_ONLY",
    description="""ACL counters are available and reported only per interface"""
    )

LOG_ACTION = yang.Identity(
    base="None",
    value="LOG_ACTION",
    description="""Base identity for defining the destination for logging
actions"""
    )

INTERFACE_AGGREGATE = yang.Identity(
    base="ACL_COUNTER_CAPABILITY",
    value="INTERFACE_AGGREGATE",
    description="""ACL counters are reported per interface, and also aggregated
and reported per ACL entry."""
    )

REJECT = yang.Identity(
    base="FORWARDING_ACTION",
    value="REJECT",
    description="""Drop the packet and send an ICMP error message to the source"""
    )

LOG_SYSLOG = yang.Identity(
    base="LOG_ACTION",
    value="LOG_SYSLOG",
    description="""Log the packet in Syslog"""
    )

AGGREGATE_ONLY = yang.Identity(
    base="ACL_COUNTER_CAPABILITY",
    value="AGGREGATE_ONLY",
    description="""ACL counters are aggregated over all interfaces, and reported
only per ACL entry"""
    )

LOG_NONE = yang.Identity(
    base="LOG_ACTION",
    value="LOG_NONE",
    description="""No logging"""
    )

ACL_COUNTER_CAPABILITY = yang.Identity(
    base="None",
    value="ACL_COUNTER_CAPABILITY",
    description="""Base identity for system to indicate how it is able to report
counters"""
    )


# Classes to support containers and lists
class InputInterface_Config_144(yang_base.BaseBinding):
    """
    Config data
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class InputInterface_State_150(yang_base.BaseBinding):
    """
    State information
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        # Meta
        self._meta["config"] = False
        

class InputInterfaceTop_InputInterface_140(yang_base.BaseBinding):
    """
    Input interface container
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = InputInterface_State_150()
        self.config = InputInterface_Config_144()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class Actions_Config_208(yang_base.BaseBinding):
    """
    Config data for ACL actions
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.forwarding_action = Identityref(_meta={"mandatory": True}, base="FORWARDING_ACTION")
        self.log_action = Identityref(_meta={"mandatory": False}, base="LOG_ACTION")
        # Meta
        self._meta["config"] = True
        

class Actions_State_214(yang_base.BaseBinding):
    """
    State information for ACL actions
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.forwarding_action = Identityref(_meta={"mandatory": True}, base="FORWARDING_ACTION")
        self.log_action = Identityref(_meta={"mandatory": False}, base="LOG_ACTION")
        # Meta
        self._meta["config"] = False
        

class ActionTop_Actions_203(yang_base.BaseBinding):
    """
    Enclosing container for list of ACL actions associated
    with an entry
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Actions_State_214()
        self.config = Actions_Config_208()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class AclEntry_Config_321(yang_base.BaseBinding):
    """
    Access list entries config
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.sequence_id = Uint32(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class AclEntry_State_327(yang_base.BaseBinding):
    """
    State information for ACL entries
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.matched_octets = yang.Counter64(_meta={"mandatory": False}, )
        self.sequence_id = Uint32(_meta={"mandatory": False}, )
        self.description = String(_meta={"mandatory": False}, )
        self.matched_packets = yang.Counter64(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class AclEntries_AclEntry_308(yang.List):
    """
    List of ACL entries comprising an ACL set
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = AclEntry_State_327()
        self.config = AclEntry_Config_321()
        self.input_interface = InputInterfaceTop_InputInterface_140()
        self.actions = ActionTop_Actions_203()
        # list
        # leaf
        self.sequence_id = Leafref(_meta={"mandatory": False}, path="../config/sequence-id")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "sequence_id"


class AccessListEntriesTop_AclEntries_304(yang_base.BaseBinding):
    """
    Access list entries container
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.acl_entry = AclEntries_AclEntry_308()
        # leaf
        # Meta
        self._meta["config"] = True
        

class AclSet_Config_390(yang_base.BaseBinding):
    """
    Access list config
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class AclSet_State_396(yang_base.BaseBinding):
    """
    Access list state information
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.description = String(_meta={"mandatory": False}, )
        self.name = String(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class AclSets_AclSet_376(yang.List):
    """
    List of ACL sets, each comprising of a list of ACL
    entries
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = AclSet_State_396()
        self.config = AclSet_Config_390()
        self.acl_entries = AccessListEntriesTop_AclEntries_304()
        # list
        # leaf
        self.name = Leafref(_meta={"mandatory": False}, path="../config/name")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "name"


class AclSetTop_AclSets_372(yang_base.BaseBinding):
    """
    Access list entries variables enclosing container
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.acl_set = AclSets_AclSet_376()
        # leaf
        # Meta
        self._meta["config"] = True
        

class AclEntry_State_458(yang_base.BaseBinding):
    """
    Operational state data for per-interface ACL entries
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.matched_octets = yang.Counter64(_meta={"mandatory": False}, )
        self.sequence_id = Leafref(_meta={"mandatory": False}, path="/acl/acl-sets/acl-set[name=current()/../../../../set-name]/acl-entries/acl-entry/sequence-id")
        self.matched_packets = yang.Counter64(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class AclEntries_AclEntry_442(yang.List):
    """
    List of ACL entries assigned to an interface
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = AclEntry_State_458()
        # list
        # leaf
        self.sequence_id = Leafref(_meta={"mandatory": False}, path="../state/sequence-id")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "sequence_id"


class InterfaceAclEntriesTop_AclEntries_437(yang_base.BaseBinding):
    """
    Enclosing container for list of references to ACLs
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.acl_entry = AclEntries_AclEntry_442()
        # leaf
        # Meta
        self._meta["config"] = False
        

class IngressAclSet_Config_512(yang_base.BaseBinding):
    """
    Configuration data 
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="/acl/acl-sets/acl-set/config/name")
        # Meta
        self._meta["config"] = True
        

class IngressAclSet_State_519(yang_base.BaseBinding):
    """
    Operational state data for interface ingress ACLs
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="/acl/acl-sets/acl-set/config/name")
        # Meta
        self._meta["config"] = False
        

class IngressAclSets_IngressAclSet_499(yang.List):
    """
    List of ingress ACLs on the interface
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = IngressAclSet_State_519()
        self.config = IngressAclSet_Config_512()
        self.acl_entries = InterfaceAclEntriesTop_AclEntries_437()
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="../config/set-name")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "set_name"


class InterfaceIngressAclTop_IngressAclSets_494(yang_base.BaseBinding):
    """
    Enclosing container the list of ingress ACLs on the
    interface
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.ingress_acl_set = IngressAclSets_IngressAclSet_499()
        # leaf
        # Meta
        self._meta["config"] = True
        

class EgressAclSet_Config_575(yang_base.BaseBinding):
    """
    Configuration data 
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="/acl/acl-sets/acl-set/config/name")
        # Meta
        self._meta["config"] = True
        

class EgressAclSet_State_582(yang_base.BaseBinding):
    """
    Operational state data for interface egress ACLs
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="/acl/acl-sets/acl-set/config/name")
        # Meta
        self._meta["config"] = False
        

class EgressAclSets_EgressAclSet_562(yang.List):
    """
    List of egress ACLs on the interface
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = EgressAclSet_State_582()
        self.config = EgressAclSet_Config_575()
        self.acl_entries = InterfaceAclEntriesTop_AclEntries_437()
        # list
        # leaf
        self.set_name = Leafref(_meta={"mandatory": False}, path="../config/set-name")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "set_name"


class InterfaceEgressAclTop_EgressAclSets_557(yang_base.BaseBinding):
    """
    Enclosing container the list of egress ACLs on the
    interface
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.egress_acl_set = EgressAclSets_EgressAclSet_562()
        # leaf
        # Meta
        self._meta["config"] = True
        

class Interface_Config_637(yang_base.BaseBinding):
    """
    Configuration for ACL per-interface data
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.id = oc_if.InterfaceId(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = True
        

class Interface_State_644(yang_base.BaseBinding):
    """
    Operational state for ACL per-interface data
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.id = oc_if.InterfaceId(_meta={"mandatory": False}, )
        # Meta
        self._meta["config"] = False
        

class Interfaces_Interface_624(yang.List):
    """
    List of interfaces on which ACLs are set
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Interface_State_644()
        self.config = Interface_Config_637()
        self.ingress_acl_sets = InterfaceIngressAclTop_IngressAclSets_494()
        self.egress_acl_sets = InterfaceEgressAclTop_EgressAclSets_557()
        # list
        # leaf
        self.id = Leafref(_meta={"mandatory": False}, path="../config/id")
        # Meta
        self._meta["config"] = True
        self._meta["key"] = "id"


class AclInterfacesTop_Interfaces_619(yang_base.BaseBinding):
    """
    Enclosing container for the list of interfaces on which
    ACLs are set
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        self.interface = Interfaces_Interface_624()
        # leaf
        # Meta
        self._meta["config"] = True
        

class Acl_Config_689(yang_base.BaseBinding):
    """
    Global config data for ACLs
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        

class Acl_State_696(yang_base.BaseBinding):
    """
    Global operational state data for ACLs
    """
    def __init__(self):
        super().__init__()
        # container
        # list
        # leaf
        self.counter_capability = Identityref(_meta={"mandatory": False}, base="ACL_COUNTER_CAPABILITY")
        # Meta
        self._meta["config"] = False
        

class AclTop_Acl_684(yang_base.BaseBinding):
    """
    Top level enclosing container for ACL model config
    and operational state data
    """
    def __init__(self):
        super().__init__()
        # container
        self.state = Acl_State_696()
        self.config = Acl_Config_689()
        self.acl_sets = AclSetTop_AclSets_372()
        self.interfaces = AclInterfacesTop_Interfaces_619()
        # list
        # leaf
        # Meta
        self._meta["config"] = True
        


# Top level
class Acl(AclTop_Acl_684):
    """Top level class"""
    pass
