# state.py

from abc import ABC, abstractmethod

"""
Паттерн состояние
Позволяет изменять поведение объекта в зависимости от 
его описанного состояния


Задача. Корзина товаров в онлайн-магазине
"""


class DeleteProductError(Exception):

    def __init__(self, text):
        self.text = text


class Product:

    def __init__(self, name):
        self.name = name


class BasketState(ABC):

    @staticmethod
    @abstractmethod
    def add(basket, product: Product):
        ...

    @staticmethod
    @abstractmethod
    def remove(basket, product: Product):
        ...


class Basket:

    def __init__(self, state: BasketState):
        self._state = state
        self.products: list[Product] = []

    def set_state(self, state: BasketState):
        self._state = state

    def add(self, product: Product):
        self._state.add(self, product)

    def remove(self, product: Product):
        self._state.remove(self, product)


class FullBasket(BasketState):

    @staticmethod
    def add(basket: Basket, product: Product):
        basket.products.append(product)
        print(f"В корзине {len(basket.products)} товаров")

    @staticmethod
    def remove(basket: Basket, product: Product):
        if len(basket.products) == 1:
            basket.products.pop()
            basket.set_state(EmptyBasket())
            print("Корзина пуста")
        else:
            basket.products.remove(product)
            print(f"В корзине {len(basket.products)} товаров")


class EmptyBasket(BasketState):

    @staticmethod
    def add(basket: Basket, product: Product):
        basket.products.append(product)
        basket.set_state(FullBasket())
        print(f"В корзине {len(basket.products)} товаров")

    @staticmethod
    def remove(basket: Basket, product: Product):
        raise DeleteProductError("Невозможно выполнить операцию удаления товара из пустого состояния")


p1 = Product("Футболка")
p2 = Product("Шорты")

basket = Basket(EmptyBasket())
basket.add(p1)
basket.add(p2)
basket.remove(p1)
basket.remove(p2)


