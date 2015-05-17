# Blackjack 2
# From 1 to 7 players compete against a dealer
# UPDATED: Allowing players to bet

import cards, games

class BJ_Card(cards.Card):
    """ A Blackjack Card. """
    ACE_VALUE = 1

    @property
    def value(self):
        if self.is_face_up:
            v = BJ_Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v

class BJ_Deck(cards.Deck):
    """ A Blackjack Deck. """
    def populate(self):
        for suit in BJ_Card.SUITS:
            for rank in BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Deck empty. Reshuffling deck.")
                    self.populate()
                    self.shuffle()


class BJ_Hand(cards.Hand):
    """ A Blackjack Hand. """
    def __init__(self, name):
        super(BJ_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
        return rep

    @property
    def total(self):
        # if a card in the hand has value of None, then total is None
        for card in self.cards:
            if not card.value:
                return None

        # add up card values, treat each Ace as 1
        t = 0
        for card in self.cards:
              t += card.value

        # determine if hand contains an Ace
        contains_ace = False
        for card in self.cards:
            if card.value == BJ_Card.ACE_VALUE:
                contains_ace = True

        # if hand contains Ace and total is low enough, treat Ace as 11
        if contains_ace and t <= 11:
            # add only 10 since we've already added 1 for the Ace
            t += 10

        return t

    def is_busted(self):
        return self.total > 21


class BJ_Player(BJ_Hand):
    """ A Blackjack Player. """
    bankroll = 50000
    wager = 0
    lost = False
    won = False
    pushed = False
    isBetting = False

    def __str__(self):
        rep = self.name + ":\t" + super(BJ_Hand, self).__str__()
        if self.total:
            rep += "(" + str(self.total) + ")" + " Bankroll: £" + str(self.bankroll)
        if self.is_betting:
            rep += " Wager: £" + str(self.wager)
        return rep

    def is_bankrupt(self):
        return self.bankroll == 0

    def is_hitting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want a hit? (Y/N): ")
        return response == "y"

    def is_betting(self):
        response = games.ask_yes_no("\n" + self.name + ", do you want to bet? (Y/N): ")
        return response == "y"

    def bet(self):
        response = games.ask_number("\n" + self.name + ", how much do you want to bet? : ", 0, self.bankroll + 1)
        self.wager = response
        # Remove bet from the bankroll
        self.bankroll -= response
        return response

    def bust(self):
        print(self.name, "busts.")
        self.lose()

    def lose(self):
        print(self.name, "loses.")
        self.lost = True

    def win(self):
        print(self.name, "wins.")
        self.won = True

    def push(self):
        print(self.name, "pushes.")
        self.pushed = True


class BJ_Dealer(BJ_Hand):
    """ A Blackjack Dealer. """
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "busts.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()


class BJ_Game(object):
    """ A Blackjack Game. """

    def __init__(self, names):
        self.players = []
        for name in names:
            player = BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer("Dealer")

        self.deck = BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def remove_players(self):
        bp = []
        for player in self.players:
            if not player.is_bankrupt():
                bp.append(player)
        return bp

    def players_left(self):
        return len(self.players) > 0

    def play(self):
        pot = 0
        numPlayersWon = 0

        # deal initial 2 cards to everyone
        self.deck.deal(self.players + [self.dealer], per_hand = 2)
        self.dealer.flip_first_card()    # hide dealer's first card
        for player in self.players:
            print(player)
        print(self.dealer)

        # Asks players if they want to bet
        for player in self.players:
            if player.is_betting():
                # All bets added to the pot
                player.isBetting = True
                player.bet()
                pot += player.wager

        # deal additional cards to players
        for player in self.players:
            self.__additional_cards(player)

        self.dealer.flip_first_card()    # reveal dealer's first

        if not self.still_playing:
            # since all players have busted, just show the dealer's hand
            print(self.dealer)
        else:
            # deal additional cards to dealer
            print(self.dealer)
            self.__additional_cards(self.dealer)

            if self.dealer.is_busted():
                # everyone still playing wins
                for player in self.still_playing:
                    player.win()
            else:
                # compare each player still playing to dealer
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()

        # distribute pot among players who pushed
        for player in self.players:
            if player.pushed and player.isBetting:
                player.bankroll += player.wager
                pot -= player.wager
            if player.won and player.isBetting:
                numPlayersWon += 1

        # divide and distribute among players who won
        for player in self.players:
            if player.won and player.isBetting:
                player.bankroll += int(pot/numPlayersWon)

        # remove everyone's cards
        for player in self.players:
            player.clear()
        self.dealer.clear()

        # remove wager
        for player in self.players:
            player.wager = 0

        # Remove bankrupted players
        self.players = self.remove_players()

def main():
    print("\t\tWelcome to Blackjack!\n")

    names = []
    number = games.ask_number("How many players? (1 - 7): ", low = 1, high = 8)
    for i in range(number):
        name = input("Enter player name: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":

        game.play()
        if game.players_left():
            again = games.ask_yes_no("\nDo you want to play again?: ")
        else:
            again = "n"


main()
input("\n\nPress the enter key to exit.")



