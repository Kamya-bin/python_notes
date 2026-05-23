# Type Conversion
age = "18"
print(int(age) + 2)     # converts string to integer
print(float(age))       # converts string to decimal
print(str(100))         # converts integer to string
print(type(age))
print(type(int(age)))

# Comments
# Single-line comment
"""
Multi-line comment
used for explanation
"""

# range()
# range(start, stop, step)
for i in range(1, 10, 2):
    print(i)
# start = 1
# stop before 10
# step = +2

# List Slicing
nums = [1, 2, 3, 4, 5]
print(nums[0:3])   # elements from index 0 to 2
print(nums[:2])    # from beginning to index 1
print(nums[-1])    # last element

# String Slicing
name = "Kamya"
print(name[0:3])   # Kam
print(name[::-1])  # reverse string using step = -1

# Useful List Methods
nums = [5, 2, 8, 1]

nums.sort()        # ascending order
print(nums)

nums.reverse()     # reverse list
print(nums)

nums.pop()         # removes last element
print(nums)

nums.insert(1, 100)   # insert 100 at index 1
print(nums)

# break and continue
# break stops the loop completely
for i in range(5):
    if i == 3:
        break
    print(i)

print("------")

# continue skips current iteration
for i in range(5):
    if i == 3:
        continue
    print(i)

# Scope
x = 10   # global variable
def test():
    x = 5   # local variable
    print(x)

test()

print(x)

# local variable exists only inside function
# global variable exists everywhere

# Default Function Arguments
def greet(name="Guest"):
    print("Hello", name)
greet()
greet("Kamya")

# *args
# accepts multiple arguments
def add(*numbers):
    print(sum(numbers))
add(1, 2, 3, 4)

# **kwargs
# accepts keyword arguments
def info(**data):
    print(data)
info(name="Kamya", age=18)

# List Comprehension
# short way to create lists
nums = [x * x for x in range(5)]
print(nums)

# Enumerate
fruits = ["apple", "banana"]
for index, fruit in enumerate(fruits):
    print(index, fruit)
# enumerate gives index + value together



# with open()
# safer file handling
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
# file closes automatically

# Built-in Functions
nums = [1, 5, 2, 9]
print(len(nums))      # number of elements
print(type(nums))     # data type
print(sum(nums))      # total sum
print(max(nums))      # largest value
print(min(nums))      # smallest value
print(sorted(nums))   # returns sorted copy

# Mutable vs Immutable
# mutable = can change
# immutable = cannot change

# list is mutable
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)

# string is immutable
name = "Kamya"
# name[0] = "R"   # error
print(name)

# tuple is immutable
my_tuple = (1, 2, 3)
# my_tuple[0] = 5   # error

# Basic Debugging
value = "100"
print(type(value))
# useful for checking variable types

# read error messages carefully
# Python usually tells what went wrong