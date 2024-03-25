from abc import ABC, abstractmethod

"""

Задача 1. Реализовать абстрактный класс Транспорт.

Создать 2 наследника: автомобиль и мотоцикл.
Используя любой из этих классов необходимо проехать/не проехать
некоторое расстояние исходя из характеристик транспорта.
Перед началом движения необходимо завести двигатель и
проверить сможет/не сможет транспорт проехать указанное 
расстояние с имеющимся запасом топлива.

"""


class Transport(ABC):

    @abstractmethod
    def start_engine(self):
        ...

    @abstractmethod
    def stop_engine(self):
        ...

    @abstractmethod
    def drive(self, distance: float):
        ...

    @abstractmethod
    def check_fuel(self, distance: float):
        ...


class Car(Transport):

    __consumption = 0.1  # л/км
    __engine = False  # не заведен по умолчанию

    def __init__(self, model: str, tank: float):
        self.__model = model
        self.__tank = tank

    def start_engine(self):
        if not self.__engine:
            self.__engine = True
            print("Двигатель заведен")
        else:
            print("Двигатель уже заведен")

    def stop_engine(self):
        if self.__engine:
            self.__engine = False
            print("Двигатель остановлен")
        else:
            print("Двигатель уже остановлен")

    def check_fuel(self, distance: float) -> bool:
        return self.__tank / self.__consumption >= distance

    def drive(self, distance: float):
        self.start_engine()
        if self.check_fuel(distance):
            print("Поездка выполнена")
            self.__tank -= distance * self.__consumption
            print("Осталось топлива: ", self.__tank)
        else:
            print("Недостаточно топлива для поездки")
        self.stop_engine()


class Bike(Transport):
    ...


def trip(transport: Transport):

    transport.drive(100)  # ехать 100 км.


car = Car("Kia", 48)
trip(car)
