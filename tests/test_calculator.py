"""
This module contains tests for calculator operations.
"""
from decimal import Decimal  # Standard library import
import pytest  # Third-party import
from calculator import MyCalculator  # First-party import

def test_addition():
    """Test addition using MyCalculator."""
    assert MyCalculator.add(Decimal(2), Decimal(2)) == Decimal(4), "Addition failed"

def test_subtraction():
    """Test subtraction using MyCalculator."""
    assert MyCalculator.subtract(Decimal(5), Decimal(3)) == Decimal(2), "Subtraction failed"

def test_multiplication():
    """Test multiplication using MyCalculator."""
    assert MyCalculator.multiply(Decimal(3), Decimal(3)) == Decimal(9), "Multiplication failed"

def test_division():
    """Test division using MyCalculator."""
    assert MyCalculator.divide(Decimal(10), Decimal(2)) == Decimal(5), "Division failed"

def test_divide_by_zero():
    """Ensure MyCalculator raises an error for divide by zero."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        MyCalculator.divide(Decimal(10), Decimal(0))

def test_division_by_one():
    """Test division by one using MyCalculator."""
    assert MyCalculator.divide(Decimal(10), Decimal(1)) == Decimal(10), "Division by one failed"

def test_negative_multiplication():
    """Test multiplication with a negative number using MyCalculator."""
    assert MyCalculator.multiply(Decimal(-3), Decimal(3)) == Decimal(-9), "Multiplication with negative number failed"

def test_non_decimal_inputs():
    """Ensure MyCalculator raises TypeError for non-decimal inputs."""
    with pytest.raises(TypeError):
        MyCalculator.add(2, 2)  # Passing integers instead of Decimal
