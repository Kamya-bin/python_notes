# This is a comment. It is ignored by Python and is used to explain code to humans who are lazy and explain to brainless people=(me😭).

#  Hello! I am Kamya learning python language. I am a beginner and I am excited to learn more about programming.
#  I hope to create some cool projects in the future. Let's get started!
#  Just me, forgot to introduce myself😅. I am not a student in Year 1 Btech (not started yet), I am 1 month early seeking some fun stuff✨.
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