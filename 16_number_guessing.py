#Number Guessing Game
import random
secret_number = random.randint(1, 100)
tries_left = 7
guessed_correctly = False
print("I have picked a number between 1 and 100.")
print("You have 7 attempts to guess it!")
while tries_left > 0:
    print("\nAttempts remaining:", tries_left)
    guess = int(input("Enter your guess: "))
    if guess == secret_number:
        print("Congratulations! You guessed it right!")
        print("You used", (8 - tries_left), "attempts.")
        guessed_correctly = True
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")
    tries_left = tries_left - 1
if not guessed_correctly:
    print("\nGame Over! You ran out of tries.")
    print("The secret number was:", secret_number)
print("Would you like to play again? (Restart the program to play)")