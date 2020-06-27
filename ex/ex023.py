# Basic of Python
# Project 1hour

# Title : Quiz(Loop)
# Date : 2020-06-27
# Creator : tunealog

# Quiz) Taxi System
#
# Rule1 : Number of passengers is 50
# Rule2 : Time of drive is random at 5 ~ 50min
# Rule3 : You can drive during 5 ~ 15min
#
# Example 1 (Result):
# [O] 1 passenger (driving time : 15min)
# [ ] 2 passenger (driving time : 50min)
# [O] 3 passenger (driving time : 5min)
# ...
# [ ] 50 passenger (driving time : 16min)
#
# Total number of passengers : 2 person

from random import *
passenger = list(range(1, 51))
oxCount = 0

# for count in range(1, 51):
for count in passenger:
    passengerTime = randint(5, 50)
    if 5 <= passengerTime <= 15:
        ox = "O"
        oxCount += 1
    else:
        ox = " "
    print(f"[{ox}] {count} passenger (driving time : {passengerTime}min")
print(f"Total number of passengers : {oxCount} person")
