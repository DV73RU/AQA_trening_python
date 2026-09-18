from abc import ABC, abstractmethod


class BaseReporter(ABC):
    """Класс репортёр"""

    @abstractmethod
    def publish(self, result) -> str:
        """Метод публикует отчёт """
        pass


class ConsoleReporter(BaseReporter):
    """Класс отправки отчёта в консоль"""

    def publish(self, result) -> str:
        """Метод отправляет отчёт в консоль"""
        return f"Тест: {result}"


class FileReporter(BaseReporter):
    """Класс отправки отчёта в файл"""

    def publish(self, result) -> str:
        with open("file.txt", "w", encoding="UTF-8") as f:
            f.write(str(result))
        # Возвращаем строку (например, путь к файлу), чтобы соблюсти контракт
        return f"Отчёт успешно записан в файл file.txt"

# class TelegramReporter(BaseReporter):
#     """Класс отправки репорта в Телеграм"""
#     def publish(self, result, token) -> str: #<- Тут нарушение контракта, ожидаем токен, которого нет в родителе
#         return result

# Исправленная версия TelegramReporter

class TelegramReporter(BaseReporter):
    """Класс отправки репорта в Телеграм"""
    def __init__(self,token):
        self.token = token

    def publish(self, result) -> str: #<- Тут нарушение контракта, ожидаем токен, которого нет в родителе
        #Реализация отправки сообщения в телеграм с применением self.token
        return f"Результат {result} отправлен в телеграмм"

