
"""
=========================================================
PYTHON LAMBDA: BASIC TO ADVANCED
Author: Binod Shrestha
Description: Lambda functions with examples, questions,
             answers, and practice exercises.
=========================================================
"""


# =========================================================
# 1. WHAT IS A LAMBDA FUNCTION?
# =========================================================

print("\n===== 1. BASIC LAMBDA =====")

# A lambda is a small anonymous function.
# Syntax: lambda arguments: expression

add = lambda a, b: a + b

print("Addition:", add(10, 20))
# Output: 30


# =========================================================
# 2. LAMBDA WITH ONE ARGUMENT
# =========================================================

print("\n===== 2. ONE ARGUMENT =====")

square = lambda number: number ** 2

print("Square:", square(5))
# Output: 25


# =========================================================
# 3. LAMBDA WITH MULTIPLE ARGUMENTS
# =========================================================

print("\n===== 3. MULTIPLE ARGUMENTS =====")

multiply = lambda a, b, c: a * b * c

print("Multiplication:", multiply(2, 3, 4))
# Output: 24


# =========================================================
# 4. LAMBDA WITH NO ARGUMENTS
# =========================================================

print("\n===== 4. NO ARGUMENTS =====")

greeting = lambda: "Hello, Binod!"

print(greeting())
# Output: Hello, Binod!


# =========================================================
# 5. LAMBDA WITH CONDITIONAL EXPRESSIONS
# =========================================================

print("\n===== 5. CONDITIONAL EXPRESSION =====")

check_number = lambda number: (
    "Even" if number % 2 == 0 else "Odd"
)

print(check_number(10))
print(check_number(7))


# =========================================================
# 6. LAMBDA WITH IF-ELSE
# =========================================================

print("\n===== 6. FIND THE LARGER NUMBER =====")

larger = lambda a, b: a if a > b else b

print("Larger number:", larger(15, 25))
# Output: 25


# =========================================================
# 7. LAMBDA WITH BUILT-IN FUNCTIONS
# =========================================================

print("\n===== 7. BUILT-IN FUNCTIONS =====")

numbers = [5, 2, 9, 1, 7]

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))

# Use lambda as a key for sorting.
students = [
    ("Ram", 75),
    ("Sita", 90),
    ("Hari", 82)
]

students_sorted = sorted(
    students,
    key=lambda student: student[1]
)

print("Students sorted by marks:", students_sorted)


# =========================================================
# 8. LAMBDA WITH MAP()
# =========================================================

print("\n===== 8. MAP =====")

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda n: n ** 2, numbers))

print("Squares:", squares)
# Output: [1, 4, 9, 16, 25]


# =========================================================
# 9. LAMBDA WITH FILTER()
# =========================================================

print("\n===== 9. FILTER =====")

numbers = [10, 15, 20, 25, 30, 35]

even_numbers = list(
    filter(lambda n: n % 2 == 0, numbers)
)

print("Even numbers:", even_numbers)
# Output: [10, 20, 30]


# =========================================================
# 10. LAMBDA WITH REDUCE()
# =========================================================

print("\n===== 10. REDUCE =====")

from functools import reduce

numbers = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)
# Output: 15

product = reduce(lambda a, b: a * b, numbers)

print("Product:", product)
# Output: 120


# =========================================================
# 11. SORTING USING LAMBDA
# =========================================================

print("\n===== 11. SORTING =====")

numbers = [40, 10, 30, 20, 50]

ascending = sorted(numbers, key=lambda n: n)
descending = sorted(numbers, key=lambda n: n, reverse=True)

print("Ascending:", ascending)
print("Descending:", descending)

# Sort words by length.
words = ["Python", "SQL", "Programming", "Data"]

words_sorted = sorted(words, key=lambda word: len(word))

print("Words by length:", words_sorted)


# =========================================================
# 12. LAMBDA WITH DICTIONARIES
# =========================================================

print("\n===== 12. DICTIONARIES =====")

employees = [
    {"name": "Ram", "salary": 30000},
    {"name": "Sita", "salary": 45000},
    {"name": "Hari", "salary": 35000}
]

employees_sorted = sorted(
    employees,
    key=lambda employee: employee["salary"]
)

for employee in employees_sorted:
    print(employee)


# =========================================================
# 13. LAMBDA WITH NESTED DATA
# =========================================================

print("\n===== 13. NESTED DATA =====")

products = [
    ("Laptop", 80000, 5),
    ("Mouse", 1000, 20),
    ("Keyboard", 2500, 10)
]

# Sort by price.
products_by_price = sorted(
    products,
    key=lambda product: product[1]
)

print("Products by price:", products_by_price)

# Calculate price multiplied by quantity.
values = list(
    map(lambda product: product[1] * product[2], products)
)

print("Inventory values:", values)


# =========================================================
# 14. LAMBDA WITH ANY() AND ALL()
# =========================================================

print("\n===== 14. ANY AND ALL =====")

numbers = [2, 4, 6, 8, 9]

has_odd = any(map(lambda n: n % 2 != 0, numbers))
all_even = all(map(lambda n: n % 2 == 0, numbers))

