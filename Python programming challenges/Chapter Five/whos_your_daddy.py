# Who's your Daddy? program
#
# Lets the user enter the name of a male and produces the name of his father.

sonFather = {}

choice = None
while choice != "0":

    print(
    """

    Who's your Daddy?

    0 - Quit
    1 - Look up a Son-Father pair
    2 - Add a Son-Father pair
    3 - Replace a Son-Father pair
    4 - Delete a Son-Father pair
    """

    )

    choice = input("Choice: ")
    print()

    # exit
    if choice == "0":
        print("Goodbye!")

    # get a pair
    elif choice == "1":
        son = input("Who do you want me to look up for who their father is?: ")
        if son in sonFather:
            pair = sonFather[son]
            print("\n", son, "father is", pair)
        else:
            print("\nSorry, I don't know", son)

    # add a pair
    elif choice == "2":
        son = input("What son-father pair do you want to add?: ")
        if son not in sonFather:
            pair = input("\nWho's the father?: ")
            sonFather[son] = pair
            print("\n", son, "pair has been added.")
        else:
            print("\nThat son-father pair already exists! Try redefine it.")

    # redefine an existing pair
    elif choice == "3":
        son = input("What son-father pair do you want me to redefine?: ")
        if son in sonFather:
            pair = input("What's the new son-father pair?: ")
            sonFather[son] = pair
            print("\n", son, "pair has been redefined.")
        else:
            print("\nThat son-father pair doesn't exist! Try adding it.")

    # delete an existing pair
    elif choice == "4":
        son = input("What son-father pair do you want me to delete?: ")
        if son in sonFather:
            del sonFather[son]
            print("\nOkay, I deleted", term)
        else:
            print("\nI can't do that!", son, "pair doesn't exist.")

    # some unknown choice
    else:
        print("\nSorry, but", choice, "isn't a valid choice.")

input("\n\nPress the enter key to exit.")
            

    
        
        
