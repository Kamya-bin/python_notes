# This is a comment. It is ignored by Python and is used to explain code to humans.

# Modules: are reusable Python files. We can import them to use their functions. The random module allows us to generate random numbers.
# modules are always at the top of the file. We can import multiple modules if needed.
import random 
import time

#  Hello! I am Kamya learning python language and I am sharing my notes for better understanding.
#  Just me, forgot to introduce myself😅. I am a student.
#This tells Python to display text on the screen.
print("Hello world!")

#Variables (Storing Data)
# name stores text (string)
# age stores a number (integer)
name = "Kamya"
age = 123456
print(name)
print(age)

#Basic Math
a = 10
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)

# If Statements 
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# For loop:
for i in range(5):
    print(i)

# Functions (Reusable Code)
def greet(name):
    print("Hello " + name)
greet("Kamya")

# input - output
name = input("Enter your name: ")
print("Hello", name)

#  Data Types
# Python stores different kinds of data.

# Type	     Example
# String	 "hello"
# Integer	   10
# Float       3.14
# Boolean	  True
age = int(input("Enter your age: "))
print(age + 5)
# Example variables for different data types
name = "Kamya"
marks = 85
pi = 3.14
is_student = True

# Lists (Store Multiple Things)
fruits = ["apple", "banana", "mango"]
print(fruits)
print(fruits[0])

# Add Items to List [.append()]
fruits = ["apple", "banana"]
fruits.append("mango")
print(fruits)

# Loop Through List
fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

# Dictionaries: A dictionary stores data in key : value format.
# Example:
student = {
    "name": "Kamya",
    "age": 123456,
    "course": "xyz"
}
print(student["name"])
print(student["course"])

# Change Values
student["age"] = 3456
print(student)

# Add New Data
student["city"] = "abc"
print(student)

# While Loops
# A while loop repeats while condition is true.
count = 1
while count <= 5:
    print(count)
    count += 1

# Infinite Loop Example
# DO:  while True:
# then: print("Hello")
#  This runs forever unless stopped.I cant do in this terminal because it will crash. Be careful with infinite loops!

# Write File
file = open("notes.txt", "w")

file.write("Python is fun!")

file.close()
# This creates:
# notes.txt with the text "Python is fun!" inside it. If you run this code again, it will overwrite the file.
#  To add to the file instead of overwriting, use "a" mode:
# Read File
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

# Modules
# Modules are reusable Python files.
# Python already has many built-in modules. We can also create our own modules.
# Random Module
number = random.randint(1, 10)
print(number)

# Time Module
print("Start")
time.sleep(2)
print("End")
# Waits 2 seconds.

# String Operations
name = "Kamya"
print(name.upper())      # KAMYA
print(name.lower())      # kamya
print(len(name))         # length
print(name[0])           # first letter
print(name[-1])          # last letter

# String Formatting
name = "Kamya"
age = 18
print(f"My name is {name} and I am {age} years old.")

# User Input Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

# Comparison Operators
a = 10
b = 5
print(a > b)
print(a < b)
print(a == b)
print(a != b)

# Logical Operators
age = 20
has_id = True
if age >= 18 and has_id:
    print("Entry allowed")

# Nested If Statements
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")

# List Operations
numbers = [1, 2, 3]
numbers.append(4)
numbers.remove(2)
print(numbers)
print(len(numbers))

# Tuples
colors = ("red", "blue", "green")
print(colors[0])
# Tuples cannot be changed after creation.

# Sets
nums = {1, 2, 3, 3, 4}
print(nums)
# Sets remove duplicate values automatically.

# Functions With Return
def add(a, b):
    return a + b
result = add(5, 3)
print(result)

# Try Except (Error Handling)
try:
    num = int(input("Enter number: "))
    print(num)
except ValueError:
    # Dont use a bare except: because it can hide other errors and make debugging difficult.
    # This only runs if the user enters something that isn't a number
    # Why the warning?
# A bare except: catches every possible error, including ones you might not want to ignore. For example:
# If you try to stop the program by pressing Ctrl+C, a bare except might catch that signal and prevent the program from closing.
# If you have a typo in your variable name inside the try block, it will just say "Invalid input" instead of telling you there is a bug in your code.
    print("Invalid input")

# Random Password Generator
chars = "abcdefghijklmnopqrstuvwxyz123456789"
password = ""
for i in range(8):
    password += random.choice(chars)
print(password)

# Number Guessing Game
secret = random.randint(1, 10)
guess = int(input("Guess number: "))
if guess == secret:
    print("Correct!")
else:
    print("Wrong!")
    print("Number was", secret)

# Classes and Objects (Very Important Later)
class Student:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)
s1 = Student("Kamya")
s1.show()