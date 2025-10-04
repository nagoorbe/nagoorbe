def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

if __name__ == "__main__":
    print("Running tests...")
    print(is_palindrome("racecar")) 
    print(is_palindrome("world"))    
