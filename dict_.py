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

