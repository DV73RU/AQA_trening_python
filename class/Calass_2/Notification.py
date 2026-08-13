def send_message(object_notification: object, message: str):
    """Функция принимает объект и текст сообщения"""
    return object_notification.send(message)  # Функция вернёт вызов метода 'send' переданного объекта


class Notification:
    """Класс отправки сообщения"""

    def __init__(self, message: str, object_notification: object):
        self.message = message # Текст сообщения
        self.object_notification = object_notification # Объект отправки

    def send(self):
        """Метод отправки сообщения"""
        pass


class EmailNotification(Notification):
    """Класс отправки сообщение на Email"""
    def __init__(self, message, mail, object_notification: object):
        super().__init__(message, object_notification)
        self.message = message
        self.mail = mail

    def send(self):
        pass