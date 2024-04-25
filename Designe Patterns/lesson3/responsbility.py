# responsibility.py

from abc import ABC, abstractmethod

"""
Паттерн цепочка обязанностей
Позволяет настраивать уровни ответственности между классами

"""


class Account:

    successor = None  # преемник
    name = None

    def __init__(self, balance: float):
        self.__balance = balance

    def can_pay(self, amount: float):
        return self.__balance >= amount

    def next(self, account):
        if issubclass(account.__class__, Account):
            self.successor = account

    def pay(self, amount: float):
        if self.can_pay(amount):
            print(f"Оплата совершена картой {self.name}")
        elif self.successor is not None:
            self.successor.pay(amount)
        else:
            raise Exception("Недостаточно средств...")


class SberbankCard(Account):

    name = "Сбербанк карта"


class TinkoffCard(Account):

    name = "Тинькофф карта"


class AlfaCard(Account):

    name = "Альфа карта"


sberbank = SberbankCard(1000)
tinkoff = TinkoffCard(2000)
alfa = AlfaCard(3000)

sberbank.next(tinkoff)
tinkoff.next(alfa)

sberbank.pay(4000)


