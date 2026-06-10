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


n = [1, 2, 3, 90, 45, 1, 33, 98]
maximum1 = n[0]
maximum2 = n[1]
for i in n:
    if maximum1 < i:
        maximum1 = maximum2
        maximum2 = i

print(maximum2,maximum1)