import pytest
from task_06_property_dataclass_enum import Product


def test_product_property_valid():
    p = Product("Book", 500)
    assert p.price == 500
    p.price = 1000
    assert p.price == 1000


def test_product_property_invalid():
    p = Product("Pen", 10)
    with pytest.raises(ValueError):
        p.price = 0
    with pytest.raises(ValueError):
        p.price = -5


def test_product_fields_and_type():
    p = Product("Test", 1.5)
    assert hasattr(p, "name")
    assert hasattr(p, "price")
    assert isinstance(p.name, str)
    assert isinstance(p.price, float)


def test_order_dataclass_and_fields():
    from task_06_property_dataclass_enum import Order

    p = Product("Book", 100)
    o = Order("Заказ1", 2, p)
    assert o.name == "Заказ1"
    assert o.quantity == 2
    assert o.product is p


def test_order_status_enum():
    from task_06_property_dataclass_enum import OrderStatus

    assert OrderStatus.NEW.name == "NEW"
    assert OrderStatus.PAID.value == 2
    assert len(set(OrderStatus)) == 4
    assert {e.name for e in OrderStatus} == {"NEW", "PAID", "SHIPPED", "CANCELLED"}
