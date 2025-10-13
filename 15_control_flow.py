def custom_filter(nums):
    result = []
    for x in nums:
        if x < 0:
            break
        if x % 3 == 0:
            continue
        result.append(x)
    return result

print(custom_filter([1,2,3,4,5,6,-1,7]))
