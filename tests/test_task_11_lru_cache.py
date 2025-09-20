import pytest
from task_11_lru_cache import LRUCache


def test_lru_basic():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_lru_update_existing_key():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    assert cache.get(1) == 10
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3


def test_lru_capacity_one():
    cache = LRUCache(1)
    cache.put(1, 1)
    assert cache.get(1) == 1
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2


def test_lru_get_nonexistent():
    cache = LRUCache(2)
    assert cache.get(42) == -1
    cache.put(1, 1)
    assert cache.get(2) == -1


def test_lru_eviction_order():
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.get(1)
    cache.put(4, 4)
    assert cache.get(2) == -1  # 2 должен быть вытеснен
    assert cache.get(1) == 1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


def test_lru_multiple_evictions():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(2) == -1
    assert cache.get(3) == -1
    assert cache.get(4) == 4


def test_lru_get_refreshes():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(1) == 1
    assert cache.get(3) == 3


def test_lru_put_refreshes():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(1, 10)
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(1) == 10
    assert cache.get(3) == 3


def test_lru_capacity_zero():
    cache = LRUCache(0)
    cache.put(1, 1)
    assert cache.get(1) == -1
    cache.put(2, 2)
    assert cache.get(2) == -1


def test_lru_stress():
    cache = LRUCache(50)
    for i in range(100):
        cache.put(i, i)
    for i in range(50):
        assert cache.get(i) == -1
    for i in range(50, 100):
        assert cache.get(i) == i


def test_lru_put_same_key_many_times():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    cache.put(1, 3)
    assert cache.get(1) == 3
    cache.put(2, 2)
    cache.put(3, 3)
    assert cache.get(1) == -1 or cache.get(2) == -1  # один из них должен быть вытеснен


def test_lru_types():
    cache = LRUCache(2)
    cache.put("a", 1)
    cache.put("b", 2)
    assert cache.get("a") == 1
    cache.put("c", 3)
    assert cache.get("b") == -1
    assert cache.get("c") == 3
    assert cache.get("a") == 1


def test_lru_get_does_not_add():
    cache = LRUCache(2)
    cache.get(1)
    cache.put(2, 2)
    assert cache.get(1) == -1
    assert cache.get(2) == 2
