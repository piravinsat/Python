# Car Salesman Program
#
# Ask user to enter base price of car and then returns
# final price with extra fees added on

base = int(input("Enter the base price of car "))

tax = (base / 100) * 20

licence = (base / 100) * 7

dealerPrep = 124

destCharge = 43

actualPrice = base + tax + licence + dealerPrep + destCharge

print("\n\nThe final price is ", actualPrice)

input("\nPress the enter key to exit.")
