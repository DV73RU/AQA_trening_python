class TestCase:
    framework = "pytest"

    def __init__(self, name, status):
        self.name = name
        self.status = status

    def get_info(self):
        return f"{self.name} - {self.status}"

    @classmethod
    def set_framework(cls, framework):
        if not cls.is_valid_framework(framework):
            raise ValueError(f"Не допустимое значение {framework}")
        cls.framework = framework

    @staticmethod
    def is_valid_framework(framework):
        return framework in ("pytest","unittest")


    @staticmethod
    def is_valid_status(status):
        return status in ("PASSED","FAILED","SKIPPED")


test = TestCase("test_login", "PASSED")


TestCase.set_framework("unittest")

print(TestCase.framework)  # ?
print(test.framework)      # ?

test.framework = "playwright"

print(TestCase.framework)  # ?
print(test.framework)      # ?

print(test.__dict__)