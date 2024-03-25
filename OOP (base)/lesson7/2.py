""" SOLID """

"""

2. Принцип открытости/закрытости (Open‐Closed Principle)

Классы должны быть открыты для расширения, но закрыты для модификации

"""


class Car:

    def __init__(self, model):
        self.model = model

    def drive(self, distance: float):
        raise NotImplementedError


class ElectricCar(Car):
    ...


class GasCar(Car):
    ...


class GasolineCar(Car):
    ...

