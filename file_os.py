import os


#
# folder = "userdata"
# file = "user.txt"
#
# path = os.path.join(folder,file)
#
# if not os.path.exists(folder):
#     os.mkdir(folder)
#
# with open(path,"w") as file:
#     file.write("User: Anna\n")
#     file.write("User: Bob\n")
#     file.write("User: Tom\n")
# with open(path,"r") as file:
#     # print(file.readlines())
#     for line in file:
#         print(line.strip())


# folder = "shop_data"
# filename = "products_price.txt"
#
# path = os.path.join(folder,filename)
# if not os.path.exists(folder):
#     os.mkdir(folder)
#
# with open(path,"w") as file:
#     file.write("aple:50\n")
#     file.write("banana:30\n")
#     file.write("milk:100\n")
#     file.write("bread:40\n")
#     file.write("cheese:150\n")
#
# with open(filename,"r") as file:
#     # text = file.read()
#     # print(text)
#     lst = file.readlines()
#     for line in lst:
#         # print(line.strip())
#         # print(lst)
#         name, price = line.strip().split(":")
#         if int(price) > 50:
#             print(f"{name} - {price}")
#         # print(price)

folder = "logs"
name_file = "actions.txt"

path = os.path.join(folder,name_file)

if not os.path.exists(folder):
    os.mkdir(folder)

with open(path,"w") as file:
    file.write("login\n")
    file.write("open_page\n")
    file.write("click_button\n")

with open(path,"a") as file:
    file.write("send_form\n")
    file.write("logaut\n")

count = 0
with open(path,"r") as file:
    for line in file:
        count = count + 1
        print(f"Действие: {line.strip()}")
print(f"Количестов действий: {count}")