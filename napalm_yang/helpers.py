import yaml
import os
import sys
import jinja2

from napalm_yang import jinja_filters

import logging
logger = logging.getLogger("napalm-yang")


def yaml_include(loader, node):
    # Get the path out of the yaml file
    file_name = os.path.join(os.path.dirname(loader.name), node.value)

    with file(file_name) as inputfile:
        return yaml.load(inputfile)


yaml.add_constructor("!include", yaml_include)


def config_logging(level=logging.DEBUG, stream=sys.stdout):
    logger.setLevel(level)
    ch = logging.StreamHandler(stream)
    formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)


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
        return yaml.load(f)


def _resolve_rule(rule, **kwargs):
    if isinstance(rule, dict):
        return {k: _resolve_rule(v, **kwargs) for k, v in rule.items()}
    elif isinstance(rule, list):
        return [_resolve_rule(e, **kwargs) for e in rule]
    elif isinstance(rule, str):
        return template(rule, **kwargs)
    else:
        return rule


def resolve_rule(rule, attribute, keys, extra_vars=None, translation_model=None,
                 parse_bookmarks=None, replacing=False, merging=False, negating=False,
                 process_all=True):
    if isinstance(rule, list):
        return [resolve_rule(r, attribute, keys, extra_vars, translation_model, parse_bookmarks,
                             replacing, merging, negating, process_all) for r in rule]
    elif isinstance(rule, str):
        if rule in ["unnecessary"]:
            return [{"mode": "skip", "reason": rule}]
        elif rule in ["not_implemented", "not_supported"]:
            return [{"mode": "gate", "reason": rule}]
        else:
            raise Exception("Not sure what to do with rule {} on attribute {}".format(rule,
                                                                                      attribute))
    kwargs = dict(keys)
    rule = dict(rule)
    kwargs["model"] = translation_model
    kwargs["bookmarks"] = parse_bookmarks
    kwargs["attribute"] = attribute
    kwargs["extra_vars"] = extra_vars
    kwargs["replacing"] = replacing
    kwargs["merging"] = merging
    kwargs["negating"] = negating

    for k, v in rule.items():
        if k in ["key", "value"] and not process_all:
            # don't process keys or values as we will do it at "processing time"
            # instead of ahead of time
            rule[k] = v
        else:
            rule[k] = _resolve_rule(v, **kwargs)

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
                            extensions=['jinja2.ext.do'],
                            keep_trailing_newline=True,
                            )
    env.filters.update(jinja_filters.load_filters())

    template = env.from_string(string)

    return template.render(**kwargs)
