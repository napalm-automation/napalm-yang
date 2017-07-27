import os

from glob import glob

import yaml

from jinja2 import Environment, FileSystemLoader, StrictUndefined


BASE_PATH = os.path.dirname(__file__) or "."
EXAMPLES_PATH = "{}/../test/unit/test_parser/".format(BASE_PATH)
EXAMPLES = sorted([x for x in glob('{}/*'.format(EXAMPLES_PATH))])


def get_examples():
    examples = []
    for e in EXAMPLES:
        with open("{}/mocked.txt".format(e), "r") as f:
            mocked = f.read()

        with open("{}/example.yaml".format(e), "r") as f:
            example = yaml.load(f.read())

        examples.append({"mocked": mocked, "example": example})
    return examples


def indent_text(text, indent=4):
    return "\n".join(["{}{}".format(" " * indent, l) for l in text.splitlines()])


def render_examples(examples):
    env = Environment(loader=FileSystemLoader(BASE_PATH),
                      trim_blocks=True,
                      undefined=StrictUndefined)
    jinja_filters = {
        "to_yaml": lambda obj: yaml.dump(obj, default_flow_style=False),
        "indent": indent_text,
    }
    env.filters.update(jinja_filters)

    template = env.get_template('examples.j2')
    return template.render(examples=examples)


def save_text(text):
    with open("{}/yang/parsers/examples.rst".format(BASE_PATH), "w+") as f:
        f.write(text)


if __name__ == "__main__":
    examples = get_examples()
    text = render_examples(examples)
    save_text(text)
