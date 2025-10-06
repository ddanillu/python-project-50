def build_diff(d1, d2):
    tree = {}
    for key in d1.keys():
        v1 = d1.get(key)
        if key in d2:
            v2 = d2.get(key)
            if isinstance(v1, dict) and isinstance(v2, dict):
                tree[key] = build_diff(v1, v2)
            elif v1 == v2:
                tree[key] = {"type": "unchanged", "value": v1}
            else:
                tree[key] = {
                    "type": "changed", "old_value": v1, "new_value": v2
                    }
        else:
            tree[key] = {"type": "removed", "value": v1}
    for key in d2.keys():
        v2 = d2.get(key)
        if key not in d1:
            tree[key] = {"type": "added", "value": v2}
    return tree