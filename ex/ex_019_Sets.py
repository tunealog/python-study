# Basic of Python

# Title : Sets
# Date : 2020-06-26
# Creator : tunealog

# Set Examples
my_set = {1, 2, 2, 3, 3, 3}

# {1, 2, 3}
print(my_set)

java = {"James", "Tom", "Bill"}
python = set(["Rose", "James"])

# {'James'}
print(java & python)
# {'James'}
print(java.intersection(python))

# {'Tom', 'James', 'Rose', 'Bill'}
print(java | python)
# {'Tom', 'James', 'Rose', 'Bill'}
print(java.union(python))

# {'Tom', 'Bill'}
print(java - python)
# {'Tom', 'Bill'}
print(java.difference(python))

# {'James', 'Rose', 'Paul'}
python.add("Paul")
print(python)

# {'James', 'Rose'}
python.remove("Paul")
print(python)
