# Basic of Python

# Title : Standard Input Output
# Date : 2020-06-28
# Creator : tunealog

import sys

# python,Java?Hello
print("python", "Java", sep=",", end="?")
print("Hello")

# Standard Ouput
print("python", "Java", file=sys.stdout)

# Standard error
print("python", "Java", file=sys.stderr)

scores = {"math": 0, "english": 50, "computer": 100}
for subject, score in scores.items():
    #    print(subject, score)
    # math    :   0
    # english :  50
    # computer: 100
    print(subject.ljust(8), str(score).rjust(4), sep=":")

for num in range(1, 11):
    print("Waiting Number : " + str(num).zfill(3))

answer = input("Input anything: ")
# Input type is string
print(type(answer))
print("Result is " + answer + "!")
