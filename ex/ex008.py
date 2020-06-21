# Basic of Python
# Project 1hour

# Title : Function-Practice
# Date : 2020-06-21
# Creater : tunealog

# Function Name - examTest
def examTest(name, total):
    if total < 5:
        print(name + " : C")
    elif total >= 5 and total <= 9:
        print(name + " : B")
    else:
        print(name + " : A")


# C
examTest("Tom", 4)
# B
examTest("Bob", 5)
# B
examTest("Soy", 9)
# A
examTest("Judy", 10)
