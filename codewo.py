# def number_to_string(num):
#     string = str(num)
#     return string
#
#
# num = 1234
# print(number_to_string(num))
from os import mkdir

from urllib3 import proxy_from_url

# def remove_char(s):
#     new_r = s[1:-1]
#     return new_r
#
# s = "Привет"
# print(remove_char(s))
#
# def remove_char_2(s):
#     new_s = s.rstrip()
#     return new_s
#
# s = "ПРИВЕТ"
# print(remove_char_2(s))



# def solution(stones):
    # Do some magic

# km = "RGBRGBRGGB"
# res = 0
# g = ""
# for i in km:
#     if i == g:
#         res = res + 1
#     else:
#         g = i
# print(res)
#
# def sum_two_smallest_numbers(numbers):
#     res = 0
#     numbers.sort()
#     for i in numbers:
#         i = float(i)
#         res = numbers[0] + numbers[1]
#     return res
#
# lst = [1,8,10,329,23]
# print(sum_two_smallest_numbers(lst))

# def area_or_perimeter(l , w):
#     res = 0
#     if l == w:
#         res = l*w
#     else:
#         res = (l + w)*2
#     return res
#
# print(area_or_perimeter(10,9))

# def sp_eng(sentence):
#
#     # sentence.lower()
#     h = "english"
#     return h in sentence.lower()
#
# s = "abcEnglishdef"
# print(sp_eng(s))

# def polindrom(s):
#     if s[:].lower() == s[::-1].lower():
#         print("Полиндром")
#     else:
#         print("Не полиндром")
#
# polindrom("Анна")


# n = 10
# res = 0
# a = 1
# b = 1
# while a < n:
#     res = res + a
#     a, b = b, a+b
#     # res = res + a
#     print(a)
# print(res)

# n = [1,2,3,4,5,6,7,8,9]
# even = [x for x in n if x % 2 == 0]
#
# if even:
#     sun = sum(even)
#     sr = sun/len(even)
#     print(f"Средне арифмет {sr}")
# else:
#     print(f"Нет чётных чеисел")
#
# n = 10
# a = 0
# b = 1
# idx = 0
# coun = 0
# while coun < n:
#         if idx %2 == 0:
#             print(a, end=" ")
#             coun = coun +1
#
#         a, b  = b, a + b
#         idx = idx +1
#

    # ch = 1
    # while ch < 20:
    #     ch = ch + 1
    #     if ch % 3 == 0 and ch % 5 == 0:
    #         print(f"FizzBuzz - {ch}")
    #     elif ch % 3 == 0:
    #         print(f"Fizz - {ch}")
    #     elif ch % 5 == 0:
    #         print(f"Buzz - {ch}")
    #     else:
    #         print(ch)
    # else:
        # print(n)


# n = [1, 2, 3, 90, 45, 1, 33, 98]
# maximum1 = n[0]
# maximum2 = n[1]
# for i in n:
#     if maximum1 < i:
#         maximum1 = maximum2
#         maximum2 = i
#
# print(maximum2,maximum1)

# for n in range(1,500):
#     res = 0
#     col = len(str(n))
#     for i in str(n):
#         i = int(i)
#         s = i**col
#         res = res + s
#     if res == n:
#         print(res)

# n = int(input("Введи число: "))
# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# n = input("Число: ")
# res = 0
# for i in n:
#     i = int(i)
#     res = res + i
# print(res)

# n = int(input("Число : "))
# new = ""
# while n != 0:
#     i = n // 2 # Запомнили остаток
#     print(i)
# i = 10
# print(f"Деление {n} / { i} = {n/i}") # Деление
# print(f"Остаток {n} // {i} = {n//i}") # Убираем посде запятой
# print(f"Остаток от деления {n} % {i} = {n%i}")
# bit = ""
# while n != 0:
#     dig = n % 10
#     n = n // 10
#     print(dig)
# s = 0
# for x in range(1,n + 1):
#     s = x ** 2
#     print(f"{x}^2 = {s}")
# print(s)



# n = int(input())
# bin_ = ""
# while n > 0:
#     dig = n % 2 # Получаем остаток от деления 0 или 1 и передаём в переменную
#     bin_ = str(dig) + bin_# Прибавляем к переменой полученный 0 или 1
#     n = n // 2 # уменьшаем т
# print(bin_)


# s = input('Введите слова: ')
# shift = int(input("Введите ствиг: "))
# new_s = ""
# for i in s:
#     cod_i = ord(i)
#     shift_code_i = cod_i + shift
#     buk = chr(shift_code_i) # Из нового кода в символ
#     new_s = new_s + buk
# print(new_s)

# n = input("Введите число: ")
# n = input("Введите предложение: ")
#
# dst = {}
# for word in n.split(): #Разбили строку на слова.
#     if word not in dst: #Есло в словаре нет слова
#         dst[word] = 0 # Добавить слово ключ со значением 0
#     dst[word] = dst[word] + 1 # На каждой итерации к ключю слову прибавляем значение 1
# # print(dst)
#
# for key,val in dst.items(): #Распаковываем словарь
#     print(f"{key}: {val}")
#Анаграмма
# n1 = input("Первое слово: ")
# n2 = input("Второе слово: ")
# dst1= {}
#
# for i in n1:
#     if i not in dst1:
#         dst1[i] = 0
#     dst1[i] += 1
# dst2 = {}
# for i in n2:
#     if i not in dst2:
#         dst2[i] = 0
#     dst2[i] +=1
#
# if dst1 == dst2:
#     print("Анограмма")
# else:
#     print("Не анограмаа")

# n = 15
# a=0
# b=1
# for i in range(0,n+1):
#     print(a, end=" ")
#     a, b = b, a + b
#

# n = [64, 34, 25, 12, 22, 11, 90]
# for i in range(len(n)): # Тут формируются индексы скиска от 0 до длинны списка не включительно
#     for j in range(len(n)-1): # Тут формируеминдекс тогоже списка от 0 до длинны списка:
#         if n[j] > n[j+1]:
#             n[j],n[j+1] = n[j+1], n[j]
# print(n)
#ищем индекс введеного числа
# n = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
# target = int(input("Что ищем: "))
#
# left = 0
# right = len(n) - 1
#
# while left <= right:
#     mid = (left + right) // 2
#     if n[mid] == target:
#         print(mid)
#         # нашли — что делаем?
#
#     elif target > n[mid]:
#         left = mid + 1
#         # ищем правее — что меняем?
#
#     else:
#         right = mid - 1
#         # ищем левее — что меняем?
#

# n = [1, 2, 3, 2, 1, 4, 5, 4, 6]
# new_list  = []
# for i in n:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

# s = input("Введи числа через пробел: ")
# count = 0
# su = 0
# for i in s.split():
#     i = int(i)
#     count = count + 1
#     su = su + i
# res = su/count
# print(res)
#
# n = [4, 8, 2, 15, 6, 11, 3, 9]
# n_big = []
# n_smol = []
# count = 0
# su = 0
# for i in n:
#     i = int(i)
#     count = count + 1
#     su = su + i
#
# res = su/count
#
# for i in n:
#     if i > res:
#         n_big.append(i)
#     if i < res:
#         n_smol.append(i)
# print(f"Больше среднего: {n_big}")
# print(f"Меньше среднено: {n_smol}")

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# line = 0
# for i in matrix:
#     line = line + 1
#     res = 0
#     for j in i:
#        res =res + j
#     print(f"Строка {line}: {res}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for idx, val in enumerate(matrix):
    res = 0
    print(val[idx])
    for i, v in  enumerate(val):
        # print(val[i])
        # pass
        res = res + v
    # print(res)