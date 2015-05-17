# One-card War
# Each player gets a single card and the highest card wins

import cards, games

class W_Card(cards.Card):
    """ A war Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = W_Card.RANKS.index(self.rank) + 1
        else:
            v = None
        return v

class W_Deck(cards.Deck):
    """ A war Deck. """
    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))

class W_Hand(cards.Hand):
    """ A war Hand. """
    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(W_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        t = 0
        for card in self.cards:
            t = card.value

        return t

class W_Player(W_Hand):
    """ A war Player. """

    def lose(self):
        print(self.name, "loses.")

    def win(self):
        print(self.name, "wins.")

class W_Game(object):
    """ A war Game. """
    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)

        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    def play(self):
        # deal one card to everyone
        self.deck.deal(self.players, per_hand = 1)
        for player in self.players:
            print(player)

        i = 0
        highest_total = 0

        for player in self.players:
            if player.total > highest_total:
                highest_total = player.total
                highest_player = i
                i = i + 1

        self.players[i-1].win()
        # remove everyone's cards
        for player in self.players:
            player.clear()

def main():
    print("\t\tWelcome to one-card War! \n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ",
                              low = 1, high = 8)

    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)

    print()

    game = W_Game(names)

    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nDo you want to play again? ")

main()
input("\n\nPress the enter key to exit.")
            
        
            
