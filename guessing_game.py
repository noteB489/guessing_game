import random
import builtins

# Generate a random number between 1 and 100.
random_number = random.randint(1, 100)

chances = 5

while chances > 0:
    user_guess = int(input("What is your guess? "))

    if user_guess == random_number:
        print("Correct! The number was", random_number)
        break
    elif user_guess < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")

    chances -= 1

if chances == 0:
    print("You have lost. The number was", random_number)