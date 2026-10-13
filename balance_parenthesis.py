input_chars = input("Input: ")

count = 0
for char in input_chars:
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1

if count == 0:
    print("Output: Balanced")
else:
    print("Output: Not balanced")