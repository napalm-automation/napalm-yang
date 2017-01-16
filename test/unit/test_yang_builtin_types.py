"""Tests for yang types."""
from napalm_yang import yang_builtin_types
import pytest

from decimal import Decimal


integer_tests = [
    # Type, range of values to test, are they valid?
    (yang_builtin_types.Int8, [-128, -100, 0, 100, 127, 052, 0xf], True),
    (yang_builtin_types.Int8, [-129, 128, True, False, None, "asd"], False),
    (yang_builtin_types.Int16, [-32768, -100, 0, 100, 32767, 052, 0xff], True),
    (yang_builtin_types.Int16, [-32769, 32768, True, False, None, "asd"], False),
    (yang_builtin_types.Int32, [-2147483648, -100, 0, 100, 2147483647, 052, 0xff], True),
    (yang_builtin_types.Int32, [-2147483649, 2147483648, True, False, None, "asd"], False),
    (yang_builtin_types.Int64, [-9223372036854775808, -100, 0, 100, 9223372036854775807, 052,
                                0xff], True),
    (yang_builtin_types.Int64, [-9223372036854775809, 9223372036854775808,
                                True, False, None, "asd"], False),
    (yang_builtin_types.Uint8, [0, 100, 255, 052, 0xff], True),
    (yang_builtin_types.Uint8, [-1, 256, True, False, None, "asd"], False),
    (yang_builtin_types.Uint16, [0, 100, 65535, 052, 0xff], True),
    (yang_builtin_types.Uint16, [-1, 65536, True, False, None, "asd"], False),
    (yang_builtin_types.Uint32, [0, 100, 4294967295, 052, 0xff], True),
    (yang_builtin_types.Uint32, [-1, 4294967296, True, False, None, "asd"], False),
    (yang_builtin_types.Uint64, [0, 100, 18446744073709551615, 052, 0xff], True),
    (yang_builtin_types.Uint64, [-1, 18446744073709551616, True, False, None, "asd"], False),
]

integer_range_tests = [
    # range, values to test, are they valid?
    ("10..20", [10, 15, 20, 020, 0xf], True),
    ("10..20", [-129, 128, 9, 21, 25, True, False, None, "asd"], False),
    ("10..20|30|40..50", [10, 15, 20, 30, 45, 020, 0xf], True),
    ("10..20|30|40..50", [-129, 128, 9, 21, 25, True, False, None, "asd"], False),
    ("min..20", [-128, 15, 20, 020, 0xf], True),
    ("min..20", [-129, 128, 21, 25, True, False, None, "asd"], False),
    ("10..max", [10, 15, 20, 020, 0xf, 127], True),
    ("10..max", [-129, 128, 9, 128, True, False, None, "asd"], False),
    ("min..max", [-128, -100, 0, 100, 127, 052, 0xf], True),
    ("min..max", [-129, 128, True, False, None, "asd"], False),
]


decimal64_tests = [
    # fraction_digits, range, values to test, are they valid?
    (1, None, ['-922337203685477580.8', '922337203685477580.7', -1, -1.2, 0, 20], True),
    (1, None, ['-922337203685477580.9', '922337203685477580.8'], False),
    (18, None, ['-9.223372036854775808', '9.223372036854775807', -1, -1.2, 0, 9], True),
    (18, None, ['-9.223372036854775809', '9.223372036854775808', -10, -9.3, 21, 25], False),
    (18, "-1.5..1.5|1.1", ['-1.49999999', '1.4999999', -1, -1.2, 0, 1.1], True),
    (18, "-1.5..1.5|10.5", ['-1.500001', '1.500001', -10, -9.3, 21, 25], False),
]

dotted_regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])"  # noqa
string_tests = [
    # length, pattern, values to test, are they valid?
    (None, None, ["", "asd", u"asdasd"], True),
    (None, None, [0, False, True, None], False),
    ("0|10..20", None, ["", "0123456789", "01234567890", "01234567890123456789"], True),
    ("0|10..20", None, [True, "012345678", "012345678901234567890"], False),
    (None, dotted_regex, ["1.2.3.4", "10.20.123.248"], True),
    (None, dotted_regex, ["1.2.3", "1.10.20.123.248", "", False, 1, None], False),
    ("1..5", "[a-z]+", ["word"], True),
    ("1..5", "[a-z]+", ["Word", "longword", "two words", "1word"], False),
]


boolean_tests = [
    # values to test, are they valid?
    ([True, False, "true", "false"], True),
    (["True", "False", "asd", 0, 1, None], False),
]


def obj_value_test(yang_obj, value, is_valid):
    failed = False
    try:
        yang_obj(value)
    except ValueError:
        failed = True

    if is_valid:
        assert not failed, "{} is a valid value for type {}".format(value, yang_obj.__class__)
    else:
        assert failed, "{} isn't a valid value for type {}".format(value, yang_obj.__class__)


class TestYangBuiltinTypes:
    """Wrap tests and fixture."""

    @pytest.mark.parametrize("yang_type, values, is_valid", integer_tests)
    def test_integer_values(self, yang_type, values, is_valid):
        """Test that each type accepts correct values."""
        for value in values:
            yang_obj = yang_type()
            obj_value_test(yang_obj, value, is_valid)

    @pytest.mark.parametrize("range_, values, is_valid", integer_range_tests)
    def test_integer_range(self, range_, values, is_valid):
        """Test that each type accepts correct values when a range is passed."""
        for value in values:
            yang_obj = yang_builtin_types.Int8(range_=range_)
            obj_value_test(yang_obj, value, is_valid)

    @pytest.mark.parametrize("fraction_digits, range_, values, is_valid", decimal64_tests)
    def test_decimal64(self, fraction_digits, range_, values, is_valid):
        """Test that each type accepts correct values when a range is passed."""
        for value in values:
            value = Decimal(value)
            yang_obj = yang_builtin_types.Decimal64(fraction_digits=fraction_digits, range_=range_)
            obj_value_test(yang_obj, value, is_valid)

    @pytest.mark.parametrize("length, pattern, values, is_valid", string_tests)
    def test_string(self, length, pattern, values, is_valid):
        """Test that each type accepts correct values when a range is passed."""
        for value in values:
            yang_obj = yang_builtin_types.String(length=length, pattern=pattern)
            obj_value_test(yang_obj, value, is_valid)

    @pytest.mark.parametrize("values, is_valid", boolean_tests)
    def test_boolean(self, values, is_valid):
        """Test that each type accepts correct values when a range is passed."""
        for value in values:
            yang_obj = yang_builtin_types.Boolean()
            obj_value_test(yang_obj, value, is_valid)
