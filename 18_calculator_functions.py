#Calculator Functions
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    else:
        return a / b
def modulus(a, b):
    return a % b
def power(a, b):
    return a ** b
def calculator():
    while True:
        print("\n1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        print("5.Modulus")
        print("6.Power")
        print("7.Exit")
        choice = int(input("Enter choice:"))
        if choice == 7:
            print("Exiting calculator")
            break
        if choice in [1, 2, 3, 4, 5, 6]:
            num1 = float(input("Enter first number:"))
            num2 = float(input("Enter second number:"))  
            if choice == 1:
                print("Result:",add(num1,num2))
            elif choice == 2:
                print("Result:",subtract(num1,num2))
            elif choice == 3:
                print("Result:",multiply(num1,num2))
            elif choice == 4:
                print("Result:",divide(num1,num2))
            elif choice == 5:
                print("Result:",modulus(num1,num2))
            elif choice == 6:
                print("Result:",power(num1,num2))
        else:
            print("Invalid Choice!Please enter a number between 1 and 7.")
calculator()