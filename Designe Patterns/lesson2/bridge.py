# bridge.py

from abc import ABC, abstractmethod

"""
Паттерн мост.
Позволяет отделить абстракции от реализаций таким образом, 
чтобы они могли меняться независимо друг от друга

Композиция лучше наследования
"""


class Theme(ABC):
    @abstractmethod
    def get_palette(self):
        ...


class StandardTheme(ABC):

    def get_palette(self):
        ...


class LightTheme(Theme):
    def get_palette(self):
        ...


class DarkTheme(Theme):

    def get_palette(self):
        ...


class WebPage(ABC):

    @abstractmethod
    def get_theme(self):
        ...


class HomePage(WebPage):

    def __init__(self):
        self._theme = StandardTheme()

    def change_theme(self, theme: Theme):
        self._theme = theme

    def get_theme(self):
        self._theme.get_palette()


class AboutPage(WebPage):

    def get_theme(self):
        ...


class NewsPage(WebPage):

    def get_theme(self):
        ...


page = HomePage()
page.get_theme()
