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


class GetResponse:  # Может назвать GetHeader?
    """Класс запроса"""

    def __init__(self, url):  # Принимает url
        self.url = url
        # Храним ответы
        self.headers = None

    def get(self):  # Метод отправки запроса

        response = requests.get(self.url)
        self.headers = response.headers

        return self


class BaseTest(ABC):
    """Класс тест абстрактный"""

    def __init__(self, response_obj: GetResponse):
        self.response_obj = response_obj

    @abstractmethod
    def check(self):
        pass


class HeaderTest(BaseTest):

    def check(self, response_obj: GetResponse) -> bool:
        content_type = response_obj.headers.get('Content-Type')  # Получим значение заголовка
        if content_type is None:  # Если нет значения такого заголовка
            return False  # Верни False
        return content_type.split(";")[0].strip() == self.header


response_ = GetResponse("https://catfact.ninja/fact")

try:
    print(response_.get())
except Exception as err:
    print(f"Ошибка {err}")

header_test = HeaderTest(response_)
print(header_test)
