""" День 6. Множественное наследование и миксины """

from abc import ABC, abstractmethod

"""

Множественное наследование.
    Возможность класса наследоваться от нескольких классов

class A:
    ...


class B:
    ...


class C(A, B):
    ...

Миксины.
    

"""

"""

Задача 1. Создать абстракцию наземного транспорта

Наследники абстракции:
    - Реализовать класс пассажирский трансопрт
    - Реализовать класс электротранспорт


Реализовать класс Электробус

"""


class RadioMixIn:

    __stations = {103.5: 'Европа+', 98.7: 'АвтоРадио'}

    @classmethod
    def turn_radio(cls, station: float):
        try:
            print(f"Вы слушаете радио {cls.__stations[station]}")
        except KeyError:
            print(f"Радиостанция на частоте {station} не найдена")


class GroundTransport(ABC):

    @abstractmethod
    def start_engine(self):
        ...

    @abstractmethod
    def drive(self, distance: float):
        ...


class PassengerTransport(GroundTransport):

    def __init__(self, capacity):
        self.capacity = capacity

    def start_engine(self):
        print('Двигатель заведен')

    def drive(self, distance: float):
        print("Движется пассажирский транспорт")


class ElectricTransport(GroundTransport):

    def __init__(self, voltage):
        self.voltage = voltage

    def start_engine(self):
        print('Двигатель заведен')

    def drive(self, distance: float):
        print("Движется электротранспорт")


class ElectricBus(PassengerTransport, ElectricTransport, RadioMixIn):

    def __init__(self, capacity, voltage, battery):
        ElectricTransport.__init__(self, voltage)
        PassengerTransport.__init__(self, capacity)
        self.battery = battery


bus = ElectricBus(100, 600, 100000)
print(bus.capacity)
print(bus.voltage)
bus.drive(1000)
bus.turn_radio(103.5)
print(ElectricBus.mro())
