"""
Задача 5: Dunder-методы (__str__, __add__, __eq__)

Реализуйте класс Vector, который:
- Принимает два аргумента x (int) и y (int)
- __str__ возвращает строку "Vector(x, y)"
- __add__ поддерживает сложение двух векторов: v1 + v2 -> Vector(v1.x + v2.x, v1.y + v2.y)
- __eq__ поддерживает сравнение на равенство по координатам

Примеры:
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    assert str(v1) == "Vector(1, 2)"
    assert v1 + v2 == Vector(4, 6)
    assert v1 == Vector(1, 2)
    assert v1 != v2

Args:
    x (int): Координата x.
    y (int): Координата y.

Returns:
    None
"""


# Ваш код здесь
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
