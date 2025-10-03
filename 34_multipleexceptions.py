def safe_input():
    try:
        x = int(input("Enter a number: "))
        result = 10 / x
        print(result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    except ValueError:
        print("Invalid input, enter an integer")

safe_input()
