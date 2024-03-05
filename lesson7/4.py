""" SOLID """
from abc import ABC, abstractmethod
"""

4. Принцип разделения интерфейсов (Interface Segregation Principle)

Класс не должен зависеть от методов, которые он не реализует


"""


class Programmer(ABC):

    @abstractmethod
    def write_code(self):
        ...


class FrontendProgrammer(ABC):

    @abstractmethod
    def make_web_page(self):
        ...


class BackendProgrammer(ABC):

    @abstractmethod
    def create_db(self):
        ...


class FrontendDeveloper(Programmer, FrontendProgrammer):

    def write_code(self):
        ...

    def make_web_page(self):
        ...


class BackendDeveloper(Programmer, BackendProgrammer):

    def write_code(self):
        ...

    def create_db(self):
        ...


class FullStackDeveloper(Programmer, FrontendProgrammer, BackendProgrammer):

    def write_code(self):
        ...

    def create_db(self):
        ...

    def make_web_page(self):
        ...


