# memento.py

from abc import ABC, abstractmethod


"""
Паттерн хранитель
Позволяет определять, сохранять, а также восстанавливать предыдущие состояния объектов.

"""


class DocumentRecoveryError(Exception):

    def __init__(self, text):
        self.text = text


class DocumentMemento:

    def __init__(self, text):
        self.__text: str = text

    @property
    def text(self):
        return self.__text


class Document:

    __text = ""

    def add_text(self, data: str):
        self.__text += data + '\n'

    def get_text(self):
        return self.__text

    def save(self):
        return DocumentMemento(self.__text)

    def restore(self, doc: DocumentMemento):
        self.__text = doc.text


class Editor:

    def __init__(self):
        self.__history = []

    def push(self, doc: DocumentMemento):
        self.__history.append(doc)

    def pop(self):
        if len(self.__history) > 0:
            return self.__history.pop()
        raise DocumentRecoveryError("Невозможно восстановить документ")


editor = Editor()

document = Document()
document.add_text("Строка данных 1")
document.add_text("Строка данных 2")

cur_doc = document.save()
editor.push(cur_doc)

document.add_text("Строка данных 3")
print(document.get_text())
print("-------------После восстановления -------------")
document.restore(editor.pop())
print(document.get_text())

