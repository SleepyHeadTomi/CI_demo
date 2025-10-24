import math
from decimal import Decimal

class Area:
    @staticmethod
    def parallellogram(a: int | float, b: int | float) -> int | float | str:
        if a < 0 or b < 0:
            return "The sides in a parallelogram can not be negative"

        if isinstance(a, float) or isinstance(b, float):
            result = float(Decimal(str(a)) * Decimal(str(b)))
            return result
        return a * b

    @staticmethod
    def triangle(w: int | float, h: int | float) -> int | float | str:
        if w < 0 or h < 0:
            return "The width or height in a rectangle can not be negative"

        if isinstance(w, float) or isinstance(h, float):
            result = float(Decimal(str(w)) * Decimal(str(h))) / 2
            return result
        return (w * h) / 2

    @staticmethod
    def circle(radius: int | float) -> int | float | str:
        if radius < 0:
            return "The radie of a circle can not be negative"

        if isinstance(radius, float):
            result = math.pi * float(Decimal(str(radius))) ** 2
            return result
        return math.pi * radius ** 2