class  BankAccount:
    """Бакнковский счёт"""
    def __init__(self,owner, balance): # Атрибуты обьекта
        self.owner = owner #Владелец
        self.balance = balance #Баланс

    def deposit(self,n):
        """Метод пополнения счёта"""
        self.balance = self.balance + n

    def withdraw(self,n):
        """Метод снятия наличных"""
        if self.balance < n:
            print(f"На балансе не досточно средств: {self.balance}")
        else:
            self.balance = self.balance - n
            print(f"На баланс зачислено: {n} ,Баланс: {self.balance}")

    def info(self):
        """Метод информации о болансе владельца"""
        print(f"Владелец: {self.owner}. Баланс: {self.balance}")


owner1 = BankAccount("Иванов Иван Иванович",100)
owner2 = BankAccount("Петров Иван Семёновичь", 1000)
owner1.info()

owner2.deposit(1000)
owner2.info()
owner2.withdraw(100000)