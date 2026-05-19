# names = ["Alisa", "Bob", "Den"]
# age = [10,12,13]
#
# result = zip(names,age)
# print(list(result))

# login = ["user1", "user2"]
# password = ["pass1", "pass2"]
#
# for login, password in zip(login,password):
#     print(login,password)
#
# pairs = []

# numbers = [1,2,4,5,6,7,8,9]
# res = 0
# print(numbers)
# for i in range(len(numbers)):
#     # print(i, end=" ")
#     # print(f"индех - {i}, значение - {numbers[i]}")
#     res = res + i
#     if i % 2 == 0:
#         res = res + i
#         ct = [x for x in numbers if x % 2 == 0]
#
# print(f"Cумма четных чисел: {ct} = {res}")
#
# numbers = [1,2,4,5,6,7,8,9]
# maximum = numbers[0]
# for i in numbers:
#     if i > maximum:
#         maximum = i
# print(maximum)

# numbers = []
# for i in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# print(numbers)

# numbers = [4, 7, 2, 9, 5] # Сумма чисел списка
# results = 0
# for i in numbers:
#     results += i
# print(results)

# numbers = [3, 8, 12, 5, 7, 10, 1] # Cколько чисел в списке
# res = 0
# for i in range(len(numbers)):
#     res = res + 1
# print(f"Количестово чисел в списке: {res}")

# numbers = [15, 3, 27, 8, 19] # Максимальное число в списке
# maximum = numbers[0]
# for i in numbers:
#     if i > maximum:
#         maximum = i
# print(maximum)

# numbers = [4, 15, 8, 23, 7, 11, 2] # Создать список тз чисел списка больше 10
# new_numbers = []
# for i in numbers:
#     if i > 10:
#         new_numbers.append(i)
# print(new_numbers)

# lst = []
# # res = 0
# for i in range(5):
#     n = int(input("Введите число :"))
#     lst.append(n)
# res = 0
# counts = 0
# for j in lst:
#     res = res + j
#
#     if j % 2 == 0:
#         counts = counts + 1
#
# print(f"Список:{lst}")
# print(f"Сумма: {res}")
# print(f"Чётных чисел: {counts}")

# numbers = [x for x in range(1,7)]
# print(numbers)
# numbers.append(5) # Добавляем значение в конец списка
# print(numbers)
#
# numbers.insert(6,2) # Во второй индекс вставляем значение
# print(numbers)
# numbers.remove(2) # Удаляет первое значение из списка
# print(numbers)
#
# numbers.pop(0) # Удаляет по индексу
# numbers.pop() # Удаляет последний индекс
# print(numbers)
# res = numbers.count(2) #подсчет найденных злементов
# print(res)
# name = ["Иван","Жора", "Анна"]
# print(name)
# res = name.index("Иван") # Ищем индекс по значению.
# print(res)
# name.sort()
# print(name)
# name.sort(reverse=True)
# print(name.sort(reverse=True))
# name.reverse()
# print(name)
# numbers.reverse()
# print(numbers)
# new_numbers = numbers.copy()
# print(numbers)
# new_numbers.append(1000)
# print(new_numbers)
# numbers.extend(new_numbers)
# print(numbers)

# ls = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     ls.append(n)
# print(ls)

# ls = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     if n % 2 == 0:
#         ls.append(n)
# print(ls)

# numbers = [4, 15, 8, 23, 7, 11, 2]
# new_numbers = []
# for i in numbers:
#     if i > 10:
#         new_numbers.append(i)
# print(new_numbers)

# ls = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     ls.append(n**2)
# print(ls)

# ls = []
# for i in range(5):
#     n = input("Введите слово: ")
#     if len(n) > 4:
#       ls.append(n)
# print(ls)

# numbers = [2, 3, 4, 5]
# numbers.insert(0,1)
# print(numbers)

# numbers = [10, 20, 40, 50]
# r = len(numbers)
# print(r)
# numbers.insert(int(r / 2),10)
# print(numbers)

# words = ["Я", "изучаю", "Python"]
# t = "сейчас"
# words.insert(1,t)
# print(words)

# n = int(input("Введите число: "))
# numbers = [5, 10, 15, 20]
# numbers.insert(2,n)
# print(numbers)

#
# ls = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     ls.insert(0,n)
# print(ls)

# numbers = [10, 20, 30, 40, 50]
# numbers.pop(-1)
# print(numbers)

# numbers = [5, 10, 15, 20, 25]
# numbers.pop(2)
# print(numbers)

# words = ["apple", "banana", "orange", "kiwi"]
# deleted = None
# # words.pop(-1)
# deleted = words.pop(-1)
# print(f"Удалённый элемент: {deleted}")
# print(f"Список: {words}")

# numbers = [100, 200, 300, 400]
# numbers.pop(0)
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# while len(numbers)>0:
#     print(f"Удалили: {numbers[-1]}")
#     numbers.pop(-1)
# print(numbers)

# numbers = [5, 10, 15, 20, 25]
# numbers.remove(15)
# print(numbers)
#
# fruits = ["apple", "banana", "orange", "kiwi"]
# fruits.remove("orange")
# print(fruits)
#
# numbers = [3, 7, 10, 15, 20]
# n = int(input("Введите число: "))
# numbers.remove(n)
# print(numbers)
#
# numbers = [1, 2, 3, 2, 4, 2, 5]
# numbers.remove(2)
# print(numbers)

# numbers = [0, 5, 0, 10, 15, 0, 20]
# print(numbers)
# for i in numbers:
#     if i == 0:
#         numbers.remove(0)
# print(numbers)

# numbers = [0, 5, 0, 10, 15, 0, 20]
# while 0 in numbers:
#     numbers.remove(0)
# print(numbers)

# numbers = [10, 20, 30, 40, 50]
# numbers.clear()
# print(numbers)
#
# words = ["apple", "banana", "orange"]
# words.clear()
# print(words)
#
# numbers = [3, 7, 10, 15]
# print(numbers)
# numbers.clear()
# print(numbers)
#
# numbers = [1, 2, 3, 4, 5, 6, 7]
# if len(numbers) > 5:
#     numbers.clear()
# print(numbers)
#
# ls = []
# for i in range(5):
#     n = int(input("Введите число: "))
#     ls.append(n)
# print(ls)
# q = input('Очистить список? yes/no: ')
# if q =="yes":
#     ls.clear()
#     print(ls)
# else:
#     print(ls)