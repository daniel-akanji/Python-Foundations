def palindrome(s):
    reverse = ""
    for char in s:
        reverse = char + reverse 
    if s == reverse:
        return "Palindrome"
    else:
        return "Not a palindrome"

print(palindrome("racecar"))
print(palindrome("madam"))
print(palindrome("python"))
print(palindrome("hello"))