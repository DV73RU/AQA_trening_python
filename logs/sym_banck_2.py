import json

def show_menu():
    print("+-------------------------------------+")
    print("!         МЕНЮ ДОСТУПНЫХ ОПЕРАЦИЙ     !")
    print("+-------------------------------------+")
    print("!  [Команда операци] Название опреции !")
    print("!  [Баланс]  Посмотреть баланс        !")
    print("!  [Пополнить]  Пополнение счета      !")
    print("!  [Снять]  Снятие наличных           !")
    print("!  [История]  История операций        !")
    print("!  [Выход]  Выход                     !")
    print("+-------------------------------------+")


#Читаме файд json
with open ("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

#Функция возвращяет баланс
def get_balance():
    balance = data.get("balance") # Забираем значение  из ключа balancei in
    return balance # Возвращяем значение

def get_history():
    pass
    with open("data.json", "r", encoding="utf-8") as file:
        hys = json.load(file)
        lst = []
        for i in hys['history']['type']:
            print(i)

    return i



show_menu()
#Функция пишет баланс
def set_balance(new_balance,operation_type,amount): #Пишет баланс в файл
    data['balance'] = new_balance #Читаем баланс
    data['history'].append({"type":operation_type,"amount":amount})
    with open("data.json","w",encoding="utf-8") as f: # Открываем файл для записи
        json.dump(data,f,ensure_ascii=False) #Пишем в файл

# data['balance'] = get_balance()

get_user_balance = "Баланс"
pop_user_balance = "Пополнить"
get_cash = "Снять"
exits = "Выход"
_history = "История"






while True:
    n = input("Введите Команду: ")
    if n == get_user_balance:
        print(f"Введ ина команда: {get_user_balance}")
        print(f"Ваш баланс: {get_balance()}") # Вставляем значение котророе вернула функция

    elif n == pop_user_balance:
        print(f"Вы ввели Команду: {pop_user_balance}")
        pop_ = int(input("Введите сумму: "))
        set_balance(get_balance() + pop_,"пополнение",pop_)
        print(f"Ваш баланс: {get_balance()}") # Выводим баланс


    elif n == get_cash:
        print(f"Вы ввели команду: {get_cash}")
        in_cash = int(input("Введите сумму: "))
        if in_cash > get_balance(): #Усли симаемая сумма больше баланса
            print("Не достаточно средств на балансе!")
            print(f"Ваш баланс: {get_balance()}")
        else:
            # new_balance = get_balance() - in_cash # Вычистаем из существуещего файла введенню число
            set_balance(get_balance() - in_cash,"снятие",in_cash)
            print(f"Ваш баланс: {get_balance()}")


    elif n == _history:
        print(f"Введина команда: {_history}")

        if not data['history']:
            print(f"История опреций отсутвует")

        else:
            for i in data['history']:
                print(f"{i['type']}: {i['amount']}")



    elif n == exits:
        print(f"Введенина команда: {exits}","До свидания!", sep="\n")
        break

    else:
        print("Коменла не найдена")


