# Basic of Python

# Title : Exception (Advanced)
# Date : 2020-07-04
# Creator : tunealog
class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


try:
    print("Divide Calculator(1char)")
    nums = []
    nums.append(int(input("Type the first number : ")))
    nums.append(int(input("Type the second number : ")))
    if nums[0] >= 10 or nums[1] >= 10:
        raise BigNumberError("Input : {0}, {1}".format(nums[0], nums[1]))
    nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("Error! Only 1 char")
except BigNumberError as err:
    print("BigNumberErr")
    print(err)
finally:
    print("Thankyou")
