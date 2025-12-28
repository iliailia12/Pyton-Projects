# # varibles

# full_name = "jon smith"
# age = 20
# is_new = True


# # greet function

# name = input('Enter your name')
# print(f'hi gg{name}')

# # greet function W2

# name = input('what is your name')
# print('hi' + name)

# # greet function W3

# name = input('enter your name:  ')
# fav_colour = input('enter your favorite colour')
# print(name + ' lekes ' + fav_colour)

# # greet function W3

# name = input('enter your name:   ')
# fav_colour = input('enter your favorite colour')
# print(f'{name} likes {fav_colour}')


# wryte a program that will ask the year that we were born and it will calculate and print it on the terminal

# birth_year = input('Birth year:  ')
# age = 2026 - int(birth_year)
# print(age)

# ask user kilogrmas and print on the terminal

# wheight_lbs = input('input your wheight:  ')
# wheight_kg = int(wheight_lbs )* 0.45
# print(wheight_kg)

# strings

# course = 'pyton for beginnerts'

# another = course[:]
# print(another)
# print(course[0])
# print(course[-1])
# print(course[0:4])
# print(course[0:3])
# print(course[0:])
# print(course[1:])
# print(course[:5])
# print(course[:])

# exercise for me
# name = 'jennifer'
# print(name[1:-1])

# formated strings

# first = 'jon'
# last = 'smith'
# mas = f'{first} [{last}] is a coder'
# print(mas)

# string metods

# course = 'pyton for beginners'

# print(len(course))
# print(course.upper())
# print(course.lower())
# print(course.find('y'))
# print(course.replace('beginners', 'Absolute Beginners'))
# print("pyton" in course)
# print("Pyton" in course)

# aritmetic operators

# print(10 + 10)
# print(10 - 10)
# print(10 * 10)
# print(10 / 10)
# print(10 // 10)
# print(10 ** 10)
# print(10 % 10)

# x = 10
# x = x + 3
# print(x)

# x += 3
# print(x)

# math functions x metods

# x = 2.9
# print(round(x))
# print(abs(-2.9))
# print(abs(-2.9))


# if statements

# is_hot = False
# if is_hot :
#     print('its hot day')
# print('enjoy your day')

# is_hot = True
# if is_hot :
#     print('its hot day')
# else:
#     print('its hot day')
#     print('wear warm clothes')
# print('enjoy your day')

# is_hot = False
# if is_hot :
#     print('its hot day')
# else:
#     print('its cold day')
#     print('wear warm clothes')
# print('enjoy your day')


# exercise for me
# Problem Statement:

# The price of a house is $1,000,000.
# If the buyer has good credit, they must make a down payment of 10% of the price.
# Otherwise, the buyer must make a down payment of 20% of the price.
# Print the down payment amount.

# W1

# house_price = 1000000
# good_credit = True

# if good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f'Down Payment is :  {down_payment}')

# W2

# house_price = 1000000
# good_credit = False

# if good_credit:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f'Down Payment is :  ${down_payment}')


# logical operators or and

# and

# W1
# has_high_income = True
# has_good_credit = True

# if has_high_income and has_good_credit:
#     print('good for credit and loan')

# W2

# has_high_income = True
# has_good_credit = False

# if has_high_income and has_good_credit:
#     print('good for credit and loan')

# or

# W1

# has_high_income = True
# has_good_credit = False

# if has_high_income or has_good_credit:
#     print('good for credit and loan')

# not

# has_good_credit = True
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print('good')

# has_good_credit = False
# has_criminal_record = False

# if has_good_credit and not has_criminal_record:
#     print('good')
# else:
#     print('not good')


# comparison operators

# == (Equal to)
# != (Not equal to)
# > (Greater than)
# < (Less than)
# >= (Greater than or equal to)
# <= (Less than or equal to)

# temperature = 37

# if temperature > 30 :
#     print('its hot day')
# else:
#     print('its not hot day')

# name = ''
# print(len(name))

# if len(name) < 3:
#     print('name must be list 3 characters.')

# elif len(name) >50:
#     print('name miust be maximum of 50 cheracters or less')
# else :
#     print('name looks good')


# Whyle loops

# i = 7777
# while i<=  77:
#     print(i)

# i = 1

# while i<= 5:
#     print(i)
#     i = i + 1
# print('done')


# for loops

# for i in range(1,20000,33):
#     print(i)

# for item in 'pyton':
#     print(item)

# for item in ['mosh','ilo','sata','sapa']:
#     print(item)

# for item in ['4','3','2','1']:
#     print(item)

# for i in range(100):
#     print(i)

# for i in range(5,100):
#     print(i)

# for i in range(5,100,5):
#     print(i)


