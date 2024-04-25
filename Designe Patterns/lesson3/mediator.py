# mediator.py


from abc import ABC, abstractmethod


"""
Паттерн посредник
Позволяет разделить взаимосвязи между классами и берет на себя функцию связывания. 
Классы будут общаться через класс-посредник.

"""

class Mediator(ABC):

    @abstractmethod
    def send(self, message: str, employee):
        raise NotImplementedError


class Employee:
    def __init__(self, mediator: Mediator):
        self.__mediator: Mediator = mediator

    def send(self, message):
        self.__mediator.send(message, self)

    @staticmethod
    @abstractmethod
    def notify(message: str):
        raise NotImplementedError


class Customer(Employee):
    @staticmethod
    def notify(message: str):
        print("Сообщение заказчику: ", message)


class Programmer(Employee):
    @staticmethod
    def notify(message: str):
        print("Сообщение программисту: ", message)


class Tester(Employee):
    @staticmethod
    def notify(message: str):
        print("Сообщение тестировщику: ", message)


class Manager(Mediator):

    def send(self, message: str, employee):
        if isinstance(employee, Customer):
            Programmer.notify(message)
        elif isinstance(employee, Programmer):
            Tester.notify(message)
        elif isinstance(employee, Tester):
            Customer.notify(message)



manager = Manager()
customer = Customer(manager)
programmer = Programmer(manager)
tester = Tester(manager)

customer.send("Поступил заказ на разработку приложения")
programmer.send("Приложение готово, нужно протестировать")
tester.send("Программа протестирована и готова")