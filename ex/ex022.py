# Basic of Python
# Project 1hour

# Title : Quiz(Data structure)
# Date : 2020-06-27
# Creator : tunealog

# Quiz) Create a draw program
#
# Rule1 : Number of ID is 20(1 ~ 20)
# Rule2 : The draw is random but doesn't permit duplication
# Rule3 : Use Shuffle and Sample in the random module
# Example 1 (Result):
# -------- Win --------
# Chicken : 1
# Coffee : [2, 3, 4]
# -- Congratulations --

# Example 2 (Package):
# from random import *
# first = [1, 2, 3, 4, 5]
# print(first)
# shuffle(first)
# print(first)
# print(sample(first, 1))

from random import *
iD = []
for i in range(20):
    iD.append(i+1)

chicken = sample(iD, 1)
c = chicken.pop()
iD.remove(c)
coffee = sample(iD, 3)
print("-------- Win --------")
print("Chicken : " + str(c))
print("Coffee : " + str(coffee))
print("-- Congratulations --")

# Feedback

# Create list
# iD = range(1, 21)
# print(type(iD))

# Change type(Range to List)
# iD = list(iD)

# Use Shuffle
# shuffle(iD)

# Pick Winners
# winners = sample(iD, 4)

# Formating
# print("Chicken : {0}".format(winners[0]))
# print("Coffee : {0}".format(winners[1:]))
