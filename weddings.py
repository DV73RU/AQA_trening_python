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

def make_discount(percent): # Функция приимает значение скидки
    def apply_discount(price): # Функция принимает цену и возвращяет скидку
        discount = price - (price*100/percent) # Считаем результат вычета из цены скидку
        return discount # Возвращяем подсчёт дисконта
    return apply_discount  #Возвращяем что то
