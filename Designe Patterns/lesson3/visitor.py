# visitor.py

from abc import ABC, abstractmethod
from functools import singledispatchmethod

"""
Паттерн посетитель
Позволяет создавать новые операции, не меняя классы объектов, над которыми эти операции могут выполняться.

"""


class Component(ABC):

    @abstractmethod
    def accept(self, v):
        ...

class Square(Component):

    def __init__(self, side):
        self._side = side

    def area(self):
        return self._side ** 2

    def accept(self, v):
        return v.visit(self)


class Circle(Component):

    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * self._radius ** 2

    def accept(self, v):
        return v.visit(self)


class Visitor(ABC):

    @abstractmethod
    def visit(self, figure):
        ...


class FigureAreaVisitor(Visitor):

    @singledispatchmethod
    def visit(self, figure):
        return NotImplementedError

    @visit.register(Circle)
    def _(self, figure):
        return figure.area()

    @visit.register(Square)
    def _(self, figure):
        return figure.area()


square = Square(5)
res = square.accept(FigureAreaVisitor())
print(res)