from dataclasses import dataclass, field


@dataclass
class ApiResponse:
    url: str
    status_code: int = 200
    response_time: float = 0.0

    def __post_init__(self):  # Дандер метод после инициализации


        if not isinstance(self.url, str):
            raise TypeError(f"Не верный тип {self.url}")

        if len(self.url) <= 0:
            raise ValueError(f"{self.url} - передали пустым")



        if type(self.response_time) not in (int,float):# Если не дробной
            raise TypeError(f" {self.response_time} - не соответствует типу ")
        if self.response_time < 0:
            raise ValueError(f"{self.response_time} Не должно быть отрицательным ")

        if not isinstance(self.status_code, int):
            raise TypeError(f"{self.status_code} - не соответствует типу int")

        if isinstance(self.status_code, bool):
            raise TypeError(f"Не верный тип {self.status_code}")

        if 599 < self.status_code or self.status_code < 100:
            raise ValueError(f" {self.status_code} в не диапазона 100 - 599 ")




        # self.__dict__["response_time"] = self.response_time


response2 = ApiResponse("dsds", True, 2.0)
print(response2)
