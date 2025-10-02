def even_numbers(n):
    for i in range(2, n + 1, 2):
        yield i


print(list(even_numbers(10)))
