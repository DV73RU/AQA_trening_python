#1
# for i in range(1,11):
#     print(i)


#2
# for i in range(10,0,-1):# Старт с 10 до 0 отрицательный step в обратном порядке
#     print(i)

# #3
# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)
# #4
# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)
# #5
# n = int(input("Введите число: "))
# res = 0
# for i in range(1, n+1):
#     res = res + i
# print(res)
#
# #6
# n = int(input("Введите число: "))
# res = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         res = res + i
# print(res)
#
# #7
# n = int(input("Введите число: "))
# res = 1
# for i in range(1, n+1):
#     res = res * i
#     print(i)
# print(res)

#8
#
# n = int(input("Введите число: "))
# for i in range(1,11):
#     print(f"{n} * {i} = {i*n}")



#9 Посчитать количество букв в слове
# text = input("Введите слово :")
#
# counts = 0
# for i in text:
#     counts = counts + 1
# print(counts)


#10
# res = 0
# text = input("Введите слово :")
# for i in text:
#     res = res + i
#     print(res)

#11 Посчёт гласных
# text = input("Введите слово: ")
# g = "аеёиоуыэюя"
# counts = 0
# for i in text:
#     if i in g:
#         counts = counts + 1
#         print(i)
# print(counts)

#12
# maximum = 0
# for i in range(1,6):
#     n = int(input("Введите число: "))
#     if n > maximum:
#         maximum = n
# print(f"Максимальное число: {maximum}")
#
#
#13
# minimum = 0
# for i in range(1,6):
#     n = int(input("Введите число: "))
#     if n < minimum:
#         minimum = n
# print(f"Минимальное число: {minimum}")

#14 Посчитать количество положительных чисел

# res = 0
# for i in range(1,8):
#     n = int(input("Введите число: "))
#     if n > 0:
#         res = res + n
# print(f"Сумма положительных чисел: {res}")


#15 Посчитать количество отрицательных чисел

# res = 0
# for i in range(1,8):
#     n = int(input("Введите число: "))
#     if n < 0:
#         res = res + n
# print(f"Сумма отрицательных чисел: {res}")

#16 Сумма всех чисел
# res = 0
# for i in range(1,6):
#     n = int(input("Введите число: "))
#     res = res + n
# print(f"Сумма всех чисел чисел: {res}")
#
#17 Средне арифметическое
# res = 0
# for i in range(1,6):
#     n = int(input("Введите число: "))
#     res = (res + n) / i
# print(f"Сумма средне арифметическое чисел: {res}")
#18 Квадрат числа
# res = 0
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     print(i ** 2)

# 19 Звёздочки в линию
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     print("*", end="")

#20 Квадрат из звёздочек
# n = int(input("Размер квадрата: "))
# for i in range(1, n+1):
#     print("*" * n)

# #21 Треугольник из звёздочек
# n = int(input("Размер : "))
# for i in range(1, n+1):
#     print("*" * i)

# #22 Обратный треугольник из звёздочек
# n = int(input("Размер: "))
# for i in range(n, 0, -1):
#     print("*" * i)

# 23 Число в строку
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     print(i, end=" ")
#24 Сумма чисел
# n =int(input("Введите число:"))
# res = 0
# for i in str(n):
#     res = res + int(i)
# print(res)

#25
# text = input("Введите слово: ")
# b = input("Введите букву: ")
# counts = 0
# for i in text:
#     if b == i:
#         counts = counts + 1
# print(counts)

#26 Подчёт гласных и согласных

# text = input("Введите слово:")
# g = "аеёиоуыэюя"
# s = "бвгджзйклмнпрстфхцчшщ"
#
# count_g = 0
# count_s = 0
#
# for i in text:
#     if i in g:
#         count_g = count_g + 1
#     elif i in s:
#         count_s = count_s + 1
# print(f"Гласных: {count_g}, Согласных {count_s}", sep="\n")

#27 Подсчет общих количество букв во всех словах
# counts = 0
# for i in range(1,6):
#     n = input("Введите слово: ")
#     res = 0
#     for j in n:
#         res = res + 1
#     counts = counts + res
# print(counts)


#27_1 Подсчет общих количество букв во всех словах
# counts = 0
# for i in range(1,6):
#     n = input("Введите слово: ")
#     res = 0
#     for j in n:
#         res = res + 1
#     counts = counts + res
# print(counts)


#27 Найти самое длинное слово
# counts = 0
# long_text = None
# maximum = 0
# for i in range(1,6):
#     res = 0
#     n = input("Введите слово: ")
#     for j in n:
#         res = res + 1
#     if res > maximum:
#         maximum = res
#         long_text = n
# print(f"Самое длинное слово {long_text} : {maximum} символов ")

#28 Подсчитать сумму только положительных чисел
# summa = 0
# for i in range(1,8):
#     n = int(input("Введите число: "))
#     if n > 0:
#         summa = summa + n
# print(f"Сумма положительных чисел: {summa}")


#29 Проверить есть ли буква в слове, как решить циклом?
# text = input("Введите слов: ")
# n = input("Введите букву: ")
#
# if n in text:
#     print(f'Буква "{n}" найдена')
# else:
#     print(f'Буква "{n}" не найдена')

# #29 Проверить есть ли буква в слове, решить циклом
# text = input("Введите слово: ")
# n = input("Введите букву: ")
# for i in text:
#     if i == n:
#         print("Буква найдена")
#         break
# else:
#     print("Буква не найдена")

#30 рамка вокруг слова
text = input("Введите слово: ")
w = len(text) + 4
for i in range(w):
    print("*", end="")
print()
print("* " + text + " *")
for i in range(w):
    print("*", end="")



