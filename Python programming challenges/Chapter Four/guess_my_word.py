# Guess my word
#
# Computer picks a random word and
# the player has to guess that word

import random

WORDS = ("python", "jumble", "easiest", "difficult", "answer", "xylophone")
word = random.choice(WORDS)

# Tells how many letters are in the word.
numLetters = len(word)
print("There are ", numLetters, " letters in the word.\n")

# Player is given five chances to ask if a letter is in word.
for i in range(0,5):
    letter = input("Enter a letter you want to check is in a word.\n")
    if letter in word:
        print("YES!\n")
    else:
        print("NO!\n")
    i = i - 1
        
# Player now guesses word

guess = input("Enter your guess.\n")
if guess == word:
    print("That's correct. Well done duder!")
else:
    print("Sorry that's wrong. Better luck next time.")
        
