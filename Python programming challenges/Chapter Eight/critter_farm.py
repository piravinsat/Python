# Critter Farm
# A farm of virtual pets to care for

import random

class Critter(object):
    """A virtual pet."""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom 
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m

    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")

    def eat(self, food = 4):
        print("Brruppp. Thank you.")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun = 4):
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        print("Name: ", self.name)
        print("Hunger: ", self.hunger)
        print("Boredom: ", self.boredom)

def main():
    farm = []

    for i in range(5):
        crit_name = input("What do you want to name your critter?: ")
        crit = Critter(crit_name, random.randint(0,10), random.randint(0,10))
        farm.append(crit)

    choice = None
    while choice != "0":
        print \
        ("""
        Critter Farm

        0 - Quit
        1 - Listen to all of the critters
        2 - Feed all of the critters
        3 - Play with all of the critters
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to all of the critters
        elif choice == "1":
            for crit in farm:
                crit.talk()

        # feed all of the critters
        elif choice == "2":
            for crit in farm:
                feedAmount = input("How much food do you want to feed the critters?: ")
                crit.eat(int(feedAmount))

        # play with all of the critters
        elif choice == "3":
            for crit in farm:
                playAmount = input("How long do you want to play with the critter?: ")
                crit.play(int(playAmount))

        # secret selection: exact values of object attributes
        elif choice == "99":
            for crit in farm:
                crit.__str__()

        # some unknown choice
        else:
            print("\nSorry but", choice, "isn't a valid choice.")
            
main()
("\n\nPress the enter key to exit.")
    
