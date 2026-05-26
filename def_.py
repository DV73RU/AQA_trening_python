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

def greet(name = "Гость"):
    print(f"Привет {name}")

greet("Толя")