#Simple ATM
balance = 10000
min_balance = 500
while True:
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Exit")
    choice = int(input("Enter choice:"))
    if choice == 1:
        print("Your current balance is: ₹",balance)       
    elif choice == 2:
        dep_amount = float(input("Enter amount to deposit:"))
        balance = balance + dep_amount
        print("Deposit successful!")
        print("Updated balance: ₹",balance)
    elif choice == 3:
        with_amount = float(input("Enter amount to withdraw: "))
        if (balance - with_amount) >= min_balance:
            balance = balance - with_amount
            print("Withdrawal successful!")
            print("New balance: ₹", balance)
        else:
            print("Error: Minimum balance of ₹500 must remain!")
            print("Current balance is only ₹", balance)
    elif choice == 4:
        print("Thank you for using our ATM. Have a nice day!")
        break
    else:
        print("Invalid choice!")