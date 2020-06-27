# Basic of Python
# Project 1hour

# Title : Tuple
# Date : 2020-06-22
# Creator : tunealog

# mutable vs immutable
# List vs Tuple

x = (1, 2, 3, 4)
y = ('a', 'b', 'c', 'd')
z = ("e", "fa", 5, 6)

#(1, 2, 3, 4)
print(x)

#('a', 'b', 'c', 'd')
print(y)

#('e', 'f', 5, 6)
print(z)

#(1, 2, 3, 4, 'a', 'b', 'c', 'd')
print(x + y)

# Tuple
a = (4, 2, 3, 1)

# len()
# 4
b = len(a)
print(b)

# sorted()
#(4, 2, 3, 1)
#[1, 2, 3, 4]
print(a)
c = sorted(a)
print(c)

# sum
# 10
d = sum(a)
print(d)

# For
# 4
# 2
# 3
# 1
for n in a:
    print(n)

# Index
# 3
print(a.index(1))

# In
# True
print(2 in a)

# False
print(5 in a)


# Advenced Tuple
# Added Date : 2020-06-26

# Tuple is fast than List, Dictionary
# Tuple is fixed(Can't fix)

# Tuple Example

(name, age, hobby) = "tunealog", 30, "Programing"
print(name, age, hobby)
