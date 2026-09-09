"""
6. Повторный запуск упавших тестов — средняя

Создай стратегии запуска:

запуск без повторных попыток;
одна повторная попытка после ошибки;
повторение до трёх раз;
повторение только при определённом типе ошибки.

Создай TestRunner, который получает тест и выбранную стратегию запуска.

TestRunner не должен самостоятельно определять тип стратегии. Добавление новой стратегии не должно требовать изменения TestRunner.
https://catfact.ninja/fact
"""

from abc import ABC, abstractmethod
import requests


# БАЗОВЫЕ КЛАССЫ (ЗАКРЫТЫ ДЛЯ ИЗМЕНЕНИЙ)

class TestResult:
    """Класс результат теста"""

    # тут только храним данные
    def __init__(self, test_name, test_status):
        self.test_name = test_name
        self.test_status = test_status


class GetResponse:
    """Класс для выполнения HTTP-запросов"""
    # @staticmethod
    def get(self, url: str):  # Метод отправки запроса GET
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")
            return None


class BaseTest(ABC):
    """Класс тест абстрактный"""

    @abstractmethod
    def check(self, response):
        pass


class TestRunner:
    """Класс запуска тестов. Он абсолютно ЗАКРЫТ для изменений.
    Ему не важно, какие тесты внутри списка, главное — у них есть метод check()
    """

    def __init__(self, strategy: object):  # Передадим стратегию
        self.list_tests = list_tests  # Список тестов
        self.strategy = strategy

    def run(self, response):
        # отдадим запуск списка тестов стратегии
        return self.strategy.execute(self.list_tests, response)  # Верни выполнение результата метода у strategy


# 2. АБСТРАКЦИЯ СТРАТЕГИЙ (ОТКРЫТА ДЛЯ РАСШИРЕНИЯ)
class BaseStrategy(ABC):
    """Абстрактный класс для всех стратегий"""

    @abstractmethod
    def execute(self, list_test: list):  # Метод применит список тестов
        """Каждая стратегия как пройтись по списку тестов"""
        pass


# =============================================
# Реализованы стратегии
# =============================================
class RunAllStrategy(BaseStrategy):
    """Стратегия 1: Запустить абсолютно все тесты из списка"""

    def execute(self, list_test: list): # <- Принимает список тестов
        """Метод запускает тесты по стратегии"""
        result_list = []  # Список результатов прохождения тестов
        for test in list_test:  # Возьми один тест из преданного списка тестов
            result = test.check(response)  # У теста выполни метод проверки с преданным ответом запроса
            result_list.append(result)  # Запиши результат тесто в список результатов
        return result_list  # Верни список с результатам


class StopOnFailStrategy(BaseStrategy):
    """Стратегия 2: Запускать тесты, пока не встретится 'PASSED' или 'Ошибка'"""

    def execute(self, list_test):
        result_list = []
        for test in list_test:
            result = test.check(response)
            result_list.append(result)
            # Если тест не прошел — прерываем цикл и не гоняем остальные тесты
            if result.test_status in ["PASSED", "Ошибка"]:
                print(f"[!] Логика стратегии: выполнение прервано на тесте {result.test_name}")
                break
        return result_list


# РАСШИРЕНИЕ СИСТЕМЫ (Добавляем тесты, не меняя код выше!)

class HeaderTest(BaseTest):
    """Класс проверки заголовка"""

    def __init__(self, header_content_type):
        self.header_content_type = header_content_type
        self.test_name = "Content type"  # Храним название теста

    def check(self, response):  # Принимает объект ответа при вызове
        if response is None:
            return TestResult(self.test_name, "Ошибка")

        content_type = response.headers.get("Content-Type", "")

        if self.header_content_type in content_type:

            return TestResult(self.test_name, "PASSED")
        else:
            return TestResult(self.test_name, "FAILED")


class StatusCodeTest(BaseTest):
    """Новый класс проверки статус-кода.
    Мы добавили его, вообще не трогая код TestRunner! В этом и есть суть принципа 'O'.
    """

    def __init__(self, expected_code):
        self.expected_code = expected_code
        self.test_name = "Status Code"

    def check(self, response):
        if response is None:
            return TestResult(self.test_name, "Ошибка")

        if response.status_code == self.expected_code:
            return TestResult(self.test_name, "PASSED")
        else:
            return TestResult(self.test_name, "FAILED")


# 1. Сначала отправляем запрос и получаем ответ
url_test = GetResponse()
response = url_test.get("https://catfact.ninja/fact")

# 2. Создаем объекты тестов
count_type_test = HeaderTest("application/json")
status_code_test = StatusCodeTest(200)

# 3. Формируем список тестов
list_tests = [count_type_test, status_code_test]

runner = TestRunner(list_tests, response)  # Принимает список тестов и результат запроса (ответ)

# Прогон по стратегии 1
print("------Прогон по стратегии  RunAllStrategy ---")
strategy_all = RunAllStrategy()  # Создали первую стратегию
runner_all = TestRunner(list_tests, strategy=strategy_all)  # Запускаем тесты по списку тестов и выбранной стратегии
results_all = runner_all.run(response)
for res in results_all:
    print(f"Тест: {res.test_name} | Статус: {res.test_status}")

print("\n--- Прогон по стратегии StopOnFailStrategy ---")
# 4. ЗАПУСК ВАРИАНТА Б: Меняем стратегию, НЕ МЕНЯЯ класс TestRunner!
strategy_stop = StopOnFailStrategy()
runner_stop = TestRunner(list_tests, strategy=strategy_stop)
results_stop = runner_stop.run(response)

for res in results_stop:
    print(f"Тест: {res.test_name} | Статус: {res.test_status}")
