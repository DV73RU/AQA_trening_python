# text = "hello"
# nex_text = text.upper()
# print(nex_text)
#
# text = "python programming"
#
# print(text.capitalize())
# print(text.upper())
# print(text.title())
#
# text = "   hello   "
#
# new_text = text.split()
# new_text = new_text[0].capitalize()
# print(new_text)
#
# print(new_text)
#
# new_text = text.lstrip()
# print(new_text)
# new_text = text.rstrip()
# print(new_text)

text = "I learn Python"

print(text.find("Python"))  # 8
print(text.find("Java"))    # -1


text = "banana"

print(text.find("na"))  # 2


text = "hello.py"

print(text.startswith("hello"))  # True
print(text.endswith(".py"))      # True

text = "I like Java"

new_text = text.replace("Java","Python")
print(new_text)


text = "apple,banana,orange"

lst_text = text.split(",")
for i in lst_text:
    print(i)

words = ["Python", "is", "good"]
text = " ".join(words)
print(text.title())
print(text.upper())

print(text.count("y"))

# Задача 1
text = "   hello python   "
text=text.strip()
print(text.upper())

# Задача 2
text = "I like Java"
text = text.replace("Java","Python")
print(text)

# Задача 3
text = "apple,banana,orange"
lst_text = text.split(',')
print(lst_text)

# Задача 4

text = "12345"
print(text.isdigit())

# Задача 5
text = "banana"
count_a = text.count("a")
print(count_a)

name = "Алексей"
print(name.find("А"))
print(name.istitle())

text = "Сегодня отличный день для прогулки"
# list_text = text.split()
# print(list_text)
num = text.find("отличный")
print(num)