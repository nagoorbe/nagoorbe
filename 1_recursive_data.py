def recursive_sum(data):
    total = 0
    if isinstance(data, dict):
        for value in data.values():
            total += recursive_sum(value)
    elif isinstance(data, list):
        for item in data:
            total += recursive_sum(item)
    elif isinstance(data, (int, float)):
        total += data
    return total

nested = {"a": 10, "b": [1, 2, {"c": 3, "d": [4, 5]}], "e": {"f": 6}}
print(recursive_sum(nested))  
