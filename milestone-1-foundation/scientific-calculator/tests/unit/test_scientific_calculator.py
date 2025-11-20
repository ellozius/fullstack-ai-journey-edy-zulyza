import pytest
from src.calculators.basic_calculator import BasicCalculator
from src.calculators.scientific_calculator import ScientificCalculator
import math

basic = BasicCalculator()
scientific = ScientificCalculator()

# === BasicCalculator Tests ===
def test_add():
    assert basic.add(2, 3) == 5

def test_subtract():
    assert basic.subtract(5, 2) == 3

def test_multiply():
    assert basic.multiply(4, 3) == 12

def test_divide():
    assert basic.divide(10, 2) == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        basic.divide(5, 0)

# === ScientificCalculator Tests ===
def test_power():
    assert scientific.power(2, 3) == 8

def test_sqrt():
    assert scientific.sqrt(16) == 4

def test_sqrt_negative():
    with pytest.raises(ValueError):
        scientific.sqrt(-9)

def test_factorial():
    assert scientific.factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        scientific.factorial(-1)

def test_log_default_base():
    assert scientific.log(100) == pytest.approx(math.log10(100))

def test_log_custom_base():
    assert scientific.log(8, 2) == pytest.approx(3)

def test_log_invalid_value():
    with pytest.raises(ValueError):
        scientific.log(0)

def test_log_invalid_base():
    with pytest.raises(ValueError):
        scientific.log(10, 1)

def test_radians():
    assert scientific.radians(180) == pytest.approx(math.pi)

def test_degrees():
    assert scientific.degrees(math.pi) == pytest.approx(180)

def test_sin():
    assert scientific.sin(math.pi / 2) == pytest.approx(1)

def test_cos():
    assert scientific.cos(0) == pytest.approx(1)

def test_tan():
    assert scientific.tan(0) == pytest.approx(0)
