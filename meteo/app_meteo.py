import requests
import json

# Получение координат города
input_city = input("Введите город: ")
loc_url = f"https://geocoding-api.open-meteo.com/v1/search?name={input_city}"

respons = requests.get(loc_url)
data = respons.json()
# print(data)

def temp_for_geo(latitude,longitude):

    # url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min&timezone=auto"
    # Подключение через vpn
    proxies = {
        "http": "http://iXymu9PdPw:Jc6LOE7vTj1@89.127.214.80:10080",
        "https": "http://iXymu9PdPw:Jc6LOE7vTj@89.127.214.80:10080"
    }

    try:
        print("Отправка запроса погоды через VPS...")
        print(f"Отправляем  на: {url_temp}")

        response = requests.get(url_temp, proxies=proxies, timeout=10)
        print(f"Статус ответа: {response.status_code}")
        data = response.json()
        # print(json.dumps(data, ensure_ascii=False, indent=4))
        # return data

        ls_date = data["daily"]["time"]
        temp_max = data["daily"]["temperature_2m_max"]
        temp_min = data["daily"]["temperature_2m_min"]
        cim_celci = data['daily_units']['temperature_2m_max']
        # cels = data["current_weather_units"]["temperature"]
        # return ls_date,temp_max,temp_mix
        for date, t_max, t_min in zip(ls_date,temp_max,temp_min):

            print(f"{date} | Макс: {t_max}{cim_celci} | Минимум: {t_min}{cim_celci}")

    except requests.exceptions.RequestException as e:
        print("\n Ошибка запроса:", e)
    except Exception as e:
        print("\n Другая ошибка (например, разбора JSON):", e)


latitude = None
longitude = None

for loc in data['results']:
    if loc['country'] == "Russia":
        latitude = loc['latitude']
        longitude = loc['longitude']
        print(f"\nПрогноз для {input_city} на 7 дней:")
        temp_for_geo(latitude,longitude)

        break


