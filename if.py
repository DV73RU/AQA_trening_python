# #1
# age = int(input("Введите возораст: "))
# if age >= 18:
#     print("Доступ разрешён")
# else:
#     print("Доступ запрещён")

# #2
# n = int(input("Введите число: "))
# if n > 0:
#     print("Число положительное")
# else:
#     print("Число отрицательное")

# 3
# n = int(input("Введите число: "))
# if n % 2 == 0:
#     print("Число положительное")
# else:
#     print("Число отрицательное")

#4
# passowd = input("Введите пароль: ")
# if passowd == "zaqwsx123":
#     print("Доступ открыт")
# else:
#     print("Неверный пароль")
#5
# temperature = int(input("Введите температуры на улице: "))
# if temperature >= 25:
#     print("Жарко")
# elif 10 < temperature < 25:
#     print("Нормально")
# else:
#     print("Холодно")
#6
# bulls = int(input("Введите балл: "))
# if 90 <= bulls <= 100:
#     print("Отлично")
# elif 70 <= bulls <= 89:
#     print("Хорошо")
# elif 50 <= bulls <= 69:
#     print("Удовлетворительно")
# else:
#     print("Плохо")
#7
# login = input("Введите логин: ")
# password = input("Введите пароль: ")
# if login == "admin" and password == "1234":
#     print("Вход выполнен")
# else:
#     print("Неверный логин или пароль")

#8
# us = int(input("Введите сумму покупки: "))
# if us >= 100:
#     print(f"Сумма покупки: {us}", f"Итого к оплате: {us-(us/100)*10}", sep="\n")
# else:
#     print(f"Сумма покупки: {us}", f"Итого к оплате: {us}", sep="\n")

#9
# n = int(input("Введите первое число: "))
# i = int(input("Введите второе число: "))
# op = str(input("Выберете операцию: + , - , * , /: "))
# if op == "+":
#     print(n + i)
# elif op == "-":
#     print(n - i)
# elif op == "*":
#     print(n * i)
# elif op == "/":
#     print(n / i)
# else:
#     print("Неизвестная операция")

#10
age = int(input("Введите возраст: "))
tikt = input("Есть билет: ")
vip = input("Есть VIP: ")
if age >= 18 and tikt == "yes" or vip == "yes":
    print("Доступ разрешён")
else:
    print("Доступ запрещён")

