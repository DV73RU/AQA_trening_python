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

n = int(input("Введите Ширину: "))
i = int(input("Введите высоту: "))
for i in range(1, i + 1): #Высота (количество итераций в цикле)
    print("*" * n) #Ширина (количество элементов)

