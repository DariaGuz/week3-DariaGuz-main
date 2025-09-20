import pytest
from task_13_event_emitter import EventEmitter


def test_basic_on_emit():
    em = EventEmitter()
    result = []

    def h(x):
        result.append(x)

    em.on("data", h)
    em.emit("data", 42)
    assert result == [42]


def test_multiple_handlers():
    em = EventEmitter()
    out = []
    em.on("e", lambda x: out.append(("a", x)))
    em.on("e", lambda x: out.append(("b", x)))
    em.emit("e", 1)
    assert ("a", 1) in out and ("b", 1) in out
    assert len(out) == 2


def test_off_handler():
    em = EventEmitter()
    out = []

    def h(x):
        out.append(x)

    em.on("e", h)
    em.emit("e", 1)
    em.off("e", h)
    em.emit("e", 2)
    assert out == [1]


def test_emit_no_handlers():
    em = EventEmitter()
    # Should not raise
    em.emit("no_event", 123)


def test_handler_args_kwargs():
    em = EventEmitter()
    res = {}

    def h(x, y=0):
        res["v"] = x + y

    em.on("sum", h)
    em.emit("sum", 2, y=3)
    assert res["v"] == 5


def test_off_nonexistent_handler():
    em = EventEmitter()

    def h(x):
        pass

    # Should not raise
    em.off("e", h)


def test_handler_called_multiple_times():
    em = EventEmitter()
    out = []

    def h(x):
        out.append(x)

    em.on("e", h)
    em.emit("e", 1)
    em.emit("e", 2)
    assert out == [1, 2]


def test_handler_multiple_events():
    em = EventEmitter()
    out = []

    def h(x):
        out.append(("a", x))

    em.on("e1", h)
    em.on("e2", h)
    em.emit("e1", 1)
    em.emit("e2", 2)
    assert ("a", 1) in out and ("a", 2) in out


def test_handler_duplicate_on():
    em = EventEmitter()
    out = []

    def h(x):
        out.append(x)

    em.on("e", h)
    em.on("e", h)
    em.emit("e", 1)
    # Handler должен быть вызван дважды
    assert out == [1, 1]


def test_handler_with_kwargs_only():
    em = EventEmitter()
    res = {}

    def h(*, x):
        res["x"] = x

    em.on("e", h)
    em.emit("e", x=5)
    assert res["x"] == 5
