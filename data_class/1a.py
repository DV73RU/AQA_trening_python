import dataclasses
from dataclasses import dataclass


class ShopItem:
    def __init__(self, item_id: int, name: str, price: float, has_discount: bool = False):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.has_discount = has_discount

    def __repr__(self):
        return f"ShopItem({self.item_id}, {self.name}, {self.price}, {self.has_discount})"

    def __eq__(self, other):
        if isinstance(other, ShopItem):
            return (
                        self.item_id == other.item_id and self.name == other.name and self.price == other.price and self.has_discount == other.has_discount)
        return False


@dataclass(frozen=True)
class ShopItem2:
    item_id: int
    name: str
    price: float
    has_discount: bool = False


item1 = ShopItem2(1, "Apple", 1.0, has_discount=True)
item2 = ShopItem2(2, "Qiwi", 2.0)
print(item1)
print(item1 == item2)
print(item1 == item1)
item3 = dataclasses.replace(item1, has_discount=False)
print(item3)
