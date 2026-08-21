"""
5. Публикация результатов тестов

Создай класс TestResult, хранящий:

название теста;
статус;
текст ошибки.

Создай абстрактный класс BaseReporter:

с обычным методом create_header(), формирующим общий заголовок отчёта;
с абстрактным методом publish(test_result).

Создай репортёры:

ConsoleReporter;
TelegramReporter;
JiraReporter.

Каждый репортёр должен использовать общий заголовок родителя, но по-своему формировать основную часть сообщения.
"""

from abc import ABC, abstractmethod


class TestResult:

    def __init__(self, name_test, status, text_error):
        """Храним данные"""
        self.name_test = name_test
        self.status = status
        self.text_error = text_error


class BaseReporter(ABC):

    def create_header(self, test_result):  # Метод принимает результат теста как объект
        """Метод формирует заголовок ответа"""
        if test_result.status == "FAILED":
            return f"Имя теста: {test_result.name_test}, | Статус:{test_result.status}, Текст ошибки: {test_result.text_error}"  # Сформирует и вернёт заголовки результата теста, если есть status FAILED сформируем с текстом ошибки
        else:
            return f"Имя теста: {test_result.name_test}, | Статус:{test_result.status}"  # Сформирует и вернёт заголовки результата теста, иначе сформируем без текста ошибки

    @abstractmethod
    def publish(self, test_result):
        return


class ConsoleReporter(BaseReporter):
    """Класс отправки отчёта в консоль"""

    def __init__(self, run_name):
        """Инициализируем экземпляр"""
        self.run_name = run_name  # Имя запуска

    def publish(self, test_result):
        """Метод принимает объект"""

        return f"Отправка отчёта результата теста в консоль: {self.run_name}: {self.create_header(test_result)}"  # Вернём имя принятое название запуска, вернём выполнение метода родителя с переданным объектом, результата теста)


class TelegramReporter(BaseReporter):
    """Класс отправки отчёта в телеграм"""

    def __init__(self, id_chat):
        self.id_chat = id_chat  # Экземпляр принимает id чата

    def publish(self, test_result):  # Принимает объект результат теста

        return f"Отправка отчёта результата теста в Телеграм:{self.id_chat}: {self.create_header(test_result)}"  # Вернём имя принятое id чата, вернём выполнение метода родителя с переданным объектом, результата теста)


class JiraReporter(BaseReporter):
    """Класс отправки отчёта в телеграм"""

    def __init__(self, project_name):
        self.project_name = project_name  # Экземпляр принимает имя проекта

    def publish(self, test_result):  # Принимает объект результат теста

        return f"Отправка отчёта результата теста в Jira: {self.project_name}: {self.create_header(test_result)}"  # Вернём имя принятое id чата, вернём выполнение метода родителя с переданным объектом, результата теста)


# Создаём 3 объекта - результат теста
test1 = TestResult("Логин", "PASSED", "GET 200")
test2 = TestResult("Подписка", "FAILED", "POST 404")
test3 = TestResult("Логаут", "PASSED", "POST 200")

# Создаём 3 объекта куда репортим результат
report_to_telegram = TelegramReporter("123_OZON_chat")  # Создаем
report_to_consol = ConsoleReporter("Название запуска")
report_to_jira = JiraReporter("Личный кабинет селлера")

list_tests = [test1, test2, test3]  # Собираем и все тесты в список
list_reports = [report_to_consol, report_to_telegram, report_to_jira]  # Сформировали список обектов репорта

for test in list_tests:  # Циклом перебери список результатов по списку тестов
    for report in list_reports:
        message = report.publish(test)
        print(message)
    print("----")

# Вариант
for report in list_reports:
    for test in list_tests:
        message = report.publish(test)
        print(message)
    print("----------------------------------------------------------------")

print(report_to_jira.publish(test2))
