"""
Open/Closed Principal
Программные сущности должны быть закрыты от изменения и открыты для расширения
Новые возможности лучше добавлять, а не изменять существующие

2. Публикация результата — простая

Создай класс TestResult, который хранит название теста и статус.

Создай репортёры:

ConsoleReporter;
FileReporter;
TelegramReporter.

Каждый репортёр должен публиковать полученный результат своим способом.

Создай функцию publish_result(reporter, result). При добавлении нового репортёра функцию нельзя изменять.
"""

from abc import ABC, abstractmethod


class TestResult:
    """Класс результат теста"""

    def __init__(self, name_test, status_test):  # <- Храним имя теста и его статус
        self.name_test = name_test
        self.status_test = status_test


class BaseReport(ABC):  # <- Абстрактный класс отчёта
    """Класс отчёт"""

    @abstractmethod  # <- Декоратор абстрактного метода(значит должны присутствовать в классах дочерних)
    def publish(self, test_result: TestResult):  # <- Принимает результат теста как объект
        pass


class TelegramReporter(BaseReport):  # <- Класс отправка отчёта в Telegram (дочерний  BaseReport)
    def __init__(self, token: str, id_chat: str):  # <- Экземпляр принимает id чата
        self.token = token
        self.id_chat = id_chat

    def publish(self,
                test_result: TestResult) -> None:  # <- Метод публикации отчёта в Telegram, принимает отчёт как объект
        icons = {"PASSED": "🟢", "FAILED": "🔴", "SKIPPED": "🟡"}  # Словарь - Статус:Иконка
        icon = icons.get(test_result.status_test.upper(), "⚪")  # Поиск иконки статуса и нормализация текста статуса

        # Форматируем текст в Markdown для Telegram
        markdown_text = f"{icon} Тест: `{test_result.name_test}`\nСтатус: {test_result.status_test.upper()}"

        # Здесь должна быть реальная отправка через requests, пока делаем print для демонстрации
        print(f"[Telegram API] Сообщение отправлено в чат {self.id_chat}:\n{markdown_text}\n")


class FileReporter(BaseReport):  # <- Класс отправка отчёта в файл (дочерний  BaseReport)
    def __init__(self, file_name):  # <- Экземпляр принимает имя файла
        self.file_name = file_name

    def publish(self, test_result: TestResult):  # <- Метод публикации отчёта в Telegram, принимает отчёт как объект
        # return test_result.name_test, test_result.status_test  # Вернем атрибуты экземпляра
        print(f"Записываем в отчёт в файл {self.file_name}")
        with open(self.file_name, "a+", encoding="utf-8") as file:
            file.write(f"{test_result.name_test} - {test_result.status_test}\n")


# Используя принцип 'O' из S.O.L.I.D. добавим новый репортёр


class ConsoleReporter(BaseReport):  # <- Класс отправка отчёта в консоль (дочерний  BaseReport)
    def __init__(self, name_run):  # <- Экземпляр принимает имя запуска
        self.name_run = name_run

    def publish(self, test_result: TestResult):  # <- Метод публикации отчёта в Telegram, принимает отчёт как объект
        print(f"{self.name_run}:{test_result.name_test} - {test_result.status_test} ")  # Вернем атрибуты экземпляра


def publish_result(reporter: BaseReport,
                   result: TestResult):  # <- Функция отправки отчётов принимает объект репортёр( куда шлём, и объект результат теста

    try:
        reporter.publish(result)
    except Exception as e:
        print(f"Ошибка репортёра: {reporter.__class__.__name__} : {e}")


result1 = TestResult("Логин", "PASSED")  # <- Результат теста
result2 = TestResult("Открыта корзина", "FAILED")
result3 = TestResult("Подписка на новости", "SKIPPED")
result4 = TestResult("Логаут", "BLOCKED")  # <- Ели не известный статус

telegram_report = TelegramReporter("token_sdsdwee23dre3", "id_chat1212")  # <- Отчет в телегу
file_report = FileReporter("report.txt")  # <- Отчёт в файл
console_report = ConsoleReporter("Регресс 1")

results = [result1, result2, result3, result4]

# print(telegram_report.publish(result1))
# print(file_report.publish(result1))

publish_result(telegram_report, result1)
publish_result(file_report, result1)
publish_result(console_report, result1)
