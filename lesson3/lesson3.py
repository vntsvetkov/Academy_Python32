""" День 3. Типы методов: объекта, класса и статические """

from static import CalculateAreaFigures

"""

Типы методов:
    - методы объекта (влияют на атрибуты объекта и 'класса')
        вызываются от объекта
    - методы класса (влияют только на атрибуты класса)
        вызываются от класса, объекта
    - статические методы (не влияют на атрибуты объекта)
        вызываются от класса или объекта

Типы атрибутов:
    - объекта
    - класса
    
"""


class Programmer:

    __GRADATIONS = ('Junior', 'Middle', 'Senior')
    __level: str = "Junior"

    def __init__(self, name: str, age: int, languages: list,
                 experience: float = 0):
        self.__name: str = self.__validate_name(name)
        self.__age: int = self.__validate_age(age)
        self.__languages: list = languages
        self.__experience: float = experience

    @classmethod
    def create_from_file(cls, path: str) -> object:

        with open(path, 'r', encoding='utf-8') as file:
            data = list(map(lambda x: x.rstrip('\n'), file.readlines()))
            data[1] = int(data[1])
            data[2].split()
            data[3] = float(data[3])

        return cls(*data)

    @classmethod
    def get_level(cls) -> str:
        return cls.__level

    @classmethod
    def set_level(cls, level: str) -> None:
        cls.__level = cls.__validate_level(level)

    def append_language(self, language: str):
        if language in self.__languages:
            raise Exception('Ошибка повторного добавления элемента')
        self.__languages.append(language)

    @staticmethod
    def __validate_level(level: str) -> str:
        if not isinstance(level, str):
            raise TypeError('Параметр level должен быть строкой')
        if not level:
            raise ValueError('Параметр level не может быть пустым')
        if level not in Programmer.__GRADATIONS:
            raise ValueError(f'Параметр level должен принимать одно из значений: {Programmer.__GRADATIONS}')

        return level

    @staticmethod
    def __validate_name(name: str) -> str:
        if not isinstance(name, str):
            raise TypeError('Параметр name должен быть строкой')
        if not name:
            raise ValueError('Параметр name не может быть пустым')
        a = list(filter(lambda x: 1040 <= ord(x) <= 1103, name))
        if len(a) != len(name):
            raise ValueError('Параметр name должен содержать только символы кириллицы')

        return name.capitalize()

    @staticmethod
    def __validate_age(age: int) -> int:
        if not isinstance(age, int):
            raise TypeError('Параметр age должен быть целочисленным')
        if age < 18 or age > 65:
            raise ValueError('Параметр age должен быть в диапазоне от 18 до 65')
        return age


programmer1 = Programmer("Иван",
                        34,
                        ['Python', 'SQL'],
                        10)

programmer2 = Programmer.create_from_file('programmer.txt')
Programmer.set_level('Senior')
print(Programmer.get_level())
print(programmer1.get_level())

