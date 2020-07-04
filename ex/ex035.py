# Basic of Python

# Title : Quiz(Exception)
# Date : 2020-07-04
# Creator : tunealog

# Quiz) Chicken order System
#
# Rule1 : When input under 1 or number, Return ValueError
#         Output Message : "Wrong Number or Not Number"
# Rule2 : Order is limited to 10 Chiken by onetime
#         Output Message : "Sorry, Today is over"
#         Return SoldOutError

class SoldOutError(Exception):
    pass


chicken = 10
waiting = 1
while(True):
    try:
        print("[Stock of Chicken : {0}]".format(chicken))
        order = int(input("How many chickens would you like to order?"))

        if order > 10:
            print("Sorry, Please order for under 10 Chikens")
            break

        elif order > chicken:
            print(
                "Not enough chickens. Please order under stock [Stock : {0}]".format(chicken))

        elif order < 1:
            raise ValueError

        else:
            print("[Waiting Number {0}] Order complete of {1} chickens"
                  .format(waiting, order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOutError

    except ValueError:
        print("Wrong Number or Not Number")
    except SoldOutError:
        print("Sorry, Today is over")
        break
