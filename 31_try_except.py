def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

print(divide(10, 2))  # 5.0
print(divide(10, 0))  # Error
