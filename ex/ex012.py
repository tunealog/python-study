# Basic of Python
# Project 1hour

# Title : Dictionary
# Date : 2020-06-22
# Creater : tunealog

x = {
    0: "Hello",
    1: "Hi",
    "name": "tunealog",
    "age": 20,
}

#{0: 'Hello', 1: 'Hi', 'name': 'tunealog', 'age': 20}
print(x)

# tunealog
print(x["name"])

# 20
print(x["age"])

# Hello
print(x[0])
print(x.get(0))

# Hi
print(x[1])
print(x.get(1))

# Thanks
print(x.get(3, "Thanks"))

# True
print("age" in x)

# False
print("sex" in x)

#dict_keys([0, 1, 'name', 'age'])
print(x.keys())

#dict_values(['Hello', 'Hi', 'tunealog', 20])
print(x.values())

#key : 0
#value : Hello
#key : 1
#value : Hi
#key : name
#value : tunealog
#key : age
#value : 20
for key in x:
    print("key : " + str(key))
    print("value : " + str(x[key]))

#{0: 'bye', 1: 'Hi', 'name': 'tunealog', 'age': 20}
x[0] = "bye"
print(x)

#{0: 'bye', 1: 'Hi', 'name': 'tunealog', 'age': 20, 'city': 'Newyork'}
x["city"] = "Newyork"
print(x)

# Advenced Dictionary
# Added Date : 2020-06-26

#{1: 'Hi', 'name': 'tunealog', 'age': 20, 'city': 'Newyork'}
del x[0]
print(x)

#dict_items([(1, 'Hi'), ('name', 'tunealog'), ('age', 20), ('city', 'Newyork')])
print(x.items())

x.clear()
print(x)
