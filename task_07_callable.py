"""
Задача 7: Функция высшего порядка (Callable)

Реализуйте функцию `apply_transform`, которая:
- Принимает список целых чисел numbers и функцию transform (которая принимает int и возвращает int)
- Возвращает новый список, где к каждому элементу numbers применена функция transform

Примеры:
    def double(x): return x * 2
    assert apply_transform([1, 2, 3], double) == [2, 4, 6]
    assert apply_transform([1, 2, 3], lambda x: x + 1) == [2, 3, 4]

Args:
    numbers (list[int]): Список чисел.
    transform (Callable[[int], int]): Функция-преобразователь.

Returns:
    list[int]: Новый список после преобразования.
"""


# Ваш код здесь
def apply_transform(numbers, transform):
    pass
