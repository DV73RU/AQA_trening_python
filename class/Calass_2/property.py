import requests
from requests.exceptions import HTTPError, Timeout, ConnectionError, RequestException

url = "https://catfact.ninja/fact"

try:
    # Всегда указывайте timeout, чтобы запрос не завис навсегда!
    response = requests.get(url, timeout=5)

    # ВАЖНО: При статус-кодах 404, 500 и т.д. requests НЕ вызывает исключение автоматически.
    # Этот метод принудительно вызовет HTTPError, если статус ответа >= 400.
    response.raise_for_status()

    # Если всё прошло успешно, работаем с данными
    data = response.json()
    print("Данные успешно получены:", data)

except Timeout:
    print("Ошибка: Время ожидания запроса истекло (сервер слишком долго не отвечал).")

except ConnectionError:
    print("Ошибка: Не удалось подключиться к серверу. Проверьте интернет или DNS.")

except HTTPError as http_err:
    print(f"Ошибка HTTP: {http_err} (Статус-код: {response.status_code})")

except RequestException as req_err:
    print(f"Общая ошибка requests: {req_err}")

except Exception as e:
    print(f"Непредвиденная системная ошибка: {e}")
