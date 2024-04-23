# strategy.py

from abc import ABC, abstractmethod

"""
Паттерн стратегия
Обеспечивает взаимозаменяемость разных алгоритмов, либо
вариаций алгоритма с одинаковым интерфейсом

"""


class User:
    ...


class DBStrategy(ABC):

    @staticmethod
    @abstractmethod
    def search_user(login: str) -> User:
        ...


class PGDBStrategy(DBStrategy):

    @staticmethod
    def search_user(login: str) -> User:
        ...


class RedisDBStrategy(DBStrategy):

    @staticmethod
    def search_user(login: str) -> User:
        ...


class ElasticsearchDBStrategy(DBStrategy):

    @staticmethod
    def search_user(login: str) -> User:
        ...


class Authorization:

    def __init__(self, db: DBStrategy):
        self._db = db

    def log_in(self, login: str, password: str):
        ...


db_strategy = ElasticsearchDBStrategy()
auth = Authorization(db_strategy)
