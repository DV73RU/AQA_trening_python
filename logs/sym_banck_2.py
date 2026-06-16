import json

#Читаме файд json
with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Функция возвращяет баланс
def get_balance():
    balance = data.get("balance") # Забираем значение  из ключа balance
    return balance # Возвращяем значение

#Функция пишет баланс
def set_balance(new_balance): #Пишет баланс в файл
    data['balance'] = new_balance #Читаем баланс
    with open("data.json","w",encoding="utf-8") as f: # Открываем файл для записи
        json.dump(data,f,ensure_ascii=False) #Пишем в файл

# data['balance'] = get_balance()

get_user_balance = "Баланс"
pop_user_balance = "Пополнить"
get_cash = "Снять"
exits = "Выход"




while True:
    n = input("Введите Команду: ")
    if n == get_user_balance:
        print(f"Введ ина команда: {get_user_balance}")
        print(f"Ваш баланс: {get_balance()}") # Вставляем значение котророе вернула функция

    elif n == pop_user_balance:
        print(f"Вы ввели Команду: {pop_user_balance}")
        pop_ = int(input("Введите сумму: "))
        set_balance(get_balance() + pop_)
        print(f"Ваш баланс: {get_balance()}") # Выводим баланс


    elif n == get_cash:
        print(f"Вы ввели команду: {get_cash}")
        in_cash = int(input("Введите сумму: "))
        if in_cash > get_balance(): #Усли симаемая сумма больше баланса
            print("Не достаточно средств на балансе!")
            print(f"Ваш баланс: {get_balance()}")
        else:
            # new_balance = get_balance() - in_cash # Вычистаем из существуещего файла введенню число
            set_balance(get_balance() - in_cash)
            print(f"Ваш баланс: {get_balance()}")
    elif n == exits:
        print(f"Введенина команда: {exits}","До свидания!", sep="\n")
        break

    else:
        print("Коменла не найдена")


