import time


class Deque:

    def __init__(self):
        self._data = []

    def add_first(self, item):
        """ добавление элемента item в начало """
        self._data.insert(0, item)

    def add_last(self, item):
        """ добавление элемента item в конец """
        self._data.append(item)

    def remove_first(self):
        """ удаляет и возвращает первый элемент """
        self._data.pop(0)

    def remove_last(self):
        """ удаляет и возвращает последний элемент """
        self._data.pop()

    def __str__(self):
        return f"""{self.__class__.__name__}({self._data})"""

    def copy(self):
        return self._data.copy()


d = Deque()

for i in range(100_000):
    d.add_first(1)

for i in range(100_000):
    d.remove_first()
