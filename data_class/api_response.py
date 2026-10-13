from dataclasses import dataclass, field


@dataclass
class ApiResponse:
    url: str
    status_code: int = 200
    response_time: float = 0.0
    errors: list[str] = field(default_factory=list)

    def __setattr__(self, key, value):
        if key == "url":  # Если передаём в url значение
            if type(value) is not str:  # Если не строка
                raise TypeError(f"Переданное значение '{value} в '{key}' -  не строка ,а {type(value)}'")
            if len(value) <= 0:  # Если значение пустое
                raise ValueError(f"Длинна переданного  значения '{value}' в {key} - меньше или равна '0'")
        if key == "status_code":
            if type(value) is not int:  # Если переданное значение не целое и не дробное
                raise TypeError(f"Переданное значение '{value} в '{key}' -  не ожидаемого типа ,а {type(value)}'")
            if value > 599 or value < 100:
                raise ValueError(f"Переданное значение {value} для {key} не в ожидаемом диапазоне: 100 - 599 ")

        if key == 'response_time':
            if type(value) not in (float, int):
                raise TypeError(f"Переданное значение '{value} в '{key}' -  не ожидаемого типа ,а {type(value)}'")
            if value < 0:
                raise ValueError(f"Переданное значение {value} меньше '0' ")
        super().__setattr__(key, value)  # Пишем значение в атрибуты

    @property  # Вычисляемое значение  
    def is_server_error(self) -> bool:
        return 500 <= self.status_code <= 599  # Проверит условие


response = ApiResponse("https://example.com/api")
error_raised = False

try:
    response.status_code = 700
except ValueError:
    error_raised = True

assert error_raised
assert response.status_code == 200
print(response)


response = ApiResponse("https://example.com/api")
error_raised = False

try:
    response.url = ""
except ValueError:
    error_raised = True

assert error_raised
assert response.url == "https://example.com/api"

response = ApiResponse("https://example.com/api")
error_raised = False

try:
    response.response_time = -1
except ValueError:
    error_raised = True

assert error_raised
assert response.response_time == 0.0


print(response)