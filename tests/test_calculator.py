import pytest
import logging
from math_utils.calculator import Calculator

logging.basicConfig(level=logging.DEBUG,
                    format="{asctime} {levelname} {message}",
                    style="{",
                    datefmt="%Y-%m-%d %H:%M:%S")

logging.getLogger().setLevel(logging.DEBUG)

@pytest.fixture
def calc_obj():
    return Calculator()

@pytest.mark.parametrize("a, b, expected, data_type", [
    (1, 2, 3, int),
    (-1, 2, 1, int),
    (-1, -2, -3, int),
    (1.5, 2.2, 3.7, float),
    (1.5, -2.2, -0.7, float)
])
def test_add_method_with_multiple_datasets(a, b, expected, data_type, calc_obj):
    result = calc_obj.add(a, b)

    assert result == expected
    assert type(result) == data_type

@pytest.mark.parametrize("a, b, expected, data_type", [
    (2, 1, 1, int),
    (1, 2, -1, int),
    (-1, -2, 1, int),
    (1.5, 2.2, -0.7, float),
    (-1.5, -2.2, 0.7, float)
])
def test_subtract_method_with_multiple_datasets(a, b, expected, data_type, calc_obj):
    result = calc_obj.subtract(a, b)

    assert result == expected
    assert type(result) == data_type

@pytest.mark.parametrize("a, b, expected, data_type", [
    (3, 4, 12, int),
    (-3, 4, -12, int),
    (0, 5, 0, int),
    (2.5, 1.5, 3.75, float)
])
def test_multiply_method_with_multiple_datasets(a, b, expected, data_type, calc_obj):
    result = calc_obj.multiply(a, b)

    assert result == expected
    assert type(result) == data_type

@pytest.mark.parametrize("a, b, expected", [
    (1, 0, "Cannot divide by 0"),
    (1, 2, 0.5),
    (-1, 2, -0.5),
    (1, -2, -0.5),
    (1, 3, (1/3))
])
def test_divide_method_with_multiple_datasets(a, b, expected, calc_obj):
    if b != 0:
        result = calc_obj.divide(a, b)
        assert result== expected
    else:
        with pytest.raises(ZeroDivisionError) as exc_info:
            calc_obj.divide(a, b)

        assert str(exc_info.value) == expected