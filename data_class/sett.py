from enum import Enum


class TestStatus(Enum):
    """Класс хранение значений статус теста"""
    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"
    PENDING = "Pending"


class TestConfig:
    """Класс настройки авто теста"""

    def __init__(self, name: str, timeout: int, status: TestStatus):

        self.name = name  # Имя теста
        self.timeout = timeout  # Время выполнения
        self.status: TestStatus = TestStatus.PENDING  # Значение статуса по умолчанию

    def __setattr__(self, key, value):  # Дандер метод изменения атрибутов экземпляра

        if key == "status":  # Если изменяемый атрибут статус
            if not isinstance(value, TestStatus):  # Если значение статуса не из хранителя данный Enum
                raise TypeError(f"Передали не допустимое значение '{value}' для '{key}' ")

        if key == "timeout":  # Если ключ является timeout проверь что переданное value значение является не int
            if type(value) is not int:
                raise TypeError(f"Переданный {value} не int")
            if value <= 0:
                raise ValueError(f"Не допустимое значение {value}")

        self.__dict__[key] = value  # Устанавливаем значение атрибуту


config1 = TestConfig("Login", 23, "PASSED")
print(config1.__dict__)  # Смотрим что в экземпляре

# Меняем значение атрибутов
config1.name = "Logout"
config1.timeout = 2
config1.status = TestStatus.PASSED
config1.status = TestStatus.SKIPPED
print(config1.__dict__)  # Смотрим что в экземпляре
