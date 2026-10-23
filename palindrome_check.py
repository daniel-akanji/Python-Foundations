s = input("> ")
special_chars = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', 
    ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' '
]


def is_palindrome(s: str) -> bool:
    plain_alphanumeric = "".join([char for char in s if char not in special_chars])
    words = plain_alphanumeric.lower().strip()
    reverse = ""

    for char in words:
        reverse = char + reverse
    
    if reverse == words:
        return True
    elif reverse!= words:
        return False

print(is_palindrome(s))