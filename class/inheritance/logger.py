from datetime import datetime

def logger(func):
    def wrapper(*args,**kwargs):
        res = func(*args,**kwargs)
        date = datetime.today()
        date_s = date.strftime("%Y-%m-%d %H:%M:%S")
        name_f = func.__name__
        str_ = f"{date_s} | {name_f} | args: {args} | {res}"
        with open("log.txt","a") as file:
            file.write(str_ + "\n")
        print("Записали в фал ")
    return wrapper


@logger
def summ(a,b):
    return a + b


@logger
def raz(a,b):
    return a - b

@logger
def pr(a,b):
    return  a*b
summ(10,2)
raz(20,9)
pr(2,5)