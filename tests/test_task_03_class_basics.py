import pytest
from task_03_class_basics import Person


def test_person_basic():
    p = Person("Алиса", 23)
    assert p.name == "Алиса"
    assert p.age == 23
    assert p.greet() == "Привет, меня зовут Алиса и мне 23 лет!"


def test_person_different_names_and_ages():
    p = Person("Bob", 0)
    assert p.greet() == "Привет, меня зовут Bob и мне 0 лет!"
    p2 = Person("Евгений", 100)
    assert p2.greet() == "Привет, меня зовут Евгений и мне 100 лет!"


def test_person_empty_name():
    p = Person("", 42)
    assert p.greet() == "Привет, меня зовут  и мне 42 лет!"


def test_person_type_and_fields():
    p = Person("Test", 1)
    assert isinstance(p, Person)
    assert hasattr(p, "name")
    assert hasattr(p, "age")


def test_person_field_modification():
    p = Person("X", 10)
    p.name = "Y"
    p.age = 20
    assert p.greet() == "Привет, меня зовут Y и мне 20 лет!"


def test_person_greet_multiple_calls():
    p = Person("Multi", 5)
    for _ in range(3):
        assert p.greet() == "Привет, меня зовут Multi и мне 5 лет!"
