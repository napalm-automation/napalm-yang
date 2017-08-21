from napalm_yang.jinja_filters import ip_filters
from napalm_yang.jinja_filters import json_filters
from napalm_yang.jinja_filters import vlan_filters


JINJA_FILTERS = [
    ip_filters,
    json_filters,
    vlan_filters,
]


def load_filters():
    """
    Loads and returns all filters.
    """
    all_filters = {}
    for m in JINJA_FILTERS:
        if hasattr(m, 'filters'):
            all_filters.update(m.filters())
    return all_filters
