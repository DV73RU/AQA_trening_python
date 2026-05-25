#1
# numbers = [1,2,3,4,5,6,7]
# res = 0
# for i in numbers:
#     res = res + i
# print(res)
#2


# numbers = [1,2,-3,4,5,6,-7,10,-100]
# new_list =[]
# for i in numbers:
#     if i > 0:
#         new_list.append(i)
# print(new_list)
#
# #2_2
# new_list = [i for i in numbers if i > 0]
# print(new_list)
#
# tupl = (1,2,3,4,5)
# ch = 4
# ext = ch in tupl
# print(ext)
#
# dict_1 = {1,2,3,4}
# dict_2 = {5,6,7}
# res = dict_1 | dict_2
# print(res)



# dict_1 = (1,2,3,4)
# dict_2 = (5,6,7)
# res = dict_1 + dict_2
# print(res)
#
# lest_1 = [1,2,3,3,3,5]
# print(lest_1)
# tup= set(lest_1)
# print(tup)
#
# set_1 = {1,2,3,4}
# set_2 = {3,4,5,6}
# res = set_1 & set_2
# print(res)
#
# values = ["Anna",34,"London"]
# keys = ["Name","age","city"]
#
# my_dict = dict(zip(keys,values))
# print(my_dict)

my_dict_1 = {"name":"Анна","age":12}
my_dict_2 = {"name": "Анна", "age":19,"city":"London"}
my_dict_1.update(my_dict_2)
# print(my_dict_2)
print(my_dict_1)



