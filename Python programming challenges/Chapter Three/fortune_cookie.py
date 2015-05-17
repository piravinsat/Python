# Fortune Cookie Simulator
#
# Displays one of five unique fortunes at random

import random

print("\tWelcome to 'Fortune Cookie Simulator'!")
print("\nHere's your fortune....\n")

# initalise values
randomNum = random.randrange(5)

# randomise fortunes
if randomNum == 0:
    print("The man or woman you desire feels the same about you.")
elif randomNum == 1:
    print("Meeting adversity well is the source of your strength.")
elif randomNum == 2:
    print("Never give up. You're not a failure if you don't give up.")
elif randomNum == 3:
    print("You will become great if you believe in yourself.")
else:
    print("The greatest risk is not taking one.")

input("\n\nPress the enter key to exit.")

