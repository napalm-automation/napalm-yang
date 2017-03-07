"""Some functions utils to normalize text."""
import re
import jinja2

regexp = '[^a-zA-Z0-9_]'


def template(string, **kwargs):
    template = jinja2.Environment().from_string(string)
    return template.render(**kwargs)


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
    RESERVED_KEYWORDS = ("if", "range", "type", )

    if value in RESERVED_KEYWORDS:
        value = "{}_".format(value)
    return re.sub(regexp, '_', value)


def translate_string(string, **kwargs):
    if string:
        return string.format(**kwargs)
    else:
        return ""
