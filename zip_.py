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
#
# numbers = [1, 2, 3, 2, 4, 2, 5]
# res = numbers.count(2)
# print(res)
#
# fruits = ["apple", "banana", "apple", "orange", "apple"]
# res = fruits.count("apple")

# numbers = [5, 10, 15, 10, 20, 10, 25]
# n = int(input("Введите число: "))
# res = numbers.count(n)
# print(res)
# if n not in numbers:
#     print(f"Нет такого числа {n}")


# numbers = [3, 7, 11, 7, 15, 20]
# n = int(input("Введите число: "))
# if numbers.count(n) > 0:
#     print("Есть такое число с писке")
# else:
#     print("Числа нет в списке")

# numbers = [0, 5, 0, 10, 15, 0, 20, 0]
# res = 0
# if res in numbers:
#     print(numbers.count(res))

# numbers = [i for i in range(1,6)]
# print(numbers)

# kd = [j ** 2  for j in range(1,5)]
# print(kd)
# ct = [i for i in range(1,11) if i % 2 == 0]
# print(ct)
#
# ct = [i for i in range(1,28) if i > 10]
# print(ct)

# num = [i for i in range(1,21)]
# print(num)
#
# num2 = [i **2 for i in range(1,11)]
# print(num2)
#
# num3 = [i for i in range(1,31) if i % 2 == 0]
# print(num3)
#
# numbers = [5, 12, 3, 18, 7, 25, 10]
# new_numbers =[i for i in numbers if i > 10]
# print(new_numbers)
#
# words = ["cat", "python", "dog", "apple", "hi"]
# new_words = [i for i in words if len(i) > 3]
# print(new_words)

# numbers = [5, 12, 3, 18, 7, 25, 10]
# res = 0
# for i in numbers:
#     res = res + i
# print(res)

# fruits = ['яблоко','банан','груша','банан','киви']
# while 'банан' in fruits:
#     fruits.remove('банан')
# print(fruits)

# ls = [i for i in range(10,51) if i % 5 == 0]
# print(ls)
#
# ls2 = [i ** 3 for i in range(1, 11)]
# print(ls2)
#
# numbers = [3, -5, 10, -2, 0, 7, -8]
# new_numbres = [i for i in numbers if i > 0]
# print(new_numbres)
#
# words = ["python", "java", "javascript", "go", "html", "css"]
# ls_len_words = [len(i) for i in words]
# print(ls_len_words)
#
# numbers = [1, 2, 3, 4, 5]
# new_num = [i+10 for i in numbers]
# print(new_num)

# numbers = [1, 2, 3, 4, 5, 6]
# new_num = ["чётное" if i % 2 == 0 else "Не чётное" for i in numbers]
# print(new_num)
#
# numbers = [3, -5, 0, 10, -2]
# new_num = ["плюс" if i > 0 else "минус" for i in numbers]
# print(new_num)
#
# numbers = [5, -3, 10, -7, 2]
# new_num = [0 if i < 0 else i for i in numbers]
# print(new_num)
#
# words = ["cat", "python", "code", "apple"]
# new_words = ["длинное" if len(i) > 4 else "короткое" for i in words]
# print(new_words)
#
# numbers = [1, 2, 3, 4, 5]
# new_num = [i * 2 if i % 2 == 0 else i for i in numbers]
# print(new_num)
#


# names = ["Anna", "Bob", "Tom", "Kate", "Bob"]
# n = input("Введите имя: ")
#
# if n in names:
#     idx = names.index(n)
#     print(f"Индекс: {idx}")
#
# else:
#     print("Такого имени нет")


# numbers = [14, 3, 25, 7, 1, 18, 10]
# numbers.sort(reverse=True)
# maximum = numbers[0]
# minimum = numbers[0]
# for i in numbers:
#     if i > maximum:
#         maximum = i
#     elif i < minimum:
#         minimum = i
# print(f"Самое большое число: {maximum}")
# print(f"Самое маленькое число: {minimum}")
# print(numbers)

# ls = []
# for i in range(1,6):
#     n =int(input("Введите число: "))
#     ls.append(n)
#     ls.sort(reverse=True)
# print(ls)

#4
# a = [3, 8, 12, 5]
# b = [10, 15, 2, 20]
#
# even_numbers = []
# even_numbers.extend([i for i in a if i % 2==0])
# even_numbers.extend([i for i in b if i % 2==0])
#
# print(even_numbers)

# numbers = [5, 10, 15, 20]
# new_number = numbers.copy()
# new_number.append(25)
# new_number.remove(10)
# new_number.sort(reverse=True)
# print(numbers, new_number, sep="\n")

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     print(row)
#
# for i in matrix:
#     for j in i:
#         print(j)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(matrix[1][1])
#
# matrix = [
#     [10, 20],
#     [30, 40],
#     [50, 60]
# ]
#
# for i in matrix:
#     print(i)
#
# matrix = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]
# for i in matrix:
#     for j in i:
#         print(j)
#
# matrix = [
#     [2, 4, 6],
#     [1, 3, 5],
#     [10, 20, 30]
# ]
#
# res = 0
# for i in matrix:
#     for j in i:
#         res = res + j
# print(res)
#
# matrix = [
#     [3, 8, 12],
#     [5, 10, 15],
#     [7, 2, 20]
# ]
#
# even_numbers = []
# for i in matrix:
#     for j in i:
#         if j % 2 == 0:
#             even_numbers.append(j)
# print(even_numbers)

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# row_sums = []
# # res = 0
# for i in matrix:
#     res = 0
#     for j in i:
#         res = res + j
#     row_sums.append(res)
# print(row_sums)


# matrix = [
#     [3, 8, 12],
#     [5, 20, 15],
#     [7, 2, 10]
# ]
#
# max_numbers = []
# for ls in matrix:
#     ls.sort(reverse=True)
#     max_numbers.append(ls[0])
# print(max_numbers)

# matrix = [
#     [5, 2, 3],
#     [4, 10, 6],
#     [7, 8, 15]
# ]
# new_mum = []
#
# res = 0
# for i in range(len(matrix)):
#     print(i)
#     res = res + matrix[i][i]
# print(res)

#
# matrix = [
#     [3, 8, 12],
#     [5, 10, 15],
#     [7, 2, 20]
# ]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] % 2 == 0: # Если значения четный
#             matrix[i][j] = 0
# print(matrix)
#
#

matrix = []

for i in range(1, 4):
    row = []
    for j in range(1, 4):
        row.append(i * j)
    matrix.append(row)
print(matrix)


