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

# set the initial values
theNumber = random.randint(1,100)
guess = int(input("Take a guess: "))
tries = 1
limit = 6

# guessing loop
while guess != theNumber:
    if guess > theNumber:
        print("Lower...")
    else:
        print("Higher...")

    guess = int(input("Take a guess: "))
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
