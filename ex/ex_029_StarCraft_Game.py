# Basic of Python

# Title : StarCraft Game
# Date : 2020-07-03
# Creator : tunealog

from random import *


class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("Unit {0} is Ready".format(self.name))

    def move(self, location):
        print("{0} : Move to the {1} [Speed : {2}]"
              .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} Damaged from enemy"
              .format(self.name, damage))
        self.hp -= damage
        print("{0} : Current HP is {1}"
              .format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : Broken".format(self.name))


class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage

    def attack(self, location):
        print("{0} : Attack enemy on the {1} [Damage {2}]"
              .format(self.name, location, self.damage))


class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "Marine", 40, 1, 5)

    def stimpack(self):
        if self.hp > 10:
            self.hp -= 10
            print("{0} : Use Stimpack (HP Down)".format(self.name))
        else:
            print("{0} : Not enough HP".format(self.name))


class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "Tank", 150, 1, 35)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return

        if self.seize_mode == False:
            print("{0} : Change to Seize Mode".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        else:
            print("{0} : Change to Normal Mode".format(self.name))
            self.damage /= 2
            self.seize_mode = False


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
        self.fly(self.name, location)


class Wraith(FlyableAttackUnit):

    def __init__(self):
        FlyableAttackUnit.__init__(self, "Wraith", 80, 20, 5)
        self.clocked = False

    def clocking(self):
        if self.clocked == True:
            print("{0} : Unclocking".format(self.name))
            self.clocked = False
        else:
            print("{0} : Clocking".format(self.name))
            self.clocked = True


def game_start():
    print("[Alert] Game Start")


def game_over():
    print("Player : gg")
    print("[player] exit the game")


game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()
t1 = Tank()
t2 = Tank()
w1 = Wraith()

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

for unit in attack_units:
    unit.move("North")

Tank.seize_developed = True

print("[Alert] Seize Mode is developed")

for unit in attack_units:
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    elif isinstance(unit, Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack("North")

for unit in attack_units:
    unit.damaged(randint(5, 20))

game_over()
