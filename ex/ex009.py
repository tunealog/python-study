# Basic of Python
# Project 1hour

# Title : Loop For, While
# Date : 2020-06-21
# Creater : tunealog

# For
for i in range(3):
    print(i)
    print("Judy : Hi Mary")
    print("Mary : Hi Judy")

# While
j = 0
while j < 3:
    print(j)
    print("Judy : Hi Mary")
    print("Mary : Hi Judy")
    j = j + 1

# While True
k = 0
while True:
    print(k)
    print("Judy : Hi Mary")
    print("Mary : Hi Judy")
    k = k + 1
    if k > 2:
        break

# While Continue
l = 0
while l < 3:
    print(l)
    print("Judy : Hi Mary")
    if l == 1:
        l = l + 1
        continue

    print("Mary : Hi Judy")
    l = l + 1

# Advenced Loop
# Added Date : 2020-06-27

# for waiting_no in range(0, 5):
# for waiting_no in range(5):
for waiting_no in [0, 1, 2, 3, 4]:
    print("Waiting No : {0}".format(waiting_no))
    #print(f"Waiting No : {waiting_no}")
