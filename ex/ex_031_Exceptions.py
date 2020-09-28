# Basic of Python

# Title : Exceptions
# Date : 2020-07-04
# Creator : tunealog

try:
    print("Divide Calculator")
    nums = []
    nums.append(int(input("Type the first number : ")))
    nums.append(int(input("Type the second number : ")))
    #nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error!")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("Unknown Err")
    print(err)
