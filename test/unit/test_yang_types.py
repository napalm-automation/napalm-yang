"""Tests for yang types."""
from napalm_yang import yang_types
import pytest


test_types = [
    (yang_types.boolean, True, True),
    (yang_types.boolean, False, True),
    (yang_types.boolean, 1, False),
    (yang_types.boolean, 'asdasd', False),
    (yang_types.boolean, None, False),
    (yang_types.counter32, 'asda', False),
    (yang_types.counter32, True, False),
    (yang_types.counter32, None, False),
    (yang_types.counter32, -1, False),
    (yang_types.counter32, 4294967296, False),
    (yang_types.counter32, 0, True),
    (yang_types.counter32, 4294967295, True),
    (yang_types.counter32, 7, True),
    (yang_types.counter64, 'asda', False),
    (yang_types.counter64, True, False),
    (yang_types.counter64, None, False),
    (yang_types.counter64, -1, False),
    (yang_types.counter64, 18446744073709551616, False),
    (yang_types.counter64, 18446744073709551615, True),
    (yang_types.counter64, 4294967296, True),
    (yang_types.counter64, 0, True),
    (yang_types.counter64, 4294967295, True),
    (yang_types.counter64, 7, True),
]

enumeration = {
    'a': 1,
    'b': 2,
    'c': 3,
}

test_enumeration = [
    (enumeration, 'a', 1, True),
    (enumeration, 'b', 2, True),
    (enumeration, 'd', None, False),
]


class TestYangTypes:
    """Wrap tests and fixtures."""

    @pytest.mark.parametrize("yang_type, value, is_valid", test_types)
    def test_type_values_no_options(self, yang_type, value, is_valid):
        """Test that each type accepts correct values."""
        try:
            yang_type(value)
        except ValueError:
            if is_valid:
                assert False, "{} wasn't a valid value for type {}".format(value, yang_type)
            else:
                assert True, "{} was a valid value for type {}".format(value, yang_type)

    @pytest.mark.parametrize("enumeration, description, value, is_valid", test_enumeration)
    def test_enumeration(self, enumeration, description, value, is_valid):
        """Test that each type accepts correct values."""
        try:
            e = yang_types.enumeration(description, options={'enum': enumeration})
            assert e.value == value
        except ValueError:
            if is_valid:
                assert False, "{} wasn't a valid value for boolean".format(value)
            else:
                assert True, "{} was a valid value for boolean".format(value)
