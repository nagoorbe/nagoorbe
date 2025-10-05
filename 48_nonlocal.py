def outer():
    x = 5
    def inner():
        nonlocal x
        x += 1
        return x
    print(inner())
    print(inner())

outer()
