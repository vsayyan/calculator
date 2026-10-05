import pytest
from calc import add, subtract, multiply, divide, power, modulo, average

def test_add():
    assert add(1,2) == 3
    assert add(-1,1) == 0

def test_subtract():
    assert subtract(2,1) == 1

def test_multiply():
    assert multiply(2,3) == 6

def test_divide():
    assert divide(7, 2) == 3.5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5,0)

def test_power():
    assert power(2,3) == 8

def test_modulo():
    assert modulo(7,3) == 1

def test_average():
    assert average([1,2,3,4,5,6]) == 3.5

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([])