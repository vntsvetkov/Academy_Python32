# proxy.py

from abc import ABC, abstractmethod

"""
Паттерн заместитель.
Предоставляет объект, который, в свою очередь, 
контролирует доступ к другому объекту путем перехвата всех вызовов. 

Задача. Банковский счет
"""


class Payment(ABC):

    @abstractmethod
    def get_balance(self):
        ...

    @abstractmethod
    def replenish(self, value):
        ...

    @abstractmethod
    def pay(self, value):
        ...


class BankAccount(Payment):
    _balance = 0

    def get_balance(self):
        return self._balance

    def replenish(self, value):
        self._balance += value

    def pay(self, value):
        if self._balance - value < 0:
            raise ValueError("Недостаточно средст на счете")
        self._balance -= value
        return self._balance


class Card(Payment):

    def __init__(self, account: Payment):
        self._account = account
        self._password = '0000'

    def set_password(self, new_password):
        self._password = new_password

    def get_balance(self):
        return self._account.get_balance()

    def replenish(self, value):
        self._account.replenish(value)

    def pay(self, value):
        self._account.pay(value)


# Товар
class Good:

    def __init__(self, id_good, cost):
        self.id_good = id_good
        self.cost = cost


class Shop:

    goods: list[Good]

    def add(self, good: Good):
        self.goods.append(good)

    def make_purchase(self, id_good, payment: Payment):

        def find_good():
            for good in self.goods:
                if id_good == good.id_good:
                    return good

        good = find_good()
        try:
            payment.pay(good.cost)
        except ValueError as e:
            print(e)


bank_account = BankAccount()
card = Card(bank_account)
card.set_password('1234')
card.replenish(100_000)
