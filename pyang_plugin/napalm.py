"""NAPALM output plugin."""

import logging
import optparse
import os
import sys

from pyang import plugin

from collections import defaultdict

from helpers import jinja_filters
import jinja2

from utils import text_helpers


def configure_logging(logger, debug):
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def pyang_plugin_init():
    """Register pyang plugin."""
    plugin.register_plugin(NapalmPlugin())


class NapalmPlugin(plugin.PyangPlugin):
    """NAPALM plugin for pyang."""

    def add_output_format(self, fmts):
        """Add napalm format to pyang."""
        self.multiple_modules = True
        fmts['napalm'] = self

    def add_opts(self, optparser):
        """Add options to cli."""
        optlist = [
            optparse.make_option("--napalm-help",
                                 dest="napalm_help",
                                 action="store_true",
                                 help="Print extensive help for NAPALM plugin  and exit"),
            optparse.make_option("--napalm-path",
                                 dest="napalm_models_path",
                                 action="store",
                                 default="./napalm_yang/models",
                                 help="Where to store generated modules"),
        ]
        g = optparser.add_option_group("NAPALM output specific options")
        g.add_options(optlist)

    def setup_ctx(self, ctx):
        if ctx.opts.napalm_help:
            print_help()
            sys.exit(0)

        if not (os.path.isdir(ctx.opts.napalm_models_path)):
            print("{} is not a valid path".format(ctx.opts.napalm_models_path))
            sys.exit(-1)

    def setup_fmt(self, ctx):
        ctx.implicit_errors = False

    def emit(self, ctx, modules, fd):
        global logger
        logger = logging.getLogger("napalm_pyang_plugin")
        logger = configure_logging(logger, ctx.opts.verbose)
        emit_napalm(ctx, modules, fd)


def print_help():
    print("TDB")


def _nested_default_dict():
    return defaultdict(_nested_default_dict)


def save(result, path):
    filters = jinja_filters.FilterModule()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./pyang_plugin/templates/'),
                             undefined=jinja2.StrictUndefined)

    for n, f in filters.filters().items():
        env.filters[n] = f

    template = env.get_template('module.j2')

    for module, data in result.items():
        filename = "{}.py".format(text_helpers.safe_attr_name(module))
        logger.info("Saving module: {}".format(filename))
        print(template.render(module=data))


def inspect(obj, indent=0):
    print(jinja_filters.to_json(obj))


SIMPLE = ("base", "uses", "mandatory", "default", "config", "path", "key", "value", "units", )


def _parse_simple(sub, store):
    if sub.keyword == "uses":
        try:
            store[sub.keyword].append(sub.arg)
        except:
            store[sub.keyword] = [sub.arg]
    else:
        store[sub.keyword] = sub.arg


IDENTITY = ("identity", )


def _parse_identities(sub, store, root):
    _parse(sub.substmts, store[sub.arg], root)


INFO = ("yang-version", "namespace", "prefix", "organization", "contact", "reference",
        "description", (u'openconfig-extensions', u'openconfig-version'), "import", "revision", )


def _parse_info(sub, store):
    if sub.keyword in ("yang-version", "namespace", "prefix", "organization", "contact",
                       "description", ):
        store[sub.keyword] = sub.arg
    elif sub.keyword == (u'openconfig-extensions', u'openconfig-version'):
        store[sub.keyword[0]][sub.keyword[1]] = sub.arg
    elif sub.keyword in ("import", "revision", ):
        _parse_simple(sub, store[sub.keyword][sub.arg])


NESTED = ("grouping", "container", "leaf", "type", "list", "enum", "typedef", )


def _parse_nested(sub, store, root):
    if sub.keyword in ("container", "list", ):
        unique_name = "{}_{}".format(sub.parent.arg, sub.arg)
        root["order"].append((sub.keyword, unique_name))
        _parse(sub.substmts, root[sub.keyword][unique_name], root)
        try:
            store[sub.keyword].append((sub.arg, unique_name))
        except AttributeError:
            store[sub.keyword] = [(sub.arg, unique_name)]
    else:
        _parse(sub.substmts, store[sub.arg], root)


def _parse(substmts, store, root):
    while len(substmts):
        sub = substmts.pop()
        logger.debug("Parsing {} - {}, {}".format(sub.keyword, sub.arg[0:20], sub.pos))
        if sub.keyword in INFO:
            _parse_info(sub, store["info"])
        elif sub.keyword in IDENTITY:
            _parse_identities(sub, store[sub.keyword], root)
        elif sub.keyword in NESTED:
            _parse_nested(sub, store[sub.keyword], root)
        elif sub.keyword in SIMPLE:
            _parse_simple(sub, store)
        else:
            raise Exception("We are not parsing {}".format(sub.keyword))


def merge_two_dicts(x, y):
    """Given two dicts, merge them into a new dict as a shallow copy."""
    for k, v in y.items():
        if k == "info":
            continue
        if isinstance(v, dict) and k in x.keys():
            merge_two_dicts(x[k], v)
        elif isinstance(v, list) and k in x.keys():
            x[k].extend(v)
        else:
            x[k] = v


def _process_uses(statements, groupings, store):
    for name, obj in statements.items():
        while obj["uses"]:
            u = groupings[obj["uses"].pop()]
            merge_two_dicts(obj, u)
        store[name] = obj


def _process_uses_top(uses, groupings, store):
    while uses:
        u = groupings[uses.pop()]
        merge_two_dicts(store, u)


def _process(statements, store):
    grouping = statements.pop("grouping")
    store["info"] = statements.pop("info")
    store["identity"] = statements.pop("identity")
    store["order"] = statements.pop("order")
    _process_uses(statements.pop("container"), grouping, store["container"])
    _process_uses(statements.pop("list"), grouping, store["list"])
    _process_uses_top(statements.pop("uses"), grouping, store["top"])
    inspect(store["container"]["acl-top_acl"])
    raise Exception(store["container"]["acl-top_acl"])


def emit_napalm(ctx, modules, fd):
    """
    Args:
        ctx(pyang.Context): Options passed via the CLI.
        modules(list of pyang.statements.Statement): List of yang models being processed
        fd(file): File open to written to
    """
    parsed = defaultdict(_nested_default_dict)
    print(parsed)
    result = defaultdict(_nested_default_dict)
    for module in modules:
        logger.info("Parsing model {}".format(module.pos))
        parsed[module.arg]["order"] = []
        _parse(module.substmts, parsed[module.arg], parsed[module.arg])

    for module, statements in parsed.items():
        logger.info("Processing model {}".format(module))
        _process(statements, result[module])

    save(result, ctx.opts.napalm_models_path)
