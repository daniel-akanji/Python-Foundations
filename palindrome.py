def is_palindrome(s):
    reverse = ""
    for char in s:
        reverse = char + reverse #Builds the reversed string
    if s == reverse:
        return True
    else:
        return False

print(is_palindrome("Book"))
print(is_palindrome("noon"))

# one line code is if s == s[::-1]