"""
Неожиданное исключение. Есть BaseTest с методом run() -> bool.
По контракту метод должен возвращать True или False и не выбрасывать исключения наружу.
Создай ApiTest, который соблюдает контракт, и DatabaseTest, который при ошибке выбрасывает ConnectionError.
Определи, почему это нарушение LSP, и подумай, как DatabaseTest может обработать ошибку, не ломая контракт.
"""

from abc import ABC, abstractmethod


class BaseTest(ABC):
    """Класс базового теста"""
    @abstractmethod
    def run(self) -> bool:
        pass

class ApiTest(BaseTest):
    """Класс теста API"""

    def run(self) -> bool:
        return True

# class DatabaseTest(BaseTest):
#     """Клас проверки БД"""
#     def run(self) -> bool:
#         raise ConnectionError("Ошибка коннекта к БД") # <- Ошибка контракта, принципов LSP


class DatabaseTest(BaseTest):
    """Класс проверки БД"""

    def run(self) -> bool:
        try:
            # Имитируем логику теста, которая падает
            raise ConnectionError("Ошибка коннекта к БД")
            return True
        except ConnectionError as e:

            return False