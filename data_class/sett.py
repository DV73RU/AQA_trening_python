from enum import Enum
from dataclasses import dataclass


class TestStatus(Enum):
    """Класс хранение значений статус теста"""
    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    PENDING = "Pending"


@dataclass()
class TestConfig:
    """Класс настройки авто теста"""
    name: str
    timeout: int
    status: TestStatus = TestStatus.PENDING  # По умолчанию PENDING

    # __init__ отсутствует он вшит в декораторе dataclass

    def __setattr__(self, key, value):  # Дандер метод изменения атрибутов экземпляра

        if key == "status":  # Если изменяемый атрибут статус
            if not isinstance(value, TestStatus):  # Если значение статуса не из хранителя данный Enum
                raise TypeError(f"Передали не допустимое значение '{value}' для '{key}' ")

        if key == "timeout":  # Если ключ является timeout проверь что переданное value значение является не int
            if type(value) is not int:
                raise TypeError(f"Переданный {value} не int")
            if value <= 0:
                raise ValueError(f"Не допустимое значение {value}")

        super().__setattr__(key, value) # - > Запись в значения атрибутов


config = TestConfig("Login", 5)

print(config)

config.timeout = 15
config.status = TestStatus.PASSED

print(config)

config.timeout = -2  # ValueError
