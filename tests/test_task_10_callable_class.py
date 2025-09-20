from task_10_callable_class import Power


def test_power_basic():
    cube = Power(3)
    assert cube(2) == 8
    sqrt = Power(0.5)
    assert abs(sqrt(9) - 3.0) < 1e-6


def test_power_negative_and_fractional():
    inv = Power(-1)
    assert abs(inv(2) - 0.5) < 1e-6
    root3 = Power(1 / 3)
    assert abs(root3(27) - 3.0) < 1e-6


def test_power_zero_and_one():
    p0 = Power(0)
    assert p0(123) == 1
    p1 = Power(1)
    assert p1(123) == 123


def test_power_negative_base():
    sq = Power(2)
    assert sq(-3) == 9
    odd = Power(3)
    assert odd(-2) == -8


def test_power_types_and_repeat():
    p = Power(2)
    for x in [0, 1, -1, 10]:
        assert isinstance(p(x), (int, float))
    assert p(2) == 4
    assert p(2) == 4
