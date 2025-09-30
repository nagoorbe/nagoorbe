def my_max(lst):
    if not lst:
        raise ValueError("Empty list has no maximum")
    maximum = lst[0]
    for item in lst[1:]:
        if item > maximum:
            maximum = item
    return maximum

print(my_max([10, 5, 30, 25])) 