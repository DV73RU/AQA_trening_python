# def get_name_age():
#     return "Anna", 24
#
# name, age = get_name_age()
# print(name)
# print(age)
#
# def add(a,b):
#     return  a + b
#
# res = add(10,20)
# print(res)
#
# def get_name(name = "Дмитрий"):
#     return name
#
# res = get_name("Толя")
# print(res)
# res = get_name()
# print(res)
#
# def greet(name, age):
#     return [name,age]
#
# res = greet(name="Анна", age=10)
# print(res)
#
# def summ_al(*args):
#     return sum(args)
#
# print(summ_al(1,2,3,4,5))

# def print_info(**kwargs):
#     for key,values in kwargs.items():
#         print(key,values)
#
# print_info(name = "Anna", age = 23)

# def show_args(*arges):
#
#     return arges
#
# print(show_args(1,4,4,67,8))

# def sum_numbers(*args):
#     return sum(args)
#
# print(sum_numbers(1,3,3,4,5,6))
#
# def sum_numbers_1(*args):
#     res = 0
#     for i in args:
#         res = res + i
#     return res
#
# print(sum_numbers(1,2))
#
# def max_number(*args):
#     return max(args)
#
# print(max_number(1,2,3,4,0,10))
#
#
# def max_number(*args):
#     maximum =args[0]
#     for i in args:
#         if i > maximum:
#             maximum = i
#     return maximum
#
# print(max_number(1,3,45,-1,3))
#
#
# def show_user(**kwargs):
#     for key, val in kwargs.items():
#         print(f"{key}: {val}")
#
# show_user(name = "Anna", age = 23, city = "London")
#
#
# def create_user(**kwargs):
#         print(kwargs)
#
#
# create_user(name="Bob", age=30, job="QA")
#
# def only_even(*numbers):
#     lst = []
#     for i in numbers:
#         if i % 2 == 0:
#             lst.append(i)
#
#     return lst
#
#
# print(only_even(1,2,3,4,5,6))
#
# def info(*date, **user):
#     print("Обычные аргументы:")
#     for i in date:
#         print(i)
#     print("Именованные аргументы:")
#     for key, val in user.items():
#         print(f"{key} - {val}")
#
# info(10,20, name = "Anna",city = "London")

# def summa(a,b):
#     return a + b
#
# def is_even(number):
#     return number % 2 == 0
# print(is_even(113))

# def greet(name = "Гость"):
#     print(f"Привет {name}")
#
# greet("Толя")

# squre = lambda x: x ** 2
# print(squre(5))
# print(squre(10))
#
# summa = lambda x,y: x+y
# print(summa(10,20))
# print(summa(5,7))
#
# is_even = lambda x : "even" if x % 2 == 0 else "odd"
# print(is_even(2))
# print(is_even(5))
#
# def hello():
#     message = "Hello"
#     print(message)
# hello()
#
# name = "Anna"
# def show_name():
#     print(name)
#
# show_name()
#
# count = 0
# def increase():
#     global count
#     count = count + 1
#     return count
#
# increase()
# increase()
# increase()
# print(count)
#
#
# balance = 1000
# def buy(price):
#     global balance
#     balance = balance - price
#     return balance
#
# buy(200)
# buy(150)
# print(balance)

#1
# numbers = [1, 2, 3, 4, 5]
#
# def lis_kd(ls):
#
#     return list(map(lambda x: x ** 2, ls)) #Верни список из квадратов поочеёдно из элементов переданного списка
#
# # lis_kd(numbers)
# print(lis_kd(numbers)) #Печатаем выполнение функции с переданным листом

# Задача 2 — оставить только чётные через filter
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# def lst_odd(ls):
#     return list(filter(lambda x: x % 2 == 0,ls)) #Верни список отфильровав в нём элементы согласно условию
#
# print(lst_odd(numbers))

# Задача 3 — оставить только слова длиннее 4 букв
words = ["cat", "apple", "dog", "banana", "car", "python"]

def lene_4(ls):
    return list(filter(lambda x: len(x)>4,ls))

print(lene_4(words))

# Задача 4 — перевести цены в доллары

prices = [100, 250, 500, 1000]
def r_to_dolr(ls):
    return list(map(lambda x: x / 100,ls))

print(r_to_dolr(prices))

# Задача 5 — оставить положительные числа

numbers = [-5, 10, -2, 0, 7, -1, 3]
def plus_num(ls):
    return list(filter(lambda x:x > 0,ls))

print(plus_num(numbers))

# Задача 6 — сделать имена с большой буквы

names = ["anna", "bob", "tom", "kate"]

def upp(ls):
    return list(map(lambda name: name.capitalize(),ls))

print(upp(names))

# Задача 7 — получить длину каждого слова

words = ["hello", "python", "code"]

def lens_words(ls):
    return list(map(lambda word: len(word),ls))

print(lens_words(words))

# Задача 8 — сначала отфильтровать, потом изменить

numbers = [1, 2, 3, 4, 5, 6]

def news(ls):
    return list(filter(lambda x: x % 2 == 0,ls))


print(news(numbers))