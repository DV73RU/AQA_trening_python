"""
Сужение допустимых данных. Есть BaseValidator.validate(response) -> bool, который должен работать с любым HTTP-ответом.
Создай StatusCodeValidator. Затем создай JsonValidator, который работает только при status_code == 200, а для остальных статусов выбрасывает ошибку.
 Определи нарушение и исправь поведение так, чтобы любой response был допустимым аргументом.
"""

from abc import ABC, abstractmethod
import requests


class BaseValidator(ABC):
    """Класс валидации"""

    @abstractmethod
    def validate(self, response) -> bool:
        """Метод валидации"""
        pass


class StatusCodeValidator(BaseValidator):
    """Класс валидации кода ответа запроса"""

    def validate(self, response) -> bool:
        code = response.status_code
        if code == 200:
            return True
        else:
            return False


class JsonValidator(BaseValidator):

    def validate(self, response) -> bool:
        try:
            if response.status_code != 200:  # Если статус код не 200, то False
                return False
            data = response.json()  # Если в ответе JSON формат
            return "id" in data

        except requests.exceptions.JSONDecodeError:
            return False
