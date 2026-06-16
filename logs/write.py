import json

with open("data.json","r",encoding="utf-8") as file:
    data = json.load(file)
print(data)

print(data['history'])
data["history"].append({"type": "пополнение", "amount": 300})
print(data['history'])

def get_history():
    with open("data.json","r",encoding="utf-8") as file: # Открываем файл
        data = json.load(file) # в переменную пишим словарь

    return json.dump(data,file,indent=1,ensure_ascii=False)





    # lst = []
        # for i in data['history']:
        #     lst.append((i['type'], i['amount']))
        # return lst


# with open("data.json","w",encoding="utf-8") as file:
#     data["history"].append({"type": "пополнение", "amount": 500})
#     json.dump(data,file,ensure_ascii=False,indent=1)


# for i in data['history']:
#     print(i['type'], i['amount'])
#
