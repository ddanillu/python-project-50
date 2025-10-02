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


def test_generate_diff_big_json():
    expected = read_expected('generate_result2.txt')
    assert generate_diff('filepath1.json', 'filepath2.json') == expected


def test_generate_big_yaml():
    expected = read_expected('generate_result2.txt')
    assert generate_diff('filepath1.yml', 'filepath2.yml') == expected


def test_generate_plain():
    expected = read_expected('generate_plain.txt')
    assert generate_diff('filepath1.yml', 'filepath2.yml', 'plain') == expected


def test_generate_json():
    expected = read_expected('generate_json.json')
    assert generate_diff('filepath1.yml', 'filepath2.json', 'json') == expected