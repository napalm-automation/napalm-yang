def model_to_dict(model):
    def get_key(key, model, parent_defining_module):
        key = "{} {}".format(key, "[rw]" if model._is_config else "[ro]")

        if parent_defining_module != model._defining_module:
            key = "{}:{}".format(model._defining_module, key)
        return key

    if model._yang_type in ("container", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model}
    elif model._yang_type in ("list", ):
        return {get_key(k, v, model._defining_module): model_to_dict(v)
                for k, v in model._contained_class()}
    else:
        return model._yang_type
