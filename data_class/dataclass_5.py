from dataclasses import dataclass, field


@dataclass
class TestResult:
    name: str
    status: str = field(default="PENDING")
    retries: int = field(default=0, init=False)



    def add_retry(self) -> None:
        self.retries = self.retries + 1


test_res = TestResult("Login")
test_res.add_retry()
test_res.add_retry()


print(test_res)