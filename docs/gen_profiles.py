from collections import defaultdict

import os


from jinja2 import Environment, FileSystemLoader, StrictUndefined

import napalm_yang


BASE_PATH = os.path.dirname(__file__) or "."
MAPPINGS_PATH = "{}/../napalm_yang/mappings/".format(BASE_PATH)


def is_root_model(model, module):
    model = model.replace("-", "_")
    return any(
        module == m and model.split(".")[0] in s
        for m, s in napalm_yang.SUPPORTED_MODELS
    )


def indent_text(text, indent=4):
    return "\n".join(["{}{}".format(" " * indent, l) for l in text.splitlines()])


def render(template_file, **kwargs):
    env = Environment(
        loader=FileSystemLoader(BASE_PATH), trim_blocks=True, undefined=StrictUndefined
    )
    jinja_filters = {
        "to_yaml": lambda obj: yaml.dump(obj, default_flow_style=False),
        "indent": indent_text,
        "is_root_model": is_root_model,
    }
    env.filters.update(jinja_filters)

    template = env.get_template(template_file)
    return template.render(**kwargs)


def save_text(text, filename):
    with open("{}/{}".format(BASE_PATH, filename), "w+") as f:
        f.write(text)


def get_profiles():
    profiles = defaultdict(lambda: defaultdict(dict))
    for path, dirs, files in os.walk(MAPPINGS_PATH):
        sp = path.split("/")
        if len(sp) != 8 or "translator" in path:
            continue

        profile = sp[4]
        mode = sp[6]
        module = sp[7]

        profiles[profile][mode][module] = files
    return profiles


if __name__ == "__main__":
    profiles = get_profiles()
    text = render(
        "_dynamic/profiles.j2", profiles=profiles, root=napalm_yang.SUPPORTED_MODELS
    )
    save_text(text, "root/supported_models/dynamic_models.rst")
