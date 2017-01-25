"""NAPALM output plugin."""

import logging
import optparse
import os
import sys

from pyang import plugin
from pyang.statements import Statement

from collections import defaultdict

from helpers import jinja_filters
import jinja2

from utils import text_helpers

import pprint


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
            optparse.make_option("--napalm-module",
                                 dest="napalm_module",
                                 action="store",
                                 default="",
                                 help="Module name"),
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


def _create_package(package):
    if not os.path.exists(package):
        os.makedirs(package)
        open("{}/__init__.py".format(package), "w")


def save(result, path, module_name):
    filters = jinja_filters.FilterModule()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./pyang_plugin/templates/'),
                             undefined=jinja2.StrictUndefined)

    for n, f in filters.filters().items():
        env.filters[n] = f

    template = env.get_template('module.j2')

    for module, data in result.items():
        package = "{}/{}".format(path, module_name)
        _create_package(package)

        filename = "ietf_{}".format(data["info"]["prefix"]) if "ietf" in package else \
            data["info"]["prefix"]
        filename = "{}/{}.py".format(package,
                                     text_helpers.safe_attr_name(filename))
        logger.info("Saving module: {}".format(filename))

        with open(filename, "w") as f:
            f.write(template.render(module=data))


def inspect(obj):
    if isinstance(obj, Statement):
        pprint.pprint(obj.__dict__)
    else:
        print(jinja_filters.to_json(obj))


SIMPLE = ("base", "uses", "mandatory", "default", "config", "path", "key", "value", "units",
          "range", "pattern", "when", "length", "if-feature", "yin-element", "status", )


def _parse_simple(sub, store):
    if sub.keyword == "uses":
        try:
            store[sub.keyword].append(sub.arg)
        except:
            store[sub.keyword] = [sub.arg]
    else:
        store[sub.keyword] = sub.arg


def _parse_identities(sub, store, root):
    _parse(sub.substmts, store[sub.arg], root)


INFO = ("yang-version", "namespace", "prefix", "organization", "contact", "reference",
        "description", (u'openconfig-extensions', u'openconfig-version'), "revision", )


def _parse_info(sub, store):
    if sub.keyword in ("yang-version", "namespace", "prefix", "organization", "contact",
                       "description", ):
        store[sub.keyword] = sub.arg
    elif sub.keyword == (u'openconfig-extensions', u'openconfig-version'):
        store[sub.keyword[0]][sub.keyword[1]] = sub.arg
    elif sub.keyword in ("revision", ):
        _parse_simple(sub, store[sub.keyword][sub.arg])


NESTED = ("typedef", "grouping", "container", "leaf", "type", "list", "enum", "typedef", "import",
          "leaf-list", "feature", "extension", "argument", "identity", )


def _parse_nested(sub, store, root):
    if sub.keyword in ("container", "list"):
        pos = "{}".format(sub.pos).split(":")[-1]
        unique_name = "{}_{}_{}".format(sub.parent.arg, sub.arg, pos)
        root["order"].insert(0, (sub.keyword, unique_name))
        _parse(sub.substmts, root[sub.keyword][unique_name], root)
        try:
            store[sub.keyword].insert(0, (sub.arg, unique_name))
        except AttributeError:
            store[sub.keyword] = [(sub.arg, unique_name)]
    elif sub.keyword in ("typedef", "identity"):
        order_kw = "order_{}".format(sub.keyword)
        root[order_kw].insert(0, sub.arg)
        _parse(sub.substmts, root[sub.keyword][sub.arg], root)
    elif sub.keyword in ("grouping", ):
        root["order"].insert(0, (sub.keyword, sub.arg))
        _parse(sub.substmts, root[sub.keyword][sub.arg], root)
    else:
        _parse(sub.substmts, store[sub.arg], root)


def _parse(substmts, store, root):
    while len(substmts):
        sub = substmts.pop()
        logger.debug("Parsing {} - {}, {}".format(sub.keyword, sub.arg[0:20], sub.pos))
        if sub.keyword in INFO:
            _parse_info(sub, store["info"])
        elif sub.keyword in NESTED:
            _parse_nested(sub, store[sub.keyword], root)
        elif sub.keyword in SIMPLE:
            _parse_simple(sub, store)
        else:
            raise Exception("We are not parsing {}".format(sub.keyword))


def emit_napalm(ctx, modules, fd):
    """
    Args:
        ctx(pyang.Context): Options passed via the CLI.
        modules(list of pyang.statements.Statement): List of yang models being processed
        fd(file): File open to written to
    """
    parsed = defaultdict(_nested_default_dict)
    #  result = defaultdict(_nested_default_dict)
    for module in modules:
        logger.info("Parsing model {}".format(module.pos))
        parsed[module.arg]["order"] = []
        parsed[module.arg]["order_typedef"] = []
        parsed[module.arg]["order_identity"] = []
        _parse(module.substmts, parsed[module.arg], parsed[module.arg])

    """
    for module, statements in parsed.items():
        logger.info("Processing model {}".format(module))
        _process(statements, result[module])
    """
    save(parsed, ctx.opts.napalm_models_path, ctx.opts.napalm_module)
