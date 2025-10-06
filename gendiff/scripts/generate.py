from gendiff.formatters.json import format_json
from gendiff.formatters.plain import plain_formatter
from gendiff.formatters.stylish import stringify
from gendiff.scripts.parser import read_files

from .diff_builder import build_diff

FORMATTERS = {
    'stylish': stringify,
    'plain': plain_formatter,
    'json': format_json
}


def generate_diff(file1, file2, format_name='stylish'):
    first = read_files(file1)
    second = read_files(file2)
    tree = build_diff(first, second)
    formatter = FORMATTERS.get(format_name)
    return formatter(tree)