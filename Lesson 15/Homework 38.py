class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Пользуясь случаем, действую по методу don't repeat yourself :)
    # Метод для приведения к общему знаменателю
    def common_denominator(self, other):
        """Возвращает общий знаменатель и числители"""
        _m = self.b * other.b
        self_a = self.a * round(_m / self.b)
        other_a = other.a * round(_m / other.b)
        return _m, self_a, other_a

    def __mul__(self, other):
        return Fraction(self.a * other.a, self.b * other.b)

    def __truediv__(self, other):
        return Fraction(self.a * other.b, self.b * other.a)

    def __add__(self, other):
        _m, self_a, other_a = self.common_denominator(other)
        return Fraction(self_a + other_a, _m)

    def __sub__(self, other):
        _m, self_a, other_a = self.common_denominator(other)
        return Fraction(self_a - other_a, _m)

    def __eq__(self, other):
        _m, self_a, other_a = self.common_denominator(other)
        return self_a == other_a

    def __gt__(self, other):
        _m, self_a, other_a = self.common_denominator(other)
        return self_a > other_a

    def __lt__(self, other):
        _m, self_a, other_a = self.common_denominator(other)
        return self_a < other_a

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'

f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'

f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True

# Моя проверка
f1 = Fraction(2, 6)
f2 = Fraction(6, 18)
assert f1 == f2  # True

f_g = f_a / f_b
assert str(f_g) == 'Fraction: 12, 9'
