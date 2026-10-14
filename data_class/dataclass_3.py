from dataclasses import dataclass, field


@dataclass
class TestResult:
    name: str
    status: str = "PENDING"
    errors: list[str] = field(default_factory=list)

    def add_error(self, error: str) -> None:
        self.errors.append(error)


test1 = TestResult("Login")
test2 = TestResult("Logout")

test1.add_error("HTTP 500")

print(test1.errors)
print(test2.errors)
