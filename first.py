print("This is my first python line of code")

# Data Types & Variables
age = 25
height = 5.75
name = "Oloyede"
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is he a student?:", is_student)

print(type(age))

# Control Flow
temperature = 30

if temperature > 25:
  print("It's is a hot day! 🌞")
else: 
  print("It's is a cool day! 🧊☃")


# Multiple conditions
marks = int(input("Enter the student's mark (0-100):"))
if marks > 70:
  print("Grade: Distinction 🏆")
elif marks >= 60:
  print("Grade: Credit 🏅")
elif marks >= 50:
  print("Grade: Pass 👍")
else:
  print("Grade: Fail ❌")


# LOOPS
# For loop
for i in range(5):
  print(i)

# While Loop
countdown = 5
while countdown > 0:
  print("counting down:", countdown)
  countdown -= 1

print("Blast off! 🚀")


# Lists
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

fruits[1] = "orange"
print(fruits)

fruits.append("grape")
print(fruits)

# Tuples
coordinates = (10,20)
print(coordinates[0])


# Sets
unique_numbers = {1,2,2,3,4}
print(unique_numbers)

# Dictionaries
student_info = {"name": "Daud", "age": 23, "grade": "A"}
print(student_info["name"])

student_info["age"] = 21
print(student_info)

# Function
def greet(name):
  print("Hello, " + name + "! 👋")

greet("Adebayo")
greet("Haleemah")

# Return Values
def add_numbers(x,y):
  return x + y

result = add_numbers(10, 5)
print(result)


#PYTHON TOOLKIT
# Math Module

import math

print(math.sqrt(25))

# Random module
import random

dice_roll = random.randint(1, 6)
print("You rolled a", dice_roll)