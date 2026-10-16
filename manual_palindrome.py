#for plan in plnB:
# if len(plan) gives the string length of each item in a dictionary
def manual_palindrome(text):
    work_with = text.strip()
    clean = work_with. lower()
    reverse = ""
    for char in clean:
        reverse = char + reverse
    if clean == reverse:
        return True
    return False

print(manual_palindrome("Level"))
print(manual_palindrome("Noon"))
print(manual_palindrome("Any"))