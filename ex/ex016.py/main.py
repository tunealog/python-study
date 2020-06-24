# Basic of Python
# Project 1hour

# Title : Package and Modules
# Date : 2020-06-24
# Creater : tunealog

# Animal Package
# Dog, Cat Modules
# Dog, Cat Modules can say "Hi"

# Call class "dog" from animal package
from animal import *
from animal import dog

# Call class "cat" from animal package
from animal import cat

# Instance
d = dog.Dog()
d.hi()

# Instance
c = cat.Cat()
c.hi()

# Call all of class from animal package

d = Dog()
d.hi()

c = Cat()
c.hi()
