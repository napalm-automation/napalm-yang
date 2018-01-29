import os

from glob import glob

import yaml

from jinja2 import Environment, FileSystemLoader, StrictUndefined


BASE_PATH = os.path.dirname(__file__) or "."
LIST_EXAMPLES_PATH = "{}/../test/unit/test_parser/list/".format(BASE_PATH)
LIST_EXAMPLES = sorted([x for x in glob('{}/*'.format(LIST_EXAMPLES_PATH))])

LEAF_EXAMPLES_PATH = "{}/../test/unit/test_parser/leaf/".format(BASE_PATH)
LEAF_EXAMPLES = sorted([x for x in glob('{}/*'.format(LEAF_EXAMPLES_PATH))])

def indent_text(text, indent=4):
    return "\n".join(["{}{}".format(" " * indent, l) for l in text.splitlines()])


def get_examples(EXAMPLES):
    examples = []
    for e in EXAMPLES:
        with open("{}/mocked.txt".format(e), "r") as f:
            mocked = f.read()

        with open("{}/example.yaml".format(e), "r") as f:
            example = yaml.load(f.read())

        examples.append({"mocked": mocked, "example": example})
    return examples


def get_directives():
    with open("{}/_dynamic/parser_directives.yaml".format(BASE_PATH), "r") as f:
        return yaml.load(f.read())


def render(template_file, **kwargs):
    env = Environment(loader=FileSystemLoader(BASE_PATH),
                      trim_blocks=True,
                      undefined=StrictUndefined)
    jinja_filters = {
        "to_yaml": lambda obj: yaml.dump(obj, default_flow_style=False),
        "indent": indent_text,
    }
    env.filters.update(jinja_filters)

    template = env.get_template(template_file)
    return template.render(**kwargs)


def save_text(text, filename):
    with open("{}/{}".format(BASE_PATH, filename), "w+") as f:
        f.write(text)


if __name__ == "__main__":
    examples = get_examples(LIST_EXAMPLES)
    text = render('_dynamic/examples_list.j2', examples=examples)
    save_text(text, "developers/parsers/examples_list.rst")

    examples = get_examples(LEAF_EXAMPLES)
    text = render('_dynamic/examples_leaf.j2', examples=examples)
    save_text(text, "developers/parsers/examples_leaf.rst")

    directives = get_directives()
    text = render('_dynamic/parsers.j2', directives=directives)
    save_text(text, "developers/parsers/dynamic_directives.rst")
