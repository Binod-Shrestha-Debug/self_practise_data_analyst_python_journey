rules.py

# ==================================================
# PYTHON RULES AND FUNDAMENTALS
# Author: Binod Shrestha
# ==================================================

# 1. PRINT STATEMENT
print("Hello, World!")
print("Welcome to Python")


# 2. VARIABLES
name = "Binod"
age = 25
height = 5.8
is_student = True

print(name)
print(age)
print(height)
print(is_student)


# 3. DATA TYPES
text = "Python"       # String (str)
number = 10           # Integer (int)
price = 99.50         # Float (float)
active = True         # Boolean (bool)

print(type(text))
print(type(number))
print(type(price))
print(type(active))


# 4. USER INPUT
user_name = input("Enter your name: ")
print("Hello,", user_name)

# Convert input when you need a number
# age = int(input("Enter your age: "))
# price = float(input("Enter a price: "))


# 5. NAMING RULES
# Valid variable names
first_name = "Binod"
age2 = 25
_total = 100

# Variable names are case-sensitive
score = 10
Score = 20

# Invalid examples (keep these commented)
# 2name = "Binod"       # Cannot start with a number
# first-name = "Binod"  # Hyphen is not allowed
# class = "Python"      # Reserved keyword


# 6. COMMENTS
# This is a single-line comment

"""
This is a multiline string.
It is sometimes used as a
documentation string.
"""


# 7. ARITHMETIC OPERATORS
a = 10
b = 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor division: 3
print(a % b)   # Remainder: 1
print(a ** b)  # Power: 1000


# 8. COMPARISON OPERATORS
x = 10
y = 5

print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to


# 9. LOGICAL OPERATORS
age = 20

print(age > 18 and age < 30)
print(age < 18 or age == 20)
print(not age < 18)


# 10. ASSIGNMENT OPERATORS
number = 10

number += 5   # Same as number = number + 5
print(number)

number -= 2   # Same as number = number - 2
print(number)

number *= 2   # Same as number = number * 2
print(number)

number /= 2   # Same as number = number / 2
print(number)


# 11. IF, ELIF, ELSE
marks = 75

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Grade C")


# 12. INDENTATION
# Python uses indentation to define code blocks.
if True:
    print("This line is indented correctly")


# 13. FOR LOOP
for i in range(1, 6):
    print(i)

# range(1, 6) prints 1 through 5.
# The ending number is not included.


# 14. WHILE LOOP
count = 1

while count <= 5:
    print(count)
    count += 1


# 15. BREAK AND CONTINUE
for i in range(1, 6):
    if i == 3:
        break
    print(i)  # Stops before printing 3

for i in range(1, 6):
    if i == 3:
        continue
    print(i)  # Skips 3


# 16. STRINGS
message = "Learn Python"

print(message.upper())
print(message.lower())
print(message.title())
print(len(message))
print(message[0])
print(message[0:5])


# 17. LISTS
fruits = ["Apple", "Banana", "Mango"]

fruits.append("Orange")
print(fruits)

fruits.remove("Banana")
print(fruits)

print(fruits[0])
print(len(fruits))


# 18. TUPLES
colors = ("Red", "Green", "Blue")

print(colors[0])
print(len(colors))

# Tuples cannot be modified after creation.


# 19. DICTIONARIES
student = {
    "name": "Binod",
    "age": 25,
    "course": "Python"
}

print(student["name"])
print(student["age"])

student["age"] = 26
print(student)


# 20. SETS
unique_numbers = {1, 2, 3, 3, 4}

print(unique_numbers)

# Sets store unique values and do not guarantee
# a particular display order.


# 21. FUNCTIONS
def greet(name):
    print("Hello,", name)

greet("Binod")


# 22. RETURN STATEMENT
def add(a, b):
    return a + b

result = add(10, 5)
print(result)


# 23. MEMBERSHIP OPERATORS
languages = ["Python", "Java", "SQL"]

print("Python" in languages)
print("C++" not in languages)


# 24. TYPE CONVERSION
number_text = "100"

number = int(number_text)
decimal_number = float(number_text)
text_number = str(number)

print(number)
print(decimal_number)
print(text_number)


# 25. EXCEPTION HANDLING
try:
    number = int(input("Enter a whole number: "))
    print("You entered:", number)
except ValueError:
    print("Please enter a valid whole number.")


# 26. F-STRINGS
name = "Binod"
score = 90

print(f"{name} scored {score} marks.")


# 27. FILE HANDLING
# Uncomment to create and write to a text file.
#
# with open("notes.txt", "w", encoding="utf-8") as file:
#     file.write("I am learning Python.")


# 28. IMPORTANT PYTHON RULES
# - Python is case-sensitive.
# - Indentation matters.
# - Variable names cannot start with numbers.
# - Do not use reserved keywords as variable names.
# - Use quotes around string values.
# - Use parentheses when calling functions.
# - Use a colon (:) after if, elif, else, for,
#   while, try, except, and function definitions.
# - input() returns a string by default.
# - Use meaningful variable names.
# - Comments begin with #.


print("\nPython rules and fundamentals completed!")