# price = [10,29,33]
# total = 0
# for item in price :
#     total += price
# print (total)


# nesteed loop

# for x in range(4):
#     for y in range(3):
#         print(f'{x}, {y}')

# numbers = [5,2,5,2,2]

# for x_count in numbers:
#     print('x' * x_count)

# numbers = [5, 2, 5, 2, 2]
# for x_count in numbers:
#     output = ''
#     for count in range(x_count):
#         output += 'x'  
#     print(output)  

# lists

# names = ['jon','bpb','loli']
# print (names)
# print (names[1])
# print (names[-1])
# print (names[2:])
# print (names[2:5])
# print (names[2:])
# print (names[:7])

# numbers = [3,6,7,9,2,34,1,234,567,77,65,11,21,23,32,45,99]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
#     print(max)


# 2D Lists

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ]

# matrix [0] [1] = 20
# print(matrix [0] [1])

# list metods

# numbers = [1,2,3,4,5,6,7,8,9,10 ,5,5,5,5,5,5,5,5,5,5]

# numbers.append(20)
# numbers.insert(0,2000)
# numbers.remove(2000)
# numbers.clear()
# numbers.pop()
# print(numbers.index(4))
# print(numbers.index(40000))
# print(numbers)
# print(600 in numbers)
# print(numbers.count(5))
# numbers.sort()
# numbers.reverse()
# print(numbers)
# numbers2 = numbers.copy()

# numbers = [2,1,3,4,5,5,5,53,3,2,2,1,1,1,432,345,2,22,34,3234,3,456,4357,6543,4444,4444,32221,3444,3333,2,22,2,2,2,2,222,222,22,222,22,22,34543]

# unigues = list(set(numbers))
# print(unigues)


# tuple

# normal list
# numbers = [1,2,3,4,5,6,6]

# tuple

# numbers = (1,2,3,4,5,6,7,8,9,)


# unpacking

#    normal
#               x y z
# cordinates = (1,2,3)
# cordinates = cordinates[0] * cordinates[1] *c

#    normal

# cordinates = (1,2,3)

# x = cordinates[0]
# y =  cordinates[1]
# z =  cordinates[2]

# x * y * z

# unpacking

# cordinates = (1,2,3)

# x,t,z = cordinates

# Dictionaries

# .get

# costumer = {
#     'name': 'jon smit',
#     'age': 30,
#     'is_verified':True
# }
# print(costumer['name'])
# print(costumer.get('hhh'))
# print (costumer.get('date', 'jan 1 187'))




# # Python Dictionaries Examples

# # 1. Simple Dictionary
# # Creating a dictionary with basic key-value pairs
# student = {
#     "name": "John",
#     "age": 16,
#     "grade": "10th",
# }

# # Accessing values using keys
# print(student["name"])  # Output: John
# print(student["age"])   # Output: 16

# # 2. Dictionary with Different Data Types
# person = {
#     "name": "Alice",
#     "age": 17,
#     "is_student": True,
#     "subjects": ["Math", "Science", "History"],
#     "address": {"city": "Tbilisi", "country": "Georgia"}
# }

# # Accessing nested values
# print(person["address"]["city"])  # Output: Tbilisi

# # 3. Adding and Modifying Key-Value Pairs
# student["school"] = "ABC High School"  # Adding a new key-value pair
# student["age"] = 17  # Modifying the value of an existing key

# print(student)

# # 4. Dictionary Methods
# # Using get() method
# print(person.get("name"))  # Output: Alice
# print(person.get("hobby", "No hobby found"))  # Output: No hobby found

# # Using keys() and values() methods
# print(person.keys())  # Output: dict_keys(['name', 'age', 'is_student', 'subjects', 'address'])
# print(person.values())  # Output: dict_values(['Alice', 17, True, ['Math', 'Science', 'History'], {'city': 'Tbilisi', 'country': 'Georgia'}])

# # 5. Looping through a Dictionary
# # Looping through keys and values
# for key, value in person.items():
#     print(f"{key}: {value}")

# # Output:
# # name: Alice
# # age: 17
# # is_student: True
# # subjects: ['Math', 'Science', 'History']
# # address: {'city': 'Tbilisi', 'country': 'Georgia'}

# # 6. Nested Dictionaries
# courses = {
#     "Math": {"teacher": "Mr. Smith", "room": 101},
#     "English": {"teacher": "Ms. Johnson", "room": 202},
# }

# # Accessing nested dictionary values
# print(courses["Math"]["teacher"])  # Output: Mr. Smith
# print(courses["English"]["room"])  # Output: 202

# # 7. Deleting Items from a Dictionary
# del student["grade"]  # Deletes the 'grade' key and its value
# print(student)

