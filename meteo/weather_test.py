import json

import requests



# Получение координат города
input_city = input("Введите город: ")
loc_url = f"https://geocoding-api.open-meteo.com/v1/search?name={input_city}"

def temp_for_geo(latitude,longitude):

    url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
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
        temp = data["current_weather"]["temperature"]
        cels = data["current_weather_units"]["temperature"]
        return f"Температура в {input_city}: {temp}{cels}"



    except requests.exceptions.RequestException as e:
        print("\n Ошибка запроса:", e)
    except Exception as e:
        print("\n Другая ошибка (например, разбора JSON):", e)



response = requests.get(loc_url)
data = response.json()
# print(json.dumps(data,ensure_ascii=False,indent=4))

if 'results' in data:
    for loc in data['results']:
            names_city = loc["name"]
            if loc.get('country') == "Russia": # Так как городов Москва много в разных странах по умолчанию берем из России
                latitude = loc["latitude"]
                longitude = loc['longitude']
                name = loc['name']
                print(f"Координаты города: {name}: {latitude}, {longitude}")
                print(temp_for_geo(latitude, longitude))

else:
    print(f"Нет такого города: {input_city}")

