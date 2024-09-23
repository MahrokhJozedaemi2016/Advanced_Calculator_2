from decimal import Decimal
from typing import List, Callable
from calculator.calculation import Calculation

class Calculations:
    # This class will manage a history of calculations
    history: List[Calculation] = []  # Store history of all calculations

    @classmethod
    def store_calculation(cls, calculation: Calculation):
        """Store a calculation in history."""
        cls.history.append(calculation)

    @classmethod
    def get_latest(cls) -> Calculation:
        """Get the latest calculation from history."""
        if cls.history:
            return cls.history[-1]
        return None  # Return None if the history is empty

    @classmethod
    def find_by_operation(cls, operation_name: str) -> List[Calculation]:
        """Find calculations by operation name."""
        return [calc for calc in cls.history if calc.operation.__name__ == operation_name]

    @classmethod
    def clear_history(cls):
        """Clear the history of calculations."""
        cls.history.clear()

    @classmethod
    def get_history(cls) -> List[Calculation]:
        """Retrieve the entire calculation history."""
        return cls.history