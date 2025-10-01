from itertools import chain


def stringify(nodes, replacer=' ', spaces_count=4):
    
    def iter(current_value, depth):
        if not isinstance(current_value, dict):
            return format_non_dict_value(current_value)
        indent_size = depth + spaces_count
        indent = replacer * indent_size
        indent_size_with_symbols = depth + spaces_count - 2
        indent_with_symbols = replacer * indent_size_with_symbols
        current_indent = replacer * depth
        lines = []
        for k, v in sorted(current_value.items()):
            if isinstance(v, dict):
                t = v.get('type')
                if t == 'added':
                    v_str = iter(v.get('value'), indent_size)
                    lines.append(
                        f'{indent_with_symbols}+ {k}: {v_str}'
                        )
                elif t == 'removed':
                    v_str = iter(v.get('value'), indent_size)
                    lines.append(
                        f'{indent_with_symbols}- {k}: {v_str}'
                        )
                elif t == 'unchanged':
                    v_str = iter(v.get('value'), indent_size)
                    lines.append(f'{indent}{k}: {v_str}')
                elif t == 'changed':
                    v_str = iter(v.get('old_value'), indent_size)
                    lines.append(
                        f'{indent_with_symbols}- {k}: {v_str}'
                        )
                    new_v_str = iter(v.get('new_value'), indent_size)
                    lines.append(
                        f'{indent_with_symbols}+ {k}: {new_v_str}'
                        )
                else:
                    lines.append(f'{indent}{k}: {iter(v, indent_size)}')
            else:
                lines.append(f'{indent}{k}: {iter(v, indent_size)}')
        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    
    return iter(nodes, 0)


def format_non_dict_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    return str(value)