#Bill Splitter
bill_amount = float(input("Enter total bill: "))
total_people = int(input("Total Number of people: "))
tax_percent = float(input("Tax percentage: "))
tip_percent = float(input("Tip percentage: "))
# Calculating tax amount
tax_val = (tax_percent / 100) * bill_amount
# Calculating bill amount after adding tax
after_tax = bill_amount + tax_val
# Calculating tip amount
tip_val = (tip_percent / 100) * bill_amount
# Calculating the final bill total
total_bill = after_tax + tip_val
# Calculating how much each person pays
per_person = total_bill / total_people
print("=== BILL BREAKDOWN ===")
print("Subtotal: ₹",bill_amount)
print("Tax Amount: ₹",tax_val)
print("Bill after tax: ₹",after_tax)
print("Tip Amount: ₹",tip_val)
print("Total Bill: ₹",total_bill)
print("Amount per person: ₹",per_person)