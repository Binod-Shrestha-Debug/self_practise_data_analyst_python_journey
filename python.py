
# ==========================================
# Python Examples - Basic to Intermediate
# ==========================================


# 1. VARIABLES AND DATA TYPES

name = "Binod"
age = 25
height = 5.7
is_student = True

print("\n1. Variables and Data Types")
print(name, age, height, is_student)


# 2. TYPE CASTING

number = "100"
number = int(number)

print("\n2. Type Casting")
print(number + 50)


# 3. OPERATORS

a = 10
b = 3

print("\n3. Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 4. IF, ELIF, ELSE

marks = 75

print("\n4. If-Elif-Else")

if marks >= 80:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
elif marks >= 40:
    print("Grade C")
else:
    print("Fail")


# 5. NESTED IF

age = 22
has_id = True

print("\n5. Nested If")

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")
else:
    print("Underage")


# 6. MATCH-CASE

day = 3

print("\n6. Match-Case")

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case _:
        print("Invalid day")


# 7. FOR LOOP

print("\n7. For Loop")

for i in range(1, 6):
    print(i)


# 8. WHILE LOOP

print("\n8. While Loop")

count = 1

while count <= 5:
    print(count)
    count += 1


# 9. BREAK AND CONTINUE

print("\n9. Break")

for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\nContinue")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


# 10. LIST

numbers = [10, 20, 30, 40]

print("\n10. List")
print(numbers)
print("First item:", numbers[0])

numbers.append(50)
print("After append:", numbers)


# 11. TUPLE

colors = ("red", "green", "blue")

print("\n11. Tuple")
print(colors)
print("First color:", colors[0])


# 12. SET

unique_numbers = {10, 20, 20, 30}

print("\n12. Set")
print(unique_numbers)  # Duplicate values are removed


# 13. DICTIONARY

student = {
    "name": "Binod",
    "age": 25,
    "grade": "A"
}

print("\n13. Dictionary")
print(student)
print("Name:", student["name"])


# 14. STRING METHODS

text = "  python programming  "

print("\n14. String Methods")
print(text.upper())
print(text.lower())
print(text.strip())
print(text.replace("python", "Java"))
print(text.strip().split())


# 15. FUNCTIONS

def add(a, b):
    return a + b


print("\n15. Functions")
print("Sum:", add(10, 20))


# 16. DEFAULT ARGUMENT

def greet(name="Friend"):
    print("Hello", name)


print("\n16. Default Argument")
greet()
greet("Binod")


# 17. *ARGS

def total(*numbers):
    return sum(numbers)


print("\n17. *args")
print(total(10, 20, 30, 40))


# 18. **KWARGS

def show_details(**details):
    for key, value in details.items():
        print(key, ":", value)


print("\n18. **kwargs")
show_details(name="Binod", age=25, city="Kathmandu")


# 19. LIST COMPREHENSION

squares = [number ** 2 for number in range(1, 6)]

print("\n19. List Comprehension")
print(squares)


# 20. EXCEPTION HANDLING

print("\n20. Exception Handling")

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero.")
finally:
    print("Calculation finished.")


# 21. FILE HANDLING

print("\n21. File Handling")

# Write text to a file
with open("practice.txt", "w") as file:
    file.write("Learning Python file handling.")

# Read text from the file
with open("practice.txt", "r") as file:
    print(file.read())


# 22. CLASS AND OBJECT

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_info(self):
        print("Name:", self.name)
        print("Age:", self.age)


print("\n22. Class and Object")

student1 = Student("Binod", 25)
student1.show_info()


# 23. INHERITANCE

class Animal:
    def eat(self):
        print("Animal is eating.")


class Dog(Animal):
    def bark(self):
        print("Dog is barking.")


print("\n23. Inheritance")

dog = Dog()
dog.eat()
dog.bark()


# 24. LAMBDA FUNCTION

double = lambda number: number * 2

print("\n24. Lambda Function")
print(double(5))


# 25. DICTIONARY COMPREHENSION

number_squares = {
    number: number ** 2
    for number in range(1, 6)
}

print("\n25. Dictionary Comprehension")
print(number_squares)


# ==========================================
# END OF PYTHON EXAMPLES
# ==========================================

print("\nAll Python examples completed.")
