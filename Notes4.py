import json
from random import randint

# for-else Loop
# else runs only if loop DOES NOT break
numbers = [1, 3, 5, 7]
for num in numbers:

    if num == 2:
        print("Found")
        break
else:
    print("Not found")

# pass Keyword
# pass does nothing
# useful for unfinished code
for i in range(5):
    pass


# zip()
# combines multiple lists together
names = ["Kamya", "Het"]
marks = [90, 80]
for n, m in zip(names, marks):
    print(n, m)

# Lambda Functions
# short anonymous functions
def square(x):
    return x * x
print(square(5))

# map()
# applies function to every element
nums = [1, 2, 3]
result = list(map(lambda x: x * 2, nums))
print(result)

# filter()
# filters values using condition
nums = [1, 2, 3, 4, 5]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Import Specific Functions
# cleaner imports
print(randint(1, 10))

# if __name__ == "__main__"
# used in real Python projects
def greet():
    print("Hello")
if __name__ == "__main__":
    greet()

# Basic Exception Types
try:
    num = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Common Exceptions:
# ValueError
# TypeError
# IndexError
# KeyError
# ZeroDivisionError

# join()
# converts list -> string
words = ["Python", "is", "fun"]
sentence = " ".join(words)
print(sentence)

# split()
# converts string -> list
text = "apple mango banana"
items = text.split()
print(items)

# Simple Recursion
# function calling itself
def countdown(n):

    if n == 0:
        return

    print(n)

    countdown(n - 1)
countdown(5)

# Copy vs Reference
# both variables point to same list
a = [1, 2, 3]
b = a
b[0] = 100
print(a)

# proper copy
b = a.copy()


# Nested Loops
for i in range(3):

    for j in range(3):
        print(i, j)

# Simple Pattern Program
for i in range(5):
    print("*" * i)

# any() and all()
nums = [True, True, False]
print(any(nums))
print(all(nums))
# any() -> True if at least one value is True
# all() -> True only if all values are True


# Ternary Operator
# short if-else
age = 18
message = "Adult" if age >= 18 else "Minor"
print(message)


# is vs ==
a = [1, 2]
b = [1, 2]
print(a == b)   # checks value
print(a is b)   # checks memory location

# Simple JSON
# useful for APIs and data storage
data = {
    "name": "Kamya",
    "age": 18
}
text = json.dumps(data)
print(text)


# Virtual Environment
# used to manage project packages

# create virtual environment
# python -m venv myenv


# Common Beginner Mistakes--->
# forgetting colon :
# wrong indentation
# infinite loops
# forgetting input() conversion
# modifying list while looping

age = input("Enter age: ")
print(int(age) + 5)