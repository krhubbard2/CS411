# Kelby Hubbard
# Started: 2021-11-12
# Updated: 2021-11-15
# CS411 HW5 -- HW3 w/ card replacement
# pokermodule.py

# Contains Classes needed for three card poker

from operator import attrgetter # for use of attrgetter in Hand.sort

# 4 suits (in alphabetical order)
suits = ["Clubs", "Diamonds", "Hearts", "Spades"]

# Card Class
# Contains card rank and suit -- also can print card value
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def print(self):
        # Ace
        if self.rank == 1:
            print("A of {}".format(self.suit))
        # Jack
        elif self.rank == 11:
            print("J of {}".format(self.suit))
        # Queen
        elif self.rank == 12:
            print("Q of {}".format(self.suit))
        # King
        elif self.rank == 13:
            print("K of {}".format(self.suit))
        # All other cases
        else:
            print("{} of {}".format(self.rank, self.suit))

    # Returns which place card would be in sorted Deck
    def cardPlace(self):
        if (self.suit == "Clubs"):
            return self.rank - 1
        elif (self.suit == "Diamonds"):
            return self.rank + 12
        elif (self.suit == "Hearts"):
            return self.rank + 25
        elif (self.suit == "Spades"):
            return self.rank + 38

# Hand Class
# Contains 3 Card objects -- automatically sorts then when initiated
# Sorts hand by rank (low to high) and then by suit (alphabetical)
class Hand:
    def __init__(self, c1, c2, c3):
        self.hand = [c1, c2, c3]
        self.sort()
    
    def sort(self):
        self.hand.sort(key = attrgetter('rank', 'suit'))

    # For use in Deck::remove
    def sortBySuit(self):
        self.hand.sort(key = attrgetter('suit', 'rank'))

    def print(self):
        print("Your hand contains:")
        self.hand[0].print()
        self.hand[1].print()
        self.hand[2].print()

# Deck Class
# Contains array of cards -- generates deck (52 cards) in order
class Deck:
    def __init__(self):
        self.cards = []
        self.generate()
    
    # Fills deck with 52 cards
    def generate(self):
        for suit in suits:
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))
    
    # Removes current hand from deck
    def remove(self, hand):
        hand.sortBySuit()
        for i in range(3):
            del self.cards[hand.hand[i].cardPlace() - i]
        hand.sort()
            
    def print(self):
        for c in self.cards:
            c.print()