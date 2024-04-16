# facade.py

from abc import ABC, abstractmethod

"""

Паттерн Фасад.

Паттерн, кроторый предоставляет простой интерфейс 
для работы со сложным модулем или библиотекой 

"""


class AuthorizationError(Exception):
    def __init__(self, text):
        self._text = text


#  Модуль 1
class User(ABC):
    _login: str
    _password: str

    @abstractmethod
    def get_login(self):
        ...

    @abstractmethod
    def get_password(self):
        ...


class DefaultUser(User):

    def get_login(self):
        return self._login

    def get_password(self):
        return self._password


class Administrator(User):

    def get_login(self):
        return self._login

    def get_password(self):
        return self._password


#  Модуль 2
class DBManager(ABC):

    @staticmethod
    @abstractmethod
    def search_user(login: str) -> User:
        ...


class PGDBManager(DBManager):

    @staticmethod
    def search_user(login: str) -> User:
        ...


class RedisDBManager(DBManager):

    @staticmethod
    def search_user(login: str) -> User:
        ...


# Класс фасада
class Authorization:

    def __init__(self, db: DBManager):
        self._db = db

    def log_in(self, login: str, password: str):
        user = self._db.search_user(login)
        if user is not None:
            if user.get_password() == password:
                return True

            raise AuthorizationError("Неверный логин или пароль")
        raise AuthorizationError("Пользователь не существует")


db_manager = PGDBManager()
auth = Authorization(db_manager)

cur_login = ""
cur_password = ""

try:
    status = auth.log_in(cur_login, cur_password)
except AuthorizationError as e:
    print(e)  # вернуть ошибку пользователю
else:
    print("Авторизация успешно пройдена")
