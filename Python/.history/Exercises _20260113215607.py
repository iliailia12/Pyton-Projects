
# Variables in Python

first_name = 'Asabeneh'
last_name = 'Yetayeh'
country = 'Finland'
city = 'Helsinki'
age = 250
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
    'firstname':'Asabeneh', 
    'lastname':'Yetayeh', 
    'country':'Finland',
    'city':'Helsinki'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Asabeneh', 'Yetayeh', 'Helsink', 250, True

print(first_name, last_name, country, age, is_married)
print('First name:', first_name)
print('Last name: ', last_name)
print('Country: ', country)
print('Age: ', age)
print('Married: ', is_married)




# this exercies are from https://github.com/Asabeneh this guy  is Good full stsack enjineer alse has good github and its open for enybody

# Exercises: Level 1
# 1. Inside 30DaysOfPython create a folder called day_2. Inside this folder create a file named variables.py

# I Wryte In This Folder I do Not Need New FOlder

# 2. Write a python comment saying 'Day 2: 30 Days of python programming'
# 30 Days of python programming'

# 3. Declare a first name variable and assign a value to it
first_name = 'ilia'
first_name = 'ილია'


# 4. Declare a last name variable and assign a value to it
last_nme = 'kviciani'
last_nme = 'კვიციანი'


# 5. Declare a full name variable and assign a value to it
full_name = 'Ilia Kvitsiani'
full_name = 'ილია კვიციანი'


# 6. Declare a country variable and assign a value to it
country = 'Georgia'
country = 'საქართველო'


# 7. Declare a city variable and assign a value to it
city = 'idk' 
city = 'არ ვიცი' 


# 8. Declare an age variable and assign a value to it
age = 15


# 9. Declare a year variable and assign a value to it
year = 2011


# 10. Declare a variable is_married and assign a value to it
is_married = False


# 11. Declare a variable is_true and assign a value to it
is_True = False


# 12. Declare a variable is_light_on and assign a value to it
is_light_on = False


# 13. Declare multiple variable on one line

name , age , birth_year , is_married , is_student , first_name , last_nme , full_name = 'ilia', 12 , 2011 , False , True , 'ilia' , 'kviciani' ,  'ilia kvitsiani'

# print

print(first_name)
print(first_name)
print(last_nme)
print(last_nme)
print(country)
print(country)
print(city)
print(age)
print(year)
print(is_married)
print(is_True)
print(is_light_on)
print(name , age , birth_year , is_married , is_student , first_name , last_nme , full_name)


# Exercises: Level 2

#  1. Check the data type of all your variables using type() built-in function

print(type(first_name)) 
print(type(last_nme))

print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_light_on))
print(type(is_student))
print(type(is_True))


# Using the len() built-in function, find the length of your first name

print(len(first_name)) #its 4 


# Compare the length of your first name and your last name

len(first_name) > len(last_nme)


# Declare 5 as num_one and 4 as num_two

num1 = 5
num2 = 4


# Add num_one and num_two and assign the value to a variable total

total = num1 + num2


# Subtract num_two from num_one and assign the value to a variable diff

diff = num1 - num2


# Multiply num_two and num_one and assign the value to a variable product

total = num2 * num1
product = total


# Divide num_one by num_two and assign the value to a variable division

division = num1 / num2


# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num1 % num2


# Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num1 ** num2


# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num1 // num2


# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
# Take radius as user input and calculate the area.

# წრის რადიუსი 30 მეტრია.
# გამოთვალეთ წრის ფართობი და მიანიჭეთ მნიშვნელობა ცვლადს area_of_circle
# გამოთვალეთ წრის გარშემოწერილობა და მიანიჭეთ მნიშვნელობა ცვლადს circum_of_circle
# მომხმარებლის შეყვანის სახით მიიღეთ რადიუსი და გამოთვალეთ ფართობი.


import math
radius = float(input('enter radius'))
area_of_circle = math.pi * radius **2
circum_of_circle = 2 * math.pi * radius
print(area_of_circle)
print(circum_of_circle)




# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

first_name = int(input('enter your name'))
last_name = int(input('enter your lastname'))
age = int(input('enter your age'))
country = int(input('enter your country'))

print(first_name, last_name, country, age)



# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

# i already see 


# operators

# 1. Declare your age as integer variable
age = 15   
# 2. Declare your height as a float variable
height = 1.70
# 3. Declare a variable that store a complex number
complex_number = 499 + 1999j
# 4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

base = float(input("Enter base of the triangle: "))
height = float(input("Enter height of the triangle: "))
area = 0.5 * base * height
print("The area of the triangle is:", area)



