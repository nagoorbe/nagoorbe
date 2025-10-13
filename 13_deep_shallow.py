import copy

nested = [[1,2], [3,4]]
shallow = nested.copy()
deep = copy.deepcopy(nested)

nested[0][0] = 99
print(shallow)  # affected
print(deep)     # unaffected
