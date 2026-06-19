import requests
import json
#Ответ
url = "https://catfact.ninja/fact"
response = requests.get(url)

data = response.json()
#Отыкет в види JSON
#Первый вариант
print(json.dumps(data,indent=4))
for key,val in data.items():
    if key == "fact":
        print(f"Факт: {val}")

#Втрой вариант
text = data['fact']
print(f"Факт: {text}")

#Третий вариант
print(f"Факт: {data['fact']}")