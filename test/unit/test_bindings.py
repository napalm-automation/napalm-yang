from napalm_yang import yang_base
from napalm_yang import yang_types
from napalm_yang import bindings


class Top(yang_base.BaseBinding):
    """Top class for testing."""
    config = False
    container = {'child': 'Child', }
    leaf = {
        'out-octets': {
            'type': {
                'options': {},
                'value': 'yang:counter32',
            }
        }
    }
    list_ = {}
    uses = []


class Child(yang_base.BaseBinding):
    """Top class for testing."""
    config = False
    container = {'child': 'Child', }
    leaf = {}
    list_ = {}
    uses = []


def test_bindings():
    """Test that containers are attached."""
    bindings.attach_childs(Top, globals())
    assert isinstance(Top.child, Child)
    assert isinstance(Top.out_octets, yang_types.counter32)
