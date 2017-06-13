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

from napalm_yang.jinja_filters import ip_filters, load_filters


class TestJinjaFilters(unittest.TestCase):
    def test_normalize_prefix(self):
        """
        Tests Jinja2 filter ```normalize_prefix```:

            * check if load_filters returns the correct function
            * check if raises AddrFormatError on invalid prefix
            * check if IPv4 and IPv6 prefix format is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(load_filters()['normalize_prefix'], ip_filters.normalize_prefix)

        self.assertRaises(AddrFormatError, ip_filters.normalize_prefix, 'bad')

        self.assertEqual(ip_filters.normalize_prefix('192.168.0.1'), '192.168.0.1/32')
        self.assertEqual(ip_filters.normalize_prefix('192.168.0.55 255.255.255.0'), '192.168.0.55/24')
        self.assertEqual(ip_filters.normalize_prefix('192.168.0.55/255.255.255.0'), '192.168.0.55/24')
        self.assertEqual(ip_filters.normalize_prefix('2001:0DB8:0:0000:1:0:0:1/64'), '2001:db8::1:0:0:1/64')

    def test_normalize_address(self):
        """
        Tests Jinja2 filter ```normalize_address```:

            * check if load_filters returns the correct function
            * check if raises AddrFormatError on invalid address
            * check if IPv4 and IPv6 address format is returned as expected
        """

        self.assertTrue(HAS_NETADDR)

        self.assertEqual(load_filters()['normalize_address'], ip_filters.normalize_address)

        self.assertRaises(AddrFormatError, ip_filters.normalize_address, 'bad')

        self.assertEqual(ip_filters.normalize_address('192.168.0.1'), '192.168.0.1')
        self.assertEqual(ip_filters.normalize_address('192.168.1'), '192.168.0.1')
        self.assertEqual(ip_filters.normalize_address('2001:0DB8:0:0000:1:0:0:1'), '2001:db8::1:0:0:1')
