def second_largest(lst):
    unique = []
    for num in lst:   
        if num not in unique:
            unique.append(num)
    if len(unique) < 2:
        return None
    unique.sort()
    return unique[-2]


print(second_largest([10, 20, 4, 20, 10, 8]))
