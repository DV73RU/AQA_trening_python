from dataclasses import dataclass, field
from enum import Enum


# class StatusCode(Enum):
#     200 = "200"


@dataclass
class ApiTestResult:
    """Класс результат API теста"""
    name: str
    status_code: int = field(default=200)
    response_time: float = field(default=0.0)

    def __setattr__(self, key, value):  # -> Установка значений атрибутов экземпляра
        if key == "status_code":  # Если приходит статус код
            if type(value) is not int:  # Если значение преданного статуса не целое число
                raise TypeError(f"Передано '{type(value)}' не допустимый тип значения '{value}' для '{key}'")
            if value < 100 or value > 599:  # Если значение value в этом диапазоне
                raise ValueError(f"Переданное значение '{value}' в не диапазона 100 - 599")

        if key == "response_time":  # Если приходит время ответа
            if type(value) not in (float, int):  # Если время ответа не целое и не дробное
                raise TypeError(
                    f"Передано не допустимый тип {type(value)} значения '{value}' для '{key}'")  # Выброси ошибку
            if value < 0:
                raise ValueError(f"Переданное значение '{value}' для '{key}' не может быть отрицательным ")

        super().__setattr__(key, value)  # > Устанавливаем переданные значение

    @property
    def is_success(self) -> bool:
        # Читаем свойство
        return 200 <= self.status_code <= 299


api_res = ApiTestResult("Login", 200, 2.3)
api_res2 = ApiTestResult("Logout", 300, 2)
print(api_res)
print(api_res2)

# api_res.is_success = True


# api_res.is_success = True  # не понял как сделать что бы Нельзя установить из вне, оно вычисляемое
print(api_res.is_success)
print(api_res2.is_success)
print(api_res.__dict__)
# api_res.is_success = True
api_res.status_code = 401
print(api_res.is_success)
