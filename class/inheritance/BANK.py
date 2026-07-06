class Account:
    """ Класс аккаунт банка"""

    #Атрибуты класса
    def __init__(self,owner,balance):
        self.owner = owner #<- Владелец
        self.balance = balance # <- Баланс

    def  deposit(self,n): # <- Метод экземпляра класса
        """Метод класса добавляет сумму на депозит владельца"""
        self.balance = self.balance + n

    def withdraw(self,n): # <- Метод экземпляра класса
        """Метод класса снимает с депозита сумму владельца"""
        if self.balance < n:
            print("Недостаточно средств")
        else:
            self.balance = self.balance - n

    def info(self):
        """Метод вернёт информацию об аккаунте"""

        print(f"{self.owner}  |   {self.balance}")


class Bank:
    """Класс банк"""
    accounts = []  # <- Список аккаунтов

    def add_account(self,account):
        """Метод добавляет счёт в банке"""
        self.accounts.append(account)# < - Добавляем счет аккаунта в банк

    def info(self):
        """Метод выводит все счёта в банке"""
        print(self.accounts)



user1 = Account("Иванов",200)
user2 = Account("Петров",500)
bank1 = Bank()
bank1.add_account(user1)
bank1.add_account(user2)



