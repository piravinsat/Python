# Word Jumble
#
# The computer picks a random word and then "jumbles" it
# The player has to guess the original word
# IMPROVED version: can provide a hint to player
#                   scoring system

import random

# add a scoring system
SCORE = 20
SCOREWHINT = 10

playerScore = 0

# create a tuple with the word and its hint
PYTHON = ("python", "a type of snake")
JUMBLE = ("jumble", "to mix a confused way")
EASY = ("easy", "opposite of hard")
DIFFICULT = ("difficult", "another word for hard")
ANSWER = ("answer", "the response to the question")
XYLOPHONE = ("xylophone", "an instrument starting with x")

# create a sequence of words to choose from
WORDS = (PYTHON, JUMBLE, EASY, DIFFICULT, ANSWER, XYLOPHONE)

# pick one word randomly from the sequence
wordd = random.choice(WORDS)
word = wordd[0]

# create a variable to use later to see if the guess is correct
correct = word

# create a jumbled version of the word
jumble = ""

while word:
    # picks a random position (random letter from word)
    position = random.randrange(len(word))
    # adds letter to jumble
    jumble += word[position]
    # word minus one letter above
    word = word[:position] + word[(position + 1):]

# start the game
print(
"""

           Welcome to Word Jumble!


    Unscramble the letters to make a word.
(Press the enter key at the prompt to quit.)
"""

)

scoreGiven = SCORE
print("The jumble is:", jumble)

# getting the player's guess
askHint = input("Would like a hint? y or n\n")
if askHint == "y":
        print("The hint is ", wordd[1])
        scoreGiven = SCOREWHINT

guess = input("\nYour guess: ")
while guess != correct and guess != "":
    print("Sorry, that's not it.")
    
    guess = input("Your guess: ")

# congratulating the player
if guess == correct:
    print("That's it! You guessed it!\n")
    playerScore += scoreGiven
    print("Your score is ", playerScore)

print("Thanks for playing.")

input("\n\nPress the enter key to exit.")



    
    
    
