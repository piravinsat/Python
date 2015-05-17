# Tipper program
#
# Asks user to enter bill total and then
# returns 15% and 20% percent tip.

bill = float(
        input("Enter your restaurant bill total? "))

print("\n\nA 15% tip is ", (bill/100)*15)
print("\nA 20% tip is ", (bill/100)*20)

input("\n\nPress enter to exit.")

