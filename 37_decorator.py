def call_counter(func):
    """Decorator to count how many times a function is called"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Function '{func.__name__}' call count: {wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0 
    return wrapper


@call_counter
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")
