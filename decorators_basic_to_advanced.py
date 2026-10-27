
"""
=========================================================
PYTHON DECORATORS: BASIC TO ADVANCED
Author: Binod Shrestha
Purpose: Learn decorators through examples, questions,
         answers, and practical exercises.
=========================================================

Topics:
1. What is a decorator?
2. Functions as arguments
3. Inner functions
4. Basic decorators
5. Multiple function calls
6. Decorators with arguments (*args, **kwargs)
7. Returning values
8. functools.wraps
9. Decorators with parameters
10. Multiple decorators
11. Execution time decorator
12. Repeat decorator
13. Class-based decorators
14. Questions and answers
"""


# =========================================================
# 1. BASIC CONCEPT: FUNCTIONS AS ARGUMENTS
# =========================================================

print("\n========== 1. FUNCTIONS AS ARGUMENTS ==========")


def greet():
    print("Hello, welcome to Python!")


def execute_function(func):
    func()


execute_function(greet)

# Explanation:
# A function can be passed as an argument to another function.
# Here, greet is passed without parentheses.


# =========================================================
# 2. INNER FUNCTION
# =========================================================

print("\n========== 2. INNER FUNCTION ==========")


def outer_function():
    print("This is the outer function.")

    def inner_function():
        print("This is the inner function.")

    inner_function()


outer_function()


# =========================================================
# 3. YOUR FIRST DECORATOR
# =========================================================

print("\n========== 3. BASIC DECORATOR ==========")


def my_decorator(func):
    def wrapper():
        print("Before the function")
        func()
        print("After the function")

    return wrapper


@my_decorator
def say_hello():
    print("Hello, Binod!")


say_hello()

# @my_decorator is equivalent to:
# say_hello = my_decorator(say_hello)


# =========================================================
# 4. DECORATOR WITHOUT @ SYNTAX
# =========================================================

print("\n========== 4. WITHOUT @ SYNTAX ==========")


def simple_decorator(func):
    def wrapper():
        print("Function is starting.")
        func()

    return wrapper


def show_message():
    print("Learning Python decorators.")


show_message = simple_decorator(show_message)
show_message()


# =========================================================
# 5. DECORATOR WITH MULTIPLE FUNCTION CALLS
# =========================================================

print("\n========== 5. MULTIPLE FUNCTION CALLS ==========")


def welcome_decorator(func):
    def wrapper():
        print("Welcome to Python!")
        func()

    return wrapper


@welcome_decorator
def first_function():
    print("This is the first function.")


@welcome_decorator
def second_function():
    print("This is the second function.")


first_function()
second_function()


# =========================================================
# 6. DECORATOR WITH ARGUMENTS: *args AND **kwargs
# =========================================================

print("\n========== 6. FUNCTION ARGUMENTS ==========")


def argument_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calling the function...")
        return func(*args, **kwargs)

    return wrapper


@argument_decorator
def add(a, b):
    print("Sum:", a + b)


@argument_decorator
def introduce(name, city):
    print(f"My name is {name}. I live in {city}.")


add(10, 20)
introduce(name="Binod", city="Kathmandu")


# =========================================================
# 7. DECORATOR THAT RETURNS A VALUE
# =========================================================

print("\n========== 7. RETURNING VALUES ==========")


def result_decorator(func):
    def wrapper(*args, **kwargs):
        print("Calculating result...")
        result = func(*args, **kwargs)
        print("Calculation completed.")
        return result

    return wrapper


@result_decorator
def multiply(a, b):
    return a * b


answer = multiply(5, 4)
print("Returned answer:", answer)


# =========================================================
# 8. USING FUNCTOOLS.WRAPS
# =========================================================

print("\n========== 8. FUNCTOOLS.WRAPS ==========")

from functools import wraps


def information_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Executing:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@information_decorator
def show_information():
    """Display a simple information message."""
    print("Decorators can preserve function information.")


show_information()

print("Function name:", show_information.__name__)
print("Function documentation:", show_information.__doc__)

# @wraps(func) preserves useful metadata such as
# the original function's name and documentation.


# =========================================================
# 9. DECORATOR WITH ITS OWN PARAMETERS
# =========================================================

print("\n========== 9. DECORATOR PARAMETERS ==========")


