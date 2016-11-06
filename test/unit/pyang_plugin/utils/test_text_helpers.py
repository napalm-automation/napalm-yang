"""Tests for jinja filters."""
import pytest

from pyang_plugin.utils import text_helpers


test_class_names = [
    ('asd', 'asd'),
    ('interface-counters-state_counters', 'InterfaceCountersState_Counters')
]


class TestTextHelpers:
    """Wrap tests and fixtures."""

    @pytest.mark.parametrize("orig, normalized", test_class_names)
    def test_safe_class_name(self, orig, normalized, is_valid):
        """Test class names are normalized properly."""
        assert text_helpers.safe_class_name(orig) == normalized
