import time



def timer(func): # функция принимает функцию.
    def wrapper():
        start = time.time()
        res = func()
        stop = time.time()
        print(f"Время выполнения: {func.__name__} - {stop - start:.2} сек")

        return res
    return wrapper



@timer
def get_i():
    lst = [1, 2, 3, 3]
    for i in lst:
        time.sleep(1)
            # return i
        print(i)

get_i()
