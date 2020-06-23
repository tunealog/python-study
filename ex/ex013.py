# Basic of Python
# Project 1hour

# Title : Data Structure
# Date : 2020-06-23
# Creater : tunealog

# Fruit count program
fruit = ["apple", "apple", "banana", "banana",
         "kiwi", "orange", "orange", "orange"]

# Dictinary
d = {}

for f in fruit:
    if f in d:
        d[f] = d[f] + 1
    else:
        d[f] = 1

# {'apple': 2, 'banana': 2, 'kiwi': 1, 'orange': 3}
print(d)
