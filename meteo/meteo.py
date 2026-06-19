import json
import requests
import  time
# from API_cat.cat import response
latitude = 55.75204
longitude = 37.61781
url = "https://geocoding-api.open-meteo.com/v1/search?name="
url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
print(url_temp)
response = requests.get(url_temp)
da = response.json()
print(json.dumps(da,ensure_ascii=False,indent=4))
# data = response.json()
# print(json.dumps(data,ensure_ascii=False,indent=4))
# playload = {}
while True:
    in_city = input("Город: ")
    response = requests.get(url+in_city)
    data = response.json()
    # print(json.dumps(data,ensure_ascii=False,indent=4))
    country_list = []
    for geo in data['results']:
            loc = {}
            latitude = geo['latitude']
            longitude = geo['longitude']
            country = geo['country']
            if country == "Russia":
                url_temp = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
                time.sleep(1)
                # response = requests.get(url_temp)
                # print(response.json())
                # data_ = response.json()
                # print(data_)

                print(f'{latitude} - latitude')
                print(f'{longitude} - longitude')
                # print(json.dumps(data_,ensure_ascii=False,indent=4))