""" День 9. Магические методы"""


"""
Магические методы (дандеры)

"""


class A:

    def __init__(self, x: int):
        self._x = x

    def __int__(self):
        return self._x


class Book:

    def __init__(self, name):
        self.__name = name

    def __str__(self):
        return self.__name


class Library:

    def __init__(self):
        self.__books: list[Book] = []

    def add_books(self, books: list[Book]):
        self.__books.extend(books)

    def __len__(self):
        return len(self.__books)

    def __contains__(self, item):
        return item in self.__books

    def __getitem__(self, index):
        return self.__books[index]

    def __setitem__(self, key, value):
        if key < len(self.__books):
            self.__books[key] = value
        # else:
        # Выбросить собственное исключение

    def __delitem__(self, key):
        del self.__books[key]


# d = Library()
# book = Book("Сказки")
# book1 = Book("Сказки")
# print(repr(book))
# print(repr(book1))
# print(book == book1)
# d.add_books([book1, book])
#
# print(d[0])  # Энциклопедия
# print(len(d))  # 2
# print(book in d)  # True
# d[0] = Book("Война и мир")
# del d[0]


# Задача 2. Реализовать класс Time


class Time:

    def __init__(self, h, m, s):
        self.__h = h  # валидация
        self.__m = m  # валидация
        self.__s = s  # валидация

    def __lt__(self, other) -> bool:
        if isinstance(other, Time):
            return int(self) < int(other)
        if isinstance(other, int):
            return self.__get_seconds() < other
        raise TypeError(f"'<' не поддерживается между типами Time and {other.__class__.__name__}")

    def __eq__(self, other) -> bool:
        if isinstance(other, Time):
            return int(self) == int(other)
        if isinstance(other, int):
            return self.__get_seconds() == other
        raise TypeError(f"'==' не поддерживается между типами Time and {other.__class__.__name__}")

    def __get_seconds(self) -> int:
        return self.__s + self.__m * 60 + self.__h * 3600

    def __int__(self):
        return self.__s + self.__m * 60 + self.__h * 3600

    def __hash__(self):
        # return hash(int(self))
        return hash((self.__h, self.__m, self.__s))


t1 = Time(0, 0, 0)
t2 = Time(12, 0, 0)
print(t1)
print(t2)
print(t1 == t2)

clock = {t1: "Полночь", t2: "Полдень"}
print(clock[Time(12, 0, 0)])
