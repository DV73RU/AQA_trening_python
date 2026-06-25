import requests
import json
from proxy import my_proxy
class WeatherService():
    """Класс Погода"""
    def __init__(self,city):
        """Метод инциализации"""
        self.city = city
        self.latitude = None
        self.longitude = None

    def geo_coors(self):
        """Метод получения координат города"""
        url = "https://geocoding-api.open-meteo.com/v1/search?"
        payload = {"name":self.city}

        response = requests.get(url,timeout=10,params=payload)
        data = response.json()
        # print(json.dumps(data,ensure_ascii=False,indent=4))
        for i in data['results']:
            if i['country'] == "Russia":
                self.latitude = i["latitude"]
                self.longitude = i["longitude"]
        # return self.longitude ,self.latitude
        print(f"# Координаты найдены: {self.longitude}, {self.latitude}")

    def current_weather(self):
        """Метод везарвщяет температуру"""

        if self.longitude is None or self.longitude is None:
            print("Сначало вызови geo")
            return
        url = f"https://api.open-meteo.com/v1/forecast?"

        payload = {"longitude":self.longitude, "latitude":self.latitude,"current":"temperature_2m"}

        response = requests.get(url,timeout=10,proxies=my_proxy(),params=payload)
        data = response.json()
        # print(response.url)
        # print(json.dumps(data,ensure_ascii=False,indent=4))
        temperature = data["current"]["temperature_2m"]
        simvol = data["current_units"]["temperature_2m"]
        print(f"# Сейчас температура в: {self.city} {temperature}{simvol}")

    def forecast(self):
        """Метод вызывает прогноз на 7 дней"""
        url = "https://api.open-meteo.com/v1/forecast?daily=temperature_2m_max,temperature_2m_min&current=temperature_2m&past_days=7"
        payload = {"latitude":self.latitude, "longitude":self.longitude}
        response = requests.get(url,timeout=10,params=payload,proxies=my_proxy())
        data = response.json()
        # print(response.url)
        # print(json.dumps(data,ensure_ascii=False,indent=4))
        simvol = data["current_units"]["temperature_2m"]
        dst_time = data["daily"]["time"]
        temperature_max = data["daily"]["temperature_2m_max"]
        temperature_min = data["daily"]["temperature_2m_min"]

        for date, t_max,t_min in zip(dst_time,temperature_max,temperature_min):
            print(f"# {date} | макс: {t_max}{simvol} | мин: {t_min}{simvol}")



my_meteo = WeatherService("Moscow")
my_meteo.geo_coors()
my_meteo.current_weather()
my_meteo.forecast()