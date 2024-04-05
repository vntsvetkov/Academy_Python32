# builder.py
from abc import ABC, abstractmethod

"""
Паттерн строитель.
Позволяет создавать объекты пошагово, без передачи параметров в конструктор

"""


class Car:

    def __init__(self):
        self.model = None
        self.engine = None
        self.tank = None
        self.max_speed = None

    def __str__(self):
        return self.model


class Builder(ABC):

    @abstractmethod
    def create(self):
        ...

    @abstractmethod
    def set_model(self, model):
        ...

    @abstractmethod
    def set_engine(self, engine):
        ...

    @abstractmethod
    def set_tank(self, tank):
        ...

    @abstractmethod
    def set_max_speed(self, max_speed):
        ...

    @abstractmethod
    def get_car(self):
        ...


class CarBuilder(Builder):

    _car: Car()

    def create(self):
        self._car = Car()

    def set_model(self, model):
        self._car.model = model

    def set_engine(self, engine):
        self._car.engine = engine

    def set_tank(self, tank):
        self._car.tank = tank

    def set_max_speed(self, max_speed):
        self._car.max_speed = max_speed

    def get_car(self):
        return self._car


class Director:

    def __init__(self, builder: Builder):
        self.__builder = builder

    def change_builder(self, builder: Builder):
        self.__builder = builder

    def make(self) -> Car:
        self.__builder.create()
        self.__builder.set_model('Haval')
        self.__builder.set_tank(56)
        self.__builder.set_max_speed(250)
        self.__builder.set_engine('Гибрид')
        return self.__builder.get_car()


car_builder = CarBuilder()
director = Director(car_builder)
car = director.make()
print(car)
