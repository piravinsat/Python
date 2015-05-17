# Backwards
# Prints a given message backwards

print("Welcome to the backwards program!\n")

message = input("Enter your message ")
egassem = ""
position = len(message)

for position in range(position+1, 0, -1):
    egassem += message[position-1:position]

print("The backwards message is", egassem)

input("\n\nPress the enter key to exit.")
    
