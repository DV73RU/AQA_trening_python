from enum import Enum, unique


class Bank:
    def account(self):
        print("Это бакковский аккаунт")
        print(self)


my_bank = Bank()
my_bank.account()
