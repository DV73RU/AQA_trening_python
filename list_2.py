# Переместить элемент с индексом 1 в конец списка

numbers = [1, 2, 3, 4, 5]
i = numbers.pop(1)
numbers.append(i)

numbers = [10, 20, 30, 40, 50]


i = numbers.pop(0)
numbers.append(i)
print(numbers)


# Нужно переместить элемент с индексом 2 в начало списка.
numbers = [10, 20, 30, 40, 50, 60]

i = numbers.pop(2)
numbers.insert(0,i)
print(numbers)

numbers = [5, 10, 15, 20, 25, 30]

i = numbers.pop(4)
numbers.insert(1,i)
print(numbers)