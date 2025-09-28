def is_palindrome(s):
    s = s.lower().replace(" ", "")  
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


print(is_palindrome("madam"))   
print(is_palindrome("hello"))  
