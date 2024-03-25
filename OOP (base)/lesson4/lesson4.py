""" День 4. Наследование классов. """

"""

Наследование. 
    - Последовательное (многоуровневое)
    - Множественное

"""


class ValidateError(Exception):

    def __init__(self, text):
        self.text = text


class ValidateAgeError(ValidateError):
    ...


class ValidateNameError(ValidateError):
    ...


class EmptyNameError(ValidateNameError):
    ...


class FormatNameError(ValidateNameError):
    ...


class ITEmployee:

    def __init__(self, name: str,
                 age: int,
                 experience: float,
                 level: str):
        self.__name: str = self.__validate_name(name)
        self.__age: int = age
        self.__experience: float = experience
        self._level: str = level

    def __str__(self):
        return (f"Имя: {self.__name}\n"
                f"Возраст: {self.__age}\n"
                f"Опыт работы: {self.__experience}\n")

    def print_level(self) -> None:
        print(self._level)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__validate_name(name)

    @staticmethod
    def __validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError('Параметр name должен быть строкой')
        if not name:
            raise EmptyNameError('Параметр name не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, name))
        if len(a) != len(name):
            raise FormatNameError('Параметр name должен содержать только символы кириллицы')

        return name.capitalize()


class Programmer(ITEmployee):

    def __init__(self, name: str,
                 age: int,
                 experience: float,
                 level: str,
                 languages: list):
        super().__init__(name, age, experience, level)
        self.__languages: list = languages

    def __str__(self) -> str:
        return (super().__str__() +
                f"Языки: {','.join(self.__languages)}\n"
                f"Уровень: {self._level} \n")

    def print_level(self) -> None:
        print("Текущий уровень разработчика: ")
        super().print_level()


class FrontendProgrammer(Programmer):
    ...


class BackendProgrammer(Programmer):
    ...


class Tester(ITEmployee):

    def __init__(self, name: str,
                 age: int,
                 experience: float,
                 level: str,
                 count_bug: int):
        super().__init__(name, age, experience, level)
        self.__count_bug: int = count_bug


class FunctionalTester(Tester):
    ...


class AutoTester(Tester):
    ...


class AutoMobileTester(AutoTester):
    ...


class AutoWebTester(AutoTester):
    ...


# employee = ITEmployee('Иван', 37, 10)

programmer = Programmer('Иван', 37, 10, 'Senior+', ['Java'])
tester = Tester('Петр', 29, 5, 'Middle', 150)

programmer.name = "Яков"
programmer.print_level()
