# this exercies are from https://github.com/Asabeneh this guy 

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
print(type(country))
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


def grader(score):
    if score >1 or score  < 0.6:
        return 'F'
    elif score >=0.9:
        return 'A'
    elif score >=0.8:
        return 'B'
    elif score >=0.7:
        return 'C'
    else:
        return 'D'
    
    
name = 'ilo'
name.sl