# products = 'apple, яюлоко, груша, киви, мандарин, виски, пиво, текила,лимон, папая, лайм'
#
# products = products.replace(' ','').split(',')
# print(products)
#
# i = 0
# while i< len(products):
#     if products[i] in ['виски','пиво','текилла']:
#         i = i + 1
#         continue
#     else:
#         print(f"ПРодукт на этой ттериации {products[i]} - это сож")
#         i = i + 1

# n = 0 # Переменая начальная
# res = 0 # Переменая результат суммвы
# while n >= 0: # Дотех пор пока n больше или равно нулюю
#     n = int(input("Введите число: ")) # Спрашивай ввод числа
#     if  n>=0: # Если ввели больше илит расно 0
#         res = res + n # Считай сумму
# print(f"Сумма {res}") # Вывводи сумму

# res = 0
# while True:
#     n = int(input("Введите число: "))
#     if n < 0: # Когда пользователь ввсел число меньше нуля останови цикл
#         break # Выйди из уикал
#     res = res + n # Вцикле пощитай результат
# print(f"Cумма {res}") # Выведи результат

# correct_password = "python123"
#
# while True:
#     n = input("ВВЕДИТЕ ПАРОЛЬ: ") # ввод пароля
#     if n == correct_password: # если совпало с тем то загодали
#         break # Выходи из цикла
#     print("Не верно, ещё раз") # Печатай что пароль не верный
# print("Досту разрешён") # Печатай если совпал и выходи из цикла

# pr_exit = "выход"
# pr_hi = "Привет"
# pr_time = "Время"
# prin = "Вы ввели команду"
# while True:
#     n = input("Введите команду: ").lower()
#     if n == pr_exit:
#         print(f"{prin}: {pr_exit}")
#         print("Досвидания")
#         break
#     elif n == pr_hi:
#         print(f"{prin}: {pr_hi}")
#         print(f"Привет как дела?")
#
#     elif n == pr_time:
#         print(f"{prin}: {pr_time}")
#         print(f"Время програмирования")
#
#     else:
#         print(f"Неизвестная команда")


# correct_password = "python123"
# attempts = 3
#
# while True:
#     n = input("Ведите пароль: ")
#     if n == correct_password:
#         print("Доступ разрешён")
#         break
#
#     if n != correct_password:
#         attempts = attempts -1
#         print(f"Не верно, осталось попыток: {attempts} ")
#         if attempts == 0:
#             print("Доступ заблокирован")
#             break
# while True:
#     try:
#         n = int(input("Ведите число: "))
#         print(f"Ты ввсел число {n}")
#         break
#     except ValueError:
#         print("Это не число, попробуйте ещё раз")



#
























