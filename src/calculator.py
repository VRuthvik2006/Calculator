#!/usr/bin/env python3
"""
Advanced Calculator with Trigonometric and Mathematical Functions
"""

import math
import re
import sys
from typing import Union


class AdvancedCalculator:
    """
    A calculator class that supports basic arithmetic and advanced mathematical functions
    """

    def __init__(self):
        self.last_result = 0
        self.memory = 0

    def add(self, a: float, b: float) -> float:
        """Addition"""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Subtraction"""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Multiplication"""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Division with zero check"""
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def power(self, a: float, b: float) -> float:
        """Exponentiation"""
        return a**b

    def square_root(self, a: float) -> float:
        """Square root"""
        if a < 0:
            raise ValueError("Square root of negative number is not allowed")
        return math.sqrt(a)

    def sin(self, a: float, degrees: bool = True) -> float:
        """Sine function"""
        if degrees:
            a = math.radians(a)
        return math.sin(a)

    def cos(self, a: float, degrees: bool = True) -> float:
        """Cosine function"""
        if degrees:
            a = math.radians(a)
        return math.cos(a)

    def tan(self, a: float, degrees: bool = True) -> float:
        """Tangent function"""
        if degrees:
            a = math.radians(a)
        return math.tan(a)

    def asin(self, a: float, degrees: bool = True) -> float:
        """Arc sine function"""
        if not -1 <= a <= 1:
            raise ValueError("Arc sine input must be between -1 and 1")
        result = math.asin(a)
        return math.degrees(result) if degrees else result

    def acos(self, a: float, degrees: bool = True) -> float:
        """Arc cosine function"""
        if not -1 <= a <= 1:
            raise ValueError("Arc cosine input must be between -1 and 1")
        result = math.acos(a)
        return math.degrees(result) if degrees else result

    def atan(self, a: float, degrees: bool = True) -> float:
        """Arc tangent function"""
        result = math.atan(a)
        return math.degrees(result) if degrees else result

    def log(self, a: float, base: float = math.e) -> float:
        """Logarithm with custom base (default: natural log)"""
        if a <= 0:
            raise ValueError("Logarithm input must be positive")
        if base <= 0 or base == 1:
            raise ValueError("Logarithm base must be positive and not equal to 1")
        return math.log(a, base)

    def log10(self, a: float) -> float:
        """Base-10 logarithm"""
        if a <= 0:
            raise ValueError("Logarithm input must be positive")
        return math.log10(a)

    def ln(self, a: float) -> float:
        """Natural logarithm"""
        if a <= 0:
            raise ValueError("Natural logarithm input must be positive")
        return math.log(a)

    def factorial(self, n: int) -> int:
        """Factorial function"""
        if not isinstance(n, int) or n < 0:
            raise ValueError("Factorial input must be a non-negative integer")
        return math.factorial(n)

    def absolute(self, a: float) -> float:
        """Absolute value"""
        return abs(a)

    def ceiling(self, a: float) -> int:
        """Ceiling function"""
        return math.ceil(a)

    def floor(self, a: float) -> int:
        """Floor function"""
        return math.floor(a)

    def round_number(self, a: float, decimals: int = 0) -> float:
        """Round to specified decimal places"""
        return round(a, decimals)

    def degrees_to_radians(self, degrees: float) -> float:
        """Convert degrees to radians"""
        return math.radians(degrees)

    def radians_to_degrees(self, radians: float) -> float:
        """Convert radians to degrees"""
        return math.degrees(radians)

    def store_memory(self, value: float) -> None:
        """Store value in memory"""
        self.memory = value
        print(f"Stored {value} in memory")

    def recall_memory(self) -> float:
        """Recall value from memory"""
        return self.memory

    def clear_memory(self) -> None:
        """Clear memory"""
        self.memory = 0
        print("Memory cleared")


def print_menu():
    """Print the calculator menu"""
    print("\n" + "=" * 60)
    print("         ADVANCED CALCULATOR")
    print("=" * 60)
    print("Basic Operations:")
    print("  1. Addition (+)")
    print("  2. Subtraction (-)")
    print("  3. Multiplication (*)")
    print("  4. Division (/)")
    print("  5. Power (^)")
    print("  6. Square Root (sqrt)")
    print("\nTrigonometric Functions:")
    print("  7. Sine (sin)")
    print("  8. Cosine (cos)")
    print("  9. Tangent (tan)")
    print(" 10. Arc Sine (asin)")
    print(" 11. Arc Cosine (acos)")
    print(" 12. Arc Tangent (atan)")
    print("\nLogarithmic Functions:")
    print(" 13. Natural Log (ln)")
    print(" 14. Base-10 Log (log10)")
    print(" 15. Custom Base Log (log)")
    print("\nOther Functions:")
    print(" 16. Factorial (!)")
    print(" 17. Absolute Value (abs)")
    print(" 18. Ceiling (ceil)")
    print(" 19. Floor (floor)")
    print(" 20. Round (round)")
    print(" 21. Degrees to Radians")
    print(" 22. Radians to Degrees")
    print("\nMemory Functions:")
    print(" 23. Store in Memory (MS)")
    print(" 24. Recall Memory (MR)")
    print(" 25. Clear Memory (MC)")
    print("\n 26. Expression Calculator")
    print("  0. Exit")
    print("=" * 60)


def evaluate_expression(expression: str, calc: AdvancedCalculator) -> float:
    """
    Evaluate mathematical expressions with support for advanced functions
    """
    # Replace function names with their Python equivalents
    expression = expression.replace("^", "**")
    expression = re.sub(r"\bsin\(([^)]+)\)", r"math.sin(math.radians(\1))", expression)
    expression = re.sub(r"\bcos\(([^)]+)\)", r"math.cos(math.radians(\1))", expression)
    expression = re.sub(r"\btan\(([^)]+)\)", r"math.tan(math.radians(\1))", expression)
    expression = re.sub(r"\bsqrt\(([^)]+)\)", r"math.sqrt(\1)", expression)
    expression = re.sub(r"\bln\(([^)]+)\)", r"math.log(\1)", expression)
    expression = re.sub(r"\blog10\(([^)]+)\)", r"math.log10(\1)", expression)
    expression = re.sub(r"\babs\(([^)]+)\)", r"abs(\1)", expression)
    expression = re.sub(r"\bpi\b", str(math.pi), expression)
    expression = re.sub(r"\be\b", str(math.e), expression)

    # Add implicit multiplication for parentheses
    expression = re.sub(r"(\d)(\()", r"\1*\2", expression)
    expression = re.sub(r"(\))(\d)", r"\1*\2", expression)
    expression = re.sub(r"(\))(\()", r"\1*\2", expression)

    try:
        # Use eval with restricted globals for safety
        allowed_names = {
            "math": math,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "sqrt": math.sqrt,
            "log": math.log,
            "log10": math.log10,
            "abs": abs,
            "pi": math.pi,
            "e": math.e,
        }
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def get_float_input(prompt: str) -> float:
    """Get float input with error handling"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_int_input(prompt: str) -> int:
    """Get integer input with error handling"""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")


