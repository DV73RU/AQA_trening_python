import requests
import json

url = 'https://open.er-api.com/v6/latest/USD'

respons = requests.get(url)
data = respons.json()
print(json.dumps(data,ensure_ascii=False,indent=4))

in_val = int(input("Сумма USD: "))
valut = input("Валюта: ")
res = 0
for vl, value  in data['rates'].items():
    # print(f"Валюта {vl} - Курс {value}")
    if valut == vl:
        new_value = float(value)
        res = value * in_val
        print(f"{in_val} USD = {res} {valut}")

