# Basic of Python

# Title : Lists
# Date : 2020-06-21
# Creator : tunealog

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
print(x + y)

#[1, 2, 3, 4, 'a', 'b', 'c', 'd']
x.extend(y)
print(x)

# 1
print(x[0])

#[1, 2, 3, 10, 'a', 'b', 'c', 'd']
x[3] = 10
print(x)

# err
# print(x[8])

############################
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

# sort()
#[1, 2, 3, 4]
a.sort()
print(a)

#[4, 3, 2, 1]
a.reverse()
print(a)

# []
c.clear()
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

# [1, 2, 3, 4, 5]
students = [1, 2, 3, 4, 5]
print(students)

# [101, 102, 103, 104, 105]
students = [i+100 for i in students]
print(students)

# Lists Add
# Added Date : 2020-06-26

subway = ["tunealog", "James", "Lily", "tunealog"]

#['tunealog', 'James', 'Lily', 'tunealog', 'Rocky']
subway.append("Rocky")
print(subway)

#['tunealog', 'Rose', 'James', 'Lily', 'tunealog', 'Rocky']
subway.insert(1, "Rose")
print(subway)

# Pick that end of list
# Rocky
#['tunealog', 'Rose', 'James', 'Lily', 'tunealog']
print(subway.pop())
print(subway)

# 2
print(subway.count("tunealog"))
