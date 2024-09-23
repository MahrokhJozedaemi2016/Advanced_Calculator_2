from decimal import Decimal
from typing import Callable
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

# Definition of the MyCalculator class
class MyCalculator:
    """Calculator class to perform basic arithmetic operations and track history."""

    @staticmethod
    def _check_inputs(a, b):
        """Ensure inputs are of type Decimal, else raise TypeError."""
        if not isinstance(a, Decimal) or not isinstance(b, Decimal):
            raise TypeError("Inputs must be of type Decimal")

    @staticmethod
    def _operate(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Helper method to perform the given operation and store it in history."""
        MyCalculator._check_inputs(a, b)  # Check if inputs are valid
        calc = Calculation(a, b, operation)
        result = calc.perform()  # Perform the operation
        Calculations.store_calculation(calc)  # Store the calculation in history
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition of two numbers."""
        return MyCalculator._operate(a, b, add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction of two numbers."""
        return MyCalculator._operate(a, b, subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication of two numbers."""
        return MyCalculator._operate(a, b, multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division of two numbers. Raises an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return MyCalculator._operate(a, b, divide)
