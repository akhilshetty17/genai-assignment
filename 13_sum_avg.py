#Sum and Average Calculator
count = int(input("How many numbers?"))
total_sum = 0
max_num = None 
min_num = None
# Loop to take input 
for i in range(1, count + 1):
    print("Enter number", i, ":", end=" ")
    num = float(input())
    total_sum = total_sum + num
    #Finding Maximum and Minimum
    if max_num is None or num > max_num:
        max_num = num
    if min_num is None or num < min_num:
        min_num = num
# Calculating Average
if count > 0:
    average = total_sum / count
else:
    average = 0
print("Sum:", total_sum)
print("Average:",average)
print("Maximum:",max_num)
print("Minimum:",min_num)