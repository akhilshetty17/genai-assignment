#Palindrome Checker
user_input = input("Enter word/number:")
original = user_input.lower()
reversed_val = original[::-1]
print("Original:", user_input)
print("Lowercase:", original)
print("Reversed:", reversed_val)
if original == reversed_val:
    print("\nResult:PALINDROME")
else:
    print("\nResult:NOT A PALINDROME")