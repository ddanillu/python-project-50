from itertools import chain


def format_stylish(nodes, replacer=' ', spaces_count=4):
    
    def iter(current_value, depth):
        if not isinstance(current_value, dict):
            if current_value is None:
                return 'null'
            if isinstance(current_value, bool):
                return str(current_value).lower()
            return str(current_value)
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
                    lines.append(f'{indent_with_symbols}+ {k}: {iter(v.get('value'), indent_size)}')
                elif t == 'removed':
                    lines.append(f'{indent_with_symbols}- {k}: {iter(v.get('value'), indent_size)}')
                elif t == 'unchanged':
                    lines.append(f'{indent}{k}: {iter(v.get('value'), indent_size)}')
                elif t == 'changed':
                    lines.append(f'{indent_with_symbols}- {k}: {iter(v.get('old_value'), indent_size)}')
                    lines.append(f'{indent_with_symbols}+ {k}: {iter(v.get('new_value'), indent_size)}')
                else:
                    lines.append(f'{indent}{k}: {iter(v, indent_size)}')
            else:
                lines.append(f'{indent}{k}: {iter(v, indent_size)}')
        result = chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    
    return iter(nodes, 0)