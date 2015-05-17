# Trivia Challenge
# Trivia game that reads a plain text file
# CHANGED: High-score list using plain text instead

import sys, pickle, shelve

def open_file(file_name, mode):
    """Open a file."""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Unable to open the file", file_name, "Ending program.\n", e)
        input("\n\nPress the enter key to exit.")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    """Return next line from the trivia file, formatted."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line

def next_block(the_file):
    """Return the next block of data from the trivia file."""
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)

    points = next_line(the_file)
    
    return category, question, answers, correct, explanation, points

def welcome(name, title):
    """Welcome the player and get his/her name."""
    print("\t\tWelcome to Trivia Challenge,", name,"!\n")
    print("\t\t", title, "\n")

def high_score(player):
    """Maintain a high score list into a pickled object."""
    high_scores = []

    text_file = open("write_it.txt", "r")
    for line in text_file:
        score = line
        name = text_file.readline()
        high_scores.append((score, name))
    text_file.close()

    high_scores.append(player)
    high_scores.sort(reverse=True)
    high_scores = high_scores[:10]

    text_file = open("write.it.txt","w")
    i = 0
    length = len(high_scores)
    
    while i < length:
        j = 0
        while j < 2:
            text_file.write(str(high_scores[i][j]))
            j = j + 1
        i = i + 1
    text_file.close()

    print("High Scores\n")
    print("NAME\tSCORE")
    for entry in high_scores:
        score,name = entry
        print(name, "\t", score)

def main():
    trivia_file = open_file("trivia.txt", "r")
    title = next_line(trivia_file)
    name = input("What's your name?: ")
    welcome(name, title)
    score = 0

    # get first block
    category, question, answers, correct, explanation, points = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])

        # get answer
        answer = input("What's your answer?: ")

        # check answer
        if answer == correct:
            print("\nRight!", end=" ")
            score += int(points)
        else:
            print("\nWrong.", end=" ")
        print(explanation)
        print("Score:", score, "\n\n")

        # get next block
        category, question, answers, correct, explanation, points = next_block(trivia_file)

    trivia_file.close()

    print("That was the last question!")
    print("Your final score is", score)

    # Get the high score list
    player = (score, name)
    high_score(player)

main()
input("\n\nPress the enter key to exit.")
    
