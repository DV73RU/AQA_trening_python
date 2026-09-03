"""
5. Проверка результата API-запроса — средняя

Создай отдельные проверки:

статус-кода;
времени ответа;
наличия обязательного поля в JSON;
значения конкретного заголовка.

Каждая проверка получает объект с данными HTTP-ответа и возвращает результат проверки.

Создай ResponseValidator, который принимает список проверок, выполняет каждую и возвращает список результатов.

Новые проверки должны добавляться без изменения класса ResponseValidator.
"""

import requests
import json
from abc import ABC, abstractmethod


class GetResponse:
    """Класс запроса"""

    def __init__(self, url):
        self.url = url
        self.json_data = None  # JSON ответ
        self.time = None  # Время ответа
        self.status_code = None  # Статус код
        self.headers = None  # Значение заголовка

    def get(self):
        """Метод отправляет запрос, сохраняет в объект ответ"""
        response = requests.get(self.url)  # Ответ переданного запроса от переданного url
        self.json_data = response.json()
        self.time = response.elapsed.total_seconds()
        self.status_code = response.status_code
        self.headers = response.headers
        return self  # Возвращаем объект


class BaseCheck(ABC):
    """АБСТРАКТНЫЙ КЛАСС ДЛЯ ВСЕХ ПРОВЕРОК"""

    @abstractmethod
    def check(self, response_obj: GetResponse):
        """Каждая проверка реализует этот метод"""
        pass


class StatusCodeCheck(BaseCheck):
    """Класс проверка кода ответа"""

    def __init__(self, code: int):
        """"""
        self.code = code  # Экземпляр принимает проверяемое значение статус кода

    def check(self, response_obj: GetResponse) -> bool:
        """Метод чекает код ответа от полученного объекта"""
        return response_obj.status_code == self.code  # Вернёт Тrуе если истина


class TimeCheckValue(BaseCheck):

    def __init__(self, time: float):
        self.time = time

    def check(self, response_obj: GetResponse) -> bool:
        """Метод проберет время запроса (не больше секунды)"""
        if response_obj.time > self.time:  # Если время ответа больше ожидаемого, то False
            return False
        else:
            return True


class KeyCheck(BaseCheck):

    def __init__(self, key: str):
        self.key = key

        """Класс проверки значение поля JSON ответа"""

    def check(self, response_obj: GetResponse):
        """Метод проверки наличия переданного ключа в JSON"""
        if self.key in response_obj.json_data:
            return True
        else:
            return False


class HeaderCheck(BaseCheck):
    """Класс проверки значение определенного "Content-Type" ответа"""

    def __init__(self, header: str):
        # Сохраняем ожидаемое значение заголовка (например, 'application/json')
        self.header = header

    def check(self, response_obj: GetResponse) -> bool:
        content_type = response_obj.headers.get('Content-Type')  # Получим значение заголовка
        if content_type is None:  # Если нет значения такого заголовка
            return False  # Верни False
        return content_type.split(";")[0].strip() == self.header




class ResponseValidator:
    """Класс валидации запроса по списку проверок"""

    def __init__(self, checks: list[BaseCheck]):
        self.checks = checks

    def validate(self, response_pbj: GetResponse) -> list[
        bool]:  # Метод примет объекты (в нём данные с результатами запроса), вернёт булевый список результатов
        result = []  # Создаём пустой список результата
        for check in self.checks:  # Берем каждый экземпляр и выполняем у него метод
            res = check.check(response_pbj)
            result.append(res)  # Добавляем в список результатов

        return result


get_url = GetResponse("https://catfact.ninja/fact")
response_data = get_url.get()
# Формируем список проверок
list_check = [StatusCodeCheck(200), TimeCheckValue(1.0), KeyCheck("fact"),
              HeaderCheck('application/json; charset=utf-8')]

val = ResponseValidator(checks=list_check)  # Принимает список проверок
print(val.validate(response_data))

""""""