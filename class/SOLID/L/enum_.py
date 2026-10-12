from dataclasses import dataclass, field
from enum import Enum


class TestStatus(Enum):
    PENDING = "Pending"
    PASSED = "Passed"
    SKIPPED = "Skipped"
    FAILED = "Failed"


@dataclass
class TestResult:
    name: str
    status: str = TestStatus.PENDING
    duration: float = field(default=0.0, repr=False, compare=False)  # По умолчанию 0.0, но не отображается в __repr__
    errors: list[str] = field(default_factory=list,
                              repr=False)  # По умолчанию пустой список, но не отображается в __repr__
    retries: int = field(default=0, init=False)  # По умолчанию 0, но не передается в __init__

    def __post_init__(self):
        if not isinstance(self.status, TestStatus):  # Проверка типа status на TestStatus
            raise TypeError(f"Не верный тип статуса: {self.status}")


res1 = TestResult("Login", TestStatus.PASSED)
res2 = TestResult("Login", TestStatus.PASSED)

res1.duration = 1.5
res2.duration = 2.8

res1.errors.append("Timeout")
res1.retries += 1

print(res1)
print(res1 == res2)
print(res1.errors)
