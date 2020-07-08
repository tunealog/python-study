# Basic of Python

# Title : Strings
# Date : 2020-06-20
# Creator : tunealog

# String
x = "Hello"
y = "Bye"
z = """
Hello
I'm tunealog
Nice to meet you
Bye
"""

# Hello Python
print("Hello" + "Python")

# Hello Bye
print(x + y)

# Hello ~ Bye
print(z)

# Before Casting
# print("Age : " + 10)
# TypeError: cannot concatenate 'str' and 'int' objects

# After Casting
print("Age : " + str(10))

# Int Type Casting
a = 10
b = "10"
print(a + int(b))

# Strings Add
# Added Date : 2020-06-25

# Sample ID Number
iD = "901215-1134501"

# sex : 1
print("sex : " + iD[7])
# year : 90
print("year : " + iD[0:2])
# month : 12
print("month : " + iD[2:4])
# day : 15
print("day : " + iD[4:6])
# birthday : 901215
print("birthday : " + iD[:6])
# last 7char : 1134501
print("last 7char : " + iD[7:])
# last 7char (from lastest char) : 1134501
print("last 7char (from lastest char) : " + iD[-7:])


# Sample String
python = "Python is Amazing"
# python is amazing
print(python.lower())
# PYTHON IS AMAZING
print(python.upper())
# True
print(python[0].isupper())
# 17
print(len(python))
# Java is Amazing
print(python.replace("Python", "Java"))

# 5
py_index = python.index("n")
print(py_index)
# 15
py_index = python.index("n", py_index + 1)
print(py_index)
# 5
print(python.find("n"))

# Error Return
# print(python.index("B"))
# -1 Return
print(python.find("B"))

# 2
print(python.count("n"))

# ab
print("a" + "b")
# a b
print("a", "b")
