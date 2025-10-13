def set_ops(list1, list2):
    s1, s2 = set(list1), set(list2)
    return s1 | s2, s1 & s2, s1 - s2

# Example
print(set_ops([1,2,3], [3,4,5]))
