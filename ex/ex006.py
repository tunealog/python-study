# Basic of Python
# Project 1hour

# Title : If-Else
# Date : 2020-06-20
# Creater : tunealog

x = 1
y = 2

# 1 > 2 : ""
if x > y:
    print("Hello-01")

# 2 > 1 : "Hello-02"
if not x > y:
    print("Hello-02")

# 1 > 0 && 2 > 1 : "Hello-03"
if x > 0 and y > 1:
    print("Hello-03")

# 1 > 1 && 2 > 1 : ""
if x > 1 and y > 1:
    print("Hello-04")

# 1 > 1 || 2 > 1 : "Hello-05"
if x > 1 or y > 1:
    print("Hello-05")

# False : "Bye-06"
if x > 1:
    print("Hello-06")
else:
    print("Bye-06")

# Else If : "Good-07"
if x > 1:
    print("Hello-07")
elif x == 1:
    print("Good-07")
else:
    print("Bye-07")

# Advenced If
# Added Date : 2020-06-27

# Possible
# if 0 < x < 1:

# Scanner
# x = input("text")

# List in int
a = 2
b = [2, 4]
if a in b:
    print("Okay")

# [1, 2, 3, 4, 5]
students = [1, 2, 3, 4, 5]
print(students)

# [101, 102, 103, 104, 105]
students = [i+100 for i in students]
print(students)
