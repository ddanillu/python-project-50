def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if value == '':
        return "''"
    if isinstance(value, int):
        return str(value)
    return f"'{value}'"


def plain_formatter(value, path=''):
    lines = []
    for k, v in sorted(value.items()):
        if isinstance(v, dict):
            property_path = f"{path}.{k}" if path else k
            t = v.get('type')
            if t == 'added':
                v_add = format_value(v.get('value'))
                lines.append(
                    f"Property '{property_path}' was added with value: {v_add}"
                )
            elif t == 'removed':
                lines.append(
                    f"Property '{property_path}' was removed"
                )
            elif t == 'changed':
                old_v = format_value(v.get('old_value'))
                new_v = format_value(v.get('new_value'))
                str_path = f"Property '{property_path}' was updated."
                lines.append(
                    f"{str_path} From {old_v} to {new_v}"
                )
            else:
                lines.append(plain_formatter(v, property_path))
    result = [line for line in lines if line]
    return '\n'.join(result)