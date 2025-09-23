from .scripts.read_parse_files import read_json


def generate_diff(file1, file2):
    """
    Сравнивает два плоских JSON-файла и возвращает строку-диф.
    Ключи в алфавитном порядке. Для изменений выводит сначала строку с '-',
    затем строку с '+' для одного ключа.
    """
    first = read_json(file1)
    second = read_json(file2)
    keys = sorted(set(first.keys()) | set(second.keys()))

    def formatted_value(value):
        if isinstance(value, str):
            return value
        elif isinstance(value, bool) or value is None:
            return str(value).lower()
        return str(value)
        
    
    lines = []
    indent = '  '
    for key in keys:
        in_first = key in first
        in_second = key in second
        if in_first and not in_second:
            lines.append(f"{indent}- {key}: {formatted_value(first[key])}")
        elif not in_first and in_second:
            lines.append(f"{indent}+ {key}: {formatted_value(second[key])}")
        elif in_first and in_second:
            value1 = first[key]
            value2 = second[key]
            if value1 == value2:
                lines.append(f"{indent}  {key}: {formatted_value(value1)}")
            else:
                lines.append(f"{indent}- {key}: {formatted_value(value1)}")
                lines.append(f"{indent}+ {key}: {formatted_value(value2)}")
    result = "{\n" + "\n".join(lines) + "\n}"
    return result