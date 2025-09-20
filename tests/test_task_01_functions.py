import pytest
from task_01_functions import quadratic_equation


def test_quadratic_equation_basic():
    assert quadratic_equation(2, 1) == 4.0
    assert quadratic_equation(1, 2, 3, c=4) == 9.0
    assert quadratic_equation(3, 1, c=5) == 14.0


def test_quadratic_equation_types():
    # Проверка на тип возвращаемого значения
    result = quadratic_equation(2, 1)
    assert isinstance(result, float)
