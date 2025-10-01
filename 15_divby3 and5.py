def divisible_by_3_and_5():
    return [num for num in range(1, 101) if num % 3 == 0 and num % 5 == 0]

print(divisible_by_3_and_5())
