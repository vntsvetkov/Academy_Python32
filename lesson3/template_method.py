# template_method.py

from abc import ABC, abstractmethod

"""
Шаблонный метод
Позволяет подклассам переопределять шаги алгоритма 
не изменяя его общей структуры 

"""


class DBManager(ABC):

    def search_user(self, login: str):
        self.get_connection()
        self.execute_request()
        self.close()

    @abstractmethod
    def get_connection(self):
        ...

    @abstractmethod
    def execute_request(self):
        ...

    @abstractmethod
    def close(self):
        ...


class DBPGManager(DBManager):

    def get_connection(self):
        ...

    def execute_request(self):
        ...

    def close(self):
        ...


class DBRedisManager(DBManager):

    def get_connection(self):
        ...

    def execute_request(self):
        ...

    def close(self):
        ...

