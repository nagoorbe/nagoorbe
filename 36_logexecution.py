# log execution using decorator
import time

def execution_time(func):
    """Decorator to measure execution time of a function"""
    def wrapper(*args, **kwargs):
        start = time.time()          # start timer
        result = func(*args, **kwargs)
        end = time.time()            # end timer
        print(f"Execution time of '{func.__name__}': {end - start:.6f} seconds")
        return result
    return wrapper


@execution_time
def calculate_sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    return total

print(calculate_sum(1000000))
