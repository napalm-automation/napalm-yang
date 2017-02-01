"""Tests comparing two models."""
#  import pytest

from napalm_yang import oc_if

import json

diff_1 = """{
    "interfaces": {
        "interface": {
            "both": {
                "et1": {
                    "state": {
                        "mtu": {
                            "other": 9000,
                            "mine": 1500
                        }
                    },
                    "config": {
                        "mtu": {
                            "other": 9000,
                            "mine": 1500
                        }
                    }
                }
            },
            "other": {
                "et3": {
                    "state": {
                        "_meta": {
                            "config": false
                        },
                        "type_": {
                            "_meta": {
                                "mandatory": true,
                                "nested": false,
                                "config": false,
                                "type": "Identityref"
                            },
                            "value": null
                        },
                        "admin_status": {
                            "_meta": {
                                "nested": false,
                                "mandatory": true,
                                "enum": null,
                                "config": false,
                                "type": "Enumeration"
                            },
                            "value": null,
                            "enum_value": null
                        },
                        "oper_status": {
                            "_meta": {
                                "nested": false,
                                "mandatory": true,
                                "enum": null,
                                "config": false,
                                "type": "Enumeration"
                            },
                            "value": null,
                            "enum_value": null
                        },
                        "mtu": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "Uint16"
                            },
                            "value": 9000
                        }
                    },
                    "config": {
                        "_meta": {
                            "config": true
                        },
                        "type_": {
                            "_meta": {
                                "mandatory": true,
                                "nested": false,
                                "config": false,
                                "type": "Identityref"
                            },
                            "value": null
                        },
                        "description": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "String"
                            },
                            "value": "Interface exists only in iright"
                        },
                        "mtu": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "Uint16"
                            },
                            "value": 9000
                        }
                    },
                    "_meta": {
                        "config": true,
                        "key": "name"
                    },
                    "subinterfaces": {
                        "_meta": {
                            "config": true
                        },
                        "subinterface": {
                            "list": {},
                            "_meta": {
                                "config": true,
                                "key": "index"
                            }
                        }
                    }
                }
            },
            "mine": {
                "et2": {
                    "state": {
                        "_meta": {
                            "config": false
                        },
                        "type_": {
                            "_meta": {
                                "mandatory": true,
                                "nested": false,
                                "config": false,
                                "type": "Identityref"
                            },
                            "value": null
                        },
                        "admin_status": {
                            "_meta": {
                                "nested": false,
                                "mandatory": true,
                                "enum": null,
                                "config": false,
                                "type": "Enumeration"
                            },
                            "value": null,
                            "enum_value": null
                        },
                        "oper_status": {
                            "_meta": {
                                "nested": false,
                                "mandatory": true,
                                "enum": null,
                                "config": false,
                                "type": "Enumeration"
                            },
                            "value": null,
                            "enum_value": null
                        },
                        "mtu": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "Uint16"
                            },
                            "value": 1500
                        }
                    },
                    "config": {
                        "_meta": {
                            "config": true
                        },
                        "type_": {
                            "_meta": {
                                "mandatory": true,
                                "nested": false,
                                "config": false,
                                "type": "Identityref"
                            },
                            "value": null
                        },
                        "description": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "String"
                            },
                            "value": "Interface exists only in ileft"
                        },
                        "mtu": {
                            "_meta": {
                                "mandatory": false,
                                "nested": false,
                                "config": false,
                                "type": "Uint16"
                            },
                            "value": 1500
                        }
                    },
                    "_meta": {
                        "config": true,
                        "key": "name"
                    },
                    "subinterfaces": {
                        "_meta": {
                            "config": true
                        },
                        "subinterface": {
                            "list": {},
                            "_meta": {
                                "config": true,
                                "key": "index"
                            }
                        }
                    }
                }
            }
        }
    }
}
"""


