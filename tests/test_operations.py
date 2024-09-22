from decimal import Decimal
from calculator.operations import MathOperations
import pytest

def test_add():
    """Test the add operation."""
    assert MathOperations.add(Decimal(10), Decimal(5)) == Decimal('15'), "Addition failed"

def test_subtract():
    """Test the subtract operation."""
    assert MathOperations.subtract(Decimal(10), Decimal(5)) == Decimal('5'), "Subtraction failed"

def test_multiply():
    """Test the multiply operation."""
    assert MathOperations.multiply(Decimal(10), Decimal(5)) == Decimal('50'), "Multiplication failed"

def test_divide():
    """Test the divide operation."""
    assert MathOperations.divide(Decimal(10), Decimal(5)) == Decimal('2'), "Division failed"

def test_divide_by_zero():
    """Test division by zero raises a ValueError."""
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        MathOperations.divide(Decimal(10), Decimal(0))

