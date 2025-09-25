from pathlib import Path

from gendiff.generate import generate_diff


def read_expected(name):
    p = Path(__file__).parent / 'data' / name
    return p.read_text()


def test_generate_diff_from_json_files():
    expected = read_expected('generate_result.txt')
    assert generate_diff('file1.json', 'file2.json') == expected


def test_generate_diff_from_yaml_files():
    expected = read_expected('generate_result.txt')
    assert generate_diff('file1.yaml', 'file2.yaml') == expected
