# Basic of Python

# Title : Quiz(Data Structures)
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
id = []
for i in range(20):
    id.append(i+1)

chicken = sample(id, 1)
c = chicken.pop()
id.remove(c)
coffee = sample(id, 3)
print("-------- Win --------")
print("Chicken : " + str(c))
print("Coffee : " + str(coffee))
print("-- Congratulations --")

# Feedback

# Create list
# id = range(1, 21)
# print(type(id))

# Change type(Range to List)
# id = list(id)

# Use Shuffle
# shuffle(id)

# Pick Winners
# winners = sample(id, 4)

# Formating
# print("Chicken : {0}".format(winners[0]))
# print("Coffee : {0}".format(winners[1:]))
