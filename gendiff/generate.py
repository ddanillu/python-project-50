from gendiff.parser import read_files

from .diff_builder import build_diff
from .formatters.stylish import stringify

FORMATTERS = {
    'stylish': stringify
}


def generate_diff(file1, file2, format_name='stylish'):
    first = read_files(file1)
    second = read_files(file2)
    tree = build_diff(first, second)
    formatter = FORMATTERS.get(format_name)
    return formatter(tree)