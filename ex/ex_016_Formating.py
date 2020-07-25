# Basic of Python

# Title : Formating
# Date : 2020-06-25
# Creator : tunealog

# Method 1
print("I'm %d years old" % 20)
print("I like %s " % "Python")
print("Initial of Apple is %c " % "A")
print("I like %s and %s" % ("Python", "Java"))

# Method 2
print("I'm {} years old".format(20))
print("I like {} and {}" .format("Python", "Java"))
print("I like {0} and {1}" .format("Python", "Java"))
print("I like {1} and {0}" .format("Python", "Java"))

# Method 3
print("I'm {age} years old and I like {color} color".format(
    age=20, color="Blue"))

# Method 4 (over Python 3.6)
age = 30
color = "Blue"
print(f"I'm {age} years old and I like {color} color")
