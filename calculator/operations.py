from decimal import Decimal

class MathOperations:
    """Contains static methods for basic arithmetic operations."""

    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        """Add two numbers."""
        return a + b

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        """Subtract second number from the first."""
        return a - b

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        """Multiply two numbers."""
        return a * b

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        """Divide first number by the second. Raise an error if dividing by zero."""
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

