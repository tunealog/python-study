# Basic of Python
# Project 1hour

# Title : Set
# Date : 2020-06-26
# Creater : tunealog

# Set Example
my_set = {1, 2, 2, 3, 3, 3}

# {1, 2, 3}
print(my_set)

java = {"James", "Tom", "Bill"}
python = set(["Rose", "James"])

# {'James'}
print(java & python)
print(java.intersection(python))

# {'Tom', 'James', 'Rose', 'Bill'}
print(java | python)
print(java.union(python))

# {'Tom', 'Bill'}
print(java - python)
print(java.difference(python))

# {'James', 'Rose', 'Paul'}
python.add("Paul")
print(python)

# {'James', 'Rose'}
python.remove("Paul")
print(python)