# # 8. Dictionary Comprehensions
# # Creating a dictionary using a comprehension
# numbers = {x: x**2 for x in range(5)}
# print(numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}




# phone = input('Phone : ')
# digits_mapping = {
#     '1': 'one',
#     '2': 'two',
#     '3': 'tree',
#     '4': 'four',
# }

# outfut = '' 
# for ch in phone :
#    outfut += digits_mapping.get(ch,'!') +  ''
# print(outfut)


# functions pareameters 
# def greet_name (name):
#     print(f"hi {name}")

# greet_name('joshua')

# keywrd argumments

# """
# ========================================
# KEYWORD ARGUMENTS IN PYTHON
# ========================================

# This file explains:
# - What keyword arguments are
# - Why they are useful
# - How to use them
# - *args vs **kwargs
# - Examples
# - Do & Don't list

# All explanations are written in English.
# """

# # -------------------------------------
# # 1. WHAT ARE KEYWORD ARGUMENTS?
# # -------------------------------------
# """
# Keyword arguments are arguments passed to a function
# using the parameter name.

# Instead of relying on position, you explicitly say
# which value belongs to which parameter.
# """

# def greet(name, age):
#     print(f"Name: {name}, Age: {age}")

# # Positional arguments
# greet("Alice", 20)

# # Keyword arguments
# greet(age=20, name="Alice")


# # -------------------------------------
# # 2. WHY KEYWORD ARGUMENTS ARE USEFUL
# # -------------------------------------
# """
# Advantages:
# - Code is easier to read
# - Order does NOT matter
# - Less mistakes with many parameters
# """

# def create_user(username, email, is_admin):
#     print(username, email, is_admin)

# create_user(
#     email="user@example.com",
#     is_admin=False,
#     username="student"
# )


# # -------------------------------------
# # 3. DEFAULT VALUES WITH KEYWORD ARGUMENTS
# # -------------------------------------
# """
# Default values allow parameters to be optional.
# """

# def power(base, exponent=2):
#     return base ** exponent

# print(power(5))          # uses default exponent
# print(power(5, 3))       # positional
# print(power(base=5, exponent=3))  # keyword


# # -------------------------------------
# # 4. *args vs **kwargs (IMPORTANT)
# # -------------------------------------
# """
# *args  -> collects positional arguments (tuple)
# **kwargs -> collects keyword arguments (dictionary)
# """

# def show_args(*args):
#     print("ARGS:", args)

# def show_kwargs(**kwargs):
#     print("KWARGS:", kwargs)

# show_args(1, 2, 3)
# show_kwargs(name="Tom", age=15, city="Tbilisi")


# # -------------------------------------
# # 5. USING *args AND **kwargs TOGETHER
# # -------------------------------------
# def mixed_function(a, b, *args, **kwargs):
#     print("a:", a)
#     print("b:", b)
#     print("args:", args)
#     print("kwargs:", kwargs)

# mixed_function(
#     1,
#     2,
#     3,
#     4,
#     name="Ana",
#     score=95
# )


# # -------------------------------------
# # 6. UNPACKING KEYWORD ARGUMENTS
# # -------------------------------------
# """
# You can unpack a dictionary into keyword arguments using **.
# """

# data = {
#     "name": "Luka",
#     "age": 16
# }

# def print_person(name, age):
#     print(name, age)

# print_person(**data)


# # -------------------------------------
# # 7. SMALL LIST: WHEN TO USE KEYWORD ARGUMENTS
# # -------------------------------------
# """
# USE keyword arguments WHEN:
# - Function has many parameters
# - Parameters have default values
# - You want readable code
# - Order should not matter
# """


# # -------------------------------------
# # 8. DO & DON'T LIST
# # -------------------------------------
# """
# DO:
# - Use keyword arguments for clarity
# - Combine positional + keyword when needed
# - Use **kwargs for flexible functions

# DON'T:
# - Put positional arguments AFTER keyword arguments
# - Use unclear parameter names
# - Overuse **kwargs when not needed
# """

# # ❌ WRONG (will cause error)
# # greet(name="Alice", 20)

# # ✅ CORRECT
# greet("Alice", age=20)


# # -------------------------------------
# # 9. REAL-LIFE STYLE EXAMPLE
# # -------------------------------------
# def register_student(name, age, grade, city="Unknown"):
#     print("Student Info:")
#     print("Name:", name)
#     print("Age:", age)
#     print("Grade:", grade)
#     print("City:", city)

# register_student(
#     name="Nika",
#     age=15,
#     grade=9
# )


# return functions

# num squares w1

# def square (number):
#     return number * number

# result = square(3)
# print(result)

# W2

# def square (number):
#     return number * number

# print(square(3))


# creating a reusable function 



# classes

