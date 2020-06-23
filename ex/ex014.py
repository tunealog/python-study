# Basic of Python
# Project 1hour

# Title : Class
# Date : 2020-06-23
# Creater : tunealog

# Class Name : person
class person:

    #Function : __init__
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #Function : say_hello
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
