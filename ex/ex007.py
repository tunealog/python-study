# Basic of Python
# Project 1hour

# Title : Function
# Date : 2020-06-20
# Creater : tunealog

# Function Name - chat
def chat():
    print("Jack : Hello I'm Jack")
    print("Mary : Hello I'm Mary")


# Jack : Hello I'm Jack
# Mary : Hello I'm Mary
chat()

# Function Name - para


def para(name1, name2, age):
    print("%s : How old are You" % name1)
    print("%s : I'm %d years old" % (name2, age))


# James : How old are You
# Honey : I'm 20 years old
para("James", "Honey", 20)

# Robert : How old are You
# Bunny : I'm 30 years old
para("Robert", "Bunny", 30)


# Function Name - sum
def sum(a, b):
    result = a+b
    return result


sum1 = sum(1, 2)
sum2 = sum(2, 4)

# 3
print(sum1)

# 6
print(sum2)
