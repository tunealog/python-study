# Basic of Python
# Project 1hour

# Title : Data structure Exchange
# Date : 2020-06-26
# Creater : tunealog

menu = {"coffee", "juice", "milk"}

# {'juice', 'milk', 'coffee'} <class 'set'>
print(menu, type(menu))

# ['juice', 'milk', 'coffee'] <class 'list'>
menu = list(menu)
print(menu, type(menu))

# ('juice', 'milk', 'coffee') <class 'tuple'>
menu = tuple(menu)
print(menu, type(menu))

# {'juice', 'milk', 'coffee'} <class 'set'>
menu = set(menu)
print(menu, type(menu))
