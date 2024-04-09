# singleton.py
from abc import ABC, abstractmethod

"""
Паттерн Одиночка (Singleton)
Предоставляет механизм создания только одного экземпляра класса

1. Через статичекий метод или метод класса 
2. Через метод __new__
3. Через метаклассы.
    Метакласс - класс, экземпляром которого является класс

"""

'''
class Singleton:

    _instance = None

    def __init__(self):
        self.__data = []

    @property
    def data(self):
        return self.__data

    def add(self, x):
        self.__data.append(x)

    def remove(self):
        self.__data.pop()

    @classmethod
    def get_instance(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = Singleton(*args, **kwargs)
        return cls._instance


a = Singleton.get_instance()
b = Singleton.get_instance()

a.add(1)
b.add(2)
a.remove()
print(b.data)

'''


'''
class Singleton(object):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


a = Singleton()
b = Singleton()
print(a)
print(b)
'''


class Meta(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super.__call__(cls, *args, **kwargs)
        return cls._instance


# class Singleton(metaclass=Meta):
#     ...


A = Meta('Singleton', (object, ), dict())
a = A()
b = A()
print(a)
print(b)


