from decimal import Decimal

def add(a: Decimal, b: Decimal) -> Decimal:
    """Perform addition."""
    return a + b

def subtract(a: Decimal, b: Decimal) -> Decimal:
    """Perform subtraction."""
    return a - b

def multiply(a: Decimal, b: Decimal) -> Decimal:
    """Perform multiplication."""
    return a * b

def divide(a: Decimal, b: Decimal) -> Decimal:
    """Perform division, with error handling for division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b