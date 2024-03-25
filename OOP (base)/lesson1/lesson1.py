""" День 1. Введение в ООП. Классы и объекты """

"""
Объектно-ориентированное программирование

1. Инкапсуляция
2. Наследование
3. Полиморфизм

"""

"""

Задача 1. Создать пользовательский тип 'Студент'

"""


from copy import copy, deepcopy


class Student:

    def __init__(self, name, age, group, avg_score, subjects: list) -> None:

        self.name: str = name
        self.age: int = age
        self.group: str = group
        self.avg_score: float = avg_score
        self.subjects: list = deepcopy(subjects)

    def __str__(self) -> str:
        return (f"Имя: {self.name} \n"
                f"Возраст: {self.age} \n"
                f"Группа: {self.group} \n"
                f"Средний балл: {self.avg_score} \n"
                f"Предметы: {', '.join(self.subjects)} \n")


student = Student("Иван",
                  27,
                  "127154С",
                  8.7,
                  ['Мат. анализ', 'Программирование на Python'])

subjects = ['Мат. анализ', 'Программирование на Python']

new_student = Student("Петр",23,"127154С",7.5, subjects)

subjects[0] = "Экономика"

print(new_student)


"""

Задача 2. Создать пользовательский тип 'Точка'. 
- Описать метод __str__.
- Создать 2 объекта от этого класса.
- Проверить что обе точки лежат на оси X

"""


class Point:

    def __init__(self, coor_x: int, coor_y: int):
        self.x: int = coor_x
        self.y: int = coor_y

    def __str__(self):
        return f"(x: {self.x}; y: {self.y}"


p1 = Point(1, 2)
p2 = Point(0, 3)

if p1.y == 0 and p2.y == 0:
    print("Лежат на оси Х")
else:
    print("Не лежат на оси Х")


""" Задача 3. Создать пользовательский тип 'Программист' """

class Programmer:

    def __init__(self, name: str, age: int, iq: int, level: str,
                 languages: list[str]) -> None:
        self.name: str = name
        if age < 18:
            raise ValueError("Возраст программиста не может быть меньше 18")
        self.age: int = age
        self.iq: int = iq
        self.level: str = level
        self.languages: list[str] = deepcopy(languages)

    def __str__(self) -> str:
        return f"Имя: {self.name} \n" \
               f"Возраст: {self.age} \n" \
               f"Уровень: {self.level}"

