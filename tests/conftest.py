"""
This module contains fixtures for pytest.
"""
from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.calculations import Calculations
from calculator.operations import add, subtract, multiply, divide

@pytest.fixture
def setup_sample_data():
    """Fixture to set up calculations history for testing."""
    Calculations.clear_history()  # Ensure history is cleared before tests
    Calculations.store_calculation(Calculation(Decimal('10'), Decimal('5'), add))
    Calculations.store_calculation(Calculation(Decimal('20'), Decimal('10'), subtract))
    Calculations.store_calculation(Calculation(Decimal('30'), Decimal('3'), multiply))
    Calculations.store_calculation(Calculation(Decimal('40'), Decimal('5'), divide))
