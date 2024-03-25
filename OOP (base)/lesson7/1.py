"""SOLID"""


"""

1.Принцип единственной ответственности (Single Responsibility Principle)

Требование, чтобы один класс выполнял только одну возложенную на
него задачу. 

"""

"""
Пример 1. Класс автомобиль. 
"""


class Car:

    def __init__(self, model, tank):
        self.model = model
        self.tank = tank

    def drive(self):
        ...

    def start_engine(self):
        ...


class DBCarManagement:

    name_db: str = "cars.db"

    @classmethod
    def save(cls, cars: list[Car]) -> None:
        ...

    @classmethod
    def load(cls) -> list[Car]:
        ...


class GasStation:

    fuel_reserve: float = 10000000

    @classmethod
    def refuel(cls, car: Car, quantity: float):
        if cls.fuel_reserve >= quantity:
            car.tank += quantity
            cls.fuel_reserve -= quantity
