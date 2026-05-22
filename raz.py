# text = "Python is amazing"
# words = text.split() # Разбите на слова
#
# first_let = [word[0] for word in words ] # Формируем скисок из первых индексов каждого слова
# print(first_let) # Печатам список перых символов каждого слова

data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
chunk_size = 3
chunks = [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]
# [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

lens = list(range(1,10,))
print(lens)