import requests
import json

url = "https://open.er-api.com/v6/latest/USD"

respons = requests.get(url)
data = respons.json()
print(json.dumps(data,ensure_ascii=False,indent=4))

#Команды
_exit = "Выход"
lst = "Список"
convert = "Конвертировать"

while True:
    n = input("Команда: ")
    if n == _exit:
        break
        # exit()
    elif n == lst:
        for ls in data['rates']:
            print(ls)
    elif n == convert:
        ishod = input("Исходная валюта: ")
        su = int(input("Сумма: "))
        cel = input("Целевая валюта: ")
        val_ishod = data['rates'][ishod]
        val_cel = data['rates'][cel]
        in_usd = su / val_ishod
        res = in_usd * val_cel
        print(f"{su} {ishod} = {res} {cel}")