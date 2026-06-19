import time
import requests
import json
url = "https://official-joke-api.appspot.com/random_joke"

response = requests.get(url)

data = response.json()
# print(data)

setup = data['setup']
punchline = data['punchline']
print(setup)
print("...")
time.sleep(2)
print(punchline)

