#Симулятор банкомата


# balance = 1000
#
# Команды
# km_pop = "Пополнить"
# km_cash = "Снять"
# km_balance = "Баланс"
# km_exit = "Выход"
#
# Текста
# in_command = "Введите команду: "
# goodbay = "До свидания!"
# summa = "Сумма"
# _command = "Команда:"
# bad_balans = "Недостаточно средств!"
# _balans = "Баланс"
#
# while True:
#     n = input(in_command)
#     if n == km_exit:
#         print(f"{_command}:{km_exit}")
#         print(goodbay)
#         break
#     elif n == km_balance:
#         print(f"{_command}:{km_balance}")
#         print(_balans)

balance = 1000

km_exit = "Выход"
km_pop = "Пополнить"
km_cash = "Снять"
km_balance = "Баланс"

print("Доступые команды:")
print(km_pop,km_balance,km_cash,km_exit, sep= ", ")

while True:
    n = input("Введите команду: ")
    if n == km_exit:
        print(f"Выполнена команада: {km_exit}","До свидания!", sep="\n")

        break
    elif n == km_balance:
        print(f"Выполнена команада: {km_balance}")
        print(f"Баланс: {balance}")
    elif n == km_cash:
        amount = int(input("Введите сумму: "))
        if amount > balance:
            print("Не достаточно средств!")
        else:
            balance = balance - amount
            print(f"Выполнена команада: {km_cash}, на снятие {amount}")
            print(f"Баланс: {balance}")
    elif n == km_pop:
        pop = int(input("Введите сумму: "))
        balance = balance + pop
        print(f"Выполнена команда: {km_pop} на: {pop}")
        print(f"Баланс: {balance}")
    else:
        print("Команда не найдена")