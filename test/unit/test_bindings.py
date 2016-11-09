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
    uses = [u'something']


class Child(yang_base.BaseBinding):
    """Top class for testing."""
    config = False
    container = {}
    leaf = {}
    list = {}
    uses = []


groupings = {
    'something': {
        'config': False,
        'container': {'uses_test': 'Child', },
        'leaf': {
            'uses-var': {
                'type': {
                    'options': {},
                    'value': 'yang:counter64',
                }
            },
        },
        'list': {'uses_child_list': 'Child'},
        'uses': []
    }
}


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

    assert isinstance(Top.uses_test, Child)
    assert isinstance(Top.uses_var, yang_types.counter64)
    assert isinstance(Top.uses_child_list, yang_types.yang_list)
    assert Child == Top.uses_child_list.type
    assert not Top.uses_child_list
    Top.uses_child_list['a'] = Child()
    Top.uses_child_list['b'] = Child()
    assert Top.uses_child_list
