# test_main.py

import pytest
from main import add, subtract, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 3) == 2

def test_divide():
    assert divide(6, 2) == 3

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        divide(4, 0)
