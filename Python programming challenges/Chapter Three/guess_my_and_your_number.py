# Guess My and Your Number
#
# The computer picks a random number between 1 and 100
# The player picks a number for the computer to guess
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money
# The computer tries to guess it and the computer is told if higher or lower

import random

print("\tWelcome to 'Guess My Number'!")
print("\nI'm thinking of a number between 1 and 100.")
print("Try to guess it in as few attempts as possible.\n")

playerNum = int(input("Now player, pick a number between 1 and 100 please.\n"))

# set the inital values
compNum = random.randint(1,100)
print(compNum)
playerGuess = int(input("Take a guess: "))
compGuess = 50
tries = 1

# guessing loop
while playerGuess != compNum and compGuess != playerNum:
    # player first
    if playerGuess > compNum:
        print("Lower...")
    else:
        print("Higher...")

    # computer next
    if compGuess > playerNum:
        compGuess += compGuess/2
    else:
        compGuess -= compGuess/2

    playerGuess = int(input("Take a guess: "))
    tries += 1

# congratulating the player or computer

if playerGuess == compNum:
    print("You guessed it! The number was", compNum)
    print("It only took you", tries, "tries!\n")
else:
    print("The computer is the true master! Thank you very much!\n")

input("\n\nPress the enter key to exit.")
    
