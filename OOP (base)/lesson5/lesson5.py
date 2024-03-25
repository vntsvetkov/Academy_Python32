""" День 5. Абстрактные классы. """

from abc import ABC, abstractmethod, abstractproperty, abstractclassmethod, abstractstaticmethod

"""
Абстракный класс - определяет общий интерфейс для 
всего набора подклассов. Заставляет наследников
реализовать набор своих методов.

Особенности:
1. Абстракный класс не содержит реализаций методов,
а только их описание
2. От абстрактного класса не создается экземпляр
3. Наследник ОБЯЗАН переопределить все методы 
абстрактного класса

"""


class ITEmployee:

    def __init__(self, name):
        self.__name = name


class Programmer(ABC):

    @abstractmethod
    def write_code(self):
        ...

    @staticmethod
    @abstractmethod
    def check_language(lang: str):
        ...


class FrontendProgrammer(Programmer):

    __LANGUAGES = ('JS', 'React', 'HTML', 'CSS')

    def write_code(self):
        print("Верстаю сайт на js")

    @staticmethod
    def check_language(lang: str) -> bool:
        return lang in FrontendProgrammer.__LANGUAGES


class BackendProgrammer(Programmer):

    __LANGUAGES = ('Python', 'C++', 'SQL')

    def write_code(self):
        print("Пишу программу для работы с БД")

    @staticmethod
    def check_language(lang: str) -> bool:
        return lang in BackendProgrammer.__LANGUAGES


class Tester(ABC):

    @abstractmethod
    def testing_product(self):
        ...


class FunctionalTester(Tester):
    ...


class AutoTester(Tester):
    ...


def work(developers: list[Programmer]):

    for developer in developers:
        developer.write_code()


front_programmer = FrontendProgrammer()
front_programmer.write_code()

back_programmer = BackendProgrammer()
back_programmer.write_code()

print(back_programmer.check_language('Java'))

command_develop = [front_programmer, back_programmer]

work(command_develop) # Полиморфизм

