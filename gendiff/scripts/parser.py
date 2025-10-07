import json
import os

import yaml

DATA_DIR = os.path.join('tests', 'test_data')


def read_files(filename):
    path = os.path.join(DATA_DIR, filename)
    ext = os.path.splitext(path)[1].lower()
    if ext in ('.json'):
        return json.load(open(path))
    if ext in ('.yml', '.yaml'):
        return yaml.safe_load(open(path))