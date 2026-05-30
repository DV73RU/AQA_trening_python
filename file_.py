
# with open("example.txt", "r") as f:
#     content = f.read()
#     print(content)
#Подсчёт количество срок в файле
with open("example.txt",'r') as file:
    lines = file.readlines()
    count = 0
    print(lines)
    # for i in range(len(lines)):
    #     count += i
    # print(count)
    # print(lines)
    # text = " ".join(item.strip() for item in lines)


    text = " ".join(val.strip() for val in lines)
    print(text)

    lst = [i.replace('\n', '') for i in  lines]
    print(lst)






