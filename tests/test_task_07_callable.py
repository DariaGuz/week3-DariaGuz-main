from task_07_callable import apply_transform


def test_apply_transform_double():
    def double(x):
        return x * 2

    assert apply_transform([1, 2, 3], double) == [2, 4, 6]


def test_apply_transform_lambda():
    assert apply_transform([1, 2, 3], lambda x: x + 1) == [2, 3, 4]
    assert apply_transform([-1, 0, 1], lambda x: -x) == [1, 0, -1]


def test_apply_transform_identity():
    assert apply_transform([], lambda x: x) == []
    assert apply_transform([42], lambda x: x) == [42]


def test_apply_transform_various():
    def square(x):
        return x * x

    assert apply_transform([2, -2, 0], square) == [4, 4, 0]

    def to_str(x):
        return str(x)

    assert apply_transform([1, 2], to_str) == ["1", "2"]


def test_apply_transform_types():
    def f(x):
        return x

    result = apply_transform([1, 2, 3], f)
    assert isinstance(result, list)
    for v in result:
        assert isinstance(v, int)
