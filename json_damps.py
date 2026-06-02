import json


data = {
    "name": "Дмитрий",
    "age": 25
}

json_string = json.dumps(data,indent=4,ensure_ascii=False)

print(json_string)
print(type(json_string))

json_string = '{"name": "Anna", "age": 25}' #Строка похожая на словарь

print(json_string)
print(type(json_string))

data = json.loads(json_string) #Преобразуем строку в словарь
print(data)
print(type(data))
for item, val in data.items():
    print(item,val)

for key in data.keys():
    print(key)
for item in data.values():
    print(item)