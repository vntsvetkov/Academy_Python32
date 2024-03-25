from abc import ABC, abstractmethod
from copy import copy, deepcopy

""" День 8. Взаимодействие между классами 

    1. Наследование (является)
    2. Ассоциация (один класс содержит в качестве атрибута объект
    другого класса)
        - Агрегация (один класс заимствует объект другого класса)
        
        - Композиция (один класс владеет объектом другого класса 
        и несет ответсвенность за время его жизни)
        
    
    3. Внедрение зависимостей
        - Через метод инициализации
        - Через метод установки
        - Через отдельные методы (объекта, методы класса)
        
"""

# Пример композиции

"""
class Engine(ABC):

    @abstractmethod
    def start(self):
        ...


class DieselEngine(Engine):

    def __init__(self):
        print("Создан двигатель")

    def start(self):
        print("Двигатель запущен")


class Car:

    def __init__(self):
        print("Создан автомобиль")
        self.__engine: Engine = DieselEngine()


car = Car()

"""

# Пример агрегации


class Book:

    def __init__(self, name):
        self.__name = name


class Reader:

    def __init__(self, number):
        self.__number = number


class Address:

    def __init__(self, city):
        self.city = city

    def __str__(self):
        return f"Город: {self.city['город']}"


class Library:

    def __init__(self, address: Address):
        self.__books: list[Book] = []
        self.__readers: list[Reader] = []
        self.__address: Address = deepcopy(address)

    def change_address(self, address: Address):
        self.__address = address

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address: Address):
        self.__address = address

    def add_readers(self, readers: list[Reader]):
        """

        :param readers:
        :return:
        """
        self.__readers.extend(readers)

    def add_books(self, books: list[Book]):
        """

        :param books:
        :return:
        """
        b = deepcopy(books)
        self.__books.extend(b)


address = Address({"город": "Ярославль"})
library = Library(address)
print("ДО изменений объекта address")
print("Объект адрес: ", address)
print("Адрес библиотеки:", library.address)

address.city["город"] = "Москва"
print("После изменений объекта address")
print("Объект адрес: ", address)
print("Адрес библиотеки:", library.address)

reader = Reader('12345')
library.add_readers([reader])

book = Book("Энциклопедия")
library.add_books([book])
