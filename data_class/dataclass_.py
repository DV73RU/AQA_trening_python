from dataclasses import dataclass, field


@dataclass
class TestResult:
    name: str  # Обязательное поле
    status: str = "PENDING"
    duration: float = field(default=0.0, compare=False)


test1 = TestResult("Login", "PASSED", 1.5)
test2 = TestResult("Login", "PASSED", 1.5)
test3 = TestResult("Login", "PASSED", 2.0)

print(test1 == test1)
print(test1 == test3)
print(test1 is test2)
test1.status = "FAILED"
print(test1)

