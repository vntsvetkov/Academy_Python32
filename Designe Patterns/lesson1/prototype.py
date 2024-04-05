# prototype.py
from abc import ABC, abstractmethod
from copy import copy, deepcopy

"""
Паттерн прототип.
Предоставляет возможность создать копию текущего объекта.

"""


class Prototype(ABC):
    @abstractmethod
    def clone(self):
        ...


class Person(Prototype):

    def __init__(self, name):
        self.name = name

    def clone(self) -> Prototype:
        return deepcopy(self)


class Student(Person):
    ...


person1 = Student('Вася')
person2 = person1.clone()

print(person1)
print(person2)

