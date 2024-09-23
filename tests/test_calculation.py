"""
This module contains tests for calculator operations.
"""
from decimal import Decimal
import pytest
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

# Replace MathOperations references with actual operations
@pytest.mark.parametrize("operand_a, operand_b, operation, expected", [
    (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Test addition
    (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Test subtraction
    (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
    (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
])
def test_calculation_operations(operand_a, operand_b, operation, expected):
    """
    Test calculation operations with various scenarios.

    This test ensures that the Calculation class correctly performs the arithmetic operation
    (specified by the 'operation' parameter) on two Decimal operands ('operand_a' and 'operand_b'),
    and that the result matches the expected outcome.
    """
    calc = Calculation(operand_a, operand_b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {operand_a} and {operand_b}"

def test_divide_by_zero():
    """
    Test division by zero to ensure it raises a ValueError.

    This test checks that attempting to perform a division operation with a zero divisor
    correctly raises a ValueError.
    """
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()

def test_calculation_repr():
    """
    Test the string representation of a Calculation object.
    """
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert repr(calc) == expected_repr, "The __repr__ method did not return the expected string."
