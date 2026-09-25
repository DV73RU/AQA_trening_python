import requests


URL = "https://gdebenz.ru/api/comments/usr_XC1Dkb28FaQ/recent"

headers = {
    "Accept": "*/*",
    "Referer": "https://gdebenz.ru/",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/153.0.0.0 Safari/537.36"
    )
}

response = requests.get(
    URL,
    params={"limit": 12},
    headers=headers,
    timeout=10
)

print("HTTP:", response.status_code)

response.raise_for_status()

reports = response.json()

if reports:
    latest = reports[0]

    print("Статус:", latest.get("status"))
    print("Информация:", latest.get("detail"))
    print("Дата:", latest.get("created_at"))
else:
    print("Нет данных")