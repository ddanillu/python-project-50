from gendiff.parser import read_files


def formatted_value(value):
    """
    Проверяет формат значений и преобразует значения в строки
    """
    if isinstance(value, str):
        return value
    if isinstance(value, bool) or value is None:
        return str(value).lower()
    return str(value)


def generate_diff(file1, file2):
    """
    Сравнивает два плоских JSON-файла и возвращает строку-диф.
    Ключи в алфавитном порядке. Для изменений выводит сначала строку с '-',
    затем строку с '+' для одного ключа.
    """
    first = read_files(file1)
    second = read_files(file2)
    keys = sorted(set(first.keys()) | set(second.keys()))
    lines = []
    indent = '    '
    for key in keys:
        in_first = key in first
        in_second = key in second
        if in_first and not in_second:
            lines.append(
                f"{indent[:-2]}- {key}: {formatted_value(first[key])}"
                )
        elif not in_first and in_second:
            lines.append(
                f"{indent[:-2]}+ {key}: {formatted_value(second[key])}"
                )
        else:
            value1 = first[key]
            value2 = second[key]
            if value1 == value2:
                lines.append(f"{indent}{key}: {formatted_value(value1)}")
            else:
                lines.append(f"{indent[:-2]}- {key}: {formatted_value(value1)}")
                lines.append(f"{indent[:-2]}+ {key}: {formatted_value(value2)}")
    result = "{\n" + "\n".join(lines) + "\n}"
    return result