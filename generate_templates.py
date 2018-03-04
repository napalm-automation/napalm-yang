from collections import defaultdict

import os


import napalm_yang

import yaml

models = [
    napalm_yang.models.openconfig_network_instance,
    napalm_yang.models.openconfig_interfaces,
    napalm_yang.models.openconfig_platform,
    napalm_yang.models.openconfig_vlan,
    napalm_yang.models.openconfig_system,
]

profile = "dummy"


def nested_dd():
    return defaultdict(nested_dd)


def process(model, r_config, r_state):
    if model._yang_type in ("container", ):
        ctr = model
    elif model._yang_type in ("list", None):
        ctr = model._contained_class()
    else:
        if model._is_config or model._yang_name == "config":
            r_config[model._yang_name] = {"_process": "not_implemented"}
        else:
            r_state[model._yang_name] = {"_process": "not_implemented"}
        return

    if model._yang_name == "config":
        r_config = r_config[ctr._yang_name]
        r_config["_process"] = "not_implemented"
    elif model._is_config:
        r_config = r_config[ctr._yang_name]
        r_config["_process"] = "not_implemented"
        r_state = r_state[ctr._yang_name]
        r_state["_process"] = "not_implemented"
    else:
        r_state = r_state[ctr._yang_name]
        r_state["_process"] = "not_implemented"

    for k, v in ctr:
        process_module(v, model._defining_module, r_config, r_state)


def process_module(model, module, r_config=None, r_state=None):
    if model._defining_module != module:
        r_config = result["config"][os.path.join(model._defining_module,
                                                 "{}.yaml".format(model._yang_name))]
        r_state = result["state"][os.path.join(model._defining_module,
                                               "{}.yaml".format(model._yang_name))]

    process(model, r_config, r_state)


def ddict2dict(d):
    for k, v in d.items():
        if isinstance(v, dict):
            d[k] = ddict2dict(v)
    return dict(d)


def main():
    global result
    result = nested_dd()

    for model in models:
        m = model()
        for _, v in m:
            process_module(v, None, result["config"], result["state"])

    for mode, data in result.items():
        for module, model in data.items():
            module, filename = module.split("/")

            for action in ["parsers", "translators"]:
                if action == "translators" and mode == "state":
                    continue
                elif action == "translators":
                    directory = os.path.join("napalm_yang", "mappings", "dummy", action, module)
                else:
                    directory = os.path.join("napalm_yang", "mappings", "dummy", action,
                                             mode, module)

                if not os.path.exists(directory):
                    os.makedirs(directory)

                model = ddict2dict(model)
                metadata = "---\nmetadata:\n    processor: unset\n\n"

                with open(os.path.join(directory, filename), 'w+') as f:
                    f.write(metadata + yaml.safe_dump(model, indent=4, default_flow_style=False))


if __name__ == "__main__":
    main()
