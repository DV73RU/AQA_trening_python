"""
7. Система запуска автотестов

Создай абстрактный класс BaseTest с атрибутом названия теста и абстрактным методом:

run()

Создай типы тестов:

ApiTest;
UiTest;
DatabaseTest.

Метод run() каждого теста должен возвращать объект TestResult со статусом PASSED или FAILED.

Создай абстрактный класс BaseReporter с абстрактным методом:

publish(test_result)

Создай репортёры:

ConsoleReporter;
FileReporter

Создай класс TestRunner, который:

принимает список разных тестов;
принимает объект репортёра;
запускает каждый тест через общий метод run();
получает объект TestResult;
передаёт результат репортёру через publish();
сохраняет подготовленные сообщения;
продолжает запуск, даже если один тест завершился с ошибкой;
возвращает список всех сообщений.

Нельзя определять конкретные классы тестов или репортёров через type(), isinstance() либо цепочку if/elif.
"""
from abc import ABC, abstractmethod


class TestResult:
    """Класс результат теста"""

    # тут только храним данные
    def __init__(self, test_name, status, text_error):
        self.test_name = test_name
        self.status = status
        self.text_error = text_error


class BaseTest(ABC):

    def __init__(self, test_name):
        """Метод инициализатор"""
        self.test_name = test_name  # Имя теста
        # self.status = status  # Статус теста

    @abstractmethod
    def run(self):
        """Метод запуска теста"""
        pass


class ApiTest(BaseTest):

    def run(self):
        result = TestResult(self.test_name, "PASSED", "")  # Создание экземпляра класса
        return result  # Вернёт результат теста (объект)


class UiTest(BaseTest):
    def run(self):
        result = TestResult(self.test_name, "PASSED", "")  # Создание экземпляра класса
        return result


class DatabaseTest(BaseTest):
    def run(self):
        result = TestResult(self.test_name, "FAILED", "")  # Создание экземпляра класса
        return result


class BaseReporter(ABC):
    """Абстрактный класс репорт"""

    @abstractmethod
    def publish(self, test_result):  # Принимает результат теста
        """Метод вернёт репорт"""
        pass


class ConsoleReporter(BaseReporter):
    """Класс репорт в консоль"""

    def publish(self, test_result):
        """Метод публикации репорта в консоль"""
        return f"Отправка репорта в консоль.. Имя теста: {test_result.test_name} | Статус теста: {test_result.status} | Текст ошибки: {test_result.text_error}"


class FileReporter(BaseReporter):
    """Класс запись репорта в файл"""

    def publish(self, test_result):
        """Метод публикации репорта в консоль"""

        return f"Отправка репорта в файл.. Имя теста: {test_result.test_name} | Статус теста {test_result.status} | Текст ошибки: {test_result.text_error}"




class TestRunner:
    """
    Класс запуска тестов
    принимает список разных тестов;
    принимает объект репортёра;
    запускает каждый тест через общий метод run();
    получает объект TestResult;
    передаёт результат репортёру через publish();
    сохраняет подготовленные сообщения;
    продолжает запуск, даже если один тест завершился с ошибкой;
    возвращает список всех сообщений.
    """

    def __init__(self, list_tests: list, reporter: object):  # Принимает список тестов, репортёр
        self.list_tests = list_tests  # Список тестов
        self.reporter = reporter  # Объект репортёр

    def run(self):
        messages = [] # создадим список сообщёний

        for test in self.list_tests:  # Возьми по тесту из списка тестов
            try:
                result = test.run()  # Выполни метод у каждого теста
            except Exception as err:
                result = TestResult(test.test_name, "FAILED", str(err))# Создать результат теста
                # Отправь результат в указанный репортёр
            message = self.reporter.publish(result)
            messages.append(message)  # Добавим сообщение в список
        return messages




api_test1 = ApiTest("POST /auth/login")
api_test2 = ApiTest("POST /orders")

ui_test1 = UiTest("Оформление заказа")
ui_test2 = UiTest("Корзина покупок")

database_test1 = DatabaseTest("Таблица users")
database_test2 = DatabaseTest("Значения по умолчанию")

repor_to_consol = ConsoleReporter()
repot_to_file = FileReporter()

list_tests = [api_test1, api_test2, ui_test1, ui_test2, database_test1, database_test2]


test_run = TestRunner(list_tests, repot_to_file)
test_run2 =TestRunner(list_tests,repor_to_consol)
# print(test_run.run())
# print(test_run2.run())
for message in test_run.run():
    print(message)

for message in test_run2.run():
    print(message)
