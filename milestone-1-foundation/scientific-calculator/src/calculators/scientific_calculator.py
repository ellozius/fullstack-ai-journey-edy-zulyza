import math

class ScientificCalculator:
    def power(self, base: float, exponent: float) -> float:
        return math.pow(base, exponent)

    def sqrt(self, value: float) -> float:
        if value < 0:
            raise ValueError("Tidak bisa menghitung akar dari bilangan negatif.")
        return math.sqrt(value)

    def sin(self, x: float) -> float:
        return math.sin(x)

    def cos(self, x: float) -> float:
        return math.cos(x)

    def tan(self, x: float) -> float:
        return math.tan(x)

    def log(self, value: float, base: float = 10) -> float:
        if value <= 0:
            raise ValueError("Logaritma tidak terdefinisi untuk nilai nol atau negatif.")
        if base <= 1:
            raise ValueError("Basis logaritma harus lebih besar dari 1.")
        return math.log(value, base)

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("Faktorial tidak terdefinisi untuk bilangan negatif.")
        return math.factorial(n)

    def radians(self, degrees: float) -> float:
        return math.radians(degrees)

    def degrees(self, radians: float) -> float:
        return math.degrees(radians)
