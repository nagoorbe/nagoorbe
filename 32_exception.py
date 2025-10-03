class NegativeNumberError(Exception):
    pass

def check_positive(num):
    if num < 0:
        raise NegativeNumberError("Negative number not allowed")
    return num


try:
    print(check_positive(-5))
except NegativeNumberError as e:
    print(e)
