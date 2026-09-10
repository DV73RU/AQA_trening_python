import requests
import json

from abc import ABC, abstractmethod

urls = "https://catfact.ninja/fact"


class TestResult:
    """Класс результат теста"""

    # тут только храним данные
    def __init__(self, test_name, test_status, text_error):
        self.test_name = test_name
        self.test_status = test_status
        self.text_error = text_error


class GetResponse:
    """ Класс получения ответа HTTP запроса"""

    @staticmethod
    def get(url):
        try:
            response = requests.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при запросе: {e}")  # Если не достучались по URL
            return None


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
        response = self.get_headers.get(self.url)  # Вызови get у GetResponse
        if response is None:  # Если нам вернули None
            return TestResult(self.test_name,"Ошибка","Запрос не удался")
        content_type = response.headers.get("Content-Type", "")  # Забираем значение из "Content-Type"
        if content_type.split(";")[0].strip() == self.value_header:
            return TestResult(self.test_name,"PASSED",None)
        else:
            return TestResult(self.test_name,"FAILED", f"Ожидалось: {self.value_header}, Получено: {content_type}")


class CodeTest(BaseTest):
    """Класс проверки значения статус кода"""
    def __init__(self, url, value_code):
        self.test_name = "Satus Code Test"
        self.get_code = GetResponse()
        self.url = url
        self.value_code = value_code

    def check(self):  # Метод проверяет предаваемое значение статус кода
        response = self.get_code.get(self.url)
        if response is None:
            return TestResult(self.test_name, "Ошибка", "Запрос не удался")  # Cосдай объект
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
            result = test.check()  # Выполни метод
            if result.test_status == "FAILED" or result.test_status == "Ошибка":  # Если в результате встретили "FAILED", "Ошибка"
                result = test.check()  # Запустить тот же тест ещё раз
            list_result.append(result)  # Добавь результат в список результатов
        return list_result  # Верни список результатов


# Запускальщик тестов
class TestRunner:
    """Класс запуска тестов. Он абсолютно ЗАКРЫТ для изменений.
    Ему не важно, какие тесты внутри списка
    """

    def __init__(self, strategy: BaseStrategy):  # Принимает стратегию проверок
        self.strategy = strategy
        self.list_tests = list_tests

    def run(self):
        result = self.strategy.execute(self.list_tests)
        return result  # Верни результат выполнения метода у экземпляра


header_test = HeaderTest(urls, 'application/jsons') # Проверка заголовка
code_test = CodeTest(urls,100) # Проверка статус кода

list_tests = [header_test,code_test]  # Список проверок

strategy1 = RunAllStrategy()
strategy2 = SingleRetryStrategy()

runner1 = TestRunner(strategy2)  # Запускальщик тестов принимает стратегию запуска
runner12 = TestRunner(strategy1)
print(runner1.run())
print(runner12.run())
