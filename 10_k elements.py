def rotate_list(lst, k):
    n = len(lst)
    k = k % n 
    return lst[-k:] + lst[:-k]


print(rotate_list([1, 2, 3, 4, 5], 2))
