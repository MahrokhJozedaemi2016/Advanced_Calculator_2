from decimal import Decimal
from typing import Callable

class Calculation:
    """Represents a single calculation with two operands and an operation."""
    
    def __init__(self, a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]):
        self.a = a  # First operand
        self.b = b  # Second operand
        self.operation = operation  # Operation to perform (add, subtract, etc.)
    
    def perform(self) -> Decimal:
        """Perform the operation and return the result."""
        return self.operation(self.a, self.b)

    def __repr__(self):
        """Return a simplified string representation of the calculation."""
        return f"Calculation({self.a}, {self.b}, {self.operation.__name__})"

