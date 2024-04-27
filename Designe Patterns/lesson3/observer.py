# observer.py

from abc import ABC, abstractmethod

"""
Паттерн наблюдатель
Позволяет реализовать механизм подписки, позволяющий одним объектам следить и реагировать на события, 
происходящие в других объектах.

"""

# Схожим образом работает Система подписок
from abc import ABC, abstractmethod


class CameraSystem:
    """Централизованная система наблюдения."""

    def __init__(self):
        self.__observers = set()

    # Подключить наблюдателя(камеру) к системе. (просто добавляем объект в список).
    def attach(self, observer):
        self.__observers.add(observer)

    # Отключить наблюдателя(камеру) от системы. (просто удаляем объект из список).
    def detach(self, observer):
        self.__observers.remove(observer)

    # Отправка уведомления\команды всем наблюдателям(камерам) подключенным к системе.
    # (Проходимся по списку объектов и вызываем нужный метод).
    def notify(self):
        for observer in self.__observers:
            observer.make_photo()


# Абстрактный класс наблюдателя.
class AbstractObserver(ABC):
    @abstractmethod
    def make_photo(self):  # Абстрактный наблюдатель задает метод make_photo
        pass


class Camera(AbstractObserver):
    """Камера наблюдения."""
    __repository = "C:/Cameras/Photos"

    def __init__(self, name):
        self.name = name

    def set_path(self, path):
        self.__repository = path

    def make_photo(self):
        print('{} сделала фото'.format(self.name))


if __name__ == '__main__':
    # Камер на заборе у нас будет 3.
    cam1 = Camera('Камера #1')
    cam2 = Camera('Камера #2')
    cam3 = Camera('Камера #3')

    # Создадим центральный пульт управления.
    cam_system = CameraSystem()

    # Подключим все 3 камеры к пульту управления.
    cam_system.attach(cam1)
    cam_system.attach(cam2)
    cam_system.attach(cam3)

    # Оп ! Внимание, пульт каким-то образом понял, что кто то постучал в дверь.
    # сообщим всем подключенным к пульту камерам, что нужно сделать фото.
    cam_system.notify()

    # >>> Камера #1 сделала фото
    # >>> Камера #2 сделала фото
    # >>> Камера #3 сделала фото

    # Отключим первую камеру от пульта, т.к. фотки с нее получаются не четкие :)
    cam_system.detach(cam1)

    # Вновь происходит событие.
    cam_system.notify()

    # >>> Камера #2 сделала фото
    # >>> Камера #3 сделала фото