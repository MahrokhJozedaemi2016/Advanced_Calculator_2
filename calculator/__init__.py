from decimal import Decimal
from typing import Callable
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import MathOperations

class MyCalculator:
    """Calculator class to perform basic arithmetic operations and track history."""

    @staticmethod
    def _operate(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        """Helper method to perform the given operation and store it in history."""
        calc = Calculation(a, b, operation)
        result = calc.perform()  # Perform the operation
        Calculations.store_calculation(calc)  # Store the calculation in history
        return result

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Perform addition of two numbers."""
        return MyCalculator._operate(a, b, MathOperations.add)

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Perform subtraction of two numbers."""
        return MyCalculator._operate(a, b, MathOperations.subtract)

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Perform multiplication of two numbers."""
        return MyCalculator._operate(a, b, MathOperations.multiply)

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Perform division of two numbers. Raises ValueError if dividing by zero."""
        return MyCalculator._operate(a, b, MathOperations.divide)

