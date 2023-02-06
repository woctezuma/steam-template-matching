import json
from pathlib import Path


def load_json(fname):
    with Path(fname).open(encoding="utf8") as file:
        return json.load(file)
