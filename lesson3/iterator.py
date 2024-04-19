# iterator.py

from abc import ABC, abstractmethod
from collections.abc import Iterator

"""
Паттер итератор.
Позволет обходить элементы коллекции, не раскрывая ее базовое представление.

"""

"""
Способ 1. Использование генератора

def fibon(n):
      a = 0 
      b = 1
      for i in range(n):
          yield a
          a, b = b, a + b

for x in fibon(10):
    print(x)
    
"""

"""
Способ 2. Реализовать в классе __next__ и __iter__



class FibonacciGenerator:
    def __init__(self, count):
        self.prev = 0
        self.cur = 1
        self.count = count

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        if self.prev > self.count:
            raise StopIteration
        return result

    def __iter__(self):
        return self


numbers = FibonacciGenerator(3)

for n in numbers:
    print(n)


it = iter(FibonacciGenerator(5))
print(next(it))
"""


"""
Способ 3. Реализовать collections.abc.Iterator -> аналог функции iter()



class FibonacciGenerator:
    def __init__(self, count):
        self.prev = 0
        self.cur = 1
        self.count = count

    def __next__(self):
        result = self.prev
        self.prev, self.cur = self.cur, self.prev + self.cur
        if self.prev > self.count:
            raise StopIteration
        return result

    def __iter__(self):
        return self


class FibonacciIterator(Iterator):

   def __init__(self, collection):
        self._position = 0
        self._collection = collection

   def __next__(self):
       try:
           value = self._collection[self._position]
           self._position += 1
       except IndexError:
           raise StopIteration
       return value


iterator = FibonacciIterator(list(FibonacciGenerator(5)))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


"""

"""
Способ 4. Паттерн итератор

"""

class Aggregate(ABC):

    @abstractmethod
    def iterator(self):
        """
        Возвращает итератор
        """
        pass


class MyIterator(ABC):
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    @abstractmethod
    def first(self):
        """
        Возвращает итератор к началу агрегата.
        Так же называют reset
        """
        pass

    @abstractmethod
    def next(self):
        """
        Переходит на следующий элемент агрегата.
        Вызывает ошибку StopIteration, если достигнут конец последовательности.
        """
        pass

    @abstractmethod
    def current(self):
        """
        Возвращает текущий элемент
        """
        pass


class ListIterator(MyIterator):
    def __init__(self, collection, cursor):
        """
        :param collection: список
        :param cursor: индекс с которого начнется перебор коллекции.
        так же должна быть проверка -1 >= cursor < len(collection)
        """
        super().__init__(collection, cursor)

    def first(self):
        """
        Начальное значение курсора -1.
        Так как в нашей реализации сначала необходимо вызвать next
         который сдвинет курсор на 1.
        """
        self._cursor = -1

    def next(self):
        """
        Если курсор указывает на послений элемент, то вызываем StopIteration,
        иначе сдвигаем курсор на 1
        """
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1

    def current(self):
        """
        Возвращаяем текущий элемент
        """
        return self._collection[self._cursor]


class ListCollection(Aggregate):
    def __init__(self, collection):
        self._collection = list(collection)

    def iterator(self):
        return ListIterator(self._collection, -1)


aggregate = ListCollection((1, 2, 5, 6, 8))
itr = aggregate.iterator()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())


itr.first()

while True:
    try:
        itr.next()
    except StopIteration:
        break
    print(itr.current())