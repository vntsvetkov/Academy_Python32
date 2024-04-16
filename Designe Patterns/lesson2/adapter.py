# adapter.py

from abc import ABC, abstractmethod
import json

"""

Паттерн Адаптер. 
Промежуточный клас между несовместимыми интерфейсами

"""


class Human:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.name}, {self.age}, {self.gender}'


class JsonAdapter(ABC):

    @staticmethod
    @abstractmethod
    def dumps(obj):
        ...

    @staticmethod
    @abstractmethod
    def loads(data: str):
        ...

    @staticmethod
    @abstractmethod
    def dump(obj):
        ...

    @staticmethod
    @abstractmethod
    def load(path: str):
        ...


class JsonHumanAdapter(JsonAdapter):

    @staticmethod
    def dumps(obj: Human) -> str:
        if isinstance(obj, Human):
            return json.dumps(obj.__dict__)

    @staticmethod
    def loads(data: str) -> Human:
        obj: dict = json.loads(data)
        return Human(*obj.values())


human = Human('John', 29, 'm')
json_human = JsonHumanAdapter.dumps(human)
print(json_human)
normal_human = JsonHumanAdapter.loads(json_human)
print(normal_human)
