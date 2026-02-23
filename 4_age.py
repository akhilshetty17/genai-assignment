#Age Calculator
current_date = 23
current_month = 2
current_year = 2026
birth_date = int(input("Enter your birth date (1-31):"))
birth_month = int(input("Enter your birth month (1-12):"))
birth_year = int(input("Enter your birth year:"))
#Calculating current age
age = current_year - birth_year
if (current_month < birth_month) or (current_month == birth_month and current_date < birth_date):
    age = age - 1
print("Your exact current age:",age,"years")
#Age in months
months = (age * 12) + current_month
print("Age in months:", months)
#Age in days
days = age * 365
print("Age in days:",days)
#Age in hours
hours = days * 24
print("Age in hours:",hours)
#Age in minutes
minutes = hours * 60
print("Age in minutes:",minutes)
#Years until age 100
years_til_100 = 100 - age
if years_til_100 > 0:
    print("Years until age 100:",years_til_100)
else:
    print("You are already 100 years old!")