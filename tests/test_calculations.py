from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import MathOperations

@pytest.fixture
def setup_sample_data():
    """Fixture to set up calculations history for testing."""
    Calculations.clear_history()  # Ensure history is cleared before tests
    # Adding two sample calculations for testing purposes
    Calculations.store_calculation(Calculation(Decimal('10'), Decimal('5'), MathOperations.add))
    Calculations.store_calculation(Calculation(Decimal('20'), Decimal('3'), MathOperations.subtract))

def test_store_calculation(setup_sample_data):
    """Test that a calculation is correctly stored in history."""
    new_calc = Calculation(Decimal('2'), Decimal('2'), MathOperations.add)
    Calculations.store_calculation(new_calc)
    assert Calculations.latest_calculation() == new_calc, "Latest calculation mismatch"

def test_history_length(setup_sample_data):
    """Verify that history contains the correct number of entries."""
    history = Calculations.get_history()
    assert len(history) == 2, "History length mismatch"

def test_clear_history(setup_sample_data):
    """Test clearing the history of calculations."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared"

def test_latest_calculation(setup_sample_data):
    """Test fetching the latest calculation from history."""
    latest = Calculations.latest_calculation()
    assert latest.operand1 == Decimal('20') and latest.operand2 == Decimal('3'), "Latest calculation is incorrect"

def test_find_calculations_by_operation(setup_sample_data):
    """Test finding calculations by their operation."""
    adds = Calculations.find_by_operation("add")
    assert len(adds) == 1, "Add operations not found"
    
    subtracts = Calculations.find_by_operation("subtract")
    assert len(subtracts) == 1, "Subtract operations not found"

def test_latest_when_empty():
    """Ensure None is returned when history is empty."""
    Calculations.clear_history()
    assert Calculations.latest_calculation() is None, "Latest calculation should be None for empty history"

