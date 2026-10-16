def safe_calculator(a, operator, b):
    operations = {
        '+' : lambda a , b : a + b,
        '-' : lambda a , b : a - b,
        '*' : lambda a , b : a * b,
        '**' : lambda a, b : a ** b,
        '/' : lambda a , b : round(a / b, 2),
        '%' : lambda a , b : round(a % b, 2)
    }

    try:
        num1 = float(a)
        num2 = float(b)

    except ValueError:
        return "Invalid number"

    if operator not in operations:
        return "Invalid operator"

    if operator in ['/' , '%'] and num2 == 0:
        return "Cannot divide by 0"

    result = operations[operator](num1,num2)
    return result

print(safe_calculator("10", "/" , "5"))
print(safe_calculator("five", "+", 2)) #invalid number test case
print(safe_calculator("15", "***", "20")) # invalid operator
print(safe_calculator("200", "/", "0")) #zero division