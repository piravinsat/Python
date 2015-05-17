# Counter program
# Counts from one number to the other and what by
# Sets by the user

print("Welcome to the counter program!\n\n")

startNum = int(input("Starting number: "))
endNum = int(input("\nEnding number: "))
byNum = int(input("\nBy what number: "))

for i in range(startNum, endNum, byNum):
    print(i, end=" ")

input("\n\nPress the enter key to exit.")
