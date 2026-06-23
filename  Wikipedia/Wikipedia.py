import requests

in_q = input("Введите слово: ")

url = f"https://ru.wikipedia.org/api/rest_v1/page/summary/{in_q}"

headers = {
    "User-Agent": "MyPythonApp/1.0 (study project)"  # ← только латиница
}

proxies = {
    "http": "http://iXymu9PdPw:Jc6LOE7vTj1@89.127.214.80:10080",
    "https": "http://iXymu9PdPw:Jc6LOE7vTj@89.127.214.80:10080"
}

try:
    response = requests.get(url, headers=headers, proxies=proxies, timeout=10)
    print(f"Статус: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        print(data['extract'])
    else:
        print("Статья не найдена!")

except requests.exceptions.RequestException as e:
    print("Ошибка запроса:", e)
finally:
    print("Скрипт завершён")