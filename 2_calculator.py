#Simple Calculator
num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
print("Results:")
# Addition
add = num1 + num2
print(num1,"+",num2,"=",add)
# Subtraction
sub = num1 - num2
print(num1,"-",num2,"=",sub)
# Multiplication
mul = num1 * num2
print(num1,"*",num2,"=",mul)
# Division
if num2 != 0:
    div = num1 / num2
    print(num1,"/",num2,"=",div)
    mod = num1 % num2
    print(num1,"%",num2,"=",mod)
else:
    print("Cannot divide by zero")
# Exponentiation
pwr = num1 ** num2
print(num1,"^",num2,"=", pwr)