from stack import Stack


class Expression:

    operation_priority = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
    }

    def __init__(self, expression: str):
        self.__infix_expression: str = expression
        self.__postfix_expression: list = self.to_postfix(expression)

    @property
    def infix_expression(self):
        return self.__infix_expression

    @property
    def postfix_expression(self):
        return self.__postfix_expression

    @staticmethod
    def to_postfix(expression: str) -> list:
        """
        Метод, который переводит инфиксную запись в постфиксную
        :param expression:
        :return:
        """
        pass

    def normalize_infix_expression(self):
        """
        Метод, который учитывает отрицательные значения и приводит инфиксную
        запись выражения к виду пригодному для перевода в постфиксную запись
        :return:
        """
        pass

    def check_brackets(self):
        """
        Метод, который проверяет правильность расстановки скобочек в инфиксной форме выражения
        :return:
        """

    def get_expression_value(self):
        """
        Возвращает значение выражения, записанного в постфиксной форме в поле __postfix_expression
        :return:
        """
        pass


"""
Выполните сценарий:
    1. Получить выражение в инфиксной форме
    2. Создать объект Expression
    3. Проверить правильность расстановки скобок (необязательно)
    4. Нормализовать инфиксную форму записи
    5. Вернуть значение выражения
"""