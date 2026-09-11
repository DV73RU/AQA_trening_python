import requests
import json

from abc import ABC, abstractmethod

urls = "https://catfact.ninja/fact"


class TestResult:
    """Класс результат теста"""

    # тут только храним данные
    def __init__(self, test_name, test_status, text_error, error=None):
        self.test_name = test_name
        self.test_status = test_status
        self.text_error = text_error
        self.exception = error


class GetResponse:
    """ Класс получения ответа HTTP запроса"""

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")  # Если не достучались по URL
            raise


class BaseTest(ABC):
    """Класс проверки"""

    @abstractmethod
    def check(self):
        """Метод проверки"""
        pass


class HeaderTest(BaseTest):
    """Класс проверки значения заголовка"""

    def __init__(self, url, value_header):
        self.test_name = "Header Test"
        self.get_headers = GetResponse()  # Создай экземпляр
        self.url = url
        self.value_header = value_header

    def check(self):  # Метод проверяет заголовок
        """Метод проверки заголовка"""
        try:
            response = self.get_headers.get(self.url)  # Вызови get у GetResponse
        except requests.exceptions.RequestException as error:
            return TestResult(self.test_name, "Ошибка", str(error), error)

        content_type = response.headers.get("Content-Type", "")  # Забираем значение из "Content-Type"
        if content_type.split(";")[0].strip() == self.value_header:
            return TestResult(self.test_name, "PASSED", None)
        else:
            return TestResult(self.test_name, "FAILED", f"Ожидалось: {self.value_header}, Получено: {content_type}")


class CodeTest(BaseTest):
    """Класс проверки значения статус кода"""

    def __init__(self, url, value_code):
        self.test_name = "Status Code Test"
        self.get_code = GetResponse()
        self.url = url
        self.value_code = value_code

    def check(self):  # Метод проверяет предаваемое значение статус кода
        try:
            response = self.get_code.get(self.url)
        except requests.exceptions.RequestException as error:
            return TestResult(self.test_name, "Ошибка", str(error), error)

        if response.status_code == self.value_code:
            return TestResult(self.test_name, "PASSED", None)
        return TestResult(self.test_name, "FAILED", f"Ожидалось: {self.value_code}, Получено: {response.status_code}")


class BaseStrategy(ABC):
    """Абстрактный класс для всех стратегий"""

    @abstractmethod
    def execute(self, list_test):  # Метод применит список тестов
        """Каждая стратегия как пройтись по списку тестов"""
        pass


# =============================================
# Реализованы стратегии
# =============================================
class RunAllStrategy(BaseStrategy):
    """Стратегия 1: Запустить абсолютно все тесты из списка"""

    def execute(self, list_test: list):  # <- Принимает список тестов
        """Метод запускает тесты по стратегии"""
        list_result = []
        for test in list_test:  # Возьми один тест из преданного списка тестов
            result = test.check()  # У теста выполни метод проверки с преданным ответом запроса
            list_result.append(result)
        return list_result


class SingleRetryStrategy(BaseStrategy):
    """Стратегия 2: Запускать тесты повторно c результатом "FAILED" или "Ошибка" один раз"""

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            print(f"Первая попытка запуска теста: {test.test_name}")
            result = test.check()  # Выполни метод

            if result.test_status == "FAILED" or result.test_status == "Ошибка":  # Если в результате встретили "FAILED", "Ошибка"
                print(f"Повторная попытка запуска теста: {test.test_name}")
                result = test.check()  # Запустить тот же тест ещё раз

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


class ThreeRetryStrategy(BaseStrategy):
    """Стратегия 3: Запустить тесты повторно 3 раза с результатом "FAILED" или "Ошибка" """

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            result = None
            for att in range(1, 5):
                print(f"Попытка [{att}] запуска теста: {test.test_name}")
                result = test.check()
                if result.test_status not in ["FAILED", "Ошибка"]:
                    break

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


class ExceptionTypeRetryStrategy(BaseStrategy):
    """Стратегия 4: до двух повторов только при таймауте"""

    def execute(self, list_test: list):
        list_result = []
        for test in list_test:  # Возьми каждый тест в списке
            result = None
            for att in range(1, 4):
                print(f"Попытка [{att}] запуска теста: {test.test_name}")
                result = test.check()
                if not isinstance(result.exception, requests.exceptions.Timeout):
                    break

            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


# Запускальщик тестов
class TestRunner:
    """Класс запуска тестов. Он абсолютно ЗАКРЫТ для изменений.
    Ему не важно, какие тесты внутри списка
    """

    def __init__(self, strategy: BaseStrategy, list_test: list):  # Принимает стратегию проверок
        self.strategy = strategy
        self.list_test = list_test

    def run(self):
        result = self.strategy.execute(self.list_test)
        return result  # Верни результат выполнения метода у экземпляра


header_test = HeaderTest(urls, 'application/jsons')  # Проверка заголовка
code_test = CodeTest(urls, 100)  # Проверка статус кода

list_tests = [header_test, code_test]  # Список проверок

strategy1 = RunAllStrategy()
strategy2 = SingleRetryStrategy()
strategy3 = ThreeRetryStrategy()

# runner1 = TestRunner(strategy2, list_tests)  # Запускальщик тестов принимает стратегию запуска
runner12 = TestRunner(strategy3, list_tests)
res = runner12.run()
for data in res:
    print(data.__dict__)
