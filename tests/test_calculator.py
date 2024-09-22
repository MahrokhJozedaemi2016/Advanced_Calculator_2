from decimal import Decimal
from calculator.calculator import MyCalculator

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
    try:
        MyCalculator.divide(Decimal(10), Decimal(0))
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Cannot divide by zero", "Incorrect error message for division by zero"

