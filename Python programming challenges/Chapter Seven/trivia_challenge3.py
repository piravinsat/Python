# Trivia Challenge
# Trivia game that reads a plain text file
# ADDED: High-score list

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

    # Open the new file to store the pickled lists.
    f = open("pickles1.dat", "rb")
    high_score = pickle.load(f)
    f.close()

    # Check the high score list for the lowest score
    # If the new score is higher then add to the list at the correct list
    high_score.append(player)
    # Sort the list
    high_score.sort(reverse=True)
    high_score = high_score[:10] # keep only top 10 scores

    f = open("pickles1.dat", "wb")
    pickle.dump(high_score, f)
    f.close()

    print("High Scores\n")
    print("NAME\tSCORE")
    for entry in high_score:
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
    
