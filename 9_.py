def cast_list(lst, target_type):
    new_list = []
    for val in lst:
        try:
            new_list.append(target_type(val))
        except (ValueError, TypeError):
            new_list.append(None)
    return new_list

# Example
print(cast_list(["1", "2.5", "hello"], int))
