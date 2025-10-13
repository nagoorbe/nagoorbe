def unique_chars_no_vowels(s):
    return {c for c in s if c.lower() not in "aeiou"}

print(unique_chars_no_vowels("hello world"))
