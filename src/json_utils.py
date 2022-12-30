import json


def load_json(fname):
    with open(fname, encoding="utf8") as file:
        return json.load(file)
