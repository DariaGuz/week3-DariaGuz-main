from task_05_dunder import Vector


def test_vector_str():
    v = Vector(1, 2)
    assert str(v) == "Vector(1, 2)"
    v2 = Vector(-5, 0)
    assert str(v2) == "Vector(-5, 0)"


def test_vector_add():
    v1 = Vector(1, 2)
    v2 = Vector(3, 4)
    v3 = v1 + v2
    assert isinstance(v3, Vector)
    assert v3 == Vector(4, 6)
    assert v1 + Vector(0, 0) == v1


def test_vector_eq_and_neq():
    v1 = Vector(1, 2)
    v2 = Vector(1, 2)
    v3 = Vector(2, 1)
    assert v1 == v2
    assert not (v1 != v2)
    assert v1 != v3
    assert v2 != v3


def test_vector_types_and_fields():
    v = Vector(10, -10)
    assert hasattr(v, "x")
    assert hasattr(v, "y")
    assert isinstance(v.x, int)
    assert isinstance(v.y, int)
