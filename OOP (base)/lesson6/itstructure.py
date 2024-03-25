from abc import ABC, abstractmethod


class ITEmployee:

    def __init__(self, name):
        self._name = name


class DeveloperEmployee(ITEmployee):

    def __init__(self, name, language):
        super().__init__(name)
        self._language = language

    def write_code(self):
        print('Пишу код на языке', self._language)


class FrontendDeveloper(ABC):

    @abstractmethod
    def make_page(self):
        ...


class BackendDeveloper(ABC):

    @abstractmethod
    def create_db(self):
        ...


class FrontendProgrammer(DeveloperEmployee, FrontendDeveloper):

    def __init__(self, name, language, front):
        super().__init__(name, language)
        self._only_front = front

    def make_page(self):
        print('Пишу страницу на языке ', self._language)


class BackendProgrammer(DeveloperEmployee, BackendDeveloper):

    def __init__(self, name, language, back):
        super().__init__(name, language)
        self._only_back = back

    def create_db(self):
        print('Создаю БД на языке ', self._language)


class FullStackProgrammer(DeveloperEmployee, FrontendDeveloper, BackendDeveloper):

    def __init__(self, name, language):
        super().__init__(name, language)

    def create_db(self):
        print("Работаю с базой данных")

    def make_page(self):
        print("Создаю web-страницу")

def task(developer: DeveloperEmployee):

    developer.write_code()


programmer = FullStackProgrammer('Игорь', 'Python')
task(programmer)