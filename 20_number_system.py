#Number System Functions
#Finding Factorial of n
def factorial(n):
    if n < 0:
        return "Not defined for negative numbers"
    res = 1
    for i in range(1, n + 1):
        res = res * i
    return res
#Checking if n is Prime
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True
#Finding Fibonacci number
def fibonacci(n):
    if n <= 0: 
        return 0
    elif n == 1: 
        return 1
    a, b = 0, 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b

#Sum of Digits 
def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total = total + (n % 10)
        n = n // 10
    return total
#Reverse a Number
def reverse_number(n):
    rev = 0
    is_negative = n < 0
    n = abs(n)
    while n > 0:
        rev = (rev * 10) + (n % 10)
        n = n // 10
    return -rev if is_negative else rev
#Armstrong Number
def armstrong(n):
    temp = n
    total = 0
    order = len(str(n))
    while temp > 0:
        digit = temp % 10
        total = total + (digit ** order)
        temp = temp // 10
    return total == n
#Greatest Common Divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
#LCM
def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)
#Perfect Number check
def perfect_number(n):
    if n < 1: return False
    sum_divisors = 0
    for i in range(1, n):
        if n % i == 0:
            sum_divisors = sum_divisors + i
    return sum_divisors == n
#Main Menu
def math_menu():
    while True:
        print("========NUMBER SYSTEM MENU========")
        print("1.Factorial")
        print("2.Prime Number Check")
        print("3.Fibonacci")
        print("4.Sum of Digits")
        print("5.Reverse Number")
        print("6.Armstrong Number")
        print("7.GCD")
        print("8.LCM")
        print("9.Perfect Number")
        print("10.Exit")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            n = int(input("Enter a number:"))
            print("Factorial:", factorial(n))
        elif choice == 2:
            n = int(input("Enter a number:"))
            print("Prime:",prime(n))
        elif choice == 3:
            n = int(input("Enter n value:"))
            print("Fibonacci term:",fibonacci(n))
        elif choice == 4:
            n = int(input("Enter a number:"))
            print("Sum of digits:",sum_of_digits(n))
        elif choice == 5:
            n = int(input("Enter a number:"))
            print("Reversed number:",reverse_number(n))
        elif choice == 6:
            n = int(input("Enter a number:"))
            print("Armstrong:",armstrong(n))
        elif choice == 7:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print("GCD:",gcd(a, b))
        elif choice == 8:
            a = int(input("Enter first number:"))
            b = int(input("Enter second number:"))
            print("LCM:",lcm(a, b))
        elif choice == 9:
            n = int(input("Enter a number: "))
            print("Perfect Number:",perfect_number(n))
        elif choice == 10:
            print("Exiting program..")
            break
        else:
            print("Invalid choice!")
math_menu()