import json


def filters():
    return {
        "json": lambda obj: json.dumps(obj),
    }
