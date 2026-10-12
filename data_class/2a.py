from dataclasses import dataclass

@dataclass
class TestResult:
    name: str
    status: str = 'PENDING'

result = TestResult('login')
result1  = TestResult('logaut', 'PASSED')

print(result)
print(result1)