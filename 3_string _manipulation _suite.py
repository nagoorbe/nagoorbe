def remove_vowels(s):
    return ''.join(c for c in s if c.lower() not in "aeiou")

def char_frequency(s):
    freq = {}
    for c in s:
        freq[c] = freq.get(c, 0) + 1
    return freq

def substrings_k(s, k):
    return [s[i:i+k] for i in range(len(s)-k+1)]


s = "hello"
print((s))
print(char_frequency(s))
print(substrings_k(s, 3))
