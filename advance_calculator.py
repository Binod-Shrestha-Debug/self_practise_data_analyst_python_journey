
"""
=========================================================
ADVANCED CALCULATOR
Author: Binod Shrestha
Description: Menu-driven calculator with advanced
             mathematical operations.
=========================================================
"""

import math


# =========================================================
# BASIC OPERATIONS
# =========================================================

def addition(a, b):
    return a + b


def subtraction(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def modulus(a, b):
    if b == 0:
        raise ValueError("Cannot calculate modulus by zero.")
    return a % b


def power(a, b):
    return a ** b


def floor_division(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a // b


# =========================================================
# ADVANCED OPERATIONS
# =========================================================

def square_root(a):
    if a < 0:
        raise ValueError("Cannot calculate the real square root of a negative number.")
    return math.sqrt(a)


def factorial(a):
    if not a.is_integer():
        raise ValueError("Factorial requires a whole number.")

    if a < 0:
        raise ValueError("Factorial requires a non-negative number.")

    if a > 170:
        raise ValueError("Number is too large for this calculator.")

    return math.factorial(int(a))


def percentage(a, b):
    return (a * b) / 100


def absolute_value(a):
    return abs(a)


def logarithm(a):
    if a <= 0:
        raise ValueError("Logarithm requires a positive number.")
    return math.log10(a)


def natural_logarithm(a):
    if a <= 0:
        raise ValueError("Natural logarithm requires a positive number.")
    return math.log(a)


def sine(a):
    return math.sin(math.radians(a))


def cosine(a):
    return math.cos(math.radians(a))


def tangent(a):
    if math.isclose(a % 180, 90, abs_tol=1e-10):
        raise ValueError("Tangent is undefined at this angle.")
    return math.tan(math.radians(a))


# =========================================================
# INPUT HELPERS
# =========================================================

def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a number.")


# =========================================================
# DISPLAY MENU
# =========================================================

def show_menu():
    print("\n" + "=" * 48)
    print("          ADVANCED PYTHON CALCULATOR")
    print("=" * 48)

    print("\nBASIC OPERATIONS")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (**)")
    print("7. Floor Division (//)")

    print("\nADVANCED OPERATIONS")
    print("8. Square Root")
    print("9. Factorial")
    print("10. Percentage")
    print("11. Absolute Value")
    print("12. Logarithm (base 10)")
    print("13. Natural Logarithm (ln)")
    print("14. Sine (degrees)")
    print("15. Cosine (degrees)")
    print("16. Tangent (degrees)")

    print("\nOTHER OPTIONS")
    print("0. Exit")
    print("=" * 48)


# =========================================================
# CALCULATOR LOGIC
# =========================================================

def calculator():
    while True:
        show_menu()

        choice = input("Choose an operation (0-16): ").strip()

        if choice == "0":
            print("Thank you for using the calculator!")
            break

        try:
            if choice == "1":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = addition(a, b)

            elif choice == "2":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = subtraction(a, b)

            elif choice == "3":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = multiplication(a, b)

            elif choice == "4":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = division(a, b)

            elif choice == "5":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = modulus(a, b)

            elif choice == "6":
                a = get_number("Enter base: ")
                b = get_number("Enter exponent: ")
                result = power(a, b)

            elif choice == "7":
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")
                result = floor_division(a, b)

            elif choice == "8":
                a = get_number("Enter a number: ")
                result = square_root(a)

            elif choice == "9":
                a = get_number("Enter a whole number: ")
                result = factorial(a)

            elif choice == "10":
                a = get_number("Enter the amount: ")
                b = get_number("Enter the percentage: ")
                result = percentage(a, b)

            elif choice == "11":
                a = get_number("Enter a number: ")
                result = absolute_value(a)

            elif choice == "12":
                a = get_number("Enter a positive number: ")
                result = logarithm(a)

            elif choice == "13":
                a = get_number("Enter a positive number: ")
                result = natural_logarithm(a)

            elif choice == "14":
                a = get_number("Enter angle in degrees: ")
                result = sine(a)

            elif choice == "15":
                a = get_number("Enter angle in degrees: ")
                result = cosine(a)

            elif choice == "16":
                a = get_number("Enter angle in degrees: ")
                result = tangent(a)

            else:
                print("Invalid choice. Please select from 0 to 16.")
                continue

            print("-" * 48)
            print(f"Result: {result:.10g}")
            print("-" * 48)

        except (ValueError, OverflowError) as error:
            print(f"Error: {error}")

        except Exception as error:
            print(f"Unexpected error: {error}")


# =========================================================
# RUN THE PROGRAM
# =========================================================

if __name__ == "__main__":
    calculator()
