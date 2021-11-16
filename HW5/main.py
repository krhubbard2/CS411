# Kelby Hubbard
# Started: 2021-11-12
# Updated: 2021-11-12
# CS411 HW5 -- HW3 w/ card replacement
# main.py

# Main source file -- Solves for probabilities, return rates, payouts and prints return table

import texttable as tt # for use of texttable to print Return Table

from threecardpoker import (
    generate_replacement_hands,
    generate_total_hands,
    straight_flush,
    three_of_a_kind,
    straight,
    flush,
    pair,
)
from pokermodule import Deck, Hand, Card

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

c1 = Card(4, "Spades")
c2 = Card(12, "Diamonds")
c3 = Card(1, "Hearts")
hand = Hand(c1, c2, c3)
hand.print()

replacement_hands = generate_replacement_hands(hand, 1)
print(len(replacement_hands))
for i in range(len(replacement_hands)):
    replacement_hands[i].print()