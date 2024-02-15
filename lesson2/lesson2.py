"""  День 2. Модификаторы доступа. Приватные методы и поля """

"""

Задача 1. Реализовать класс 'Программист' (Programmer)

Модификаторы доступа:
    1. публичные (public)
    2. __приватные (private)
    3. _защищенные (protected)

"""


class Programmer:

    def __init__(self, name: str, age: int, languages: list,
                 experience: float, level: str):
        self.__name: str = self.__validate_name(name)
        self.__age: int = self.__validate_age(age)
        self.__languages: list = languages
        self.__experience: float = experience
        self.__level: str = level

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = self.__validate_name(name)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = self.__validate_name(name)

    def append_language(self, language: str):
        if language in self.__languages:
            raise Exception('Ошибка повторного добавления элемента')
        self.__languages.append(language)

    def __validate_name(self, name: str) -> str:
        if not isinstance(name, str):
            raise TypeError('Параметр name должен быть строкой')
        if not name:
            raise ValueError('Параметр name не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, name))
        if len(a) != len(name):
            raise ValueError('Параметр name должен содержать только символы кириллицы')

        return name.capitalize()

    def __validate_age(self, age: int) -> int:
        if not isinstance(age, int):
            raise TypeError('Параметр age должен быть целочисленным')
        if age < 18 or age > 65:
            raise ValueError('Параметр age должен быть в диапазоне от 18 до 65')
        return age


programmer = Programmer("Иван",
                        34,
                        ['Python', 'SQL'],
                        10,
                        'Senior+')

print(programmer.name)
programmer.name = "Сергей"
print(programmer.name)
programmer.append_language('Git')
