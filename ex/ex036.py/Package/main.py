# Basic of Python

# Title : Package(2nd)
# Date : 2020-07-05
# Creator : tunealog

import random
import inspect
import travel.thailand
from travel import *
from travel import vietnam
from travel.thailand import ThailandPackage

# import travel.thailand
trip_to = travel.thailand.ThailandPackage()
trip_to.detail()

# from travel.thailand import ThailandPackage
trip_to = ThailandPackage()
trip_to.detail()

# from travel import vietnam
trip_to = vietnam.VietnamPackage()
trip_to.detail()

# from travel import *
trip_to = thailand.ThailandPackage()
trip_to.detail()

# inspect
# import random
# import inspect
print(inspect.getfile(random))
print(inspect.getfile(thailand))
