import json

with open("quiz.py","r",encoding="utf-8") as file:
    data = json.load(file)

print(json.dump(data,file,indent=4,ensure_ascii=False))