# 5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).



a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

perimeter = a + b + c

print("The perimeter of the triangle is:", perimeter)

# good vay advanced
print("Perimeter:", float(input()) + float(input()) + float(input()))




# 6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))

length = float(input("Enter length of the rectangle:  "))
width =  float(input("enter width of the rectangle: "))
are =  length * width
perimeter  = 2*(length + width)
print(area)
print(perimeter)


# 7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

pi = 3.14
r = float(input('Enter radius:  '))
area = pi * r * r
circumference = 2 * pi * r
print(area)
print(circumference)

# 8. Calculate the slope, x-intercept and y-intercept of y = 2x -2\



# 9. Slope is (m = y2-y1/x2-x1). Find the slope and [Euclidean distance](https://en.wikipedia.org/wiki/Euclidean_distance#:~:text=In%20mathematics%2C%20the%20Euclidean%20distance,being%20called%20the%20Pythagorean%20distance.) between point (2, 2) and point (6,10) 


import math
x1 , y1 = 2 , 2
x2 , y2 = 6 , 10
slope = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print(slope) 
print(distance)


# 10. Compare the slopes in tasks 8 and 9. idkვერ მივხვდი ვერ დავწერე



# 11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.

x = -5
y = x **2 + 6 * x + 9
print(x , y)

x = -4
y =  x ** 2 + 6 * x + 3
print(x , y)

x = -3
y = x**2 + 6*x + 9
print(x , y)

# 12. Find the length of 'python' and 'dragon' and make a falsy comparison statement.

txt1 = 'python'
print(len(txt1))

txt2 = 'dragon'
print(len(txt2))

txt3 = 'this is my fullstack dev jurney and aso i hate shchool'
print((len(txt3)))

txt3 = 'i like coding'
print((len(txt3)))

is_maried = False
is_strudent = True
know_coding = True
lovs_coding = True
is_adult = False
is_teacher = False

# bonus 
bonus_txt1 = 'Programming'
bonus_txt2 = 'coding'
bonus_txt3 = 'i like codins so much'
bonus_txt4 = 'phone'


print(len(bonus_txt1))
print(len(bonus_txt2))
print(len(bonus_txt3))
print(len(bonus_txt4))


print(len(bonus_txt1) < len(bonus_txt2))    
print(len(bonus_txt2) > len(bonus_txt4))   
print(len(bonus_txt4) == 10)               


# 13. Use _and_ operator to check if 'on' is found in both 'python' and 'dragon'

word1 = 'python'
word2 = 'dragon'
print('on' in word1 and 'on' in word2)


# 14. _I hope this course is not full of jargon_. Use _in_ operator to check if _jargon_ is in the sentence.

sentence = "I hope this course is not full of jargon"
print('jargon' in sentence)

# 15. There is no 'on' in both dragon and python

print(not ('on' in 'dragon' and 'on' in 'python'))

# 16. Find the length of the text _python_ and convert the value to float and convert it to string
some_txt = 'python'
print(len(some_txt))
# float(some_txt)  არასწორა not rigth
length_float = float(length)  
str(some_txt)

# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

even_or_odd = int(input('Enter your name : '))
if even_or_odd %2 == 0:
    print('number is even')
else:
    print('its  odd')

# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.

floor_division_of_7_by_3 = 7 // 3
int_value_of_2_7 = int(2.7)
print(floor_division_of_7_by_3 == int_value_of_2_7)

# ეხლა ცოტა პრაქტიკია რავი იფ ელსით

floor_division_of_7_by_3 = 7 // 3
int_value_of_2_7 = int(2.7)

if floor_division_of_7_by_3 == int_value_of_2_7:
    print('True')
else:
    print('False')
    

# 19. Check if type of '10' is equal to type of 10

print(type('10') == type(10))

# 20. Check if int('9.8') is equal to 10

print(int('9.8') == 10)

# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person? 

hours = float((input('Enter hours worked:  ')))
rate = float((input('Enter rate per hour:  ')))

pay = hours * rate
print(pay)


# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years


birth_year = input('Birth year:  ')
age = 2026 - int(birth_year)
print(age)


# 23. Write a Python script that displays the following table

# ```py
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# ```



# W1

for i in range (1,6):
    print(i, 1, i, i**2, i**3)



# w2

print(1, 1, 1, 1, 1)
print(2, 1, 2, 4, 8)
print(3, 1, 3, 9, 27)
print(4, 1, 4, 16, 64)
print(5, 1, 5, 25, 125)

# W3

