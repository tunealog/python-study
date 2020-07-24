# Basic of Python

# Title : Packages and Modules
# Date : 2020-06-24
# Creator : tunealog

# Animal Package
# Dog, Cat Modules
# Dog, Cat Modules can say "Hi"

# __init__.py
from animal import *

# Call class "dog" from animal package
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
