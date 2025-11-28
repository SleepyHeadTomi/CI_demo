import logging
from decimal import Decimal

logger = logging.getLogger("calc_class")

class Calculator:

    def add(self, a: int | float, b: int | float) -> int | float:
        logger.info("add method called")
        logger.debug(f"arguments used in call: {a=} and {b=}")

        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) + Decimal(str(b))
            result = float(result)
        else:
            result = a + b

        logger.debug(f"Result from add({a}, {b}) = {result}")
        return result


    def subtract(self, a: int | float, b: int | float) -> int | float:
        logger.info("subtract method called")
        logger.debug(f"arguments used in call: {a=} and {b=}")

        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) - Decimal(str(b))
            result = float(result)
        else:
            result = a - b
        logger.debug(f"Result from subtract({a}, {b}) = {result}")
        return result

    def multiply(self, a: int | float, b: int | float) -> int | float:
        logger.info("multiply method called")
        logger.debug(f"arguments used in call: {a=} and {b=}")

        if isinstance(a, float) or isinstance(b, float):
            result = Decimal(str(a)) * Decimal(str(b))
            result = float(result)
        else:
            result = a * b

        logger.debug(f"Result from multiply({a}, {b}) = {result}")
        return result

    def divide(self, a: int | float, b: int | float) -> float | str:
        logger.info("multiply method called")
        logger.debug(f"arguments used in call: {a=} and {b=}")

        if b == 0:
            logging.critical("Division by 0!!")
            raise ZeroDivisionError("Cannot divide by 0")

        result = a / b

        logger.debug(f"Result of divide({a}, {b}) = {result}")
        return result