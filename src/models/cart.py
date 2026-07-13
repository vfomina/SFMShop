from typing import List

from models.product import Product

class Cart:

    def __init__(self, owner, items: List[Product]) -> None:
        self.owner = owner
        self.items = items

    def __len__(self) -> int:
        return len(self.items)

    def __add__(self, other):
        return Cart(self.owner, self.items + other.items)

    def __str__(self) -> str:
        total = 0
        for item in self.items:
            total += item.get_total_price()
        return f"Корзина {self.owner}: {len(self)} товаров на {total} руб."