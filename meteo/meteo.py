import json
import requests
import  time



# Точные параметры для запроса
latitude = 55.75204
longitude = 37.61781
url_temp = f"https://open-meteo.com{latitude}&longitude={longitude}&current=temperature_2m"


# Проверьте, чтобы IP-адрес содержал все 4 группы цифр через точку
# Замените dmitriy и my_password на ваши реальные данные из 3x-ui
proxies = {
    "http": "http://iXymu9PdPw:Jc6LOE7vTj1@89.127.214.80:10080",
    "https": "http://iXymu9PdPw:Jc6LOE7vTj@89.127.214.80:10080"
}

try:
    print("Отправка запроса через VPS (3x-ui)...")
    print(f"Целевой URL: {url_temp}")

    response = requests.get(url_temp, proxies=proxies, timeout=10)

    print(f"\nУспех! Статус ответа сервера: {response.status_code}")
    print("Полученные данные о погоде:")
    print(response.json())

except requests.exceptions.ProxyError as e:
    print("\n[Ошибка Прокси]: Сервер 3x-ui отклонил подключение.")
    print("Детали ошибки:", e)
except requests.exceptions.RequestException as e:
    print("\n[Ошибка сети]: Не удалось связаться с сервером.", e)
# print(json.dumps(da,ensure_ascii=False,indent=4))
# data = response.json()
# print(json.dumps(data,ensure_ascii=False,indent=4))
# playload = {}
# while True:
#     in_city = input("Город: ")
#     response = requests.get(url+in_city)
#     data = response.json()
#     # print(json.dumps(data,ensure_ascii=False,indent=4))
#     country_list = []
#     for geo in data['results']:
#             loc = {}
#             latitude = geo['latitude']
#             longitude = geo['longitude']
#             country = geo['country']
#             if country == "Russia":
#                 url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
#                 time.sleep(1)
#                 # response = requests.get(url_temp)
#                 # print(response.json())
#                 # data_ = response.json()
#                 # print(data_)
#
#                 print(f'{latitude} - latitude')
#                 print(f'{longitude} - longitude')
#                 # print(json.dumps(data_,ensure_ascii=False,indent=4))