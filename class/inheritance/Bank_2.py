class BankAccount:
    """Класс Бонковский Аккаунт"""
    bank_name = "Рога и копыта"
    list_owner = []

    def __init__(self,owner,balans):
        self.owner = owner
        self.balans = balans

    def deposit(self,amount:float):
        """Метод экземпляра пополняет баланс"""
        if self.is_amount_valid(amount):
            self.balans = self.balans + amount
            print(f"{self.owner} - пополнил депозит на {amount} Баланс :{self.balans}")
        else:
            print(f"Сумма должна быть больше 0")

    def withdraw(self,amount):
        """Метод экземпляра снимает с баланса"""
        if not self.is_amount_valid(amount):
            print(f"Сумма должна быть больше 0")
        elif amount > self.balans:
            print("Не достойно средств")
        else:
            self.balans = self.balans - amount
            print(f"{self.owner} - снял с депозита {amount} Баланс: {self.balans}")

    @staticmethod
    def is_amount_valid(amount):
        return amount > 0

    @classmethod
    def bank_info(cls):
        """Метод класса печатает информацию о банке"""
        return f"Велкам в банк {BankAccount.bank_name}"

user_acc = BankAccount("Иванов", 100)
print(user_acc.balans)
user_acc.deposit(100)
print(user_acc.balans)
user_acc.withdraw(120)
print(user_acc.balans)
user_acc.withdraw(120)
print(user_acc.bank_info())
