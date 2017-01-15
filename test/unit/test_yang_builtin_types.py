"""Tests for yang types."""
from napalm_yang import yang_builtin_types
import pytest


integer_tests = [
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
    ("10..20", [10, 15, 20, 020, 0xf], True),
    ("10..20", [-129, 128, 9, 21, 25, True, False, None, "asd"], False),
    ("min..20", [-128, 15, 20, 020, 0xf], True),
    ("min..20", [-129, 128, 21, 25, True, False, None, "asd"], False),
    ("10..max", [10, 15, 20, 020, 0xf, 127], True),
    ("10..max", [-129, 128, 9, 128, True, False, None, "asd"], False),
    ("min..max", [-128, -100, 0, 100, 127, 052, 0xf], True),
    ("min..max", [-129, 128, True, False, None, "asd"], False),
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


test_types = [
    (yang_builtin_types.Boolean, True, True),
    (yang_builtin_types.Boolean, False, True),
    (yang_builtin_types.Boolean, 1, False),
    (yang_builtin_types.Boolean, 'asdasd', False),
    (yang_builtin_types.Boolean, None, False),
    (yang_builtin_types.String, 'asd', True),
    (yang_builtin_types.String, u'asd', True),
    (yang_builtin_types.String, None, False),
    (yang_builtin_types.String, 1, False),
]


enumeration_with_values = {
                           'UP': {
                               'value': {
                                   'value': '1',
                                  },
                              },
                           'DOWN': {
                               'value': {
                                   'value': '2',
                                  },
                              },
                           }

enumeration_without_values = {
                                'UP': {},
                                'DOWN': {},
                               }

test_enumeration = [
    (enumeration_with_values, 'UP', 1, True),
    (enumeration_with_values, 'asdasd', None, False),
    (enumeration_without_values, 'UP', None, True),
    (enumeration_without_values, 'asdasd', None, False),
]


@pytest.mark.skip
class TestYangTypes:
    """Wrap tests and fixtures."""

    @pytest.mark.parametrize("yang_type, value, is_valid", test_types)
    def test_type_values_no_options(self, yang_type, value, is_valid):
        """Test that each type accepts correct values."""
        try:
            test = yang_type()
            test.value = value
        except ValueError:
            if is_valid:
                assert False, "{} wasn't a valid value for type {}".format(value, yang_type)
            else:
                assert True, "{} was a valid value for type {}".format(value, yang_type)

    @pytest.mark.skip
    @pytest.mark.parametrize("enumeration, description, value, is_valid", test_enumeration)
    def test_enumeration(self, enumeration, description, value, is_valid):
        """Test that each type accepts correct values."""
        try:
            e = yang_builtin_types.Enumeration(options=enumeration)
            e.enum = description
            assert e.value == value
        except ValueError:
            if is_valid:
                assert False, "{} wasn't a valid value for boolean".format(value)
            else:
                assert True, "{} was a valid value for boolean".format(value)


yang_lists_init = [
    (int, {}, True),
    (int, {'a': 1}, True),
    (int, {'a': 1, 'b': 2}, True),
    (int, {'a': "1"}, False),
    (int, {'a': 1, 'b': "2"}, False),
    (int, {'a': 1, 'b': None}, False),
]


@pytest.mark.skip
class TestYangList:
    """Wrap tests and fixtures."""

    @pytest.mark.parametrize("list_type, data, is_valid", yang_lists_init)
    def test_initialization(self, list_type, data, is_valid):
        """Test the initialization process of a yang_list"""
        try:
            yl = yang_builtin_types.yang_list(list_type, data)
            assert yl.type == list_type
            assert yl.value == data
            assert all([isinstance(x, list_type) for x in yl.value.values()])
        except AttributeError:
            if is_valid:
                assert False, "An element of {} wasn't of the correct type".format(data)
            else:
                assert True

    def test_add_correct_elements(self):
        """Test adding correct elements to a yang_list."""
        yl = yang_builtin_types.yang_list(int, {})
        yl['a'] = 1
        yl['b'] = 2
        assert yl['a'] == 1
        assert yl['b'] == 2

    def test_add_wrong_elements(self):
        """Test adding correct elements to a yang_list."""
        yl = yang_builtin_types.yang_list(int, {})
        with pytest.raises(AttributeError):
            yl['a'] = 1.0

    def test_normal_dict_like_methods(self):
        """Test it actually behaves like a dict."""
        d = {'a': 1, 'b': 2}
        yl = yang_builtin_types.yang_list(int, d)

        assert d.values() == yl.values()
        assert d.keys() == yl.keys()
        assert d == {k: v for k, v in yl.items()}
        assert len(yl)
