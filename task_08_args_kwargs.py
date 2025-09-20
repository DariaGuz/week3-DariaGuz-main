"""
Задача 8: Распаковка *args и **kwargs

Реализуйте функцию `describe_creature`, которая:
- Принимает обязательные позиционные аргументы species (str) и name (str)
- Принимает произвольное количество способностей через *abilities (str)
- Принимает произвольные характеристики через **traits (любые значения)
- Возвращает словарь с ключами: "species", "name", "abilities" (tuple), "traits" (dict)

Примеры:
    d = describe_creature("dragon", "Smaug", "fire", "flight", color="red", wingspan=20)
    assert d["species"] == "dragon"
    assert d["name"] == "Smaug"
    assert d["abilities"] == ("fire", "flight")
    assert d["traits"]["color"] == "red"
    assert d["traits"]["wingspan"] == 20

Args:
    species (str): Вид существа.
    name (str): Имя.
    *abilities (str): Способности.
    **traits: Характеристики.

Returns:
    dict: Описание существа.
"""


# Ваш код здесь
def describe_creature(species, name, *abilities, **traits):
    pass
