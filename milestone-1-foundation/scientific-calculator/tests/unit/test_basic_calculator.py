import pytest
from src.calculators.basic_calculator import BasicCalculator

calculator = BasicCalculator()

def test_add():
    assert calculator.add(2, 3) == 5
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2
    
def test_subtract():
    assert calculator.subtract(5, 3) == 2
    assert calculator.subtract(-1, -1) == 0
    assert calculator.subtract(-1, 1) == -2
    
def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(-1, -1) == 1
    
def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 2) == -3
    assert calculator.divide(-6, -2) == 3
    with pytest.raises(ValueError):
        calculator.divide(1, 0)
