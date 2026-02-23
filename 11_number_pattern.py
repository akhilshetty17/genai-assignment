#Number Pattern Printer
print("1. Pattern 1 (Increasing 123)")
print("2. Pattern 2 (Same numbers 1, 22, 333)")
print("3. Pattern 3 (Decreasing 54321)")
print("4. Pattern 4 (Pyramid 12321)")

choice = int(input("Choose a pattern:"))
n = int(input("Enter height:"))
if choice == 1:
    # Pattern 1: 1, 12, 123...
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        print()
elif choice == 2:
    # Pattern 2: 1, 22, 333...
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end="")
        print()
elif choice == 3:
    # Pattern 3: 54321, 4321...
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end="")
        print()
elif choice == 4:
    # Pattern 4: 1, 121, 12321...
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()
else:
    print("Invalid choice!")