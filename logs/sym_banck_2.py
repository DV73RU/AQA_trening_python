import json

# data = {"balance": 1000}
# with open("data.json", "w") as f:
#     json.dump(data, f)

#Читаме файд json
with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Функция возвращяет баланс
def get_balance():
    balance = data.get("balance") # Забираем значение  из ключа balance
    return balance # Возвращяем значение

def set_balans(val): #Функция принимает значение баланса
    with open ("data.json", "w", encoding=False) as f: #Открывем файл
        json.dump(data,f,ensure_ascii=False)

# print(json.dumps(data, indent=4,ensure_ascii=False))

# balance = data.get("balance")

# print(balans)


get_user_balance = "Баланс"
pop_user_balance = "Пополнить"
cach = "Снять"
new_balans = get_balance()
# balance = get_balans() #Присваиваем переменной значение полученное функцикй
while True:
    n = input("Введите Команду: ")
    if n == get_user_balance:
        print(f"Введ ина команда: {get_user_balance}")
        print(f"Ваш баланс: {get_balance()}") # Вставляем значение котророе вернула функция

    if n == pop_user_balance:
        print(f"Вы ввели команду {pop_user_balance}")
        pop_ = int(input("Введите сумму: "))
        new_balance = new_balance + pop_
        # print(f"Баланс: {new_balance}")
        set_balans(new_balance) # Вызывем функцию и передаём ей новое значение
        # print(f"Ваш баланс: {get_balans()}")

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


