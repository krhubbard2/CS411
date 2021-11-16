# Kelby Hubbard
# Started: 2021-11-12
# Updated: 2021-11-15
# CS411 HW5 -- HW3 w/ card replacement
# main.py

# Main source file -- Solves for probabilities, return rates, payouts and prints return table

import texttable as tt # for use of texttable to print Return Table

from pokermodule import Deck, Hand, Card
from threecardpoker import * 

def bidGrab():
    bid = "Wrong"
    while bid.isdigit() == False:
        bid = input("Please enter bid amount (integers only): ")

        if bid.isdigit() == False:
            print("Incorrect entry. Try again: ")
        else:
            return int(bid)

bidAmount = bidGrab()

'''
################################################################################
########## HOMEWORK 3 ##########################################################
################################################################################
'''

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
# Generate total hands possible
total_hands = generate_total_hands(deck)
totalHandCount = len(total_hands)

print("Computing ORIGINAL Probability and Return Table based on a bid amount of ${}.".format(bidAmount))

# Straight Flush
totalSF = frequencySF(total_hands)
straightFlushProbability = probability(totalSF, totalHandCount)
straightFlushReturn = returnRate(straightFlushProbability, straightFlushPayout, bidAmount)

# 3 of a kind
total3 = frequency3K(total_hands)
threeKindProbability = probability(total3, totalHandCount)
threeKindReturn = returnRate(threeKindProbability, threeKindPayout, bidAmount)

# Straight
totalStraight = frequencyS(total_hands)
totalStraight -= totalSF
straightProbability = probability(totalStraight, totalHandCount)
straightReturn = returnRate(straightProbability, straightPayout, bidAmount)

# Flush
totalFlush = frequencyF(total_hands)
totalFlush -= totalSF
flushProbability = probability(totalFlush, totalHandCount)
flushReturn = returnRate(flushProbability, flushPayout, bidAmount)

# Pairs
totalPair = frequencyP(total_hands)
totalPair -= total3
pairProbability = probability(totalPair, totalHandCount)
pairReturn = returnRate(pairProbability, pairPayout, bidAmount)

# High Card (all remaining hands after removal of higher scoring hands)
totalHigh = frequencyH(total_hands, totalSF, total3, totalStraight, totalFlush, totalPair)
highProbability = probability(totalHigh, totalHandCount)
highReturn = returnRate(highProbability, highPayout, bidAmount)

# Total Return % = All returns added together
totalRet = totalReturn(straightFlushReturn, threeKindReturn, straightReturn, flushReturn, pairReturn, highReturn, bidAmount)

# ORIGINAL Return Table *HW3* (using texttable)
tab = tt.Texttable()
headings = ['Hand','Frequency','Probability','Payout (in $)','Return']
tab.header(headings)
handsTable = ['Straight Flush', 'Three of a Kind', 'Straight', 'Flush', 'Pair', 'High Card', 'Total']
freq = [totalSF, total3, totalStraight, totalFlush, totalPair, totalHigh, totalHandCount]
prob = [straightFlushProbability, threeKindProbability, straightProbability, flushProbability, pairProbability, highProbability, '100.00']
payout = [straightFlushPayout, threeKindPayout, straightPayout, flushPayout, pairPayout, highPayout, '']
returns = [straightFlushReturn, threeKindReturn, straightReturn, flushReturn, pairReturn, highReturn, totalRet]

tab.set_precision(4) # Probability differes to the 4th decimal place
for row in zip(handsTable,freq,prob,payout,returns):
    tab.add_row(row)

s = tab.draw()
print (s)


'''
################################################################################
########## HOMEWORK 5 ##########################################################
################################################################################
'''

# Payout amounts (in dollars)
straightFlushSwapPayout = 18 * bidAmount
threeKindSwapPayout = 12 * bidAmount
straightSwapPayout = 5 * bidAmount
flushSwapPayout = 3 * bidAmount
pairSwapPayout = 1 * bidAmount
highSwapPayout = 0

print("Computing HW5 Probability and Return Table based on a bid amount of ${} with the one card swap allowed and perfect play assumed.".format(bidAmount))

print("Generating all hands possible with perfect swap.")
total_hands_with_swap = generate_total_hands_with_perfect_play(deck, payoutList, bidAmount)
totalHandSwapCount = len(total_hands_with_swap)

# Straight Flush with perfect play
totalSwapSF = frequencySF(total_hands_with_swap)
straightFlushSwapProbability = probability(totalSwapSF, totalHandSwapCount)
straightFlushSwapReturn = returnRate(straightFlushSwapProbability, straightFlushSwapPayout, bidAmount)


# 3 of a kind with perfect play
totalSwap3 = frequency3K(total_hands_with_swap)
threeKindSwapProbability = probability(totalSwap3, totalHandSwapCount)
threeKindSwapReturn = returnRate(threeKindSwapProbability, threeKindSwapPayout, bidAmount)

# # Straight with perfect play
totalSwapStraight = frequencyS(total_hands_with_swap)
totalSwapStraight -= totalSwapSF
straightSwapProbability = probability(totalSwapStraight, totalHandSwapCount)
straightSwapReturn = returnRate(straightSwapProbability, straightSwapPayout, bidAmount)

# # Flush with perfect play
totalSwapFlush = frequencyF(total_hands_with_swap)
totalSwapFlush -= totalSwapSF
flushSwapProbability = probability(totalSwapFlush, totalHandSwapCount)
flushSwapReturn = returnRate(flushSwapProbability, flushSwapPayout, bidAmount)

# # Pairs with perfect play
totalSwapPair = frequencyP(total_hands_with_swap)
totalSwapPair -= total3
pairSwapProbability = probability(totalSwapPair, totalHandSwapCount)
pairSwapReturn = returnRate(pairSwapProbability, pairSwapPayout, bidAmount)

# High Card (all remaining hands after removal of higher scoring hands) with perfect play
totalSwapHigh = frequencyH(total_hands_with_swap, totalSwapSF, totalSwap3, totalSwapStraight, totalSwapFlush, totalSwapPair)
highSwapProbability = probability(totalSwapHigh, totalHandSwapCount)
highSwapReturn = returnRate(highSwapProbability, highSwapPayout, bidAmount)

# Total Return % = All returns added together
totalSwapRet = totalReturn(straightFlushSwapReturn, threeKindSwapReturn, straightSwapReturn, flushSwapReturn, pairSwapReturn, highSwapReturn, bidAmount)

# Return Table with perfect play (using texttable)
tabSwap = tt.Texttable()
headings = ['Hand','Frequency','Probability','Payout (in $)','Return']
tabSwap.header(headings)
freqSwap = [totalSwapSF, totalSwap3, totalSwapStraight, totalSwapFlush, totalSwapPair, totalSwapHigh, totalHandSwapCount]
probSwap = [straightFlushSwapProbability, threeKindSwapProbability, straightSwapProbability, flushSwapProbability, pairSwapProbability, highSwapProbability, '100.00']
returnsSwap = [straightFlushSwapReturn, threeKindSwapReturn, straightSwapReturn, flushSwapReturn, pairSwapReturn, highSwapReturn, totalSwapRet]
payoutSwap = [straightFlushSwapPayout, threeKindSwapPayout, straightSwapPayout, flushSwapPayout, pairSwapPayout, highSwapPayout, '']

tabSwap.set_precision(4) # Probability differes to the 4th decimal place
for row in zip(handsTable,freqSwap,probSwap,payoutSwap,returnsSwap):
    tabSwap.add_row(row)


s1 = tabSwap.draw()
print (s1)