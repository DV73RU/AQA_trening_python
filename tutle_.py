# names_tuple = ("Anna", "Bob", "Tom")
# names_list = ["Симён","Фёдор","Ирина"]
#
# for i, x in enumerate(names_tuple):
#     print(i, x)
#
# print(names_tuple.count('Anna'))
# print(f"Индекс значения {names_tuple.index('Anna')}")
#
# name, name1, name2 = names_tuple
# print(name,name1,name2, sep="\n")
#
# prof = ("Дмитрий", 45, "London")
# name, age, city = prof
# print(name)
# print(age)
# print(city)
from itertools import count
from tkinter.font import names

# #1
# numbers = (5, 10, 15, 20, 25)
# for i in numbers:
#     print(i)
#
# #2
# numbers = (3, 7, 10, 2, 8)
# res = 0
# for i in numbers:
#     res = res + i
# print(f"Сумма: {res}")
#
# #3
# numbers = (4, 7, 12, 9, 20, 3)
# res = 0
# counts = 0
# for i in numbers:
#     if i % 2 == 0:
#         counts = counts + 1
# print(f"Количество чётных чисел кортежа: {counts}")
#
# #4
# numbers = (11, 45, 23, 67, 12)
# maximum = numbers[0]
# for i in numbers:
#     if i > maximum:
#         maximum = i
# print(f"Максимально число кортежа: {maximum}")
#
# #5
# names = ("Anna", "Bob", "Tom", "Kate")
# n = input("Введите имя: ")
# for i in names:
#     if i == n:
#         print("Такое имя есть ")
#         break
# else:
#     print("Такого имени нет")

#1
# products = [
#     ("apple", 50),
#     ("banana", 30),
#     ("orange", 70),
#     ("milk", 100)
# ]
#
# for lst in products: #  Бежим по кортежам в списке
#     name, prise = lst # Распоковываем кортеж
#     print(f"{name} стоит {prise}") # Печатаем

#2 найти товар дороже 60
# products = [
#     ("apple", 50),
#     ("banana", 30),
#     ("orange", 70),
#     ("milk", 100),
#     ("bread", 40)
# ]
#
# for lst in products:
#     name, prise = lst # Распоковываем каждый кортеж
#     if prise > 60: # Если значение больше 60
#         print(name) # Выводи их

#3 сумма всех цен
# products = [
#     ("apple", 50),
#     ("banana", 30),
#     ("orange", 70),
#     ("milk", 100)
# ]
# results = 0
# for lst in products:
#     prise = lst[1] # Цена в элементие с инексом 1
#     results = results + prise # Складываем все цены
# print(f"Сумма всех товаров: {results}")
#
#4 список учеников и оценки

# students = [
#     ("Anna", 5),
#     ("Bob", 4),
#     ("Tom", 3),
#     ("Kate", 5),
#     ("Max", 2)
# ]
#
# for tuples in students:
#     name, cou = tuples
#     if cou == 5:
#         print(name)

#5 создать новый список из кортежей

# names = ["Anna", "Bob", "Tom"]
# ages = [20, 25, 30]
#
# res = []
#
# for i in range(len(names)):
#     # for j in range(len(ages)):
#     tup = (names[i],ages[i])
#     res.append(tup)
# print(res)

#6. Нужно создать новый список кортежей:

# products = ["apple", "banana", "milk", "bread"]
# prices = [50, 30, 100, 40]
#
# res = []
# for i in range(len(products)):
#     tub = (products[i], prices[i])
#     res.append(tub)
# print(res)

# products = ["apple", "banana", "milk", "bread"]
# prices = [50, 30, 100, 40]
#
# res = []

#Вариант через enumerate
# for i, name in enumerate(products):
#     tup = (name,prices[i])
#     res.append(tup)
# print(res)
#
# for i in range(len(products)): # Получаем индексы
#
#     if prices[i] > 40: # Перебираем все цены больше 40
#         tup = (products[i], prices[i])
#         res.append(tup) #Добавляем в список кортеж
# print(res)

#8 Нужно создать список кортежей только для товаров, у которых общая стоимость больше 100.
# products = ["apple", "banana", "milk", "bread", "cheese"]
# prices = [50, 30, 100, 40, 150]
# counts = [3, 5, 2, 4, 1]
#
# lst = []
# for i in range(len(products)):
#     total = prices[i] * counts[i]
#     if total > 100:
#         tup = (products[i],prices[i],counts[i],total)
#         lst.append(tup)
# print(lst)

