s = input("> ")
def reverse_string(s: str) -> str:
    result = ""
    pointer = len(s)-1

    while pointer >= 0:
        result += s[pointer]
        pointer -= 1

    return result



# def reverse_string(s: str) -> str:
#     reverse = ""

#     for char in s:
#         reverse = char + reverse

#     return reverse

print(reverse_string(s))

