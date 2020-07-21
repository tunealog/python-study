# Basic of Python

# Title : Data Structure
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
