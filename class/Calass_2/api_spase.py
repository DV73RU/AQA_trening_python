import json

import requests

public_ip = requests.get('https://api.ipify.org').text

print(f"IP-адрес: {public_ip}")


response = requests.get(url=f"https://ipinfo.io/{public_ip}/geo")
data1 = response.json()

json_response = json.dumps(data1,ensure_ascii=False,indent=4,)
print(json_response)