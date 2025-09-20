"""
Задача 11. LRUCache

Реализуйте класс LRUCache с фиксированным размером capacity, поддерживающий методы:
- get(key): вернуть значение по ключу, если ключ есть, иначе -1. Если ключ есть, он становится самым "свежим".
- put(key, value): добавить/обновить значение по ключу. Если размер превышает capacity, удалить самый "старый" ключ.

Пример:
cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)  # удаляет ключ 2
assert cache.get(2) == -1
cache.put(4, 4)  # удаляет ключ 1
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
"""


class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass
