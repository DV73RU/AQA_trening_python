#1
# for i in range(1,6):
#     print(i)
#2
# for i in range(1,11):
#     print(i)
#3
# for i in range(10,1,-1):
#     print(i)
#4
# for i in range(2,22,2):
#     print(i)
#5
# text = input("Введите слово: ")
# count = 5
# for i in range(count):
#     print(text)
#6
# res = 0
# for i in range(1,10):
#     res = i+res
# print(res)
#7
# intr = int(input("Ведите число: "))
# for i in range(1,11):
#     res = intr * i
#     print(f"{intr} * {i} = {res}")
#8


# total = 0
# for i in range(5):
#     num = int(input("Введите число: "))
#     total += num
# print(f"Сумма {total}")

#9
# total = 0
# for i in range(5):
#     num = int(input("Введите число: "))
#     if num % 2 == 0:
#         total = total + 1
# print(total)


#10
# h = int(input("Ширина: "))
# l = int(input("Высота: "))
# for i in range(h):
#     print("*" * l)

# #11
# res = 0
# number = 0
# for i in range(5):
#     n = int(input("Введите число: "))
#     if n % 2 == 0:
#         res = res + n
#         number = number + 1
#
# print(f"Результат сложения {number} чисел: {res}")

#12
# maximum = 0
# for i in range(5):
#     n = int(input("Введите число: "))
#     if n > maximum:
#         maximum = n
# print(f"Макимальное число: {maximum}")

#13
# maximum = 10
# count = 0
# for i in range(7):
#     n = int(input("Введите число: "))
#     if n > maximum:
#         count = count + 1
# print(f"Количество чисед больше 10: {count}")

#14
# count = 0
# n = int(input("Введите число: "))
# for i in range(1,n+1):
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i * j}")
#     print()

#15

# n = int(input("Введите Ширину: "))
# i = int(input("Введите высоту: "))
# for i in range(1, i + 1): #Высота (количество итераций в цикле)
#     print("*" * n) #Ширина (количество элементов)

# n = int(input("Введите Ширину: "))
# i = int(input("Введите высоту: "))
# for i in range(1, i + 1): #Высота (количество итераций в цикле)
#     print("*","" * n , "*") #Ширина (количество элементов)

#15
# n = int(input("Введите Ширину: "))
# h = int(input("Введите высоту: "))
# for i in range(1, h + 1): #Высота (количество итераций в цикле)
#     if i == 1 or i == h:
#         print("*" * n) #Ширина и вид первой и последней строки
#     else:
#         print("*" + " " * (n - 2) + "*") #Ширина и вид сроки не первой и не последней

#16
# minimum = int(input("Введите число: "))
# for i in range(4):
#     n = int(input("Введите число: "))
#     if n < minimum:
#         minimum = n
# print(f"Минимальное число: {minimum}")

#17
# result = 0
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     result = result + i
# print(result)

#18
# result = 1
# n = int(input("Введите число: "))
# for i in range(1, n+1):
#     result = result * i
#     print(i)
# print(result)

#21
# count_positive = 0
# count_negative = 0
# for i in range(7):
#     n = int(input("Введите число: "))
#     if n < 0:
#         count_negative = count_negative + 1
#     if n > 0:
#         count_positive = count_positive + 1
# print(f"Отрицательных чисел: {count_negative}")
# print(f"Положительных чисел: {count_positive}")

#22
# n = int(input("Введите высоту: "))
# for i in range(1, n):
#     print("*" * i)

#23
# summ = 0
# counts = 0
#
# for i in range(5):
#     n = int(input("Ведите число: "))
#     summ = summ + n
#     counts = counts + 1
# print(f"Среднее: {summ/counts}")

#24
# counts = 0
# for i in range(8):
#     n = int(input("Введите число: "))
#     if 20 >= n >= 10:
#         counts = counts + 1
# print(f"Чисел от 10 до 20: {counts}")

# #25
# n = int(input("Введите высоту: "))
# for i in range(1, n+1):
#     print("*" * i)
#
# #25
# n = int(input("Введите высоту: "))
# for i in range(n):
#     print("*" * n)


#26
#
# summ = 0
# for i in range(10):
#     n = int(input("Введите число: "))
#     if n % 3 == 0:
#         summ = summ + n
# print(f"Сумма чисел , делящихся на 3: {summ}")
#27

# maximum = None
#
# for i in range(7):
#     n = int(input("Введите число: "))
#
#     if n % 2 == 0:
#         if maximum is None:
#             maximum = n
#         elif n > maximum:
#             maximum = n
#
# if maximum is None:
#     print("Чётных чисел нет")
# else:
#     print(f"Максимальное чётное число: {maximum}")

#28
# pas = "python123"
# attempt = 3
# #
# # n = input("Введите пароль: ")
# for i in range(attempt):
#     n = input("Введите пароль: ")
#     if n == pas:
#         print("Доступ разрешён")
#         break
#     elif n != pas:
#         print("Неверный пароль")
# else:
#     print("Попытки закончились")

#29
#
# text = input("Введите слово: ")
# print("*" * (len(text) + 4)) #Ширина и вид первой и последней строки
# print("* " + text + " *") #Ширина и вид сроки не первой и не последней
# print("*" * (len(text) + 4)) #Ширина и вид первой и последней строки

# #30
# n = int(input("Введите высоту: "))
# res = 0
# for i in range(1, n+1):
#     for j in range(1, i + 1):
#         print(j,end="")
#     print()


