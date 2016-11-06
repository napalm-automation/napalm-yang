"""Useful jinja2 filters"""
import json

from utils import text_helpers


class FilterModule(object):
    """Useful jinja2 filters"""

    def filters(self):
        """Return jinja2 filters that this module provide."""
        return {
            'indent': indent,
            'safe_attr_name': text_helpers.safe_attr_name,
            'safe_class_name': text_helpers.safe_class_name,
            'to_json': to_json,
            'to_dict': to_dict,
            'to_string': to_string,
            'raise_error': raise_error,
        }


def raise_error(value, args=None):
    raise Exception("{}\n{}".format(value, to_dict(args)))


def indent(value, indentation=4):
    """Indent text."""
    return '\n'.join(["{}{}".format(" " * indentation, t) for t in value.splitlines()])


def to_json(value):
    """Dump pretty json"""
    return json.dumps(value, sort_keys=True, indent=4)


def to_string(value):
    return '"""{}"""'.format(value) if len(value.splitlines()) > 1 else "'{}'".format(value)


def to_dict(value, level=0):
    """Returns a dict object."""
    if isinstance(value, dict) and value:
        representation = "{\n"
        for k, v in value.items():
            representation += "{}'{}': {},\n".format(" " * (4*level+2), k, to_dict(v, level+1))
        representation += "{}}}".format(" " * (4*level+1))
        return representation
    elif isinstance(value, dict) and not value:
        return "{}"
    elif isinstance(value, basestring):
        return to_string(value)
    else:
        return value
