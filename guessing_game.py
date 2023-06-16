import random
import builtins

# Generate a random number between 1 and 100.
random_number = random.randint(1, 100)

chances = 5

while chances > 0:
    user_guess = int(input("What is your guess? "))

    chances -= 1

    if user_guess == random_number:
        print("Correct! The number was", random_number)
        break
    elif user_guess < random_number:
        print("Your guess is too low.", chances, "times left")
    else:
        print("Your guess is too high.", chances, "times left")

if chances == 0:
    print("You have lost. The number was", random_number)