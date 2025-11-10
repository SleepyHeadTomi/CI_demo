from decimal import Decimal

class Calculator:

    def add(self, a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) + Decimal(str(b))
            return float(result)
        return a + b


    def subtract(self, a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) - Decimal(str(b))
            return float(result)
        return a - b

    def multiply(self, a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) * Decimal(str(b))
            return float(result)
        return a * b

    def divide(self, a: int | float, b: int | float) -> float | str:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by 0")
        return a / b