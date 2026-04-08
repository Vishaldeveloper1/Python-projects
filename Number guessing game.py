import random
import math

# Taking Inputs
lower = int(input("Enter Lower bound: "))
upper = int(input("Enter Upper bound: "))

# Generating random number between the lower and upper
x = random.randint(lower, upper)

# Calculation of minimum number of guesses depends upon range
total_chances = math.ceil(math.log2(upper - lower + 1))

print(f"\n\tYou've only {total_chances} chances to guess the integer!\n")

count = 0
flag = False

# While loop for guessing
while count < total_chances:
    count += 1

    # Taking guessing number as input
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a valid integer.")
        count -= 1 # Don't penalize for a non-integer input
        continue

    # Condition testing
    if x == guess:
        print(f"Congratulations you did it in {count} try!")
        flag = True
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You guessed too high!")

# If Guessing is more than required guesses
if not flag:
    print(f"\nThe number is {x}")
    print("\tBetter Luck Next time!")