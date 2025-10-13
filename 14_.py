def my_max(lst):
    max_val = lst[0]
    for x in lst:
        if x > max_val:
            max_val = x
    return max_val

def my_min(lst):
    min_val = lst[0]
    for x in lst:
        if x < min_val:
            min_val = x
    return min_val

def my_sum(lst):
    total = 0
    for x in lst:
        total += x
    return total

print(my_max([1,5,2]))
print(my_min([1,5,2]))
print(my_sum([1,5,2]))
