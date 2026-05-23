import random

# User Input Calculator
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)
print("Division =", num1 / num2)

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