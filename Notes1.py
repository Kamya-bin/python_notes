# Modules: are reusable Python files. We can import them to use their functions. The random module allows us to generate random numbers.
# modules are always at the top of the file. We can import multiple modules if needed.
import random 
import time

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