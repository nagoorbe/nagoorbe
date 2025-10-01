def is_anagram(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

print(is_anagram("listen", "silent"))   # True
print(is_anagram("hello", "world"))     # False
