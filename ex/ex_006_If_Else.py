# Basic of Python

# Title : If Else
# Date : 2020-06-20
# Creator : tunealog

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

# If Else Add
# Added Date : 2020-06-27

# 0.7
k = 0.7
if 0 < k < 1:
    print(k)

# Okay
a = 2
b = [2, 4]
if a in b:
    print("Okay")
