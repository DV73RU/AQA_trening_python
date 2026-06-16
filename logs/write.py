import json

def set_balance():
    with open("data.json","r",encoding="utf-8") as f:
        data = json.load(f)
        val = int(input("Введите баланс: "))
        data['balance'] = val
    with open("data.json", "w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False)


set_balance()