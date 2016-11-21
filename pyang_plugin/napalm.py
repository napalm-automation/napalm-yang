"""NAPALM output plugin."""

import logging
import optparse
import os
import re
import sys

import pprint
from utils import text_helpers

from pyang import plugin

from helpers import jinja_filters

import jinja2


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
        emit_napalm(ctx, modules, fd)


def print_help():
    print("TDB")


def _stupid_insepct(obj):
    text = "# {}\n".format(obj.__class__.__name__)
    for k, v in obj.__dict__.items():
        l = 30 - len(k)
        text += "{}{}{}\n".format(k, " " * l, v)
    text += "======================"
    return text


INFORMATIONAL_STATEMENTS = [
    'namespace',
    'organization',
    'contact',
    'description',
    'yang-version',
    'prefix',
    'config',
    'reference',
    'key',
]

SIMPLE_STATEMENTS = [
    'revision',
    'uses',
]

GROUPING_STATEMENTS = [
    'grouping',
    'typedef',
]

NESTED_STATEMENTS = [
    'container',
    'list',
]

TYPE_STATEMENTS = [
    'leaf',
    'type',
]


def safe(name):
    """Given a string, return a safe version."""
    name = re.sub('-', '_', name)
    return name


def error_stmt(stmt):
    raise Exception("Not sure about this type of statement: {}\n{}".format(
                                            stmt.keyword, _stupid_insepct(stmt)))


def parse_imports(substmts):
    result = []
    for stmt in substmts:
        if stmt.keyword == 'prefix':
            result.append(stmt.arg)
        else:
            error_stmt(stmt)
    return result


def parse_simple(substmts, safe_arg=False):
    result = {}

    for s in substmts:
        result[s.keyword] = {'value': text_helpers.safe_class_name(s.arg) if safe_arg else s.arg,
                             'options': {}, }
        for o in s.substmts:
            result[s.keyword]['options'][o.arg] = parse_simple(o.substmts)

    return result


def create_store(store_type):
    store_map = {}
    store_map['typedef'] = {'info': {}, 'type': {},
                            }
    store_map['grouping'] = {'info': {}, 'leaf': {}, 'uses': {}, 'list': {},
                             'container': {}, 'config': False,
                             }
    store_map['leaf'] = store_map['typedef']
    store_map['container'] = store_map['grouping']
    store_map['list'] = store_map['grouping']
    return store_map[store_type]


def main_parser(stmts, store, nsglobal):
    for substmt in stmts:
        logger.debug("Found statement: {}".format(substmt.keyword))
        if substmt.keyword in INFORMATIONAL_STATEMENTS:
            logger.debug("Parsing information_statements")
            store['info'][substmt.keyword] = substmt.arg
        elif substmt.keyword == 'import':
            logger.debug("Parsing import")
            store['imports'][substmt.arg] = parse_imports(substmt.substmts)
        elif 'openconfig-extensions' in substmt.keyword:
            logger.debug("Parsing openconfig-extensions")
            store['openconfig-extensions'][substmt.keyword[1]] = substmt.arg
        elif substmt.keyword in SIMPLE_STATEMENTS:
            logger.debug("Parsing simple block")
            store[substmt.keyword][substmt.arg] = parse_simple(
                substmt.substmts,
                safe_arg=substmt.keyword in ['uses', ])
        elif substmt.keyword in GROUPING_STATEMENTS:
            logger.debug("Parsing grouping block")
            store[substmt.keyword][substmt.arg] = create_store(substmt.keyword)
            main_parser(substmt.substmts, store[substmt.keyword][substmt.arg], nsglobal)
        elif substmt.keyword in NESTED_STATEMENTS:
            logger.debug("Parsing nested block")
            name = '{}_{}'.format(substmt.parent.arg, substmt.arg)
            nsglobal['discovered_classes'][name] = create_store(substmt.keyword)
            store[substmt.keyword][substmt.arg] = text_helpers.safe_class_name(name)
            main_parser(substmt.substmts, nsglobal['discovered_classes'][name], nsglobal)
        elif substmt.keyword in TYPE_STATEMENTS:
            logger.debug("Parsing type block")
            store[substmt.keyword][substmt.arg] = parse_simple(substmt.substmts, safe_arg=True)
        else:
            pprint.pprint(store)
            error_stmt(substmt)


def emit_napalm(ctx, modules, fd):
    """
    Args:
        ctx(pyang.Context): Options passed via the CLI.
        modules(list of pyang.statements.Statement): List of yang models being processed
        fd(file): File open to written to
    """
    filters = jinja_filters.FilterModule()
    env = jinja2.Environment(loader=jinja2.FileSystemLoader('./pyang_plugin/templates/'),
                             undefined=jinja2.StrictUndefined)

    for n, f in filters.filters().items():
        env.filters[n] = f

    template = env.get_template('module.j2')

    global logger
    logger = logging.getLogger("napalm_pyang_plugin")
    logger = configure_logging(logger, ctx.opts.verbose)

    for module in modules:
        logger.info("Processing model {}".format(module.pos))
        parsed_module = {'info': {}, 'containers': {}, 'typedef': {}, 'imports': {}, 'uses': {},
                         'openconfig-extensions': {}, 'grouping': {}, 'revision': {},
                         'discovered_classes': {},
                         }
        parsed_module['name'] = module.i_modulename
        main_parser(module.substmts, parsed_module, parsed_module)
        pprint.pprint(parsed_module['typedef'])

        code = template.render(module=parsed_module)

        filename = "{}/{}.py".format(ctx.opts.napalm_models_path, safe(parsed_module['name']))
        with open(filename, 'w') as f:
            f.write(code)

        print(code)
