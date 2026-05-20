# name = ["Дмитрий","Саша","Лена"]
#
# for n, i in enumerate(name):
#     print(n, i)
# ls = []
# for items in enumerate(name, start=1):
#     print(items)
#     ls.append(items)
# print(ls)
#
# num = [1,2,3,4,5,6,7,8,9,10]
#
# for i, n in enumerate(num):
#     if n % 2 == 0:
#         print(f"Индекс чёт {i} - число {n}")
# for i, name in  enumerate(name):
#     print(num[i])

#
# prod = ["Мак", "Асус","Делл","XP"]
# prise = [100,150,200,340]

# res = []
# for i in range(len(prod)):
#     tub = (prod[i], prise[i] )
#     res.append(tub)
# print(res)

# ls = []
# for i, name in enumerate(prod): # Полчаем индексы и имена из спискапродуктов
#     tup = (name,prise[i]) # Создаём кортеж из имени и цены по индексу из скиска цен
#     ls.append(tup)
# print(ls)
















# #1
# names = ["Anna", "Bob", "Tom", "Maria"]
# ages = [20, 25, 18, 30]
#
# res = []
#
# for i, name in enumerate(names):
#     tup = (name,ages[i])
#     res.append(tup)
# print(res)
#
# #2
# products = ["apple", "banana", "milk", "bread", "cheese"]
# prices = [50, 30, 100, 40, 150]
#
# res_lst = []
# for i, pris in enumerate(prices):
#     if pris > 50:
#         tup = (products[i], pris)
#         res_lst.append(tup)
# print(res_lst)


# menu = ["Pizza", "Burger", "Pasta", "Salad", "Coffee"]
# prices = [12, 9, 11, 7, 4]
#
# for i, name in enumerate(menu,start=1):
#     print(f"{i}. {name} - {prices[i-1]}$")


menu = ["Pizza", "Burger", "Pasta", "Salad", "Coffee"]
prices = [12, 9, 11, 7, 4]

for i, name in enumerate(menu,start=1):
    price = prices[i-1]
    if price > 10:
        print(f"{i}. {name} - {prices[i-1]}$")