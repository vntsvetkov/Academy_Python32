""" SOLID """
from abc import ABC, abstractmethod
"""

3. Принцип подстановки Лисков (Liskov Substitution Principle)

Объекты подклассов должны быть полность взаимозаменяемыми с объектами
своих родительских классов 

"""


class Tester(ABC):

    @abstractmethod
    def testing_product(self):
        ...


class FunctionalTester(Tester):

    def testing_product(self):
        print("Выполняю ручное тестирование")


class AutoTester(Tester):

    def testing_product(self):
        print("Запускаю автотесты")


def test(tester: Tester):

    tester.testing_product()


func_tester = FunctionalTester()
auto_tester = AutoTester()

