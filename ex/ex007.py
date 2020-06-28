# Basic of Python

# Title : Function
# Date : 2020-06-20
# Creator : tunealog

# Function Name - chat
def chat():
    print("Jack : Hello I'm Jack")
    print("Mary : Hello I'm Mary")


# Jack : Hello I'm Jack
# Mary : Hello I'm Mary
chat()

# Function Name - para


def para(name1, name2, age):
    print("%s : How old are You" % name1)
    print("%s : I'm %d years old" % (name2, age))


# James : How old are You
# Honey : I'm 20 years old
para("James", "Honey", 20)

# Robert : How old are You
# Bunny : I'm 30 years old
para("Robert", "Bunny", 30)


# Function Name - sum
def sum(a, b):
    result = a+b
    return result


sum1 = sum(1, 2)
sum2 = sum(2, 4)

# 3
print(sum1)

# 6
print(sum2)

# Advenced Function
# Added Date : 2020-06-28


def deposit(balance, money):
    print(f"Deposit complete. Balance is {balance + money}dollors")
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print(f"Withdraw complete. Balance is {balance - money}dollors")
        return balance - money
    else:
        print(f"Withdraw not complete. Balance is {balance}dollors")
        return balance


def withdraw_night(balance, money):
    commission = 10
    return commission, balance - money - commission


balance = 0

# Deposit complete. Balance is 100dollors
balance = deposit(balance, 100)

# Withdraw not complete. Balance is 0dollors
# balance = withdraw(balance, 200)

# Withdraw complete. Balance is 50dollors
# balance = withdraw(balance, 50)

commission, balance = withdraw_night(balance, 50)
print(f"Commission is {commission}dollors. Balance is {balance}dollors")


# Default parameter
def profile_one(name, age=30, main_lang="Python"):
    print(f"name: {name}\nage: {age}\nmain language: {main_lang}")


profile_one("James")
profile_one("Rocky")

# Keyword parameter


def profile_two(name, age, main_lang):
    print(name, age, main_lang)


profile_two(age=40, name="Tommy", main_lang="Java")

# Mutabloe parameter


def profile_three(name, age, *language):
    print(f"name: {name}\nage: {age}")
    for lang in language:
        print(lang, end=" ")
    print("\n")


profile_three("James", 30, "Python", "Java", "C", "C++", "Javascript")
profile_three("Paul", 35, "Python", "Java")
