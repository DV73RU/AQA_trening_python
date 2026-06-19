import json
import requests

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

data = response.json()
# print(data)
# print(json.dumps(data,ensure_ascii=False,indent=4))
# count = len(data)
for i in data:
    name = i['name']
    mail = i['email']
    idx =  i['id']
    print(f"{idx}. {name} - {mail}")