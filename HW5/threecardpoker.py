# Kelby Hubbard
# Started: 2021-11-12
# Updated: 2021-11-15
# CS411 HW5 -- HW3 w/ card replacement
# threecardpoker.py

# Contains total possible hand generation and hand analysis

from pokermodule import Hand, Deck

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

# Computes probability (Outcomes / Total Outcomes)
def probability(outcomes, totalOutcomes):
    prob = outcomes / totalOutcomes
    return prob

# Computes return rate (Payout * Probability)
def returnRate(probability, payout, bidAmount):
    rate = (payout * probability) / bidAmount
    return rate

def frequencySF(total_hands):
    totalSF = 0
    for i in range(len(total_hands)):
        if straight_flush(total_hands[i]) == True:
            totalSF += 1
    return totalSF

def frequency3K(total_hands):
    total3 = 0
    for i in range(len(total_hands)):
        if three_of_a_kind(total_hands[i]) == True:
            total3 += 1
    return total3

def frequencyS(total_hands):
    totalStraight = 0
    for i in range(len(total_hands)):
        if straight(total_hands[i]) == True:
            totalStraight += 1
    return totalStraight

def frequencyF(total_hands):
    totalFlush = 0
    for i in range(len(total_hands)):
        if flush(total_hands[i]) == True:
            totalFlush += 1
    return totalFlush

def frequencyP(total_hands):
    totalPair = 0
    for i in range(len(total_hands)):
        if pair(total_hands[i]) == True:
            totalPair += 1
    return totalPair

# High Card (all remaining hands after removal of higher scoring hands)   
def frequencyH(total_hands, freqSF, freq3K, freqS, freqF, freqP):
    totalHigh = len(total_hands)
    totalHigh -= freqSF + freq3K + freqS + freqF + freqP
    return totalHigh

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

def generate_replacement_hands(hand, cardPos):
    deck = Deck()
    deck.remove(hand)
    replacement_hands = []
    for i in range(49):
        # Replacing card 1
        if cardPos == 1:
            replacement_hands.append(Hand(deck.cards[i], hand.hand[1], hand.hand[2]))
        # Replacing card 2
        if cardPos == 2:
            replacement_hands.append(Hand(hand.hand[0], deck.cards[i], hand.hand[2]))
        # Replacing card 3
        if cardPos == 3:
            replacement_hands.append(Hand(hand.hand[0]. hand.hand[1], deck.cards[i]))
    return replacement_hands

def determinePerfectPlay(hand):

    return