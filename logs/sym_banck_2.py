import json

# data = {"balance": 1000}
# with open("data.json", "w") as f:
#     json.dump(data, f)


with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# print(json.dumps(data, indent=4,ensure_ascii=False))

balance = data.get("balance")

# print(balans)


get_balance = "Баланс"
pop_balans = "Пополнить"
cach = "Снять"
new_balance = balance
while True:
    n = input("Введите Команду: ")
    if n == get_balance:
        print(f"Введ ина команда: {get_balance}")
        print(f"Ваш баланс: {balance}")

    if n == pop_balans:
        print(f"Вы ввели команду {pop_balans}")
        pop_ = int(input("Введите сумму: "))
        new_balance = new_balance + pop_
        print(f"Баланс: {new_balance}")
        data["balance"] = new_balance # Обновляем словарь новым значением баланса
        with open("data.json", "w") as f: # Пишем новое значение баланса в json
            json.dump(data,f,ensure_ascii=False)


    # else:
    #     print("Коменла не найдена")


