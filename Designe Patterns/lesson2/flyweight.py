# flyweight.py

from abc import ABC, abstractmethod

"""
Паттерн приспособленец.
Основная идея паттерна — различие между внутренним 
и внешним состоянием объекта. 
Внешнее состояние передается клиентом, 
использующим приспособленца, в некотором контексте. 
Внутреннее состояние хранится непосредственно в приспособленце 
и позволяет разделять их.
"""


class Engine:

    def __init__(self, capacity):
        self.capacity = capacity


class FactoryEngine:

    _cache = {}

    """
    1.2: Engine(1.2)
    1.7: Engine(1.7)
    """

    @classmethod
    def get_engine(cls, capacity):
        value = cls._cache.get(capacity)
        if value is None:
            cls._cache[capacity] = Engine(capacity)
        return value


class Car:

    def __init__(self, model):
        # Внутреннее состояние
        self.model = model
        # Внешнее состояние
        self.engine = None

    def set_engine(self, capacity):
        self.engine = FactoryEngine.get_engine(capacity)

