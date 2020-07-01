# Basic of Python

# Title : Class
# Date : 2020-06-23
# Creator : tunealog

class person:

    # Function : __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Function : say_hello
    def say_hello(self, to_name):
        print("Hello " + to_name + " I'm " +
              self.name + " " + self.age + " years old")


tunealog = person("tunealog", "20")
james = person("James", "30")
jenny = person("Jenny", "40")

# Hello James I'm tunealog 20years old
# Hello Jenny I'm James 30years old
# Hello tunealog I'm Jenny 40years old
tunealog.say_hello("James")
james.say_hello("Jenny")
jenny.say_hello("tunealog")


# Added Date : 2020-07-01


class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} is ready")
        print(f"HP {self.hp}, Damage {self.damage}")


marine1 = Unit("Marine", 40, 5)
marine2 = Unit("Marine", 40, 5)
tank = Unit("Tank", 150, 35)

wraith1 = Unit("Wraith", 80, 5)
print("Unit Name : {0}, Damage : {1}".format(wraith1.name, wraith1.damage))

wraith2 = Unit("Clocking Wraith", 80, 5)
wraith2.clocking = True
if wraith2.clocking == True:
    print("{0} is Clocked".format(wraith2.name))
