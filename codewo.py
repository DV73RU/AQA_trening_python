# def number_to_string(num):
#     string = str(num)
#     return string
#
#
# num = 1234
# print(number_to_string(num))
from os import mkdir

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

from preloaded import Like, Dislike, Nothing

def like_or_dislike(lst):
    return Like or Dislike or Nothing
