def send_message(object_notification: object, message: str):
    """
    Функция принимает объект и текст сообщения
    """
    return object_notification.send(message)


class Notification:
    """Класс отправки сообщения"""

    def send(self, message):
        """Метод отправки сообщения"""
        return f"Отправка сообщения..."


class EmailNotifier(Notification):
    """Класс отправки сообщение на Email дочерний класс (Notification)"""

    def __init__(self, mail):
        self.mail = mail  # Принимает майл куда отправит текст

    def send(self, message):
        return f"Отправлено сообщение на {self.mail} c текстом {message}"


class TelegramNotifier(Notification):
    """Класс отправки сообщение в Telegram """

    def __init__(self, id_name):
        self.id_name = id_name  # Принимает на id аккаунта отправит текст

    def send(self, message):
        """Метод отправляет сообщение в Telegram """
        return f"Отправлено сообщение на {self.id_name} c текстом {message}"


class SlackNotifier(Notification):
    """Класс отправки сообщения в Slack"""

    def __init__(self, nick_name):
        self.nick_name = nick_name  # Принимает nick пользователя в Slack

    def send(self, message):
        return f"Отправлено сообщение на {self.nick_name} c текстом {message}"


send_mail = EmailNotifier("mail@test.ru")
send_telegram = TelegramNotifier("13DSD2W2332DS")
send_slack = SlackNotifier("@Kolya")

list_notifications = [send_mail, send_telegram, send_slack]
for notif in list_notifications:
    print(send_message(notif, "Текст сообщения"))