class TestYangBuiltinTypes:
    """Wrap tests and fixture."""

    def test_diff_same_object(self):
        """Test the same object has no diff when compared to itself."""
        ileft = oc_if.Interfaces()

        ileft.interfaces.interface.get_element("et1")
        ileft.interfaces.interface["et1"].config.description("asdasda")
        ileft.interfaces.interface["et1"].config.mtu(1500)
        ileft.interfaces.interface["et1"].state.mtu(1500)

        assert not ileft.diff(ileft)

    def test_diff_equal_objects(self):
        """Test that two interfaces are equal have no diff."""
        ileft = oc_if.Interfaces()
        iright = oc_if.Interfaces()

        ileft.interfaces.interface.get_element("et1")
        ileft.interfaces.interface["et1"].config.description("asdasda")
        ileft.interfaces.interface["et1"].config.mtu(1500)
        ileft.interfaces.interface["et1"].state.mtu(1500)
        iright.interfaces.interface.get_element("et1")
        iright.interfaces.interface["et1"].config.description("asdasda")
        iright.interfaces.interface["et1"].config.mtu(1500)
        iright.interfaces.interface["et1"].state.mtu(1500)

        assert not ileft.diff(iright)

    def test_diff_diferent_objects(self):
        """Test diff on different objects."""
        ileft = oc_if.Interfaces()
        iright = oc_if.Interfaces()

        ileft.interfaces.interface.new_element("et1")
        ileft.interfaces.interface["et1"].config.description("Interface exists in both")
        ileft.interfaces.interface["et1"].config.mtu(1500)
        ileft.interfaces.interface["et1"].state.mtu(1500)
        ileft.interfaces.interface.new_element("et2")
        ileft.interfaces.interface["et2"].config.description("Interface exists only in ileft")
        ileft.interfaces.interface["et2"].config.mtu(1500)
        ileft.interfaces.interface["et2"].state.mtu(1500)

        iright.interfaces.interface.new_element("et1")
        iright.interfaces.interface["et1"].config.description("Interface exists in both")
        iright.interfaces.interface["et1"].config.mtu(9000)
        iright.interfaces.interface["et1"].state.mtu(9000)
        iright.interfaces.interface.new_element("et3")
        iright.interfaces.interface["et3"].config.description("Interface exists only in iright")
        iright.interfaces.interface["et3"].config.mtu(9000)
        iright.interfaces.interface["et3"].state.mtu(9000)

        assert ileft.diff(iright) == json.loads(diff_1)

    def test_compare_same_object(self):
        ileft = oc_if.Interfaces()
        iright = oc_if.Interfaces()

        ileft.interfaces.interface.get_element("et1")
        ileft.interfaces.interface["et1"].config.description("asdasda")
        ileft.interfaces.interface["et1"].config.mtu(1500)
        ileft.interfaces.interface["et1"].state.mtu(1500)
        iright.interfaces.interface.get_element("et1")
        iright.interfaces.interface["et1"].config.description("asdasda")
        iright.interfaces.interface["et1"].config.mtu(1500)
        iright.interfaces.interface["et1"].state.mtu(1500)

        assert ileft == iright

    def test_compare_different_objects(self):
        ileft = oc_if.Interfaces()
        iright = oc_if.Interfaces()

        ileft.interfaces.interface.new_element("et1")
        ileft.interfaces.interface["et1"].config.description("Interface exists in both")
        ileft.interfaces.interface["et1"].config.mtu(1500)
        ileft.interfaces.interface["et1"].state.mtu(1500)
        ileft.interfaces.interface.new_element("et2")
        ileft.interfaces.interface["et2"].config.description("Interface exists only in ileft")
        ileft.interfaces.interface["et2"].config.mtu(1500)
        ileft.interfaces.interface["et2"].state.mtu(1500)

        iright.interfaces.interface.new_element("et1")
        iright.interfaces.interface["et1"].config.description("Interface exists in both")
        iright.interfaces.interface["et1"].config.mtu(9000)
        iright.interfaces.interface["et1"].state.mtu(9000)
        iright.interfaces.interface.new_element("et3")
        iright.interfaces.interface["et3"].config.description("Interface exists only in iright")
        iright.interfaces.interface["et3"].config.mtu(9000)
        iright.interfaces.interface["et3"].state.mtu(9000)

        assert ileft != iright
