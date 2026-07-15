


class Money:
    """Класс деньги"""
    def __init__(self,amount, currency):
        self.amount = amount
        self.currency = currency # Атрибуты экземпляра: Значение, Валюта

    def info(self):
        """Метод экземпляра выводит информации о валюте"""
        print(f"{self.amount} {self.currency}")

    @classmethod
    def from_string(cls,data:str):
        """Метод конвертирует из строки в валюту"""
        amount, currency = data.split(" ")
        return cls(float(amount),str(currency))

    @classmethod
    def from_dict(cls,data:dict):
        """"Метод класса из словаря в валюту"""
        amount = data.get("amount")
        currency = data.get("currency")
        return cls(amount,currency)

    def convert(self,rate):
        """Метод экземпляра конвертирует в переданную значение в USD в Руб по курсу 90 Руб за 1 USD"""
        return Money(self.amount * rate, self.currency)



rub = Money(100,"Rub")
rub.info()

rub_str = Money.from_string("108.50 Rub")
rub_str.info()

eur_dct = Money.from_dict({"amount": 50, "currency": "EUR"})
eur_dct.info()

usd = Money(100,"USD")
# rub1 = Money(90,"RUB")
rub1 =usd.convert(90)
rub1.info()