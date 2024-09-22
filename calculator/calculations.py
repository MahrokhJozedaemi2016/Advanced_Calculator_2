from typing import List
from calculator.calculation import Calculation

class Calculations:
    """Manages the history of calculations performed."""

    _history: List[Calculation] = []

    @classmethod
    def store_calculation(cls, calculation: Calculation):
        """Add a new calculation to the history."""
        cls._history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the full history of calculations."""
        return cls._history

    @classmethod
    def clear_history(cls):
        """Clear the calculation history."""
        cls._history.clear()

    @classmethod
    def latest_calculation(cls) -> Calculation:
        """Return the most recent calculation."""
        return cls._history[-1] if cls._history else None

