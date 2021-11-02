# Kelby Hubbard
# Started: 2021-10-09
# Updated: 2021-10-15
# CS411 HW3
# threecardpoker.py

from operator import attrgetter # for use of attrgetter in Hand.sort
import texttable as tt # for use of texttable to print Return Table

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


# Hand Class
# Contains 3 Card objects -- automatically sorts then when initiated
# Sorts hand by rank (low to high) and then by suit (alphabetical)
class Hand:
    def __init__(self, c1, c2, c3):
        self.hand = [c1, c2, c3]
        self.sort()
    
    def sort(self):
        self.hand.sort(key = attrgetter('rank', 'suit'))

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
    
    def generate(self):
        for suit in suits:
            for rank in range(1,14):
                self.cards.append(Card(rank,suit))
    
    def print(self):
        for c in self.cards:
            c.print()

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

def bidGrab():
    bid = "Wrong"

    while bid.isdigit() == False:
        bid = input("Please enter bid amount (integers only): ")

        if bid.isdigit() == False:
            print("Incorrect entry. Try again: ")
        else:
            return int(bid)

bidAmount = bidGrab()

# Payout amounts (in dollars)
straightFlushPayout = 35 * bidAmount
threeKindPayout = 17 * bidAmount
straightPayout = 9 * bidAmount
flushPayout = 5 * bidAmount
pairPayout = 2 * bidAmount
highPayout = 0
payoutList = [straightFlushPayout, threeKindPayout, straightPayout, flushPayout,pairPayout, highPayout]

# Generate Deck
deck = Deck()
print("Generating all possible hands")
# Generate total hands possible
total_hands = generate_total_hands(deck)
totalHandCount = len(total_hands)

print("Computing Probability and Return Table based on a bid amount of ${}.".format(bidAmount))

# Straight Flush
totalSF = 0
for i in range(totalHandCount):
    if straight_flush(total_hands[i]) == True:
        totalSF += 1
straightFlushProbability = probability(totalSF, totalHandCount)
straightFlushReturn = returnRate(straightFlushProbability, straightFlushPayout, bidAmount)

# 3 of a kind
total3 = 0
for i in range(totalHandCount):
    if three_of_a_kind(total_hands[i]) == True:
        total3 += 1
threeKindProbability = probability(total3, totalHandCount)
threeKindReturn = returnRate(threeKindProbability, threeKindPayout, bidAmount)

# Straight
totalStraight = 0
for i in range(totalHandCount):
    if straight(total_hands[i]) == True:
        totalStraight += 1
totalStraight -= totalSF
straightProbability = probability(totalStraight, totalHandCount)
straightReturn = returnRate(straightProbability, straightPayout, bidAmount)

# Flush
totalFlush = 0
for i in range(totalHandCount):
    if flush(total_hands[i]) == True:
        totalFlush += 1
totalFlush -= totalSF
flushProbability = probability(totalFlush, totalHandCount)
flushReturn = returnRate(flushProbability, flushPayout, bidAmount)

# Pairs
totalPair = 0
for n in range(totalHandCount):
    if pair(total_hands[n]) == True:
        totalPair += 1
totalPair -= total3
pairProbability = probability(totalPair, totalHandCount)
pairReturn = returnRate(pairProbability, pairPayout, bidAmount)

# High Card (all remaining hands after removal of higher scoring hands)
totalHigh = 132600
totalHigh -= totalSF + total3 + totalStraight + totalFlush + totalPair
highProbability = probability(totalHigh, totalHandCount)
highReturn = returnRate(highProbability, highPayout, bidAmount)

# Total Return % = All returns added together
totalReturn = (((straightFlushReturn + threeKindReturn + straightReturn + flushReturn + pairReturn + highReturn) / bidAmount) * 100) * bidAmount
# print("Total Return: {}%".format(totalReturn))

# Return Table (using texttable)
tab = tt.Texttable()
headings = ['Hand','Frequency','Probability','Payout (in $)','Return']
tab.header(headings)
handsTable = ['Straight Flush', 'Three of a Kind', 'Straight', 'Flush', 'Pair', 'High Card', 'Total']
freq = [totalSF, total3, totalStraight, totalFlush, totalPair, totalHigh, totalHandCount]
prob = [straightFlushProbability, threeKindProbability, straightProbability, flushProbability, pairProbability, highProbability, '100.00']
payout = [straightFlushPayout, threeKindPayout, straightPayout, flushPayout, pairPayout, highPayout, '']
returns = [straightFlushReturn, threeKindReturn, straightReturn, flushReturn, pairReturn, highReturn, totalReturn]

tab.set_precision(4) # Probability differes to the 4th decimal place
for row in zip(handsTable,freq,prob,payout,returns):
    tab.add_row(row)

s = tab.draw()
print (s)

# FIXME: Maybe have hand return what the win is?
def handPayout(hand, payoutList):
    payoutAmount = 0
    if (straight_flush(hand)):
        payoutAmount = payoutList[0]
    elif (three_of_a_kind(hand)):
        payoutAmount = payoutList[1]
    elif (straight_flush(hand)):
        payoutAmount = payoutList[2]
    elif (straight(hand)):
        payoutAmount = payoutList[3]
    elif (flush(hand)):
        payoutAmount = payoutList[4]
    elif (pair(hand)):
        payoutAmount = payoutList[5]
    else:
        payoutAmount = 0
    return payoutAmount

hand3 = Hand(Card(1, "Clubs"), Card(1, "Spades"), Card(1, "Hearts"))
hand3.print()
print("Your hand payout based on your bid of ${} is ${}".format(bidAmount, handPayout(hand3, payoutList)))
