"""
Задача 9: Класс с __slots__ и методом

Реализуйте класс Vector3D, который:
- Использует __slots__ для ограничения набора атрибутов: только x, y, z (float)
- При инициализации принимает x, y, z и сохраняет их как атрибуты
- Имеет метод length(self), возвращающий длину вектора (sqrt(x^2 + y^2 + z^2))
- При попытке добавить новый атрибут (например, v.color = "red") должно возникать исключение AttributeError

Примеры:
    v = Vector3D(1.0, 2.0, 2.0)
    assert v.x == 1.0 and v.y == 2.0 and v.z == 2.0
    assert abs(v.length() - 3.0) < 1e-6
    try:
        v.color = "red"
    except AttributeError:
        pass

Args:
    x (float): Координата x.
    y (float): Координата y.
    z (float): Координата z.

Returns:
    None
"""

import math


# Ваш код здесь
class Vector3D:
    __slots__ = ('x', 'y', 'z')

    def __init__(self, x: float, y: float, z: float):
        self.x = x
        self.y = y
        self.z = z

    def length(self) -> float:
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5