print("Has an odd number:", has_odd)
print("Are all numbers even:", all_even)


# =========================================================
# 15. LAMBDA WITH A FUNCTION
# =========================================================

print("\n===== 15. FUNCTION RETURNING LAMBDA =====")


def make_multiplier(factor):
    return lambda number: number * factor


double = make_multiplier(2)
triple = make_multiplier(3)

print("Double:", double(10))
print("Triple:", triple(10))


# =========================================================
# 16. LAMBDA WITH AVERAGE
# =========================================================

print("\n===== 16. AVERAGE =====")

average = lambda a, b, c: (a + b + c) / 3

print("Average:", average(70, 80, 90))
# Output: 80.0


# =========================================================
# 17. PRACTICAL EXAMPLE: SALES ANALYSIS
# =========================================================

print("\n===== 17. SALES ANALYSIS =====")

sales = [
    {"product": "Laptop", "amount": 80000},
    {"product": "Mouse", "amount": 1500},
    {"product": "Keyboard", "amount": 3000},
    {"product": "Monitor", "amount": 20000}
]

# Sort sales from highest to lowest.
sales_sorted = sorted(
    sales,
    key=lambda sale: sale["amount"],
    reverse=True
)

print("Sales ranked by amount:")

for sale in sales_sorted:
    print(sale["product"], ":", sale["amount"])

# Find high-value sales.
high_value_sales = list(
    filter(lambda sale: sale["amount"] >= 10000, sales)
)

print("High-value sales:", high_value_sales)

# Calculate total sales.
total_sales = reduce(
    lambda total, sale: total + sale["amount"],
    sales,
    0
)

print("Total sales:", total_sales)


# =========================================================
# 18. LAMBDA VS DEF
# =========================================================

print("\n===== 18. LAMBDA VS DEF =====")

# Lambda: best for short expressions.
add_lambda = lambda a, b: a + b


# def: better for complex or multi-step logic.
def add_function(a, b):
    return a + b


print("Lambda result:", add_lambda(10, 20))
print("Regular function result:", add_function(10, 20))


# =========================================================
# 19. QUESTIONS AND ANSWERS
# =========================================================

print("\n===== 19. QUESTIONS AND ANSWERS =====")

"""
Q1. What is a lambda function?
Answer: A small anonymous function defined with lambda.

Q2. Can a lambda take multiple arguments?
Answer: Yes. Example: lambda a, b: a + b

Q3. Can a lambda contain multiple statements?
Answer: No. A lambda body must be a single expression.

Q4. What does map() do?
Answer: Applies a function to each item in an iterable.

Q5. What does filter() do?
Answer: Selects items for which a condition is true.

Q6. What does reduce() do?
Answer: Combines iterable items into a single result.

Q7. Can lambda use if-else?
Answer: Yes, using a conditional expression.

Q8. Can lambda return a value?
Answer: Yes. Its expression result is returned automatically.

Q9. When should we use def instead?
Answer: When the logic is complex or needs multiple statements.

Q10. Is lambda always better than def?
Answer: No. Choose the clearest option for the task.
"""


# =========================================================
# 20. PRACTICE QUESTIONS WITH ANSWERS
# =========================================================

print("\n===== 20. PRACTICE QUESTIONS =====")


# QUESTION 1:
# Write a lambda that adds two numbers.
# ANSWER:

q1 = lambda a, b: a + b
print("Q1:", q1(5, 10))


# QUESTION 2:
# Write a lambda that cubes a number.
# ANSWER:

q2 = lambda n: n ** 3
print("Q2:", q2(3))


# QUESTION 3:
# Check whether a number is positive or not.
# ANSWER:

q3 = lambda n: "Positive" if n > 0 else "Zero or negative"
print("Q3:", q3(5))


# QUESTION 4:
# Filter numbers greater than 10.
# ANSWER:

q4 = list(filter(lambda n: n > 10, [5, 12, 8, 20, 15]))
print("Q4:", q4)


# QUESTION 5:
# Convert a list of names to uppercase.
# ANSWER:

q5 = list(map(lambda name: name.upper(), ["ram", "sita", "hari"]))
print("Q5:", q5)


# QUESTION 6:
# Sort numbers by their remainder when divided by 3.
# ANSWER:

q6 = sorted([8, 4, 7, 3, 10, 6], key=lambda n: n % 3)
print("Q6:", q6)


# QUESTION 7:
# Calculate the total of a list using reduce().
# ANSWER:

q7 = reduce(lambda a, b: a + b, [10, 20, 30, 40])
print("Q7:", q7)


# QUESTION 8:
# Find the highest-priced product.
# ANSWER:

q8 = max(products, key=lambda product: product[1])
print("Q8:", q8)


# QUESTION 9:
# Calculate a 10% discount on a price.
# ANSWER:

q9 = lambda price: price * 0.90
print("Q9:", q9(1000))


# QUESTION 10:
# Sort students by marks from highest to lowest.
# ANSWER:

q10 = sorted(students, key=lambda student: student[1], reverse=True)
print("Q10:", q10)


# =========================================================
# END OF FILE
# =========================================================

print("\nAll Python lambda examples completed!")
