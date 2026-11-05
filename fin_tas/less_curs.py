# def test_login():
#     """Функция тестирует авторизацию"""
#     print("Проверяем авторизацию")
from functools import wraps


def log_test(func):  # Принимает функцию короную декорируем
    """Функция декорирует тест добавляя логирование тестирования """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[INFO]: Тест запущен")
        result = func(*args, **kwargs)  # Запускаем переданную функцию
        print("[INFO] Тест остановлен")
        return result

    return wrapper # Верни декорирование


@log_test  # Тут мы декорируем логами функцию теста API
def api_test(status_code: int):
    """Тест проверки статуса кода ответа API"""
    print("Проверка ответа от API")
    if status_code == 200:
        return "PASSED"
    return "FAILED"


res = api_test(200)
print(f"Результат: {res}")

print(api_test.__doc__)
print(api_test.__name__)

