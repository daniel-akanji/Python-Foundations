initial_no = int(input("Type a number: "))

reference = initial_no
sign = -1 if reference < 0 else 1 #value_if_true if condition else value_if_false(Ternary operator if/else one liner)
num = abs(reference)
output = 0

while num > 0:
    output = (output * 10) + (num % 10)
    num = num // 10

refined_output = sign * output
print(f"Input: {initial_no} --> Output: {refined_output}")