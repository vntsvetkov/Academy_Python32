# factory.py
from abc import ABC, abstractmethod
from builder import Builder, CarBuilder
"""
Паттерн Фабричный метод (фабрика)

Позволяет создавать конкретные реализации общего интерфейса

"""


class Transport(ABC):

    @abstractmethod
    def delivery(self):
        ...


class Car(Transport):

    def delivery(self):
        print("Выполняю перевозку пассажиров")


class Truck(Transport):

    def delivery(self):
        print("Выполняю доставку груза")


class SystemReservation(ABC):

    @abstractmethod
    def create_transport(self, cb: Builder) -> Transport:
        ...


class CarReservation(SystemReservation):

    def create_transport(self, cb: Builder) -> Transport:
        # алгоритм создания авто
        return cb.get_car()


class TruckReservation(SystemReservation):

    def create_transport(self, tb: Builder) -> Transport:
        return Truck()


fabric = CarReservation()
car_builder = CarBuilder()
fabric.create_transport(car_builder)
