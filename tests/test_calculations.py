"""
This module contains tests for the Calculations class.
"""
from decimal import Decimal
from calculator.operations import add
from calculator.calculation import Calculation
from calculator.calculations import Calculations

def test_store_calculation(setup_sample_data):
    """Test storing a calculation in history."""
    calc = Calculation(Decimal('2'), Decimal('2'), add)
    Calculations.store_calculation(calc)
    assert Calculations.get_latest() == calc, "Failed to store the calculation."

def test_history_length(setup_sample_data):
    """Test that history has the correct number of entries."""
    assert len(Calculations.get_history()) == 4, "History does not contain the expected number of calculations."

def test_clear_history(setup_sample_data):
    """Test clearing the entire calculation history."""
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History was not cleared."

def test_latest_calculation(setup_sample_data):
    """Test getting the latest calculation."""
    assert Calculations.get_latest().a == Decimal('40') and Calculations.get_latest().b == Decimal('5'), \
        "Did not get the correct latest calculation."

def test_find_calculations_by_operation(setup_sample_data):
    """Test finding calculations by operation."""
    add_operations = Calculations.find_by_operation("add")
    assert len(add_operations) == 1, "Did not find the correct number of calculations with add operation."

def test_multiply_and_divide_operations(setup_sample_data):
    """Test multiplication and division operations in history."""
    assert len(Calculations.find_by_operation("multiply")) == 1, "Did not find the correct number of multiply operations."
    assert len(Calculations.find_by_operation("divide")) == 1, "Did not find the correct number of divide operations."

def test_get_latest_with_empty_history():
    """Test getting the latest calculation when the history is empty."""
    Calculations.clear_history()
    assert Calculations.get_latest() is None, "Expected None for latest calculation with empty history."

def test_get_full_history(setup_sample_data):
    """Test retrieving the entire history of calculations."""
    history = Calculations.get_history()
    assert len(history) == 4, "The full history was not retrieved correctly."
