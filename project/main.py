with open("data/user.txt","w") as file:
    file.write("Anna\n")
    file.write("Bob\n")
    file.write("Tom\n")

with open("data/user.txt","r") as file:
    for line in file:
        print(line.strip())

with open("data/user.txt", "w") as file:
    file.write("Anna\n")
    file.write("Bob\n")
    file.write("Tom\n")

with open("data/user.txt", "r") as file:
    for line in file:
        print(line.strip())
