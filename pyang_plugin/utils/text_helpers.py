"""Some functions utils to normalize text."""


def safe_class_name(value):
    """Return a safe class name. For example, from interface-state to InterfaceState"""
    value = value.replace(":", "_")
    return ''.join([t.title() for t in value.split('-')])


def safe_attr_name(value):
    """Return a safe attr name. For example, from in-octets to in_octets"""
    reserved_keywords = []
    value = value.replace(":", "_")
    if value in reserved_keywords:
        value = "{}_".format(value)
    return '_'.join([t for t in value.split('-')])
