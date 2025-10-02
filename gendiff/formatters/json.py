from json import dumps


def format_json(diff):
    return dumps(diff, indent=4)