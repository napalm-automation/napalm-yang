"""Tests for yang types."""
from napalm_yang import yang_types
import pytest


test_types = [
    (yang_types.Boolean, True, True),
    (yang_types.Boolean, False, True),
    (yang_types.Boolean, 1, False),
    (yang_types.Boolean, 'asdasd', False),
    (yang_types.Boolean, None, False),
    (yang_types.Uint32, 'asda', False),
    (yang_types.Uint32, True, False),
    (yang_types.Uint32, None, False),
    (yang_types.Uint32, -1, False),
    (yang_types.Uint32, 4294967296, False),
    (yang_types.Uint32, 0, True),
    (yang_types.Uint32, 4294967295, True),
    (yang_types.Uint32, 7, True),
    (yang_types.Uint64, 'asda', False),
    (yang_types.Uint64, True, False),
    (yang_types.Uint64, None, False),
    (yang_types.Uint64, -1, False),
    (yang_types.Uint64, 18446744073709551616, False),
    (yang_types.Uint64, 18446744073709551615, True),
    (yang_types.Uint64, 4294967296, True),
    (yang_types.Uint64, 0, True),
    (yang_types.Uint64, 4294967295, True),
    (yang_types.Uint64, 7, True),
    (yang_types.String, 'asd', True),
    (yang_types.String, u'asd', True),
    (yang_types.String, None, False),
    (yang_types.String, 1, False),
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
            e = yang_types.Enumeration(options=enumeration)
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
            yl = yang_types.yang_list(list_type, data)
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
        yl = yang_types.yang_list(int, {})
        yl['a'] = 1
        yl['b'] = 2
        assert yl['a'] == 1
        assert yl['b'] == 2

    def test_add_wrong_elements(self):
        """Test adding correct elements to a yang_list."""
        yl = yang_types.yang_list(int, {})
        with pytest.raises(AttributeError):
            yl['a'] = 1.0

    def test_normal_dict_like_methods(self):
        """Test it actually behaves like a dict."""
        d = {'a': 1, 'b': 2}
        yl = yang_types.yang_list(int, d)

        assert d.values() == yl.values()
        assert d.keys() == yl.keys()
        assert d == {k: v for k, v in yl.items()}
        assert len(yl)
