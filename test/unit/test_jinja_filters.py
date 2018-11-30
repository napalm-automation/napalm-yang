"""
Test Jinja filters
"""

# Python3 support
from __future__ import print_function
from __future__ import unicode_literals

# Python std lib
import unittest

# third party libs
try:
    from netaddr.core import AddrFormatError

    HAS_NETADDR = True
except ImportError:
    HAS_NETADDR = False

from napalm_yang.jinja_filters import ip_filters, load_filters, vlan_filters


class TestJinjaFilters(unittest.TestCase):
    def test_netmask_to_cidr(self):
        """
        Tests Jinja2 filter ```netmask_to_cidr```:

            * check if load_filters returns the correct function
            * check if returns empty string on None
            * check if raises AddrFormatError on invalid mask
            * check if prefix length is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(load_filters()["netmask_to_cidr"], ip_filters.netmask_to_cidr)

        self.assertRaises(AddrFormatError, ip_filters.netmask_to_cidr, "bad")

        self.assertEqual(ip_filters.netmask_to_cidr(None), "")
        self.assertEqual(ip_filters.netmask_to_cidr("255.255.255.0"), 24)
        self.assertEqual(ip_filters.netmask_to_cidr("255.255.255.255"), 32)

    def test_cidr_to_netmask(self):
        """
        Tests Jinja2 filter ```cidr_to_netmask```:

            * check if load_filters returns the correct function
            * check if returns empty string on None
            * check if raises AddrFormatError on invalid prefix length
            * check if network mask is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(load_filters()["cidr_to_netmask"], ip_filters.cidr_to_netmask)

        self.assertRaises(AddrFormatError, ip_filters.cidr_to_netmask, "bad")

        self.assertEqual(ip_filters.cidr_to_netmask(None), "")
        self.assertEqual(ip_filters.cidr_to_netmask(24), "255.255.255.0")
        self.assertEqual(ip_filters.cidr_to_netmask("24"), "255.255.255.0")
        self.assertEqual(ip_filters.cidr_to_netmask(32), "255.255.255.255")

    def test_normalize_prefix(self):
        """
        Tests Jinja2 filter ```normalize_prefix```:

            * check if load_filters returns the correct function
            * check if returns empty string on None
            * check if raises AddrFormatError on invalid prefix
            * check if IPv4 and IPv6 prefix format is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(
            load_filters()["normalize_prefix"], ip_filters.normalize_prefix
        )

        self.assertRaises(AddrFormatError, ip_filters.normalize_prefix, "bad")

        self.assertEqual(ip_filters.normalize_prefix(None), "")
        self.assertEqual(ip_filters.normalize_prefix("192.168.0.1"), "192.168.0.1/32")
        self.assertEqual(
            ip_filters.normalize_prefix("192.168.0.55 255.255.255.0"), "192.168.0.55/24"
        )
        self.assertEqual(
            ip_filters.normalize_prefix("192.168.0.55/255.255.255.0"), "192.168.0.55/24"
        )
        self.assertEqual(
            ip_filters.normalize_prefix("2001:0DB8:0:0000:1:0:0:1/64"),
            "2001:db8::1:0:0:1/64",
        )

    def test_normalize_address(self):
        """
        Tests Jinja2 filter ```normalize_address```:

            * check if load_filters returns the correct function
            * check if returns empty string on None
            * check if raises AddrFormatError on invalid address
            * check if IPv4 and IPv6 address format is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(
            load_filters()["normalize_address"], ip_filters.normalize_address
        )

        self.assertRaises(AddrFormatError, ip_filters.normalize_address, "bad")

        self.assertEqual(ip_filters.normalize_address(None), "")
        self.assertEqual(ip_filters.normalize_address("192.168.0.1"), "192.168.0.1")
        self.assertEqual(ip_filters.normalize_address("192.168.1"), "192.168.0.1")
        self.assertEqual(
            ip_filters.normalize_address("2001:0DB8:0:0000:1:0:0:1"),
            "2001:db8::1:0:0:1",
        )

    def test_prefix_to_addrmask(self):
        """
        Tests Jinja2 filter ```prefix_to_addrmask```:

            * check if load_filters returns the correct function
            * check if returns empty string on None
            * check if raises AddrFormatError on invalid prefix
            * check if IPv4 address and netmask format is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(
            load_filters()["prefix_to_addrmask"], ip_filters.prefix_to_addrmask
        )

        self.assertRaises(AddrFormatError, ip_filters.prefix_to_addrmask, "bad")

        self.assertEqual(ip_filters.prefix_to_addrmask(None), "")
        self.assertEqual(
            ip_filters.prefix_to_addrmask("192.168.0.1/24"), "192.168.0.1 255.255.255.0"
        )
        self.assertEqual(
            ip_filters.prefix_to_addrmask("192.168.0.0/32", "/"),
            "192.168.0.0/255.255.255.255",
        )

    def test_vlan_range_to_openconfig(self):
        self.assertEqual(
            vlan_filters.vlan_range_to_oc("1, 2, 4-10"), ["1", " 2", " 4..10"]
        )
        self.assertEqual(
            vlan_filters.vlan_range_to_oc("1, 2, 4-10, 100-200"),
            ["1", " 2", " 4..10", " 100..200"],
        )

    def test_openconfig_to_vlan_range(self):
        self.assertEqual(vlan_filters.oc_to_vlan_range([1, 2, "4..10"]), "1,2,4-10")
        self.assertEqual(
            vlan_filters.oc_to_vlan_range([1, "2", "4..10", "100..200"]),
            "1,2,4-10,100-200",
        )
