import json


data = {
    "name": "Anna",
    "age": 25,
    "city": "Moscow"
}

data_users =  [
    {"id": 1, "name": "Anna"},
    {"id": 2, "name": "Bob"}
]

with open("data.json","w") as file:
    json.dump(data,file,ensure_ascii=False, indent=4)

with open("data.json", "r") as file:
    loaded = json.load(file)
# print(loaded)
# for item in loaded:
    # print(item)
# print(type(loaded))
# print(loaded)
# for items in loaded:
#     print(items['name'])

with open("users.json", "w") as file:
    json.dump(data_users, file,ensure_ascii=False, indent=4)

with open("users.json", "r") as file:
    users = json.load(file)
    for user in users:
        print(user["name"])
        print(user["id"])
