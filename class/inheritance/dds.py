tasks = ["Задача 1", "Задача 2", "Задача 3"]


def cycle_task(*tasks):
    while True:
        for tsk in tasks:
            yield tsk


gen = cycle_task(*tasks)

for i in range(7):
    print(next(gen))

if __name__ == '__main__':
    cycle_task(*tasks)
    cycle_task(*tasks)
    cycle_task(*tasks)