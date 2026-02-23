#Factorial Calculator
num = int(input("Enter a number:"))
if num < 0:
    print("Factorial not defined for negative numbers")
elif num == 0:
    print("0! = 1")
else:
    fact = 1
    steps = ""
    for i in range(num,0,-1):
        fact = fact * i
        if i == 1:
            steps = steps + str(i)
        else:
            steps = steps + str(i) + " x "
    print(num,"! =",steps,"=",fact)