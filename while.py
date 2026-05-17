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
# n = int(input("Введити число: "))
# counts = 0
# res = None
# while n != 0: #Пока n не вавно 0
#     n = n // 10 # Дели n на 10
#     counts = counts + 1 # Считаеи количество делений
# print(counts)

#10
# n = int(input("Введите число: "))
# rev = 0 # Переменная для ревесионного числа
# while n != 0: # Пока n не равно О выполняй цикл
#     dig = n % 10 # Получаем последнюю цифру числа
#     rev = rev * 10 + dig # Получаме первую цифру реверс числ
#     n = n // 10 # Получаем новое число без последней цифры
# print(rev)



#11 Сумма цифр числа
# n = int(input("Введите число: "))
#
# res = 0
# dig = 0
# while n != 0:
#     dig = n % 10
#     print(dig)
#     n = n // 10
#     res = res + dig
# print(res)

#12 Количестов чётных цифр
# n = int(input("Введите число: "))
# counts = 0
# dig = 0
# while n != 0:
#     dig = n % 10
#     if dig % 2 == 0:
#         print(dig)
#         counts = counts + 1
#     n = n // 10
# print(f"Количестов чётных чисел {counts}")

#13 Максимальная цифра
# n = int(input("Введите число: "))
# maximum = 0
# dig = 0
# while n != 0:
#     dig = n % 10
#     if dig > maximum:
#         maximum = dig
#     n = n // 10
# print(f"Максимальная цифра: {maximum}")

#14
# passwd = "qwerty"
# while True:
#     input_pass = input("Введите пароль: ")
#     if input_pass == passwd:
#         print("Доступ разрешён")
#         break
#     else:
#         print("Доступ запрешён")

#15 Меню программы
print("1.Сказать привет","2.Сказать пока","3.Выйти", sep="\n")

while True:

    # print("1.Сказать привет","2.Сказать пока","3.Выйти", sep="\n")
    input_menu = int(input("Введите команду: "))
    if input_menu == 3:
        break
    elif input_menu == 2:
        print("Пока")
    elif input_menu == 1:
        print("Привет")

