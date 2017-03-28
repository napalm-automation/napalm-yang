import yaml

from napalm_yang.parsers.text import TextParser
from napalm_yang.parsers.xml import XMLParser

from napalm_yang.translators.text import TextTranslator
from napalm_yang.translators.xml import XMLTranslator

import os
import jinja2

from napalm_yang.jinja_filters import ip_filters

import logging
logger = logging.getLogger("napalm-yang")


def get_parser(parser):
    parsers = {
        "TextParser": TextParser,
        "XMLParser": XMLParser,
        "TextTranslator": TextTranslator,
        "XMLTranslator": XMLTranslator,
    }
    return parsers[parser]


def find_yang_file(profile, filename, path):
    """
    Find the necessary file for the given test case.

    Args:
        device(napalm device connection): for which device
        filename(str): file to find
        path(str): where to find it relative to where the module is installed
    """
    # Find base_dir of submodule
    module_dir = os.path.dirname(__file__)
    full_path = os.path.join(module_dir, 'mappings', profile, path, filename)

    if os.path.exists(full_path):
        return full_path
    else:
        msg = "Couldn't find parsing file: {}".format(full_path)
        logger.error(msg)
        raise IOError(msg)


def read_yang_map(yang_prefix, attribute, profile, parser_path):
    logger.info("Finding parser for {}:{}".format(yang_prefix, attribute))

    found = False
    for p in profile:
        filename = os.path.join(yang_prefix, "{}.yaml".format(attribute))

        try:
            filepath = find_yang_file(p, filename, parser_path)
            found = True
            logger.debug("Found on profile: {}, {}".format(p, filepath))
        except IOError:
            pass

    if not found:
        return

    with open(filepath, "r") as f:
        return yaml.load(f.read())


def resolve_rule(rule, attribute, keys, extra_vars=None, translation_model=None,
                 parse_bookmarks=None):
    if isinstance(rule, list):
        raise Exception("Wrong rule for attr: {}. List can be used only on leafs".format(attribute))
    elif isinstance(rule, str):
        if rule in ["unnecessary", "not_implemented"]:
            return {"mode": "skip", "reason": rule}
        else:
            raise Exception("Not sure what to do with rule {} on attribute {}".format(rule,
                                                                                      attribute))
    kwargs = dict(keys)
    rule = dict(rule)
    kwargs["model"] = translation_model
    kwargs["bookmarks"] = parse_bookmarks
    kwargs["attribute"] = attribute
    kwargs["extra_vars"] = extra_vars

    for k, v in rule.items():
        if isinstance(v, dict):
            resolve_rule(v, attribute, keys, extra_vars, translation_model, parse_bookmarks)
        elif isinstance(v, list):
            for e in k:
                resolve_rule(e, attribute, keys, extra_vars, translation_model, parse_bookmarks)
        elif isinstance(v, str):
            rule[k] = template(v, **kwargs)

    if "when" in rule.keys():
        w = rule["when"]
        try:
            import ast
            w = ast.literal_eval(w)
        except Exception:
            w = True if w in ["true", "True"] else False
        if not w:
            return {"mode": "skip", "reason": "criteria failed"}
        rule["when"] = bool(w)

    return rule


def template(string, **kwargs):
    env = jinja2.Environment(
                            undefined=jinja2.StrictUndefined,
                            keep_trailing_newline=True,
                            )
    env.filters.update(ip_filters.filters())

    template = env.from_string(string)

    return template.render(**kwargs)
