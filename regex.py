 #search for pattern
import re
text="Hello World"
match=re.search("World",text)
print(match.group())

text="ihave 2 apples and 5 mangoes"
print(re.findall(r"\d",text))

text="python is fun"
print(re.findall(r"\w+",text))


text="My pin is 1234"
print(re.sub(r"\d","*",text))