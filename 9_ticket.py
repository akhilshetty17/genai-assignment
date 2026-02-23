#Ticket Pricing System
user_age = int(input("Enter your age:"))
day = input("Enter day of the week:")
num_tickets = int(input("How many tickets do you want?"))
if user_age < 3:
    base_price = 0 
elif 3 <= user_age <= 12:
    base_price = 150 
elif 13 <= user_age <= 59:
    base_price = 300
else:
    base_price = 200 
discount = 0
if day == "Friday" or day == "Saturday" or day == "Sunday":
    discount = 0.20 
price_after_discount = base_price * (1 - discount)
total_amount = price_after_discount * num_tickets
print("Base Price per ticket: ₹",base_price)
print("Price after discount: ₹",price_after_discount)
print("Number of tickets:",num_tickets)
print("Total Amount to pay: ₹",total_amount)