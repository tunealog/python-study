# Basic of Python

# Title : Class
# Date : 2020-06-23
# Creator : tunealog

class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

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
#########################################################################

class Unit_1:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print(f"{self.name} is ready")
        print(f"HP {self.hp}, Damage {self.damage}")


marine1 = Unit_1("Marine", 40, 5)
marine2 = Unit_1("Marine", 40, 5)
tank = Unit_1("Tank", 150, 35)

wraith1 = Unit_1("Wraith", 80, 5)
print("Unit_1 Name : {0}, Damage : {1}".format(wraith1.name, wraith1.damage))


#########################################################################

# Add Parameter
wraith2 = Unit_1("Clocking Wraith", 80, 5)
wraith2.clocking = True

if wraith2.clocking == True:
    # error
    # if wraith1.clocking == True:
    print("{0} is Clocked".format(wraith2.name))

#########################################################################

# Classes
# Inheritances
# Multiple Inheritances
# Added Date : 2020-07-02


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("Unit moves")
        print("{0} : Move to the {1} [Speed : {2}]"
              .format(self.name, location, self.speed))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : Attack enemy on the {1} [Damage {2}]"
              .format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} Damaged from enemy"
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : Current HP is {1}"
              .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Broken".format(self.name))


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : Flying to the {1} [Speed {2}]"
              .format(name, location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("Unit moves")
        self.fly(self.name, location)

# firebat1 = AttackUnit("FireBat", 50, 16)
# firebat1.attack("West")

# firebat1.damaged(25)
# firebat1.damaged(25)


valkyrie = FlyableAttackUnit("Valkyrie", 200, 6, 5)
valkyrie.fly(valkyrie.name, "East")

# Overloading
# Move Command : Vulture = move / Battlecruiser = fly
# Create def move in def fly


vulture = AttackUnit("Vulture", 80, 10, 20)
battlecruiser = FlyableAttackUnit("BattleCruiser", 500, 25, 3)

vulture.move("West")  # move
# battlecruiser.fly(battlecruiser.name, "East") # fly
battlecruiser.move("East")  # move in fly

# Pass
# Super
# Added Date : 2020-07-03


class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0) # Possible
        super().__init__(name, hp, 0)  # Can't Using for Multiple Inheritance
        self.location = location


supply_depot = BuildingUnit("Supply Depot", 500, "West")


def game_start():
    print("[Alert] The new games beginning")


def game_over():
    pass


game_start()
game_over()  # pass
