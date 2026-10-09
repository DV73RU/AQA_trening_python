from dataclasses import dataclass
from enum import Enum


class TestStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    PENDING = "Pending"


@dataclass
class TestResult:
    name: str
    status: TestStatus = TestStatus.PENDING  # Статус по умолчанию

    def __post_init__(self):
        if not isinstance(self.status, TestStatus):  # Если статус не является объектом TestStatus
            raise ValueError(f"Не допустимое значение статуса: {self.status} ")  # Выбрасываем ошибку


res = TestResult("Login", TestStatus.PENDING)
print(res.__dict__)
print(res)
