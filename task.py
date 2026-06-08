# объявление функции
# from tutle_ import result
from datetime import datetime,timedelta
from tkinter.font import names

# объявление функции
# def draw_triangle(fill, base):
#     mid = base // 2
#     # print(mid)
#     for i in range(1,mid+1):
#         print(f"{fill * i}")
#         # print(fill)
#     for i in (range(mid+1,-1,-1)):
#         print(f"{fill * i}")
#         # print(fill)
#
#
# # считываем данные
# fill = input()
# base = int(input())
#
# # вызываем функцию
# draw_triangle(fill, base)


# объявление функции
# def print_perm_time_call(msc_time):
#     pass
#
# # считываем данные
# msc_time = input()
#
# # вызываем функцию

# print_perm_time_call(msc_time)
# def print_perm_time_call(msc_time):
#     msc_time = msc_time.split(":")
#     h_msk = msc_time[0]
#     m_msk = msc_time[1]
#     h_per = int(h_msk) + 2
#     if h_per < 10:
#         h_per =  '0' + str(h_per)
#     print(f"Созвон будет в {h_per}:{m_msk}.")
#
#
# msc_time = input()
# print_perm_time_call(msc_time)

    # print(f"Время у меня - {time_now.hour}:{time_now.minute}")
    # hour_perm = time_now + timedelta(hours=1)
    # # minute_perm = hour + timedelta(minute=0)
    # print(f"Время в перми - {hour_perm.hour}:{hour_perm.minute}")



# объявление функции
# def print_symbol_counts(s):
#     # pass
#     dst = {}
#     for buk in s.lower():
#         # print(buk)
#         if buk not in dst:
#             dst[buk] = 1
#         else:
#
#             dst[buk] = dst[buk] + 1
#
#     for b, val  in sorted(dst.items()):
#         print(f"{b}: {val}")
#
# # считываем данные
# s = input()
# print_symbol_counts(s)

# def code_format(text) -> str:
#
#     return f"<code>{text}</code>"
# text = str(input())
# print(code_format(text))

# def get_days(month) -> str:
#     days = 30 + (month + month // 8) % 2 - (2 if month == 2 else 0)
#     return days
#
# n = int(input())
#
# print(get_days(n))

# def math_round_to_int(num):
#     ost = num % 1 #Остаток от деления
#     if ost >= 0.5:
#         print(int(num+1 - ost))
#     else:
#         print(int(num))
# n = float(input())
# math_round_to_int(n)

# def get_factors(num):
#     lst = []
#     for i in range(1,num+1):
#         if num % i == 0:
#             lst.append(i)
#     return lst
#
# b = int(input())
#
# print(get_factors(b))