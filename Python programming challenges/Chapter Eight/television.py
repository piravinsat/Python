# Television Simulator
# User can enter the channel number and change the volume

class Television(object):
    """A television."""
    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume

    def changeChannel(self, newChannel = 0):
        self.channel = newChannel
        print("Channel Number: ",  self.channel)

    def raiseVolume(self):
        self.volume += 1
        if self.volume > 100:
            self.volume = 100
        print("Volume: ", self.volume)

    def lowerVolume(self):
        self.volume -= 1
        if self.volume < 0:
            self.volume = 0
        print("Volume: ", self.volume)

def main():
    tele = Television()

    choice = None
    while choice != "0":
        print \
        ("""
        Television Simulator

        0 - Quit
        1 - Enter a channel number
        2 - Raise the volume
        3 - Lower the volume
        """)

        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Television switched off.")

        # enter a channel number
        elif choice == "1":
            ch = input("Enter a channel number: ")
            tele.changeChannel(ch)

        # raise the volume
        elif choice == "2":
            tele.raiseVolume()

        # lower the volume
        elif choice == "3":
            tele.lowerVolume()

        # some unknown choice
        else:
            print("\nSorry but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.")
