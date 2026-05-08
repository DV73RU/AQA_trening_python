# #1
# name = input("Как тебя зовут? ")
# print(f'Привет, {name}!')
# #2
# city = input("В каком городе ты живёшь? ")
# print(f'Ты живёшь в городе, {city}!')
# #3
# ya = input("Любимый язык программирования? ")
# print(f'{ya} - Отличный выбор!')
#4
# name = input('Твое имя ')
# last_name = input('Твоя фамилия ')
# print(f'Полное имя: {name} {last_name}')
#5
# country = input("В какой стране живёшь? ")
# city = input("В каком городе живёшь? ")
# print(f'Ты живёшь в {country}, город {city}')
#6
# age = int(input("Сколько тебе лет? "))
# print(f"Чрез год тебе будут {age+1}")
# #7
# n = int(input("Введите сило "))
# print(f"Сумма: {n+n}")
#8
# n = int(input("Первое число "))
# i = int(input("Второе число "))
# print(f'Разность: {n-i}', f'Произвeдение: {n*i}',f'Сумма: {n+i}', sep="\n")

#9
# ch = int(input("Количество рабочих часов: "))
# st = int(input("Ставка в час: "))
# print(f'Зарплата: {ch * st} евро')
#10

# prise = int(input("Цена товара: "))
# coun = int(input("Количество товара: "))
# print(f"Итог: {prise * coun} евро")
#11
# prise = float(input("Цена товара с копейками: "))
# print(f"Новая цена: {prise * 2}")
#12
# h = float(input("Ширина комнаты: "))
# l = float(input("Длинна комнаты: "))
# print(f"Площадь комнаты: {h * l}")

#13
# h = float(input("Расстояние в километрах: "))
# d = float(input("Время в часах: "))
# print(f"Скорость: {h * d} км/ч")
#14
# prise = float(input("Цена в евро: "))
# cur = float(input("Курс евро к доллару: "))
# print(f"Цена в долларах: {prise * cur}")
#15
# ves = float(input("Вес: "))
# rost = float(input("Рост в метрах: "))
# print(f"BMI: {(ves / rost) ** 2 }")
#16
# name = str(input("Введите имя: "))
# age = int(input("Введите возраст: "))
# city = str(input("Введите город: "))
# print(f"Меня зовут {name}, мне {age}, я живу в {city}.")
#17
# name = str(input("Название товара: "))
# prise = float(input("Цена товара: "))
# n = int(input("Количество товара: "))
# print(f"Товар: {name}",f'Цена: {prise} евро', f'Количество: {n}', f'Итого: {prise * n} евро', sep="\n")
# #18
# car = str(input("Марка машины: "))
# ear = int(input("Год выпуска: "))
# print(f"Машина: {car}, год выпуска: {ear}")
#19
# name_curs = str(input("Название курса: "))
# n = int(input("Количество уроков: "))
# print(f"Курс {name_curs} содержит {n} уроков")
#20
# name_user = str(input("Введите имя: "))
# roles = str(input("Введите роль: "))
# print("=== USER CARD ===")
# print(f"Name: {name_user}", f"Role: {roles}", sep="\n")
# print("=================")
#21
# n = str(input("Сколько часов ты работал?: "))
# ch = int(input("Какая ставка в час?: "))
# res = n * ch
# print(f"Ты заработал {res} евро")
#22 Пропущено, было такое
#23
# name = str(input("Ваше имя: "))
# age = int(input("Возраст: "))
# city = input("Город: ")
# proff = input("Профессия: ")
# print("Анкета", f"Имя: {name}", f"Возраст {age}", f"Город: {city}", f"Профессия: {proff}", sep="\n")
#24
# minuts = float(input("Введите минуты: "))
# print(f"Это {minuts / 60 } часов")
#25
# n = int(input("Введите первое число: "))
# i = int(input("Введите второе число: "))
# print(f"{n} + {i} = {n+i}")
# print(f"{n} - {i} = {n-i}")
# print(f"{n} * {i} = {n * i}")
# print(f"{n} / {i} = {n / i}")
#26
# name = input("Введите имя: ")
# age = int(input("Введите возраст: "))
# print(f"{name}, через 10 лет тебе будет {age + 10}")
#27
# c = float(input("Введите температуру в Цельсиях: "))
# print(f"Температура в Фаренгейтах {c * 9 / 5 + 32}")
name1 = input("Введите имя друга 1:")
name2 = input("Введите имя друга 2:")
name3 = input("Введите имя друга 3:")
print(f"Мои друзья: {name1},{name2},{name3}")

