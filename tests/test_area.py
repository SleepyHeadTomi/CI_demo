import pytest
from math import pi
from math_utils.area import Area

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (2.1, 3.4, 7.14),
    (-2, 2, "The sides in a parallelogram can not be negative"),
    (0, 2, 0)
])
def test_parallellogram(a, b, expected):
    assert Area.parallellogram(a, b) == expected

@pytest.mark.parametrize("w, h, expected", [
    (2, 3, 3),
    (2.1, 3.4, 3.57),
    (-2, 2, "The width or height in a rectangle can not be negative"),
    (0, 2, 0)
])
def test_triangle(w, h, expected):
    assert Area.triangle(w, h) == expected

@pytest.mark.parametrize("radius, expected", [
    (2, pi * 2 ** 2),
    (2.1, pi * 2.1 ** 2),
    (-2, "The radie of a circle can not be negative"),
    (0, 0)
])
def test_circle(radius, expected):
    assert Area.circle(radius) == expected