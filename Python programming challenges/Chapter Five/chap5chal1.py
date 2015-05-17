# Random sentence generator
#
# Prints a list of words in random order to make up a sentence.
# Prints all the words but doesn't repeat them.

import random

words = ["Mortimer", "and", "Randolph", "Duke", "are", "commodity", "brokers",
         "who", "enjoy", "a", "little", "wager", "now", "and", "then"]
sentence = []


# Loop until all the words are used
while len(words) > 0:
    selectedWord = random.choice(words)
    # Add to list called sentence
    sentence.append(selectedWord)
    # Then delete the selected word from list
    words.remove(selectedWord)

# Print sentence
for word in sentence:
    print(word)
