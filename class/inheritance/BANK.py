

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

    def info(self): #<- Метод экземпляра класса
        """Метод вернёт информацию об аккаунте"""
        print(f"{self.owner}  |   {self.balance}")


class Bank:
    """Класс банк"""
    def __init__(self):
        self.accounts = []  # <- Список аккаунтов

    def add_account(self,account): # <- Метод экземпляра класс Банк
        """Метод добавляет счёт в банке"""
        self.accounts.append(account)# < - Добавляем счет аккаунта в банк

    def info(self): # <- Метод экземпляра класс Банк
        """Метод выводит все счёта в банке"""
        for account in self.accounts:
            account.get_result()

    def find_by_owner(self,name):# < - Метод экземпляра класса Банк
        """Метод возвращает счет по Фамилии"""

        found = False
        for account in self.accounts:
            if account.owner == name:
                account.get_result()
                found = True
        if not found:
            print("Нет такого")

    def total_balance(self): # < - Метод экземпляра класса Банк.
        """Метод возвращает сумму всех счетов"""
        res = 0
        for account in self.accounts:
            res = res + account.balance
        print(f"Всего в банке {res}")




user1 = Account("Иванов",200) # Создаём экземпляр класса Account
user2 = Account("Петров",500) # Создаём экземпляр класса Account
bank1 = Bank() # Создаём экземпляр класс Банк
bank1.add_account(user1)
bank1.add_account(user2)
# bank1.info()
# bank1.find_by_owner("Иванов")
# bank1.find_by_owner("Петров")
bank1.find_by_owner("Cидоров")
bank1.total_balance()


