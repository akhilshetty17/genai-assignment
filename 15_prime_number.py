#Prime Number Checker
n = int(input("Enter the number:"))
if n < 2:
    print(n, "is not a prime number.")
else:
    is_prime = True
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            is_prime = False
            break
    if is_prime:
        print(n, "is a prime number.")
    else:
        print(n, "is not a prime number.")
#Finding all primes in a given range
start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))
print("The prime numbers between", start, "and", end, "are:")
for num in range(start, end + 1):
    if num > 1:
        is_p = True
        for j in range(2, int(num/2) + 1):
            if num % j == 0:
                is_p = False
                break
        if is_p:
            print(num, end=" ")