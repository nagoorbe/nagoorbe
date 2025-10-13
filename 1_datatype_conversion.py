
def type_count(lst):
    counts = {"int": 0, "float": 0, "str": 0, "bool": 0}
    for item in lst:
        if isinstance(item, bool):
            counts["bool"] += 1
        elif isinstance(item, int):
            counts["int"] += 1
        elif isinstance(item, float):
            counts["float"] += 1
        elif isinstance(item, str):
            counts["str"] += 1
    return counts


print(type_count([1, 2.5, "hello", True, False, 7]))
