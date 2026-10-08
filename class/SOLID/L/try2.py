from enum import Enum


class TestStatus(Enum):
    PASSED = "Passed"
    FAILED = "Failed"
    SKIPPED = "Skipped"

status = TestStatus

list_test_result = [TestStatus.SKIPPED,TestStatus.PASSED,TestStatus.PASSED,TestStatus.FAILED,TestStatus.PASSED] # Вернулся список результатов прогона

print(list_test_result) # Проверю что в списке члены Enum

for test_res in  list_test_result:
    if test_res == TestStatus.FAILED:
        print("Тест упал")
    elif test_res == TestStatus.PASSED:
        print("Тест пройден")
    elif test_res == TestStatus.SKIPPED:
        print("Тест пропущен")


