import pytest
from task_02_mutable_default import append_hi


def test_append_hi_default():
    assert append_hi() == ["Hi!"]
    assert append_hi() == ["Hi!"]


def test_append_hi_custom():
    lst = ["Hello"]
    result = append_hi(lst)
    assert result == ["Hello", "Hi!"]
    # Проверяем, что исходный список изменился
    assert lst == ["Hello", "Hi!"]
