from typing import List
from models.exceptions import InvalidOrderError, ValidationError
from models.product import Product

class Order:

    def __init__(self, user, products: List[Product]) -> None:
        self.user = user

        if not products:
            raise InvalidOrderError(
                "Заказ невалиден: пустой список товаров"
            )
        self.products = products

    @property
    def total(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total

    def add_product(self, product):
        if isinstance(product, Product):
            self.products.append(product)
        else:
            raise ValidationError(
                "Продукт невалиден, невозможно добавить"
            )

    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.get_total_price()
        return total

    def __str__(self) -> str:
        return f"Заказ пользователя {self.user.name} на сумму {self.total} руб."