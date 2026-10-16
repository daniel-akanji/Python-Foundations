def my_upper(s):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "" 
    for char in s:
        if char in lower:
            char = chr(ord(char) - 32) # ord() gives the ASCII value of a character while chr() gives the character of the input ASCII value
        upper = upper + char
    return upper

print(my_upper("lAke"))
print(my_upper("learn2earn"))

#UPPERCASE = 65 - 90
#lowercase = 97 - 122