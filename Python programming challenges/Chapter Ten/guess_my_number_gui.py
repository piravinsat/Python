# Guess My Number game (GUI Version)
#
# The computer picks a random number between 1 and 100
# The player tries to guess it and the computer lets
# the player know if the guess is too high, too low
# or right on the money

from tkinter import *
import random

theNumber = random.randint(1,100)
tries = 0

class Application(Frame):
    """ GUI application that embeds the Guess My Number game. """
    def __init__(self, master):
        """ Initialise Frame. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create widgets to get number and to display messages. """
        # create title label
        Label(self,
              text = "Welcome to 'Guess My Number'!"
              ).grid(row = 0, column = 0, columnspan = 2, sticky = W)

        # create number label
        Label(self,
              text = "I'm thinking of a number between 1 and 100."
              ).grid(row = 1, column = 0, columnspan = 2, sticky = W)

        # create instruction label
        Label(self,
              text = "Try to guess it in as few attempts as possible."
              ).grid(row = 2, column = 0, columnspan = 2, sticky = W)

        # create a label and text entry for guesses
        Label(self,
              text = "Guess:"
              ).grid(row = 4, column = 0, sticky = W)
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 4, column = 1, sticky = W)

        # create a submit button
        Button(self,
               text = "OK",
               command = self.game
               ).grid(row = 5, column = 0, sticky = W)

        self.game_txt = Text(self, width = 75, height = 10, wrap = WORD)
        self.game_txt.grid(row = 6, column = 0, columnspan = 4)

    def game(self):
        """Fill text box with message based on the guess input. """

        # set the initial values
        limit = 6
        global tries
        global theNumber
        print(theNumber)
        
        # get values from the GUI
        guess = int(self.guess_ent.get())

        if guess > theNumber:
            # Fill text box with "Lower"
            message = "LOWER"      
            self.game_txt.delete(0.0, END)
            self.game_txt.insert(0.0, message)
            tries += 1
            print(tries)
        elif guess < theNumber:
            # Fill text box with "Higher"
            message = "HIGHER"
            self.game_txt.delete(0.0, END)
            self.game_txt.insert(0.0, message)
            tries += 1
            print(tries)

        # congratulating the player
        # Fill text box with a "You guessed it!", the number of tries
        # and the number
        elif guess == theNumber and tries < limit:
            message = "You guessed it! The number of tries is "
            message += str(tries)

            self.game_txt.delete(0.0, END)
            self.game_txt.insert(0.0, message)

        else:
            message = "Run out of tries, sorry!"

            self.game_txt.delete(0.0, END)
            self.game_txt.insert(0.0, message)

# main
root = Tk()
root.title("Guess My Number")
app = Application(root)
root.mainloop()
