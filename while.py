# i = 1
# while i <= 10:
#     print(i)
#     i = i + 1



#1 Число от 1 до 10
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

#2 Число ои 10 до 1
# i = 10
# while i >= 1:
#     print(i)
#     i = i - 1

#3 Чётные от 1 до 20
# i = 1
# while i <= 20:
#     i = i + 1
#     if i % 2 ==0:
#         print(i)
#4
# n = int(input("Введите число: "))
# res = 0
# i = 1
# while i <= n:
#     res = res + i
#     i =  i + 1
# print(res)

#5
# n = int(input("Введите число: "))
# res = 1
# i = 1
# while i <= n:
#     res = res * i
#     i =  i + 1
# print(res)

#6
# n = int(input("Введите число: "))
# res = 0
# i = 1
# while i <= n:
#     i = i + 1
#     if i % 2 == 0:
#         res = res + i
#     i =  i + 1
# print(res)

#7
# res = 0
# while True:
#     n = int(input("Введите число: "))
#     if n != 0:
#        res = res + n
#     else:
#         break
# print(res)

#8

# secret = 7
# while True:
#     n = int(input("Введите число: "))
#     if n == secret:
#         print("Угадал")
#         break
#     else:
#         print("Не угадал")

#9
n = int(input("Введити число: "))
counts = 0
res = 0
while res == 0: # Пока i не станет равной нулю
    res = i // 10 # Дели n на 10, пока результат делегия не станет равно нулю
    counts = counts + 1 # Считаеи количество делений
    print(counts)