def main():
    """Main calculator function"""
    calc = AdvancedCalculator()

    print("Welcome to the Advanced Calculator!")
    print(
        "This calculator supports basic arithmetic and advanced mathematical functions."
    )

    while True:
        print_menu()

        try:
            choice = input("\nEnter your choice (0-26): ").strip()

            if choice == "0":
                print("Thank you for using the Advanced Calculator!")
                break

            elif choice == "1":  # Addition
                a = get_float_input("Enter first number: ")
                b = get_float_input("Enter second number: ")
                result = calc.add(a, b)
                print(f"{a} + {b} = {result}")

            elif choice == "2":  # Subtraction
                a = get_float_input("Enter first number: ")
                b = get_float_input("Enter second number: ")
                result = calc.subtract(a, b)
                print(f"{a} - {b} = {result}")

            elif choice == "3":  # Multiplication
                a = get_float_input("Enter first number: ")
                b = get_float_input("Enter second number: ")
                result = calc.multiply(a, b)
                print(f"{a} * {b} = {result}")

            elif choice == "4":  # Division
                a = get_float_input("Enter dividend: ")
                b = get_float_input("Enter divisor: ")
                result = calc.divide(a, b)
                print(f"{a} / {b} = {result}")

            elif choice == "5":  # Power
                a = get_float_input("Enter base: ")
                b = get_float_input("Enter exponent: ")
                result = calc.power(a, b)
                print(f"{a} ^ {b} = {result}")

            elif choice == "6":  # Square Root
                a = get_float_input("Enter number: ")
                result = calc.square_root(a)
                print(f"√{a} = {result}")

            elif choice == "7":  # Sine
                a = get_float_input("Enter angle in degrees: ")
                result = calc.sin(a)
                print(f"sin({a}°) = {result}")

            elif choice == "8":  # Cosine
                a = get_float_input("Enter angle in degrees: ")
                result = calc.cos(a)
                print(f"cos({a}°) = {result}")

            elif choice == "9":  # Tangent
                a = get_float_input("Enter angle in degrees: ")
                result = calc.tan(a)
                print(f"tan({a}°) = {result}")

            elif choice == "10":  # Arc Sine
                a = get_float_input("Enter value (-1 to 1): ")
                result = calc.asin(a)
                print(f"asin({a}) = {result}°")

            elif choice == "11":  # Arc Cosine
                a = get_float_input("Enter value (-1 to 1): ")
                result = calc.acos(a)
                print(f"acos({a}) = {result}°")

            elif choice == "12":  # Arc Tangent
                a = get_float_input("Enter value: ")
                result = calc.atan(a)
                print(f"atan({a}) = {result}°")

            elif choice == "13":  # Natural Log
                a = get_float_input("Enter positive number: ")
                result = calc.ln(a)
                print(f"ln({a}) = {result}")

            elif choice == "14":  # Base-10 Log
                a = get_float_input("Enter positive number: ")
                result = calc.log10(a)
                print(f"log10({a}) = {result}")

            elif choice == "15":  # Custom Base Log
                a = get_float_input("Enter positive number: ")
                base = get_float_input("Enter positive base (≠1): ")
                result = calc.log(a, base)
                print(f"log_{base}({a}) = {result}")

            elif choice == "16":  # Factorial
                n = get_int_input("Enter non-negative integer: ")
                result = calc.factorial(n)
                print(f"{n}! = {result}")

            elif choice == "17":  # Absolute Value
                a = get_float_input("Enter number: ")
                result = calc.absolute(a)
                print(f"|{a}| = {result}")

            elif choice == "18":  # Ceiling
                a = get_float_input("Enter number: ")
                result = calc.ceiling(a)
                print(f"ceil({a}) = {result}")

            elif choice == "19":  # Floor
                a = get_float_input("Enter number: ")
                result = calc.floor(a)
                print(f"floor({a}) = {result}")

            elif choice == "20":  # Round
                a = get_float_input("Enter number: ")
                decimals = get_int_input("Enter decimal places: ")
                result = calc.round_number(a, decimals)
                print(f"round({a}, {decimals}) = {result}")

            elif choice == "21":  # Degrees to Radians
                degrees = get_float_input("Enter degrees: ")
                result = calc.degrees_to_radians(degrees)
                print(f"{degrees}° = {result} radians")

            elif choice == "22":  # Radians to Degrees
                radians = get_float_input("Enter radians: ")
                result = calc.radians_to_degrees(radians)
                print(f"{radians} radians = {result}°")

            elif choice == "23":  # Store Memory
                value = get_float_input("Enter value to store: ")
                calc.store_memory(value)

            elif choice == "24":  # Recall Memory
                result = calc.recall_memory()
                print(f"Memory contains: {result}")

            elif choice == "25":  # Clear Memory
                calc.clear_memory()

            elif choice == "26":  # Expression Calculator
                print("\nExpression Calculator")
                print("Supported functions: sin, cos, tan, sqrt, ln, log10, abs")
                print("Constants: pi, e")
                print("Operators: +, -, *, /, ^ (power), ()")
                print("Example: sin(30) + cos(60) * sqrt(16)")

                expression = input("Enter expression: ")
                result = evaluate_expression(expression, calc)
                print(f"Result: {result}")

            else:
                print("Invalid choice. Please enter a number between 0 and 26.")

        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\n\nExiting calculator...")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
