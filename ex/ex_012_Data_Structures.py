# Basic of Python

# Title : Data Structures
# Date : 2020-06-23
# Creator : tunealog

# Fruit Count
list_fruit = ["apple", "apple", "banana", "banana",
              "kiwi", "orange", "orange", "orange"]

# Dictinary
dict_empty = {}

for fruit in list_fruit:
    if fruit in dict_empty:
        dict_empty[fruit] = dict_empty[fruit] + 1
    else:
        dict_empty[fruit] = 1

# {'apple': 2, 'banana': 2, 'kiwi': 1, 'orange': 3}
print(dict_empty)


# Data Structures Add
# Added Date : 2020-06-26
###################################################
############# set > list > tuple > set ############
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
###################################################
