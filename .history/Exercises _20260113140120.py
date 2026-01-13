
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

print(not ('on' in 'dragon' and 'on' in 'python'))~

# 16. Find the length of the text _python_ and convert the value to float and convert it to string
?


# 17. Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
# 18. Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# 19. Check if type of '10' is equal to type of 10
# 20. Check if int('9.8') is equal to 10
# 21. Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person? 
# 22. Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
# 23. Write a Python script that displays the following table

# ```py
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125
# ```
