def log_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Function: {func.__name__}, Args: {args}, Result: {result}")
        return result
    return wrapper

@log_decorator
def add(a, b):
    return a + b

add(3, 4)
