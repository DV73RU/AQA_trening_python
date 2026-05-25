# # user = {"name": "Anna", "age": 25, "city": "Moscow", "job": "QA"}
# #
# # print(user)
# #
# # user["name"] = "Дмитрий"
# # print(user)
# #
# # del user["job"]
# # print(user)
#
# product = {
#     "title": "Milk",
#     "price": 100,
#     "count": 5
# }
#
# # print(product["title"])
# # print(product["price"])
#
# value = product.pop("count")
# print(product,value)
#
# product["count"] = 5
#
# for key in product:
#     print(key)
#
# product["new"] = 1
# print(product)
#
# new = product.pop("new")
# print(product)
#
# print(product.values())
# print(product.keys())
#
# for key in product.keys():
#     print(key)
#
# for value in product.values():
#     print(value)
#
# for key, value in product.items():
#     print(f"Название: {key} - Количество: {value}")
#
# print(product.get("count"))
#
# product.update({"price": 200})
# print(product)
#
# new_dict = product.copy()
# print(new_dict)
# print(product)
#
# new_dict.setdefault("count",10)
#
# print(product.get("count"))
#
# print(product.get("price"))
#
# product.update({"price":300})
# # product.pop("count")
# print(product)
#
# for key, value in product.items():
#     print(key, value)

#1
# user = {
#     "name": "Anna",
#     "age": 25,
#     "city": "Moscow"
# }
#
# print(f"Имя: {user.get("name")}")
# print(f"Возраст: {user.get("age")}")
# print(f"Город: {user.get("city")}")
#

#3
# product = {
#     "title": "Milk",
#     "price": 100,
#     "count": 5
# }
#
# product.update({"price":200})
# product["category"] = "Food"
# product.pop("count")
# print(product)

#4
prices = {
    "apple": 50,
    "banana": 30,
    "milk": 100,
    "bread": 40,
    "cheese": 150
}

for key,value in prices.items():
    if value > 50:
        print(key, value)

#5
# prices = {
#     "apple": 50,
#     "banana": 30,
#     "milk": 100,
#     "bread": 40
# }
#
# res = 0
# for value in prices.values():
#     res = res + value
# print(res)

#6

students = {
    "Anna": 5,
    "Bob": 4,
    "Tom": 3,
    "Kate": 5,
    "Max": 2
}

for key,value in students.items():
    if value == 5:
        print(key)