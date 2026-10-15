from dataclasses import dataclass, field



@dataclass(order=True)
class TestResult:
    duration :float
    name: str = field(compare=False)
    status: str = field(default="PENDING", compare=False)

results = [
    TestResult(2.5, "Login", "PASSED"),
    TestResult(0.8, "Logout", "PASSED"),
    TestResult(1.3, "Payment", "FAILED"),
]
# Сортировка по возрастанию поля duration
sorted_results = sorted(results, key=lambda test: test.duration)

# Проверяем результат
for test in sorted_results:
    print(f"{test.duration} - {test.name}")
