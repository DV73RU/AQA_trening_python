import json

with open("quiz.json","r",encoding="utf-8") as file:
    data = json.load(file)


# print(data)

# print(json.dumps(data,ensure_ascii=False,indent=4))

count_q = 0
total = len(data["questions"])

for num,val in enumerate(data["questions"],start=1):

    question = val['question']
    options =  val['options']
    answer = val['answer']

    print(f"Вопрос {num}: {question}")
    for idx,otv in enumerate(options,start=1):
        print(f'{idx}. {otv}')
    n = input("Ваш ответ: ")

    if n == answer:
        count_q = count_q + 1
        print("Верно! ✓")

    else:
        print(f"Не верно! Правильный ответ :{answer}")

print(f"Результат: {count_q} из {total}")