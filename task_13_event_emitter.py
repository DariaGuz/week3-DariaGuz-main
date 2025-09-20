"""
Задача 13. EventEmitter

Реализуйте класс EventEmitter, поддерживающий подписку на события, отписку и вызов событий:
- on(event, handler): подписать handler (callable) на событие event.
- off(event, handler): отписать handler от события event.
- emit(event, *args, **kwargs): вызвать все обработчики, подписанные на event, с переданными аргументами.

Пример:
em = EventEmitter()
def h1(x): print("h1", x)
def h2(x): print("h2", x)
em.on("data", h1)
em.on("data", h2)
em.emit("data", 42)  # h1 42\nh2 42
em.off("data", h1)
em.emit("data", 99)  # h2 99
"""


class EventEmitter:
    def __init__(self):
        pass

    def on(self, event: str, handler):
        pass

    def off(self, event: str, handler):
        pass

    def emit(self, event: str, *args, **kwargs):
        pass