table = {
    1: [1, 1, 1, 1],
    2: [1, 2, 4, 8],
    3: [1, 3, 9, 27],
    4: [1, 4, 16, 64],
    5: [1, 5, 25, 125]
}

print(1, *table[1])
print(2, *table[2])
print(3, *table[3])
print(4, *table[4])
print(5, *table[5])






# 04_Day_Strings



# Single line comment
letter = 'P'                # A string could be a single character or a bunch of texts
print(letter)               # P
print(len(letter))          # 1
greeting = 'Hello, World!'  # String could be  a single or double quote,"Hello, World!"
print(greeting)             # Hello, World!
print(len(greeting))        # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = '''I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python.'''
print(multiline_string)
# Another way of doing the same thing
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String Concatenation
first_name = 'Asabeneh'
last_name = 'Yetayeh'
space = ' '
full_name = first_name  +  space + last_name
print(full_name) # Asabeneh Yetayeh
# Checking length of a string using len() builtin function
print(len(first_name))  # 8
print(len(last_name))   # 7
print(len(first_name) > len(last_name)) # True
print(len(full_name)) # 15

#### Unpacking characters 
language = 'Python'
a,b,c,d,e,f = language # unpacking sequence characters into variables
print(a) # P
print(b) # y
print(c) # t 
print(d) # h
print(e) # o
print(f) # n

# Accessing characters in strings by index
language = 'Python'
first_letter = language[0]
print(first_letter) # P
second_letter = language[1]
print(second_letter) # y
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter) # n

# If we want to start from right end we can use negative indexing. -1 is the last index
language = 'Python'
last_letter = language[-1]
print(last_letter) # n
second_last = language[-2]
print(second_last) # o

# Slicing

language = 'Python'
first_three = language[0:3] # starts at zero index and up to 3 but not include 3
last_three = language[3:6]
print(last_three) # hon
# Another way
last_three = language[-3:]
print(last_three)   # hon
last_three = language[3:]
print(last_three)   # hon

# Skipping character while splitting Python strings
language = 'Python'
pto = language[0:6:2] # 
print(pto) # pto

# Escape sequence
print('I hope every one enjoying the python challenge.\nDo you ?') # line break
print('Days\tTopics\tExercises')
print('Day 1\t3\t5')
print('Day 2\t3\t5')
print('Day 3\t3\t5')
print('Day 4\t3\t5')
print('This is a back slash  symbol (\\)') # To write a back slash
print('In every programming language it starts with \"Hello, World!\"')

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = 'thirty days of python'
print(challenge.capitalize()) # 'Thirty days of python'

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)

challenge = 'thirty days of python'
print(challenge.count('y')) # 3
print(challenge.count('y', 7, 14)) # 1
print(challenge.count('th')) # 2`

# endswith(): Checks if a string ends with a specified ending

challenge = 'thirty days of python'
print(challenge.endswith('on'))   # True
print(challenge.endswith('tion')) # False

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument

challenge = 'thirty\tdays\tof\tpython'
print(challenge.expandtabs())   # 'thirty  days    of      python'
print(challenge.expandtabs(10)) # 'thirty    days      of        python'

# find(): Returns the index of first occurrence of substring

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# format()	formats string into nicer output    
first_name = 'Asabeneh'
last_name = 'Yetayeh'
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I live in {}.'.format(first_name, last_name, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi # radius ## 2
result = 'The area of circle with {} is {}'.format(str(radius), str(area))
print(result) # The area of circle with 10 is 314.0

# index(): Returns the index of substring
challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isalnum(): Checks alphanumeric character

challenge = 'ThirtyDaysPython'
print(challenge.isalnum()) # True

challenge = '30DaysPython'
print(challenge.isalnum()) # True

challenge = 'thirty days of python'
print(challenge.isalnum()) # False

challenge = 'thirty days of python 2019'
print(challenge.isalnum()) # False

# isalpha(): Checks if all characters are alphabets

challenge = 'thirty days of python'
print(challenge.isalpha()) # True
num = '123'
print(num.isalpha())      # False

# isdecimal(): Checks Decimal Characters

challenge = 'thirty days of python'
print(challenge.find('y'))  # 5
print(challenge.find('th')) # 0

# isdigit(): Checks Digit Characters

challenge = 'Thirty'
print(challenge.isdigit()) # False
challenge = '30'
print(challenge.digit())   # True

# isdecimal():Checks decimal characters

num = '10'
print(num.isdecimal()) # True
num = '10.5'
print(num.isdecimal()) # False


# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = '30DaysOfPython'
print(challenge.isidentifier()) # False, because it starts with a number
challenge = 'thirty_days_of_python'
print(challenge.isidentifier()) # True


