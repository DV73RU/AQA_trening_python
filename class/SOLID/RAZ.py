import requests
import json

url = "https://catfact.ninja/fact"
response = requests.get(url)
data = response.json()
json = json.dumps(data,ensure_ascii=False,indent=4)
# print(json)

print(response.headers)

content_tupe =  response.headers.get('Content-Type')
print(content_tupe)