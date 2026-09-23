from abc import ABC, abstractmethod


class Order:
    """Храним данные о покупки"""

    def __init__(self, products: list, amount: float):
        self.products = products  # -> Список покупок
        self.amount = amount  # -> Сумма заказа

    def get_info(self):
        list_to_str = ", ".join(self.products)
        return f"Товары: {list_to_str} на сумму {self.amount} руб."


class BasePayment(ABC):
    """Абстрактный класс способа оплаты"""

    @abstractmethod
    def pay(self, order):
        """Метод способа оплаты"""
        pass


class CashPayment(BasePayment):
    """Класс оплаты наличными"""

    def pay(self, order):
        """Метод способа оплаты наличными"""
        print(f"Оплата наличными {order.amount} руб")


class CardPayment(BasePayment):
    """Класс оплаты банковской картой"""

    def pay(self, order):
        """Метод способа оплаты банковской картой """
        print(f"Оплата картой {order.amount} руб")


class PayPalPayment(BasePayment):
    """Класс оплаты PayPal"""

    def pay(self, order):
        """Метод способа оплаты PayPal """
        print(f"Оплата PayPal {order.amount} руб")


class OrderProcessor:
    """Процессинг оплаты"""

    def __init__(self, method_pay: BasePayment):
        self.method_pay = method_pay

    def process(self, order: Order):
        print(f"Обрабатываем заказ: {order.get_info()}")
        self.method_pay.pay(order)


aple = "aple"
pear = "pear"
kiwi = "kiwi"

list_produkt = [aple, pear, kiwi]

order1 = Order(list_produkt, 2000)

order_proc = OrderProcessor(CashPayment())
order_proc.process(order1)