#9 Создай список кортежей только для товаров, у которых количество больше 2.
#
# products = ["apple", "banana", "milk", "bread", "cheese"]
# prices = [50, 30, 100, 40, 150]
# counts = [3, 5, 2, 4, 1]
#
# result = []
# for i in range(len(products)):
#      if counts[i] > 2:
#         tup = (products[i],prices[i],counts[i])
#         result.append(tup)
# print(result)

# #10
#
# products = ["apple", "banana", "milk", "bread", "cheese"]
# prices = [50, 30, 100, 40, 150]
# counts = [3, 5, 2, 4, 1]
#
# result = []
# for i in range(len(products)):
#     total_price = prices[i] * counts[i]
#     if prices[i] > 40 and counts[i] > 1:
#         tup = (products[i], prices[i], counts[i], total_price)
#         result.append(tup)
# print(result)

#11

# products = ["apple", "banana", "milk", "bread", "cheese"]
# prices = [50, 30, 100, 40, 150]
# counts = [3, 5, 2, 4, 1]
#
# result = []
# for i in range(len(products)):
#     price = prices[i]
#     product = products[i]
#     count = counts[i]
#     total_price = price * count
#     if total_price > 150:
#         tup = (product,total_price)
#         result.append(tup)
# print(result)

# # products = [
# #     ("apple", 50, 3),
# #     ("banana", 30, 5),
# #     ("milk", 100, 2),
# #     ("bread", 40, 4),
# #     ("cheese", 150, 1)
# # ]
#
# result = []
#13_1
# for tb in products:
#     name = tb[0]
#     price = tb[1]
#     count = tb[2]
#     total = price * count
#     if total > 150:
#         tub = (name,total)
#         result.append(tub)
# print(result)

#13_2
# for name, price, count in products:
#     print(name,price,count)
#     total = price * count
#     if total > 150:
#         tub = (name,total)
#         result.append(tub)
# print(result)

#13
# products = [
#     ("apple", 50, 3),
#     ("banana", 30, 5),
#     ("milk", 100, 2),
#     ("bread", 40, 4),
#     ("cheese", 150, 1)
# ]
#
# max_product = None
# max_total = 0
#
# for nane,price,count in products:
#     total = price*count
#     if total > max_total:
#         max_total = total
#         max_product = nane
# print(f"Самый дорогой товар по общей стоимости: {max_product}, {max_total}")

#14 Нужно разделить товары на два списка:

# products = [
#     ("apple", 50, 3),
#     ("banana", 30, 5),
#     ("milk", 100, 2),
#     ("bread", 40, 4),
#     ("cheese", 150, 1)
# ]
#
# cheap = []
# expensive = []
#
# for name,price,count in products:
#     if price < 100:
#         tup = (name,price,count)
#         cheap.append(tup)
#     elif price >= 100:
#         tup = (name,price,count)
#         expensive.append(tup)
# print(cheap, expensive, sep="\n")

#
# На складе
# products = [
#     ("apple", 50, 10),
#     ("banana", 30, 8),
#     ("milk", 100, 5),
#     ("bread", 40, 12)
# ]
#
# # Проданные
# sold = [
#     ("apple", 3),
#     ("banana", 2),
#     ("milk", 5),
#     ("bread", 4)
# ]
# # Остаток = На складе - проданные
# result = []
# res = 0
# for ls in range(len(products)):
#     # print(products[ls][2]) #Берём количество products из индекса
#     # print(sold[ls][1]) #Берём количесто остатков из индекса
#     name = products[ls][0]
#     price = products[ls][1]
#     ost =products[ls][2] - sold[ls][1]
#     # print(ost)
#     tub = (name,price,ost)
#     # print(tub)
#     result.append(tub)
# print(result)

#17
#На складе
products = [
    ("phone", 500, 6),
    ("laptop", 1200, 3),
    ("tablet", 700, 4),
    ("mouse", 50, 10)
]
#Продано
sold = [
    ("phone", 2),
    ("laptop", 1),
    ("tablet", 4),
    ("mouse", 6)
]
result = []
for idx in range(len(products)):
    name = products[idx][0]
    price = products[idx][1]
    count = products[idx][2] #  на складе
    sell = sold[idx][1] #Продано
    res_ost = count - sell # После продаж на складе
    vir = sell * price # Выручка
    tub =(name,price,res_ost,vir)
    result.append(tub)
print(result)