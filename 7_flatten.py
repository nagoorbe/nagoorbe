def flatten(nested):
    flat = []
    for sublist in nested:
        for item in sublist:
            flat.append(item)
    return flat


print(flatten([[1, 2], [3, 4], [5]]))
