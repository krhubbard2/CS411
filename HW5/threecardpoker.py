# Kelby Hubbard
# Started: 2021-11-12
# Updated: 2021-11-12
# CS411 HW5 -- HW3 w/ card replacement
# threecardpoker.py

# Contains total possible hand generation and hand analysis

from pokermodule import Hand, Deck

# Generate total amount of possible hands
# Hand contains 3 cards, no repeated cards, repeated hands in different order OK.
def generate_total_hands(deck):
    total_hands = []
    for i in range(52):
        for j in range(52):
            for k in range(52):
                if (i != j) and (j != k) and (i != k):
                    total_hands.append(Hand(deck.cards[i],deck.cards[j],deck.cards[k]))
    sum = len(total_hands)
    if sum != 132600: 
        raise ValueError("Error generating total number of hands")
    return total_hands

def generate_total_replacement_hands(hand):
    deck = Deck()
    deck.remove(hand)
    total_replacements = [hand]

    
    return

# Returns true if hand contains straight flush
# Straight Flush -- 3 suited in a sequence
def straight_flush(hand):
    if (straight(hand)) and (flush(hand)):
        return True
    return False

# Returns true if hand contains 3 of a kind
# 3 of a Kind -- 3 of the same rank
def three_of_a_kind(hand):
    if (hand.hand[0].rank == hand.hand[1].rank == hand.hand[2].rank):        
        return True
    return False

# Returns true if hand contains a straight
# Straight -- 3 in sequence (includes AKQ)
def straight(hand):
    # In the case of AKQ
    if (hand.hand[0].rank == 1 and hand.hand[1].rank == 12 and hand.hand[2].rank == 13):
        return True
    if (hand.hand[0].rank == hand.hand[1].rank - 1 and hand.hand[0].rank == hand.hand[2].rank - 2):
        return True
    return False

# Returns true if hand contains flush
# Flush -- 3 cards of same suit
def flush(hand):
    if (hand.hand[0].suit == hand.hand[1].suit == hand.hand[2].suit):
        return True
    return False

# Returns true if hand contains pair
# Pair -- 2 cards of same rank
def pair(hand):
    if (hand.hand[0].rank == hand.hand[1].rank or hand.hand[0].rank == hand.hand[2].rank or hand.hand[1].rank == hand.hand[2].rank):
        return True
    return False

