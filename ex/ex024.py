# Basic of Python
# Project

# Title : Quiz(Function)
# Date : 2020-06-28
# Creator : tunealog

# Quiz) Standard weight program
#
# Male : height(m) * height(m) * 22
# FeMale : height(m) * height(m) * 21
#
# Rule1 : Calculate the standard weight at each function
#           * Function name : std_weight
#           * Parameter : height, gender
# Rule2 : Standard weight is displayed to 2decimal places
#
# Example 1 (Result):
# The standard weight for a 175cm tall male is 67.38kg

def std_weight(height, gender):
    if gender == "male":
        standardWeight = round(height**2*22*0.0001, 2)
    else:
        standardWeight = round(height**2*21*0.0001, 2)
    return standardWeight


gender = "male"
height = 175
standardWeight = std_weight(height, gender)
print(
    f"The standard weight for a {height}cm tall {gender} is {standardWeight}kg")
