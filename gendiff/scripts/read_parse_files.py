import json
import os

DATA_DIR = os.path.join('tests', 'data')


def read_json(filename):
    path = os.path.join(DATA_DIR, filename)
    return json.load(open(path))