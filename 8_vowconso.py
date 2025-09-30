def count_vowels_consonants(s):
    vowels = "aeiouAEIOU"
    v_count, c_count = 0, 0
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                v_count += 1
            else:
                c_count += 1
    return v_count, c_count

print(count_vowels_consonants("Hello World"))
