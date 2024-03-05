""" SOLID """
from abc import ABC, abstractmethod

"""
5. Принцип инверсии зависимостей (Dependency Inversion Principle)

Классы верхнего уровня не должны зависеть от классов нижнего
уровня. И то и другое должно зависеть от абстракций, но не
от конкретных реализаций.

"""


class C(ABC):

    @abstractmethod
    def f(self):
        ...


class B(C):
    def f(self):
        ...


class A:

    def __init__(self, c: C):
        self.c = c

    def d(self):
        self.c.f()


"""

Пример 1. Класс магазин. 
В магазине можно расплачиваться 3 способами: наличные, карта,
по qr-коду.

"""


class Payment(ABC):

    @abstractmethod
    def pay(self):
        ...


class Cash(Payment):

    def pay(self):
        print("Оплачено наличными")


class Card(Payment):

    def pay(self):
        print("Оплачено картой")


class QRCode(Payment):

    def pay(self):
        print("Оплчено по qr-коду")


class Shop:

    def __init__(self):
        self.payment = None

    @property
    def payment(self):
        return self.payment

    @payment.setter
    def payment(self, payment: Payment):
        self.payment = payment

    def do_pay(self):
        self.payment.pay()


card = Card()
qr_code = QRCode()

shop = Shop()
shop.payment = card
shop.do_pay()
