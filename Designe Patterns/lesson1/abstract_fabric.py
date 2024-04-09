# abstract_fabric.py

from abc import ABC, abstractmethod

"""
Паттерн Абстрактная фабрика.

Фабрика, которая группирует зависимые фабрики

"""


class Phone(ABC):
    ...


class AndroidPhone(Phone):
    ...


class IPhone(Phone):
    ...


class Charger(ABC):
    ...


class LightCharger(Charger):
    ...


class TypeCCharger(Charger):
    ...


class MobilePhoneFactory(ABC):

    @abstractmethod
    def create_phone(self) -> Phone:
        ...

    @abstractmethod
    def create_charger(self) -> Charger:
        ...


class IOSSetFactory(MobilePhoneFactory):

    def create_phone(self) -> Phone:
        return IPhone()

    def create_charger(self) -> Charger:
        return LightCharger()


class AndroidSetFactory(MobilePhoneFactory):

    def create_phone(self) -> Phone:
        return AndroidPhone()

    def create_charger(self) -> Charger:
        return TypeCCharger()


class MobileSet:
    __mobile_set = []

    def add(self, unit):
        self.__mobile_set.append(unit)


class MobileShop:

    def __init__(self, factory: MobilePhoneFactory):
        self.__factory = factory

    def create_mobile_set(self) -> MobileSet:
        mobile_set = MobileSet()
        mobile = self.__factory.create_phone()
        charger = self.__factory.create_charger()
        mobile_set.add(mobile)
        mobile_set.add(charger)
        return mobile_set


ios_factory = IOSSetFactory()
shop = MobileShop(ios_factory)
mob_set = shop.create_mobile_set()
print(mob_set)
