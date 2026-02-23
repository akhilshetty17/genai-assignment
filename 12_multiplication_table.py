#Multiplication Table Generator
num = int(input("Enter number:"))
end_range = int(input("Enter range:"))
print("\nMultiplication Table of", num)
for i in range(1, end_range + 1):
    result = num * i
    print(num,"x",i,"=",result)