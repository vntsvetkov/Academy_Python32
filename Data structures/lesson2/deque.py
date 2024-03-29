import time
from linkedlist1 import LinkedList


class Deque:

    def __init__(self):
        self._data = LinkedList()

    def add_first(self, item):
        """ добавление элемента item в начало """
        self._data.add_first(item)

    def add_last(self, item):
        """ добавление элемента item в конец """
        self._data.add_last(item)

    def remove_first(self):
        """ удаляет и возвращает первый элемент """
        self._data.remove_first()

    def remove_last(self):
        """ удаляет и возвращает последний элемент """
        self._data.remove_last()

    def __str__(self):
        return f"""{self.__class__.__name__}({self._data})"""

    def __len__(self):
        return len(self._data)


d = Deque()

t = time.time()

for i in range(1_000_000):
    d.add_first(1)

for i in range(1_000_000):
    d.remove_first()

t = time.time() - t
print(t)
