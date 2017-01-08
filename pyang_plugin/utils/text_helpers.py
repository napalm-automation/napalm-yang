"""Some functions utils to normalize text."""
import re

regexp = '[^a-zA-Z0-9_]'


def safe_class_name(value):
    """Return a safe class name. For example, from interface-state to InterfaceState"""
    if ":" in value:
        module, cls = value.split(":")
        module = safe_attr_name(module)
        cls = ''.join([t.title() for t in cls.split('-')])
        cls = re.sub(regexp, '', cls)
        return "{}.{}".format(module, cls)
    else:
        value = ''.join([t.title() for t in value.split('-')])
        return re.sub(regexp, '', value)


def safe_attr_name(value):
    """Return a safe attr name. For example, from in-octets to in_octets"""
    return re.sub(regexp, '_', value)
