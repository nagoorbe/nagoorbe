nums = [1,2,3,4,5,6,9]

evens = [x for x in nums if x % 2 == 0]
squared_odds = [x**2 for x in nums if x % 2 != 0]
tuples_div3 = [(x, x**2) for x in nums if x % 3 == 0]

print(evens, squared_odds, tuples_div3)
