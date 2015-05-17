# Guess My Number
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

# ask_number function
def ask_number(question, low, high, step = 1):
    """ Ask for a number within a range. """
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response

# set the initial values
theNumber = random.randint(1,100)
guess = ask_number("Take a guess: ", 1, 100)
tries = 1
limit = 6

# guessing loop
while guess != theNumber:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")

    guess = ask_number("Take a guess: ", 1, 100)
    tries += 1

    if tries == limit :
        break

# congratulating the player

if tries < limit :
    print("You guessed it! The number was", theNumber)
    print("It only took you", tries, "tries!\n")
else:
    print("YOU SUCK!\n")

input("\n\nPress the enter key to exit.")
