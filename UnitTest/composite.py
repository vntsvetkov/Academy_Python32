# composite.py

from abc import ABC, abstractmethod

"""
Паттерн компоновщик.
Предполагает, что при разработке «контейнерных» объектов, 
которые собирают и упорядочивают «объекты содержимого», 
вы упрощаете операции, если предоставляете контейнерам 
и объектам содержимого общий набор методов.


Задача. Получить общий объем файлов каталога
"""


class SystemObject(ABC):

    @abstractmethod
    def get_size(self):
        ...


class File(SystemObject):

    def __init__(self, name, size: int):
        self._name = name
        self._size = size

    def get_size(self):
        return self._size


class Folder(SystemObject):
    __number = 1

    def __init__(self, name):
        self._name = name
        self._container: list[SystemObject] = []

    def get_container(self):
        return self._container

    def add(self, data: SystemObject):
        self._container.append(data)

    def get_size(self):
        result = 0
        for element in self._container:
            result += element.get_size()
        return result


if __name__ == '__main__':
    file1 = File('Файл 1', 120)
    file2 = File('Файл 2', 150)
    file3 = File('Файл 3', 170)

    folder1 = Folder('Папка 1')
    folder2 = Folder('Папка 2')
    folder1.add(file1)
    folder1.add(folder2)
    folder2.add(file2)
    folder2.add(file3)

    print(folder1.get_size())
    """
    folder1
        - folder2
            - file2
            - file3
        - file1
    """