def repeat(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say_python():
    print("I am learning Python!")


say_python()

# repeat(3) means the decorated function runs three times.


# =========================================================
# 10. STACKING MULTIPLE DECORATORS
# =========================================================

print("\n========== 10. MULTIPLE DECORATORS ==========")


def star_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("*" * 30)
        result = func(*args, **kwargs)
        print("*" * 30)
        return result

    return wrapper


def uppercase_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        if isinstance(result, str):
            return result.upper()

        return result

    return wrapper


@star_decorator
@uppercase_decorator
def get_message():
    return "hello from binod"


print(get_message())

# Decorators are applied from the bottom upward.
# uppercase_decorator wraps get_message first.
# star_decorator wraps the result afterward.


# =========================================================
# 11. PRACTICAL EXAMPLE: EXECUTION TIME
# =========================================================

print("\n========== 11. EXECUTION TIME ==========")

import time


def execution_timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            end_time = time.perf_counter()
            elapsed = end_time - start_time
            print(f"{func.__name__} took {elapsed:.6f} seconds")

    return wrapper


@execution_timer
def count_numbers():
    total = 0

    for number in range(100_000):
        total += number

    return total


print("Total:", count_numbers())


# =========================================================
# 12. PRACTICAL EXAMPLE: CHECKING ARGUMENTS
# =========================================================

print("\n========== 12. ARGUMENT VALIDATION ==========")


def positive_numbers_only(func):
    @wraps(func)
    def wrapper(a, b):
        if a < 0 or b < 0:
            raise ValueError("Both numbers must be non-negative.")

        return func(a, b)

    return wrapper


@positive_numbers_only
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")

    return a / b


print("Division result:", divide(10, 2))

# Try divide(-10, 2) to see the validation error.
# Try divide(10, 0) to see the zero-division check.


# =========================================================
# 13. CLASS-BASED DECORATOR
# =========================================================

print("\n========== 13. CLASS-BASED DECORATOR ==========")


class CallCounter:
    def __init__(self, func):
        wraps(func)(self)
        self.func = func
        self.calls = 0

    def __call__(self, *args, **kwargs):
        self.calls += 1
        print("Function called:", self.calls, "time(s)")
        return self.func(*args, **kwargs)


@CallCounter
def display_name(name):
    print("Name:", name)


display_name("Binod")
display_name("Shrestha")
display_name("Binod Shrestha")


# =========================================================
# 14. QUESTION AND ANSWER SECTION
# =========================================================

print("\n========== 14. QUESTIONS AND ANSWERS ==========")


# Q1. What is a decorator?
#
# Answer:
# A decorator is a callable that takes another function
# or callable and returns a wrapped or modified callable.


# Q2. What does the @ symbol do?
#
# Answer:
# It applies a decorator to a function or class.
#
# Example:
# @my_decorator
# def greet():
#     print("Hello")
#
# Equivalent to:
# def greet():
#     print("Hello")
#
# greet = my_decorator(greet)


# Q3. What is a wrapper function?
#
# Answer:
# A wrapper is a function inside a decorator that adds
# behavior before or after calling the original function.


# Q4. Why do we use *args and **kwargs?
#
# Answer:
# They allow a wrapper to accept positional and keyword
# arguments without knowing their exact names in advance.


# Q5. Why do we use functools.wraps?
#
# Answer:
# It preserves important metadata from the original
# function, including its name and documentation.


# Q6. Can a decorator return a value?
#
# Answer:
# Yes. The wrapper should return the original function's
# result when that result needs to be preserved.


# Q7. Can we use more than one decorator?
#
# Answer:
# Yes. Multiple decorators can be stacked on a function.
# They are applied from the bottom upward.


# Q8. What is a parameterized decorator?
#
# Answer:
# It is a decorator factory that accepts its own arguments,
# such as @repeat(3).


# Q9. Where are decorators used in real projects?
#
# Answer:
# Logging, timing, caching, authorization, validation,
# and web frameworks.


# Q10. What is a class-based decorator?
#
# Answer:
# A class can act as a decorator by implementing __call__.
# An instance of that class can then wrap function calls.


# =========================================================
# 15. PRACTICE QUESTIONS WITH ANSWERS
# =========================================================

print("\n========== 15. PRACTICE QUESTIONS ==========")


# ---------------------------------------------------------
# QUESTION 1
# Create a decorator that prints "Starting..."
# before calling the function.
#
# ANSWER:
# ---------------------------------------------------------

def starting_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Starting...")
        return func(*args, **kwargs)

    return wrapper


@starting_decorator
def task_one():
    print("Task one is running.")


task_one()


# ---------------------------------------------------------
# QUESTION 2
# Create a decorator that prints "Finished!"
# after calling the function.
#
# ANSWER:
# ---------------------------------------------------------

def finished_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print("Finished!")
        return result

    return wrapper


@finished_decorator
def task_two():
    print("Task two is running.")


task_two()


# ---------------------------------------------------------
# QUESTION 3
# Create a decorator that doubles a returned number.
#
# ANSWER:
# ---------------------------------------------------------

def double_result(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2

    return wrapper


@double_result
def get_number():
    return 10


print("Doubled result:", get_number())


# ---------------------------------------------------------
# QUESTION 4
# Create a decorator that runs a function twice.
#
# ANSWER:
# ---------------------------------------------------------

@repeat(2)
def practice_message():
    print("Practice makes progress!")


practice_message()


# ---------------------------------------------------------
# QUESTION 5
# Create a decorator that logs a function's name.
#
# ANSWER:
# ---------------------------------------------------------

def log_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Running function:", func.__name__)
        return func(*args, **kwargs)

    return wrapper


@log_name
def calculate_total(a, b):
    return a + b


print("Total:", calculate_total(15, 25))


# =========================================================
# END OF PYTHON DECORATORS
# =========================================================

print("\nAll decorator examples completed!")
