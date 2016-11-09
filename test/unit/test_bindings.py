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
    list = {'child_list': 'Child'}
    uses = []


class Child(yang_base.BaseBinding):
    """Top class for testing."""
    config = False
    container = {'child': 'Child', }
    leaf = {}
    list = {}
    uses = []


def test_bindings():
    """Test that containers are attached."""
    bindings.attach_childs(Top, globals())
    assert isinstance(Top.child, Child)
    assert isinstance(Top.out_octets, yang_types.counter32)
    assert isinstance(Top.child_list, yang_types.yang_list)
    assert Child == Top.child_list.type
    assert not Top.child_list
    Top.child_list['a'] = Child()
    Top.child_list['b'] = Child()
    assert Top.child_list
