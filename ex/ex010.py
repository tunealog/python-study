# Basic of Python
# Project 1hour

# Title : List
# Date : 2020-06-21
# Creater : tunealog

x = [1, 2, 3, 4]
y = ['a', 'b', 'c', 'd']
z = ["e", "f", 5, 6]

#[1, 2, 3, 4]
print(x)

#['a', 'b', 'c', 'd']
print(y)

#['e', 'f', 5, 6]
print(z)

#[1, 2, 3, 4, 'a', 'b', 'c', 'd']
print(x+y)

# 1
print(x[0])

#[1, 2, 3, 10]
x[3] = 10
print(x)

# err
# print(x[4])


# List.
a = [4, 2, 3, 1]

# len()
# 4
b = len(a)
print(b)

# sorted()
#[4, 2, 3, 1]
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
