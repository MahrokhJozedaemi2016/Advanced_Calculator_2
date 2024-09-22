from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import MathOperations  # Import your modified operations

@pytest.mark.parametrize("x, y, op, result", [
    (Decimal('10'), Decimal('5'), MathOperations.add, Decimal('15')),
    (Decimal('10'), Decimal('5'), MathOperations.subtract, Decimal('5')),
    (Decimal('10'), Decimal('5'), MathOperations.multiply, Decimal('50')),
    (Decimal('10'), Decimal('2'), MathOperations.divide, Decimal('5')),
    (Decimal('10.5'), Decimal('0.5'), MathOperations.add, Decimal('11.0')),
    (Decimal('10.5'), Decimal('0.5'), MathOperations.subtract, Decimal('10.0')),
    (Decimal('10.5'), Decimal('2'), MathOperations.multiply, Decimal('21.0')),
    (Decimal('10'), Decimal('0.5'), MathOperations.divide, Decimal('20')),
])
def test_perform_operations(x, y, op, result):
    """Test the operations on the Calculation class."""
    calculation = Calculation(x, y, op)
    assert calculation.perform() == result, f"Operation failed: {op.__name__}"

def test_calculation_string_representation():
    """Test that Calculation provides the correct string representation."""
    calculation = Calculation(Decimal('10'), Decimal('5'), MathOperations.add)
    expected = "Calculation(10, 5, add)"
    assert str(calculation) == expected, "String representation mismatch"

def test_division_by_zero():
    """Ensure division by zero raises ValueError."""
    calculation = Calculation(Decimal('10'), Decimal('0'), MathOperations.divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calculation.perform()

