import pytest
from task_09_slots import Vector3D


def test_vector3d_basic():
    v = Vector3D(1.0, 2.0, 2.0)
    assert v.x == 1.0
    assert v.y == 2.0
    assert v.z == 2.0
    assert abs(v.length() - 3.0) < 1e-6


def test_vector3d_zero_and_negative():
    v = Vector3D(0.0, 0.0, 0.0)
    assert v.length() == 0.0
    v2 = Vector3D(-1.0, -2.0, -2.0)
    assert abs(v2.length() - 3.0) < 1e-6


def test_vector3d_slots_forbidden_attr():
    v = Vector3D(1, 2, 3)
    with pytest.raises(AttributeError):
        v.color = "red"


def test_vector3d_types():
    v = Vector3D(1, 2, 3)
    assert isinstance(v.x, (int, float))
    assert isinstance(v.y, (int, float))
    assert isinstance(v.z, (int, float))
