from decimal import Decimal

class Calculator:
    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) + Decimal(str(b))
            return float(result)
        return a + b

    @staticmethod
    def subtract(a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) - Decimal(str(b))
            return float(result)
        return a - b
    @staticmethod
    def multiply(a: int | float, b: int | float) -> int | float:
        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) * Decimal(str(b))
            return float(result)
        return a * b
    @staticmethod
    def divide(a: int | float, b: int | float) -> float | str:
        if b == 0:
            return "Cannot divide by 0"
        return a / b