# decorator.py

from abc import ABC, abstractmethod

"""
Паттерн декоратор
Предоставление классам новых функциональных возможностей

"""

class Notification(ABC):

    @abstractmethod
    def send(self, _):
        ...

class NotificationSender(Notification):

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


class EmailNotificationSender(DecoratorNotificationSender):

    def __init__(self, notification: NotificationSender):
        self._notification = notification

    def send(self, message):
        print(f"Уведомление по email: {message}")
        super().send(message)


notification_sender = NotificationSender()
notification_sender = SMSNotificationSender(notification_sender)
notification_sender = EmailNotificationSender(notification_sender)
notification_sender.send("Привет")
