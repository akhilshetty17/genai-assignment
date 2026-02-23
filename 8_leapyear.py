#Leap Year Checker
year = int(input("Enter a year:"))
if (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a Leap year")
    print("Reason: It follows the rule of being divisible by 4 and (not 100 or 400).")
else:
    print(year,"is NOT a leap year")
    print("Reason: It does not meet the specific divisibility criteria.")