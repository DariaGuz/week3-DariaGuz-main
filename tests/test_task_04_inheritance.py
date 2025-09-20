import pytest
from task_04_inheritance import Animal, Dog


def test_animal_speak():
    a = Animal("Кот")
    assert a.speak() == "Я — Кот, я не знаю, что сказать."
    b = Animal("Лев")
    assert b.speak() == "Я — Лев, я не знаю, что сказать."


def test_dog_speak():
    d = Dog("Шарик")
    assert d.speak() == "Гав! Меня зовут Шарик."
    d2 = Dog("Бобик")
    assert d2.speak() == "Гав! Меня зовут Бобик."


def test_inheritance_type():
    d = Dog("Тузик")
    assert isinstance(d, Dog)
    assert isinstance(d, Animal)


def test_field_access_and_modification():
    d = Dog("Рекс")
    assert hasattr(d, "name")
    d.name = "Барбос"
    assert d.speak() == "Гав! Меня зовут Барбос."
    a = Animal("Слон")
    a.name = "Мышь"
    assert a.speak() == "Я — Мышь, я не знаю, что сказать."
