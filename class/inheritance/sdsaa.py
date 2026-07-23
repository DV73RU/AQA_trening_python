def summ(a,b):
    return a + b

def razz(a:int,b:int)->int:
    return a - b

def exampl(funct): # Обёртка для функций, выведет результат работы функции и красиво оформит
    def wrapper(a,b): # Принимаем значение переданной функции
        res = funct(a,b)
        print("----------")
        print(res)
        print("----------")
        return res
    return wrapper


@exampl
def su(a:int,b:int) -> int:
    return a + b

@exampl
def raz(a:int,b:int):
    return a -b

su(10,12)
raz(10,2)
