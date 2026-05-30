
# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)
#Подсчёт количество срок в файле
with open("example.txt",'r') as file:
    lines = file.readlines()
    count = 0
    for i in range(len(lines)):
        count += i
    print(count)
    print(lines)