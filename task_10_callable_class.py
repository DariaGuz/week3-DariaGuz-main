"""
Задача 10: Класс с dunder-методом __call__

Реализуйте класс Power, который:
- При инициализации принимает степень p (float)
- При вызове экземпляра как функции (через __call__) возвращает a ** p, где a — переданный аргумент

Примеры:
    cube = Power(3)
    assert cube(2) == 8
    sqrt = Power(0.5)
    assert abs(sqrt(9) - 3.0) < 1e-6

Args:
    p (float): Степень.
    a (float): Число для возведения в степень.

Returns:
    float: Результат возведения в степень.
"""


# Ваш код здесь
class Power:
    def __init__(self, p: float):
        self.p = p

    def __call__(self, a: float):
        return a ** self.p
