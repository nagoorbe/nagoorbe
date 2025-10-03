def safe_division(a, b):
    attempts = 3
    for i in range(attempts):
        try:
            return a / b
        except ZeroDivisionError:
            print(f"Attempt {i+1}: Cannot divide by zero")
            b = int(input("Enter a new denominator: "))
    return "Failed after 3 attempts"

print(safe_division(10,0))
