# def order(x):
#     print("создаю замыкания с x =",x)
#

# def outer(x):
#     def inner(y):
#         return x+y
#     return inner
#
# f = outer(10)
# print(f(5))
# print(f(10))

# def outer():
#     name = "Анна"
#     def inner():
#         print(name)
#     return inner
#
# func = outer()
# func()
#
# def make_mulippliner(n):
#     def multiply(x):
#         return n * x
#     return multiply
#
# double = make_mulippliner(2)
# triple = make_mulippliner(3)
#
# print(double(10))
# print(double(10))

# def counter():
#
#     count = 0
#     def add():
#         nonlocal count
#         count = count + 1
#         return count
#     return add
#
# c = counter()
# print(c())
# def make_power(n):
#     def inter(x):
#         res =  x ** n
#         return res
#     return inter
#
# squre = make_power(3)
# cude = make_power(2)
# print(squre(5))
# print(cude(2))

# def make_discount(percent): # Функция приимает значение скидки
#     def apply_discount(price): # Функция принимает цену и возвращяет скидку
#         discount = price - (price * percent / 100) # Считаем результат вычета из цены скидку
#         return discount # Возвращяем подсчёт дисконта
#     return apply_discount  #Возвращяем что то
#
# disсount_10 = make_discount(10) # Скидка 10%
# disсount_25 = make_discount(25) # Скидка 25%
#
# disсount_90 = make_discount(90)  # Скидка 90%
#
# print(disсount_10(100))
# print(disсount_10(200))
# print(disсount_25(1000))
# print(disсount_90(100))

# def make_password_checker(min_length): #Функция принимает проверяемое значение количества знаков в пароле
#     def check_password(password): #Функция принимает значение пароля
#         return len(password) >= min_length #Вернём булевое значение условия
#
#     return check_password #Вернём внутренню функцию
#
#
# checker_6 = make_password_checker(6) # Проверяющая функция количество символов (6 символов)
# checker_10 = make_password_checker(10)
#
# print(checker_6("qwerty"))
# print(checker_6("abc"))
# print(checker_10("qwerty12345"))
# print(checker_10("qwerty"))

# def make_tax_calculator(tax_percent): #Функция принимает процент налога:
#     def price_un(price): #Функция принимает цену товара, и считает новую цену с учетом налога.
#         res = price + price * tax_percent / 100 #Посчитываем цену с учётом процентов
#         return res #Вернём результат
#     return price_un
#
# percent_10 = make_tax_calculator(10) #Процентная ставка 10%
# percent_25 = make_tax_calculator(25) #Процентная ставка 25%
#
# print(percent_10(100)) #Печатаем итоговую цену с учетом процентной ставки 10% и цены товара 100
# print(percent_25(280)) #Печатаем итоговую цену с учетом процентной ставки 25% и цены товара 280

# def make_prefix(prefix): # Принимаем префикс
#     def add_prefix(name):
#         return prefix + name # Вернем значение префикса + имя
#     return add_prefix
#
# prefix_mr = make_prefix("Mr. ")
# prefix_dr = make_prefix("Dr. ")
# prefix_user = make_prefix("User: ")
#
# print(prefix_mr("Smith"))
# print(prefix_dr("House"))
# print(prefix_user("Alex"))

# def make_suffix(suffix):
#     def add_url(url):
#         return f"{url}{suffix}"
#     return add_url
#
# com = ".com"
# ru = ".ru"
# vl = "!"
#
# add_com = make_suffix(com)
# add_ru = make_suffix(ru)
# add_execlaim = make_suffix(vl)
# print(add_com("google"))
# print(add_ru("yandex"))
# print(add_execlaim("Hi"))


def make_clicker():
    count = 0
    def add_counts():
        nonlocal count
        count = count + 1
        return count
    return add_counts

clicker = make_clicker()
print(clicker())
