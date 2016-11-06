from napalm_yang import yang_base


class Top(yang_base.BaseBinding):
    """Top class for testing."""
    config = False
    container = {'child': 'Child', }
    leaf = {
      'name': {
          'type': 'leafref',
          'description': 'References the configured name of the interface',
         },
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


def test_container():
    """Test that containers are attached."""
    yang_base.attach_childs(Top, globals())
    assert isinstance(Top.child, Child)
