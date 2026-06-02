import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Имя","Возраст"])
    writer.writerow(["Анна","23"])
    writer.writerow(["Иван","30"])

with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)