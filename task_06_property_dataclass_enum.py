"""
Задача 6: Property, dataclass, enum

1. Реализуйте класс Product:
    - Конструктор принимает name (str) и price (float)
    - price — property: при установке значения price проверяйте, что оно > 0, иначе выбрасывайте ValueError

2. Реализуйте dataclass Order:
    - name (str)
    - quantity (int)
    - product (Product)

3. Реализуйте enum OrderStatus с вариантами: NEW, PAID, SHIPPED, CANCELLED

Примеры:
    p = Product("Book", 500)
    p.price = 1000
    try:
        p.price = -1
    except ValueError:
        pass

    from dataclasses import dataclass
    o = Order("Заказ1", 2, p)
    assert o.name == "Заказ1"
    assert o.quantity == 2
    assert o.product is p

    from enum import Enum
    assert OrderStatus.NEW.name == "NEW"
    assert OrderStatus.PAID.value == 2

Args:
    name (str): Имя.
    price (float): Цена.
    quantity (int): Количество.

Returns:
    None
"""

from dataclasses import dataclass
from enum import Enum


class Product:
    pass


@dataclass
class Order:
    pass


class OrderStatus(Enum):
    pass
