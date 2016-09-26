"""NAPALM output plugin."""

import logging
import optparse
import os
import re
import sys

import json

from collections import defaultdict

from pyang import plugin

from jinja2 import Environment, FileSystemLoader


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
                                 default="./models",
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
    print("# {}".format(obj.__class__.__name__))
    for k, v in obj.__dict__.items():
        l = 30 - len(k)
        print("{}{}{}".format(k, " " * l, v))
    print("======================")


MODULE_INFORMATIONAL_STATEMENTS = [
    'namespace',
    'organization',
    'contact',
    'description',
    'revision',
]


def safe(name):
    """Given a string, return a safe version."""
    name = re.sub('-', '_', name)
    return name


def emit_napalm(ctx, modules, fd):
    """
    Args:
        ctx(pyang.Context): Options passed via the CLI.
        modules(list of pyang.statements.Statement): List of yang models being processed
        fd(file): File open to written to
    """
    env = Environment(loader=FileSystemLoader('./pyang_plugin/templates/'))
    template = env.get_template('module.j2')

    global logger
    logger = logging.getLogger("napalm_pyang_plugin")
    logger = configure_logging(logger, ctx.opts.verbose)

    for module in modules:
        logger.info("Processing model {}".format(module.pos))
        parsed_module = {'info': {}, 'containers': {}, 'typedefs': {}, }
        parsed_module['name'] = module.i_modulename

        for substmt in module.substmts:
            logger.debug("Found statement: {}".format(substmt.keyword))
            if substmt.keyword in MODULE_INFORMATIONAL_STATEMENTS:
                parsed_module['info'][substmt.keyword] = substmt.arg
            elif substmt.keyword == 'prefix':
                parsed_module['info']['prefix'] = substmt.arg
                prefix = substmt.arg
            elif substmt.keyword == 'typedef':
                parsed_module['typedefs'][substmt.arg.replace('-ref', '')] = process_containers(
                                                                          substmt,
                                                                          parsed_module['typedefs'],
                                                                          prefix,
                                                                          '')
            elif substmt.keyword in ['import', 'identity', 'feature', ]:
                # TODO
                pass
            elif substmt.keyword == "container":
                parsed_module['containers'][substmt.arg] = process_containers(
                                                                       substmt,
                                                                       parsed_module['typedefs'],
                                                                       prefix,
                                                                       '/{}:{}'.format(prefix,
                                                                                       substmt.arg))
            else:
                raise Exception("Not sure about this type of statement: {}".format(substmt.keyword))

        code = template.render(module=parsed_module)

        filename = "{}/{}.py".format(ctx.opts.napalm_models_path, safe(parsed_module['name']))
        with open(filename, 'w') as f:
            f.write(code)

        print(json.dumps(parsed_module))


def process_containers(container, typedefs, prefix, path):
    logger.debug("Processing container {} in path {}".format(container.arg, path))
    parsed = defaultdict(dict)

    for substmt in container.substmts:
        logger.debug("Processing substmt: {}".format(substmt.keyword))
        if substmt.keyword in ['description', 'key', 'reference', 'mandatory', 'default',
                               'if-feature', 'units', 'config', 'base', 'range', 'path',
                               'value']:
            parsed[substmt.keyword] = substmt.arg
        elif substmt.keyword in ['enum', ]:
            parsed['enum'][substmt.arg] = substmt.i_value
        elif substmt.keyword in ['type', ]:
            parsed[substmt.keyword] = {
                'value': substmt.arg,
                'options': process_containers(substmt, typedefs, prefix, path)
            }
        elif substmt.keyword in ['leaf', 'leaf-list']:
            parsed[substmt.keyword][substmt.arg] = process_containers(substmt, typedefs,
                                                                      prefix, path)
        elif substmt.keyword in ['list', 'container']:
            path = '{}/{}:{}'.format(path, prefix, substmt.arg)
            for t, d in typedefs.items():
                # TODO build entire path rather than do this naive comparison
                if path in d['type']['options']['path']:
                    parsed[substmt.keyword][substmt.arg] = {'type': t}
                    d.update(process_containers(substmt, typedefs, prefix, path))
                    break
            else:
                parsed[substmt.keyword][substmt.arg] = {'type': substmt.arg}
                typedefs[substmt.arg] = process_containers(substmt, typedefs, prefix, path)
        else:
            raise Exception("Not sure about this type of statement: {}".format(substmt.keyword))

    return parsed
