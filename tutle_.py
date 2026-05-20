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

#1
numbers = (5, 10, 15, 20, 25)
for i in numbers:
    print(i)

#2
numbers = (3, 7, 10, 2, 8)
res = 0
for i in numbers:
    res = res + i
print(f"Сумма: {res}")

#3
numbers = (4, 7, 12, 9, 20, 3)
res = 0
counts = 0
for i in numbers:
    if i % 2 == 0:
        counts = counts + 1
print(f"Количество чётных чисел кортежа: {counts}")

#4
numbers = (11, 45, 23, 67, 12)
maximum = numbers[0]
for i in numbers:
    if i > maximum:
        maximum = i
print(f"Максимально число кортежа: {maximum}")

#5
names = ("Anna", "Bob", "Tom", "Kate")
n = input("Введите имя: ")
for i in names:
    if i == n:
        print("Такое имя есть ")
        break
else:
    print("Такого имени нет")
