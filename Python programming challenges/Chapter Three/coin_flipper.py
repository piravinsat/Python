# Coin flipper simulator
#
# Flips a coin 100 times and then
# displays the number of heads and tails.

import random

print("\tWelcome to 'Coin Flipper'!")

# initalise values
randomNum = 0
heads = 0
tails = 0
counter = 0

# Loop through
while counter < 100:
    if randomNum == 0:
        heads += 1
    else:
        tails += 1

    counter += 1
    randomNum = random.randrange(2)

# Display heads and tails
print("\nThe number of heads is ", heads, "and number of tails is ", tails)

input("\n\nPress the enter key to exit.")
