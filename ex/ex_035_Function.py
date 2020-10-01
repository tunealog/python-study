# Basic of Python

# Title : Functions
# Date : 2020-07-05
# Creator : tunealog

import random

# input
age = input("How old are you?")
print("I'm {0} years old".format(age))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())  # 사용할 수 있는것들을 표시
print(dir(random))  # 랜덤모듈 내에서 사용할 수 있는것들을 표시

lst = [1, 2, 3]
print(dir(lst))  # 리스트에서 사용할 수 있는것들을 표시

name = "Jim"
print(dir(name))  # 리스트에서 사용할 수 있는것들을 표시
