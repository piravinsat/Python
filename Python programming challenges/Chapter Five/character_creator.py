# Character Creater program
#
# The player spends 30 points to four different attributes: Strength, Health,
# Wisdom, and Dexterity. You spend and take points from/to the pool.

# set up inital values
pool = 30
strength = 0
health = 0
wisdom = 0
dexterity = 0

characters = []

choice = None
while choice != "0":

    print(
        """

        Character Creator

        0 - Quit
        1 - Display characters
        2 - Create character
        3 - Add points to attributes
        4 - Take points to pool
        """

        )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Good-bye.")
    # display characters
    elif choice == "1":
        print("Characters\n")
        print("NAME\tSTRENGTH\tHEALTH\tWISDOM\tDEXTERITY")
        for entry in characters:
            name, strength, health, wisdom, dexterity = entry
            print(name, "\t", strength, "\t", health, "\t", wisdom, "\t", dexterity)
    # create character
    elif choice == "2":
        name = input("What is the character's name?: ")
        print("With the pool of 30 points\n")
        pool = 30

        strength = int(input("How much do you want to spend on the STRENGTH attribute?: "))
        while strength > pool:
            print("Not enough points in the pool")
            strength = int(input("How much do you want to spend on the STRENGTH attribute?: "))
        pool = pool - strength
        
        health = int(input("How much do you want to spend on the HEALTH attribute?: "))
        while health > pool:
            print("Not enough points in the pool")
            health = int(input("How much do you want to spend on the HEALTH attribute?: "))
        pool = pool - health
    
        wisdom = int(input("How much do you want to spend on the WISDOM attribute?: "))
        while wisdom > pool:
            print("Not enough points in the pool")
            wisdom = int(input("How much do you want to spend on the WISDOM attribute?: "))
        pool = pool - wisdom
        
        dexterity = int(input("How much do you want to spend on the DEXTERITY attribute?: "))
        while dexterity > pool:
            print("Not enough points in the pool")
            dexterity = int(input("How much do you want to spend on the DEXTERITY attribute?: "))                                                      
        pool = pool - dexterity
        
        entry = [name, strength, health, wisdom, dexterity, pool]
        characters.append(entry)
    # add points to attribute
    elif choice == "3":
        i = 0
        answer = input("Enter the name of the character you want to access")
        for entry in characters:
            if entry[0] != answer:
                i = i + 1
            else:
                break
        pool = characters[i][5]
        points = int(input("How many points out of ", pool, " would like to add?: "))
        attribute = input("Where would like to add points to?: ")

        if attribute == "STRENGTH":
            characters[i][1] += points
            characters[i][5] -= points
        elif attribute == "HEALTH":
            characters[i][2] += points
            characters[i][5] -= points
        elif attribute == "WISDOM":
            characters[i][3] += points
            characters[i][5] -= points
        elif attribute == "DEXTERITY":
            characters[i][4] += points
            characters[i][5] -= points
    # take points to pool
    elif choice == "4":
        i = 0
        answer = input("Enter the name of the character you want to access")
        for entry in characters:
            if entry[0] != answer:
                i = i + 1
            else:
                break
        pool = characters[i][5]
        points = int(input("How many points would like to put back into the pool?: "))
        attribute = input("Where would you like to take points from?: ")

        if attribute == "STRENGTH":
            characters[i][1] -= points
            characters[i][5] += points
        elif attribute == "HEALTH":
            characters[i][2] -= points
            characters[i][5] += points
        elif attribute == "WISDOM":
            characters[i][3] -= points
            characters[i][5] += points
        elif attribute == "DEXTERITY":
            characters[i][4] -= points
            characters[i][5] += points

    # some unknown choice
    else:
        print("Sorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
        
                     
            

    
            
        
        
        
        
        
    
