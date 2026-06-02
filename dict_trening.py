text = "apple banana apple orange banana apple"


dict_1  = {}
minimum = 0
for word in text.split():
    if word in dict_1: #Если слово есть в словаре
        dict_1[word] = dict_1[word] + 1 #Берем слово всловаре и прибавляем знасчение на один
    else:
        dict_1[word] = 1 # Если слова нет то значение 1



print(dict_1)
min_value = float("inf")
min_word = None
for word, val in dict_1.items():
    if val < min_value:
        min_value = val
        min_word = word
print(f"{min_word} - {min_value}")
