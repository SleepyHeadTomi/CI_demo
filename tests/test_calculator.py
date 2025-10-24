import pytest
from math_utils.calculator import Calculator

@pytest.mark.parametrize("a, b, expected, data_type", [
    (1, 2, 3, int),
    (-1, 2, 1, int),
    (-1, -2, -3, int),
    (1.5, 2.2, 3.7, float),
    (1.5, -2.2, -0.7, float)
])
def test_add(a, b, expected, data_type):
    assert Calculator.add(a,b) == expected
    assert type(Calculator.add(a,b)) == data_type

@pytest.mark.parametrize("a, b, expected, data_type", [
    (2, 1, 1, int),
    (1, 2, -1, int),
    (-1, -2, 1, int),
    (1.5, 2.2, -0.7, float),
    (-1.5, -2.2, 0.7, float)
])
def test_subtract(a, b, expected, data_type):
    assert Calculator.subtract(a, b) == expected

@pytest.mark.parametrize("a, b, expected, data_type", [
    (3, 4, 12, int),
    (-3, 4, -12, int),
    (0, 5, 0, int),
    (2.5, 1.5, 3.75, float)
])
def test_multiply(a, b, expected, data_type):
    assert Calculator.multiply(a, b) == expected
    assert type(Calculator.multiply(a, b)) == data_type

@pytest.mark.parametrize("a, b, expected", [
    (1, 0, "Cannot divide by 0"),
    (1, 2, 0.5),
    (-1, 2, -0.5),
    (1, -2, -0.5),
    (1, 3, (1/3))
])
def test_divide(a, b, expected):
    assert Calculator.divide(a, b) == expected