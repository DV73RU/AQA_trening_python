from abc import ABC, abstractmethod

"""
Создай абстрактный класс ResponseValidator с абстрактным методом:

validate(response)

Создай валидаторы:

StatusCodeValidator — проверяет код ответа;
BodyValidator — проверяет содержимое тела ответа;
HeadersValidator — проверяет наличие нужного заголовка.

Каждый валидатор должен возвращать True или False.

Передай один тестовый ответ всем валидаторам и выведи результаты.
"""


class ResponseValidator(ABC):
    """Базовый абстрактный класс валидации ответа"""

    @abstractmethod  # Декоратор абстрактного метода
    def validate(self, response):
        """Метод валидации ответа"""
        # Принимает ответ


class StatusCodeValidator(ResponseValidator):
    """Класс валидации статус кода (дочерний от ResponseValidator)"""

    def validate(self, response: dict):
        """
        Метод принимает коды ответов
        наличие ключа
        """
        if "status_code" in response:  # Если есть такой ключ
            return response["status_code"] == 200  # Проверь его статус 200
        else:
            return False


class BodyValidator(ResponseValidator):
    """Класс валидации тело ответа (дочерний от ResponseValidator)"""

    def validate(self, response: dict):
        """
        Метод валидации тело ответа

        """

        if "body" in response:  # Если есть такой ключ
            return response["body"] == {"token": "abc123", "user_id": 42}
        else:
            return False


class HeadersValidator(ResponseValidator):
    """Класс валидации заголовка ответа (дочерний от ResponseValidator)"""

    def validate(self, response: dict):
        """
        Метод валидации заголовка ответа
        несколько необходимых заголовков.
        """
        headers = response.get("headers")  # Забери значение ключа "headers" из ответа
        return isinstance(headers,
                          dict) and "Content-Type" in headers and "Server" in headers  # Проверь словарь ли это, и есть ли там нужные ключи


response = {
    "status_code": 200,
    "body": {
        "token": "abc123",
        "user_id": 42
    },
    "headers": {
        "Content-Type": "application/json",
        "Server": "nginx"
    }
}

valid_status = StatusCodeValidator()
valid_body = BodyValidator()
valid_headers = HeadersValidator()

list_validators = [valid_status, valid_body, valid_headers]  # Список сальдируемых параметров ответа

for object_valids in list_validators:
    message = object_valids.validate(response)
    print(message)
