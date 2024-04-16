# decorator.py

from abc import ABC, abstractmethod

"""
Паттерн декоратор
Предоставление классам новых функциональных возможностей

"""


class NotificationSender:

    def send(self, message):
        print(f"Уведомление в личном кабинете: {message}")


class DecoratorNotificationSender(NotificationSender):

    _notification: NotificationSender

    def send(self, message):
        self._notification.send(message)


class SMSNotificationSender(DecoratorNotificationSender):

    def __init__(self, notification: NotificationSender):
        self._notification = notification

    def send(self, message):
        print(f"Уведомление по sms: {message}")
        super().send(message)


# notification_sender = SMSNotificationSender(NotificationSender())
# notification_sender.send("Привет")


def decorator(name):
    def outer(f):
        def wrapper(*args, **kwargs):
            result = f(*args, **kwargs)  # Привет
            return result + " " + name
        return wrapper
    return outer


@decorator("Вася")
def func():
    return "Привет"


my_func = func()