# islower():Checks if all alphabets in a string are lowercase

challenge = 'thirty days of python'
print(challenge.islower()) # True
challenge = 'Thirty days of python'
print(challenge.islower()) # False

# isupper(): returns if all characters are uppercase characters

challenge = 'thirty days of python'
print(challenge.isupper()) #  False
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) # True


# isnumeric():Checks numeric characters

num = '10'
print(num.isnumeric())      # True
print('ten'.isnumeric())    # False

# join(): Returns a concatenated string

web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
result = '#, '.join(web_tech)
print(result) # 'HTML# CSS# JavaScript# React'

# strip(): Removes both leading and trailing characters

challenge = ' thirty days of python '
print(challenge.strip('y')) # 5

# replace(): Replaces substring inside

challenge = 'thirty days of python'
print(challenge.replace('python', 'coding')) # 'thirty days of coding'

# split():Splits String from Left

challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']

# title(): Returns a Title Cased String

challenge = 'thirty days of python'
print(challenge.title()) # Thirty Days Of Python

# swapcase(): Checks if String Starts with the Specified String
  
challenge = 'thirty days of python'
print(challenge.swapcase())   # THIRTY DAYS OF PYTHON
challenge = 'Thirty Days Of Python'
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON

# startswith(): Checks if String Starts with the Specified String

challenge = 'thirty days of python'
print(challenge.startswith('thirty')) # True
challenge = '30 days of python'
print(challenge.startswith('thirty')) # False







print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
print('Day 1\t5\t5')
print('Day 2\t6\t20')
print('Day 3\t5\t23')
print('Day 4\t1\t35')
print('This is a backslash  symbol (\\)') # To write a backslash
print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote

# output
# I hope every one is enjoying the Python Challenge.
# Are you ?
# Days	Topics	Exercises
# Day 1	5	    5
# Day 2	6	    20
# Day 3	5	    23
# Day 4	1	    35
# This is a backslash  symbol (\)
# In every programming language it starts with "Hello, World!"







# 1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'. 
# 1. გააერთიანეთ სტრიქონები „Thirty“, „Days“, „Of“, „Python“ ერთ სტრიქონად, „Thirty Days Of Python“.

# w1
print('Thirty Days Of Python')

# W2



# 2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
# 3. Declare a variable named company and assign it to an initial value "Coding For All".
# 4. Print the variable company using _print()_.
# 5. Print the length of the company string using _len()_ method and _print()_.
# 6. Change all the characters to uppercase letters using _upper()_ method.
# 7. Change all the characters to lowercase letters using _lower()_ method.
# 8. Use capitalize(), title(), swapcase() methods to format the value of the string _Coding For All_.
# 9. Cut(slice) out the first word of _Coding For All_ string.
# 10. Check if _Coding For All_ string contains a word Coding using the method index, find or other methods.
# 11. Replace the word coding in the string 'Coding For All' to Python.
# 12. Change Python for Everyone to Python for All using the replace method or other methods.
# 13. Split the string 'Coding For All' using space as the separator (split()) .
# 14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
# 15. What is the character at index 0 in the string _Coding For All_.
# 16. What is the last index of the string _Coding For All_.
# 17. What character is at index 10 in "Coding For All" string.
# 18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
# 19. Create an acronym or an abbreviation for the name 'Coding For All'.
# 20. Use index to determine the position of the first occurrence of C in Coding For All.
# 21. Use index to determine the position of the first occurrence of F in Coding For All.
# 22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
# 23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 26. Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 27. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
# 28. Does '\'Coding For All' start with a substring _Coding_?
# 29. Does 'Coding For All' end with a substring _coding_?
# 30. '&nbsp;&nbsp; Coding For All &nbsp;&nbsp;&nbsp; &nbsp;' &nbsp;, remove the left and right trailing spaces in the given string.
# 31. Which one of the following variables return True when we use the method isidentifier():
#     - 30DaysOfPython
#     - thirty_days_of_python
# 32. The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
# 33. Use the new line escape sequence to separate the following sentences.
#     ```py
#     I am enjoying this challenge.
#     I just wonder what is next.
#     ```
# 34. Use a tab escape sequence to write the following lines.
#     ```py
#     Name      Age     Country   City
#     Asabeneh  250     Finland   Helsinki
#     ```
# 35. Use the string formatting method to display the following:

# ```sh
# radius = 10
# area = 3.14 * radius ** 2
# The area of a circle with radius 10 is 314 meters square.
# ```

# 36. Make the following using string formatting methods:

# ```sh
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144
# ```
