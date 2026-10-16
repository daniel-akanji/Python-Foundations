text = input("Input: ")
shift = int(input("Shift: "))
Mode = input("Mode: ")
valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

for char in text:
    if char not in valid_chars:
        print("Invalid input entered")
        
    if Mode == "encrypt" and char in valid_chars:
        crypt = chr(ord(char) + shift)
    

    if Mode == "decrypt" and char in valid_chars:
        crypt = chr(ord(char) - shift)

    output = output + crypt

print(f"Input: Text: {text} | Shift: {shift} | Mode: {Mode} --> Output: {output}")