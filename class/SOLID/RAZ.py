import requests
import json

from abc import ABC, abstractmethod

urls = "https://catfact.ninja/fact"


# response = requests.get(url)
# # data = response.json()
# # json = json.dumps(data,ensure_ascii=False,indent=4)
# # # print(json)
# #
# # print(response.headers)
# # print(response.json())
#
# content_tupe = response.headers.get('Content-Type')
# status_code = response.status_code
#
# print(content_tupe)
# print(status_code)


# Функция возврата определенного заголовка ответа
def get_value_header(url: str, header: str):  # Принимает url и значение заголовка
    response = requests.get(url)
    value_header = response.headers.get(header)
    return value_header


# Функция возврата статус кода запроса
def get_value_status_code(url: str):
    response = requests.get(url)
    value_code = response.status_code
    return value_code


# Функция возврата всего

def get_response(url: str):
    response = requests.get(url)
    status_code = response.status_code
    headers = response.headers
    date = response.json()
    d_json = json.dumps(date, ensure_ascii=False, indent=4)
    return d_json


# header = get_value_header(urls, 'Content-Type')
# print(header)
# code = get_value_status_code(urls)
# print(code)

# otv = get_response(urls)
# print(otv)


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
        self.get_headers = GetResponse()  # Создай экземпляр
        self.url = url
        self.value_header = value_header

    def check(self):  # Метод принимает проверяемое значение заголовка
        """Метод проверки заголовка"""
        response = self.get_headers.get(self.url)  # Вызови get у GetResponse
        if response is None:  # Если нам вернули None
            return "FAILED - Запрос не удался (сетевая ошибка)"
        content_type = response.headers.get("Content-Type", "")  # Забираем значение из "Content-Type"
        if content_type.split(";")[0].strip() == self.value_header:
            return f"{content_type} - PASSED"
        else:
            return f"{content_type} - FAILED (Ожидалось: {self.value_header})"


class CodeTest(BaseTest):

    def __init__(self, url, value_code):
        self.get_code = GetResponse()
        self.url = url
        self.value_code = value_code

    def check(self):  # Метод проверяет предаваемое значение статус кода
        response = self.get_code.get(self.url)
        if response is None:
            return "FAILED - Запрос не удался (сетевая ошибка)"
        if response.status_code == self.value_code:
            return f"{response.status_code} - PASSED"
        return f"{response.status_code} - FAILED (Ожидалось: {self.value_code})"





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
        result_list = []  # Список результатов прохождения тестов
        for test in list_test:  # Возьми один тест из преданного списка тестов
            result = test.check()  # У теста выполни метод проверки с преданным ответом запроса
            result_list.append(result)  # Запиши результат тесто в список результатов
        return result_list  # Верни список с результатам



# Запускальщик тестов
class TestRunner:
    """Класс запуска тестов. Он абсолютно ЗАКРЫТ для изменений.
    Ему не важно, какие тесты внутри списка, главное — у них есть метод check()
    """

    def __init__(self, strategy: object):
        self.strategy = strategy

    def run(self):
        return self.strategy.execute # Верни результат выполнения метода у экземпляра

list_tests = [HeaderTest(urls, 'application/json'), CodeTest(urls, 200)]

runner1 = TestRunner(list_tests)
print(runner1.run())
