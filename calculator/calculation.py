from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a single arithmetic calculation."""

    def __init__(self, x: Decimal, y: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        """Initialize operands and the operation."""
        self.operand1 = x
        self.operand2 = y
        self.operation = operation

    def perform(self) -> Decimal:
        """Execute the calculation and return the result."""
        return self.operation(self.operand1, self.operand2)

    def __repr__(self) -> str:
        """String representation of the Calculation object."""
        return f"Calculation({self.operand1}, {self.operand2}, {self.operation.__name__})"

