import json

# data = {"balance": 1000}
# with open("data.json", "w") as f:
#     json.dump(data, f)

#Читаме файд json
with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Функция возвращяет баланс
def get_balans():
    balance = data.get("balance")
    return balance







# print(json.dumps(data, indent=4,ensure_ascii=False))

# balance = data.get("balance")

# print(balans)


get_user_balance = "Баланс"
pop_user_balans = "Пополнить"
cach = "Снять"
balance = get_balans() #Присваиваем переменной значение полученное функцикй
while True:
    n = input("Введите Команду: ")
    if n == get_user_balance:
        print(f"Введ ина команда: {get_user_balance}")
        print(f"Ваш баланс: {balance}")

    # if n == pop_balans:
    #     print(f"Вы ввели команду {pop_balans}")
    #     pop_ = int(input("Введите сумму: "))
    #     new_balance = new_balance + pop_
    #     print(f"Баланс: {new_balance}")
    #     data["balance"] = new_balance # Обновляем словарь новым значением баланса
    #     with open("data.json", "w") as f: # Пишем новое значение баланса в json
    #         json.dump(data,f,ensure_ascii=False)
    #
    # if n == cach:
    #     print(f"Вы ввели команду {cach}")
    #     in_cash = int(input("Введите сумму: "))
    #     new_balance = new_balance - in_cash
    #     data["balance"] = new_balance
    #     print(f"Баланс : {new_balance}")
    #     with open("data.json", "w") as f:
    #         json.dump(data,f,ensure_ascii=False)

        # else:
    #     print("Коменла не найдена")


