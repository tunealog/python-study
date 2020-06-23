# Basic of Python
# Project 1hour

# Title : Inheritance
# Date : 2020-06-24
# Creater : tunealog

# Class Name : person
class Person:

    #Function : __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Function : say_hello
    def say_hello(self, to_name):
        print("Hello " + to_name + " I'm " +
              self.name + " " + self.age + " years old")

    #Function : introduce
    def introduce(self):
        print("Hello I'm " +
              self.name + " " + self.age + " years old")


tunealog_a = Person("tunealog", "20")
james_a = Person("James", "30")
jenny_a = Person("Jenny", "40")

# Hello James I'm tunealog 20years old
# Hello Jenny I'm James 30years old
# Hello tunealog I'm Jenny 40years old
tunealog_a.say_hello("James")
james_a.say_hello("Jenny")
jenny_a.say_hello("tunealog")


class Police(Person):
    def arrest(self, to_arrest):
        print("My job is " + to_arrest)


class Programmer(Person):
    def program(self, to_program):
        print("I'm " + to_program)


tunealog_b = Person("tunealog", "20")
james_b = Police("James", "30")
jenny_b = Programmer("Jenny", "40")

# Hello I'm tunealog 20 years old
tunealog_b.introduce()

# Hello I'm James 30 years old
james_b.introduce()

# My job is Police
james_b.arrest("Police")

# err
# james_b.program("Programmer")

# Hello I'm Jenny 40 years old
jenny_b.introduce()

# err
# jenny_b.arrest("Police")

# I'm Programmer
jenny_b.program("Programmer")
